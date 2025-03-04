# Import necessary libraries
from flask import Flask, request, render_template, jsonify  # Flask web framework
import os  # For file handling
import psycopg2  # To connect with PostgreSQL database
import pandas as pd  # To read and process dataset
import ffmpeg  # To extract audio from video
import speech_recognition as sr  # For speech-to-text conversion
from sklearn.feature_extraction.text import TfidfVectorizer  # Text processing
from fuzzywuzzy import process  # For fuzzy string matching (better keyword detection)

# Initialize the Flask app
app = Flask(__name__)

# Define an "uploads" folder to store uploaded videos
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

# ---------------- DATABASE CONNECTION ----------------

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="bank_complaints",  # Database name
        user="postgres",  # Database username
        password="root",  # Database password
        host="localhost",  # Database host (running locally)
        port="5432"  # Default PostgreSQL port
    )
    cursor = conn.cursor()  # Create a cursor to interact with the database
    print("✅ Database connected successfully")
except Exception as e:
    print(f"❌ Database connection error: {e}")  # Print error if connection fails

# ---------------- LOAD & PROCESS THE DATASET ----------------

# Load the banking dataset (contains department names, categories, and keywords)
df = pd.read_csv("banking_dataset.csv")  # Read dataset from CSV

# Create a TF-IDF model for keyword matching
vectorizer = TfidfVectorizer()
keyword_corpus = df["keywords"].astype(str).tolist()  # Convert keywords column to list
keyword_matrix = vectorizer.fit_transform(keyword_corpus)  # Transform into a matrix

# ---------------- CATEGORIZATION FUNCTION ----------------

def categorize_complaint(text):
    """
    Function to categorize the complaint based on its text using fuzzy matching.
    - It compares the given text with stored keywords and finds the best match.
    """
    text = text.lower()  # Convert the input text to lowercase for better matching
    
    # Use fuzzy matching to find the best keyword match from the dataset
    best_match, score = process.extractOne(text, df["keywords"].tolist())

    # If match score is above 70%, return department and category
    if score > 70:
        matched_row = df[df["keywords"] == best_match].iloc[0]  # Get matching row
        return matched_row["department"], matched_row["category"]
    
    return "Unknown", "Uncategorized"  # If no good match found, return default values

# ---------------- FLASK ROUTES ----------------

@app.route('/')
def home():
    """
    Home route - Renders an HTML page (index.html).
    """
    return render_template('index.html')

@app.route('/upload-video', methods=['POST'])
def upload_video():
    """
    API route to upload a video, extract audio, convert it to text, 
    categorize the complaint, and store it in the database.
    """
    # Check if a file is included in the request
    if 'video' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    video = request.files['video']  # Get the uploaded video file

    # Check if a file is selected
    if video.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the video file
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    audio_path = video_path.replace(".mp4", ".wav")  # Convert filename to .wav
    video.save(video_path)

    try:
        # ---------------- STEP 1: EXTRACT AUDIO FROM VIDEO ----------------
        ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)

        # ---------------- STEP 2: CONVERT AUDIO TO TEXT ----------------
        recognizer = sr.Recognizer()  # Create a speech recognizer
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)  # Record the audio
            text = recognizer.recognize_google(audio_data)  # Convert speech to text

        # ---------------- STEP 3: CATEGORIZE THE COMPLAINT ----------------
        department, category = categorize_complaint(text)

        # ---------------- STEP 4: STORE IN DATABASE ----------------
        cursor.execute(
            """
            INSERT INTO tickets (video_path, transcript, department, category)
            VALUES (%s, %s, %s, %s) RETURNING id;
            """,
            (video_path, text, department, category)
        )
        ticket_id = cursor.fetchone()[0]  # Get the auto-generated ticket ID
        conn.commit()  # Save changes in the database

        # ---------------- STEP 5: RETURN RESPONSE ----------------
        return jsonify({
            "message": "Ticket generated successfully",
            "ticket_id": ticket_id,
            "transcript": text,
            "department": department,
            "category": category
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error if anything fails

# ---------------- RUN THE FLASK APP ----------------

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask server in debug mode
