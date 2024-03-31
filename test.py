import pytest
import joblib
import os
import requests
import threading
import subprocess
import time
from score import score


def test_docker():
    """Tests the spam classification Docker container."""
    sample_email = "wow, you won a prize of 100 lakhs please fill below form to avail the money."
    spam_threshold = 0.5

    try:
        # Launch the container
        build_spam_classifier()
        launch_spam_classifier()

        print('Sending Request')
        payload = {'text': sample_email, 'threshold': spam_threshold}
        response = requests.post('http://127.0.0.1:5000/score', json=payload)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()

        # Check if the response contains 'prediction' and 'propensity' keys and values int and float respectively
        assert 'prediction' in data and isinstance(data['prediction'], int)
        assert 'propensity' in data and isinstance(data['propensity'], float)

        prediction = data['prediction']
        propensity = data['propensity']
        print(f"Prediction: {prediction}, Propensity: {propensity}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending request to container: {e}")
        # Log the error for further investigation
        with open("test_results.txt", "a") as f:
            f.write(f"Test failed! Error: {e}\n")
    finally:
        # Stop the container (considering adding logic to check if container exists)
        subprocess.run(["docker", "stop", "spam_container"], check=True)
        subprocess.run(["docker", "rm", "spam_container"], check=True)


def build_spam_classifier():
    """Builds the Docker image named 'spam-classifier'."""
    subprocess.run(["docker", "build", "-t", "spam-classifier", "."])


def launch_spam_classifier():
    """Runs the built image in a detached mode."""
    subprocess.run(["docker", "run", "-d", "-p", "5000:5000", "--name", "spam_container", "spam-classifier"])