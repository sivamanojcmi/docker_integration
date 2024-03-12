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

## Usage

1. **Training the Model**: Run the `train.ipynb` notebook to train the logistic regression model using the provided dataset and save it as a pickle file (`logistic_reg.pkl`).

2. **Scoring Text Messages**: 
   - Use the `score.score()` function from `score.py` module to score individual text messages.
   - Alternatively, launch the Flask application using `python app.py` and send HTTP POST requests to the `/score` endpoint with JSON data containing the 'text' field.

3. **Testing**: Run the unit tests and integration tests using `pytest` to ensure the correctness of the scoring function and Flask application.
