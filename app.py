from flask import Flask, render_template, request, send_from_directory
import os
from watermark import add_text_watermark

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    filename = None

    if request.method == "POST":

        file = request.files.get("image")
        text = request.form.get("watermark", "")

        if file and file.filename != "":

            input_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            output_filename = "watermarked_" + file.filename
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_filename)

            file.save(input_path)

            add_text_watermark(input_path, output_path, text)

            filename = output_filename

    return render_template("index.html", filename=filename)


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/outputs/<filename>")
def output_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
