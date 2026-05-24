"""Flask server app."""
from flask import Flask, request
import EmotionDetection.emotion_detection as ed

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_api():
    """Return emotion analysis for a given text."""
    text_to_analyze = request.args.get("textToAnalyze")

    result = ed.emotion_detector(text_to_analyze)
    if not text_to_analyze or result is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
