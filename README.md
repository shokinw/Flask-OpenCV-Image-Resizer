🖼️ Image Resizer Web App (Flask + OpenCV)

This is a simple web application that allows users to upload an image and resize it by entering custom width and height values. The image processing is handled using OpenCV, and the web interface is built with Flask.

I built this project to understand how backend image processing works and how OpenCV can be integrated into a web application.

💡 What This Project Does

Upload an image from your computer

Enter desired width and height

Resize the image using OpenCV

Download the resized version instantly<img width="1919" height="790" alt="Screenshot 2026-02-21 062425" src="https://github.com/user-attachments/assets/75af0ace-2623-4063-986e-a88e231b3a95" />



🛠 Tech Used

Python

Flask

OpenCV (cv2)

NumPy

HTML

📂 Project Structure
Flask-OpenCV-Image-Resizer/
│
├── app.py
├── requirements.txt
├── static/uploads/
└── templates/index.html
⚙️ How To Run This Project
<img width="1910" height="997" alt="Screenshot 2026-02-21 062530" src="https://github.com/user-attachments/assets/c32f7fe4-7337-415a-9e90-8f902a281c57" />


Clone the repository

git clone https://github.com/showkinw/Flask-OpenCV-Image-Resizer.git

Go inside the project folder

cd Flask-OpenCV-Image-Resizer

Create virtual environment

python -m venv venv

Activate it
Windows:

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the app

python app.py

Open browser and go to

http://127.0.0.1:5000
🧠 What I Learned

Handling file uploads in Flask

Working with image processing using OpenCV

Connecting frontend form data with backend logic

Managing project structure properly

🚀 Future Improvements

Maintain aspect ratio automatically

Add image preview before download

Add drag & drop upload

Deploy it online

👩‍💻 About Me

Samridhi Sharma
B.Tech CSE | AI & ML Enthusiast
Interested in building practical Python-based applications.
