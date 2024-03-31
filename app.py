from flask import Flask, request, jsonify

# Assume 'score' module contains the score function
import score
import joblib
import warnings
import pytest

warnings.filterwarnings("ignore")

with open("logistic_reg.pkl", "rb") as model_file:
    model = joblib.load(model_file)

app = Flask(__name__)

# Define a function for input validation
def is_valid_input(text, threshold):
    if not text.strip():
        return False, "Text input cannot be empty."
    try:
        threshold = float(threshold)
        if threshold < 0 or threshold > 1:
            raise ValueError("Threshold must be between 0 and 1.")
    except ValueError:
        return False, "Threshold must be a valid number between 0 and 1."
    return True, ""

@app.route("/", methods=["GET", "POST"])
def score_endpoint():
    if request.method == "POST":
        text = request.form.get("text", "")
        threshold = request.form.get("threshold", "")
        
        # Validate input
        is_valid, error_message = is_valid_input(text, threshold)
        if not is_valid:
            return jsonify({"error": error_message})

        # Get the prediction and propensity score from the score function
        prediction, propensity = score.score(text, model, float(threshold))

        # Response in JSON format
        response = {
            "prediction": int(prediction),
            "propensity": float(propensity)
        }
        return jsonify(response)

    elif request.method == "GET":
        # HTML format inside Flask code
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Spam Classifier</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        flex-direction: column; /* Added */
                    }
                    h1 {
                        text-align: center;
                        margin-top: 20px; /* Adjusted */
                    }
                    form {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1>Spam Classifier</h1>
                <form action="/" method="post">
                    <label for="text">Enter Text:</label><br>
                    <input type="text" id="text" name="text"><br><br>
                    <label for="threshold">Threshold:</label><br>
                    <input type="number" id="threshold" name="threshold" step="0.01" min="0" max="1"><br><br>
                    <input type="submit" value="Predict">
                </form>
            </body>
            </html>
        """

if __name__ == "_main_":
    # Run the app
    app.run(debug=True, host = "0.0.0.0", port = 5000)