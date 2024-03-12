import joblib
import sklearn
import score
import pytest

log_reg_model = joblib.load("logistic_reg.pkl")
text = "Subject: do not have money , get software cds from here !  software compatibility . . . . ain ' t it great ?  grow old along with me the best is yet to be .  all tradgedies are finish ' d by death . all comedies are ended by marriage ."
threshold = 0.55

class TestScore:

    expected_input_format = (str, sklearn.linear_model._logistic.LogisticRegression, float)
    expected_output_format = (bool, float)

    def test_smoke(self):
        try:
            # Call the score function with the provided parameters
            output = score.score(text, log_reg_model, threshold)
            # Check if the output is not None
            assert output is not None
        
        except Exception as e:
            # Print the exception for debugging purposes
            print(f"Exception occurred: {e}")
            # Return False if any exception occurs
            return False
        
    def test_format(self):
        sample_input = (text, log_reg_model, threshold)
        sample_input_format = tuple(type(input_) for input_ in sample_input)
        
        assert sample_input_format == self.expected_input_format, "Input format does not match expected format."
        
        try:
            output = score.score(*sample_input)
            output_format = tuple(type(item) for item in output)
            
            assert output_format == self.expected_output_format, "Output format does not match expected format."
            
        except Exception:
            return None

    def test_prediction(self):
        output = score.score(text, log_reg_model, threshold)
        prediction = output[0]
        assert prediction in (0, 1)
    
    def test_propensity(self):
        output = score.score(text, log_reg_model, threshold)
        propensity = output[1]
        assert propensity >= 0 and propensity <= 1
    
    def test_threshold_0(self):
        threshold = 0
        output = score.score(text, log_reg_model, threshold)
        prediction = output[0]
        assert prediction == 1
    
    def test_threshold_1(self):
        threshold = 1
        output = score.score(text, log_reg_model, threshold)
        prediction = output[0]
        assert prediction == 0
    
    def test_spam_input(self):
        spam_input = "Subject: save your money buy getting this thing here  you have not tried cialls yet ?  than you cannot even imagine what it is like to be a real man in bed !  the thing is that a great errrectlon is provided for you exactly when you want .  ciaiis has a iot of advantaqes over viagra  - the effect iasts 36 hours !  - you are ready to start within just 10 minutes !  - you can mix it with aicohol ! we ship to any country !  get it riqht now ! . "
        output = score.score(spam_input, log_reg_model, threshold)
        prediction = output[0]
        assert prediction == 1
    
    def test_non_spam_input(self):
        non_spam_input = "Just wanted to follow up on our conversation from yesterday. I've attached the document you requested. Let me know if you need anything else."
        output = score.score(non_spam_input, log_reg_model, threshold)
        prediction = output[0]
        assert prediction == 0


import os
import requests

def test_flask():
    # Launch the Flask app
    os.system("python app.py &")

    # Test the response from the localhost endpoint
    response = requests.post('http://127.0.0.1:5000', data={'text': 'Subject: want to accept credit cards ? 126432211  aredit cpproved  no cecks  do it now  126432211', 'threshold': 0.50})
    assert response.status_code == 200
    data = response.json()
    assert 'prediction' in data
    assert 'propensity' in data

    # Close the Flask app
    os.system("pkill -f 'python app.py'")