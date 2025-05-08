from flask import Flask, request, render_template
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""
    if request.method == "POST":
        audio = request.files["audio_file"]
        if audio:
            file_path = os.path.join("uploads", audio.filename)
            os.makedirs("uploads", exist_ok=True)
            audio.save(file_path)
            result = model.transcribe(file_path)
            transcription = result["text"]
            os.remove(file_path)
    return render_template("index.html", transcription=transcription)

if __name__ == "__main__":
    app.run(debug=True)
