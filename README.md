# Ideathon

📌 Ticket Creation System
This project allows users to upload complaint videos, converts the audio to text, categorizes the complaint, and generates a ticket stored in a database.

📁 Project Structure
ticket_creation/
│-- app.py                     # Main Flask application
│-- banking_dataset.csv         # Dataset for categorizing complaints
│-- requirements.txt            # Required dependencies
│-- templates/
│   ├── index.html              # Web interface for uploading videos
│-- README.md                   # Project documentation

🚀 Features
✅ Upload complaint videos
✅ Convert speech to text
✅ Categorize complaints using NLP
✅ Store tickets in a database
✅ Web interface for easy access

📦 Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/Sneha-Edugunoori/Ideathon.git
cd Ideathon/ticket_creation

2️⃣ Install Dependencies
Before running the project, install the required dependencies:
pip install -r requirements.txt

🔧 Setup Database (PostgreSQL)
Make sure you have PostgreSQL installed. Open psql and run:
CREATE DATABASE bank_complaints;
\c bank_complaints

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    video_path TEXT NOT NULL,
    transcript TEXT NOT NULL,
    department TEXT NOT NULL,
    category TEXT NOT NULL
);

▶️ Run the Application
After installing dependencies and setting up the database, start the Flask app:
python app.py

📧 Contact Information
👩‍💻 Sneha Edugunoori
📍 Data Science Engineering Student(Second year)
🔗 GitHub: Sneha-Edugunoori
🔗 LinkedIn: Sneha Edugunoori
