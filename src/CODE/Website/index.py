from flask import Flask, render_template, Response
from camera import gen_frames

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/designer/')
def designer():
    return render_template("designer.html")

@app.route('/stats/')
def stats():
    return render_template("stats.html")

# Convert to function that reads images from ROS message
@app.route('/video_feed/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
