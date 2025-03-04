Here's your **properly formatted README** with correct Markdown syntax for GitHub:  

---

```md
# Ideathon  

## 📌 Ticket Creation System  

The **Ticket Creation System** is a Flask-based application that allows users to upload complaint videos. The system processes the audio, converts it to text, categorizes the complaint using **Natural Language Processing (NLP)**, and generates a ticket that is stored in a **PostgreSQL database**.  

---

## 📁 Project Structure  

```bash
ticket_creation/
│-- app.py                 # Main Flask application
│-- banking_dataset.csv     # Dataset for categorizing complaints
│-- requirements.txt        # Required dependencies
│-- templates/
│   ├── index.html         # Web interface for uploading videos
│-- README.md              # Project documentation
```

---

## 🚀 Features  

- Upload complaint videos  
- Convert speech to text  
- Categorize complaints using NLP  
- Store tickets in a PostgreSQL database  
- Web interface for easy interaction  

---

## 📦 Installation Guide  

### 1. Clone the Repository  

To get started, clone the repository using:  

```sh
git clone https://github.com/Sneha-Edugunoori/Ideathon.git  
cd Ideathon/ticket_creation  
```

### 2. Install Dependencies  

Before running the project, install the required dependencies:  

```sh
pip install -r requirements.txt  
```

---

## 🔧 Setup Database (PostgreSQL)  

Ensure **PostgreSQL** is installed on your system. Then, open **psql** and run the following commands to create a database and table:  

```sql
CREATE DATABASE bank_complaints;  
\c bank_complaints  

CREATE TABLE tickets (  
    id SERIAL PRIMARY KEY,  
    video_path TEXT NOT NULL,  
    transcript TEXT NOT NULL,  
    department TEXT NOT NULL,  
    category TEXT NOT NULL  
);
```

---

## ▶️ Run the Application  

Once dependencies are installed and the database is set up, start the Flask application:  

```sh
python app.py  
```

The app will run on **http://127.0.0.1:5000/**. Open your browser and start using the **Ticket Creation System**!  

---

## 📧 Contact Information  

👩‍💻 **Sneha Edugunoori**  
📍 **Data Science Engineering Student (Second Year)**  
🔗 **GitHub**: [Sneha-Edugunoori](https://github.com/Sneha-Edugunoori)  
🔗 **LinkedIn**: [Sneha Edugunoori](https://www.linkedin.com/in/sneha-edugunoori)  
```
