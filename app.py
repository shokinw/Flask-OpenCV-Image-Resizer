from flask import Flask, render_template, request, send_file
import cv2
import os
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resize", methods=["POST"])
def resize_image():
    file = request.files["image"]
    width = int(request.form["width"])
    height = int(request.form["height"])

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    resized = cv2.resize(img, (width, height))

    output_path = os.path.join(UPLOAD_FOLDER, "resized_" + file.filename)
    cv2.imwrite(output_path, resized)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)