from flask import Flask, request, render_template, jsonify
import os, base64, time
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/documents")
def documents():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("documents.html", files=files)

@app.route("/upload_documents", methods=["POST"])
def upload_documents():
    user_id = request.form.get("user_id")
    remark = request.form.get("remark")
    images = []
    for i in range(1, 3):
        img_data = request.form.get(f"image{i}")
        if img_data:
            img_bytes = base64.b64decode(img_data.split(",")[-1])
            filename = f"{UPLOAD_FOLDER}/{user_id}_{i}_{int(time.time())}.jpg"
            with open(filename, "wb") as f:
                f.write(img_bytes)
            images.append(filename)
    return jsonify({"status": "success", "saved": len(images)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
