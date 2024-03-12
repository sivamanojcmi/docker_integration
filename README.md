# Spam Detection Project

This project aims to develop a spam detection system using machine learning techniques. The system is designed to classify incoming messages as either spam or non-spam (ham).

## Model Selection

For this project, the TF-IDF vectorization and logistic regression models were chosen based on the results obtained in the initial assignment. In the first assignment, these models demonstrated superior performance compared to other alternatives. Therefore, they were selected for implementation in this project.

Specifically, logistic regression was directly utilized in the `train.ipynb` notebook. It was identified as the most effective model based on the evaluation results from the first assignment.

## File Descriptions

- `app.py`: Flask application that exposes an API endpoint for scoring text messages for spam.
- `score.py`: Module containing the scoring function for text messages using the trained model.
- `test.py`: Contains unit tests and integration tests for the scoring function and Flask application.
- `train.ipynb`: Jupyter Notebook used for training the logistic regression model and saving it as a pickle file.
- `coverage.txt`: The coverage report provides insights into the percentage of code covered by tests, helping evaluate the comprehensiveness of the test suite. It shows the number of statements (Stmts) in each file, the number of statements missed (Miss), and the coverage percentage (Cover). 

## Functions and Test Cases

### `score.py`

This module contains functions for preprocessing text data and scoring it using a trained model.

#### Functions:

#### `preprocess_text(text: str) -> List[str]`

Preprocesses the input text by converting it to lowercase, removing punctuation, numbers, and stop words, tokenizing it, and performing lemmatization.

- `text`: Input text string.
- Returns a list of preprocessed tokens.

#### `score(text: str, model, threshold: float) -> Tuple[bool, float]`

Scores the input text using the provided model and threshold.

- `text`: Input text string.
- `model`: Trained model object.
- `threshold`: Threshold value for prediction.
- Returns a tuple containing the prediction (True for spam, False for non-spam) and the propensity score.

### `test.py`

This module contains unit tests for the functions in the `score.py` module.

#### Test Cases:

- `TestScore.test_smoke()`: Tests if the `score` function returns a non-None output.
- `TestScore.test_format()`: Tests if the input and output formats of the `score` function match the expected formats.
- `TestScore.test_prediction()`: Tests if the prediction output of the `score` function is either 0 or 1.
- `TestScore.test_propensity()`: Tests if the propensity score output of the `score` function is between 0 and 1.
- `TestScore.test_threshold_0()`: Tests if the `score` function returns a prediction of 1 when the threshold is set to 0.
- `TestScore.test_threshold_1()`: Tests if the `score` function returns a prediction of 0 when the threshold is set to 1.
- `TestScore.test_spam_input()`: Tests the `score` function with a sample spam input.
- `TestScore.test_non_spam_input()`: Tests the `score` function with a sample non-spam input.

#### Integration Test

- `test_flask()`: Integration test that launches the Flask app using the command line, tests the response from the localhost endpoint, and closes the Flask app using the command line.

### `app.py`

This module contains the implementation of a Flask API for scoring text data using a trained model.

### API Endpoints

#### `POST /`

Accepts text input and an optional threshold for prediction. Returns a JSON response containing the prediction and propensity score.

#### Request Parameters:

- `text`: Text input string.
- `threshold`: (Optional) Threshold value for prediction (default is 0.5).

#### Example Request:

```http
POST / HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "text": "Your text input here",
    "threshold": 0.5
}
