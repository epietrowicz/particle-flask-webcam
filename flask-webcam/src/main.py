from flask import Flask, Response, render_template, request
from camera import generate_frames

app = Flask(__name__)


@app.route("/")
def home():
    real_ip = request.headers.get("CF-Connecting-IP", request.remote_addr)
    print(f"Real IP: {real_ip}")
    return render_template("index.html")


@app.route("/video-capture")
def video_capture():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
