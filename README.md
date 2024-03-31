# Unit Test Script for Spam Classification Docker Container

This repository contains a Python script (`test.py`) for unit testing a spam classification Docker container. This README file provides a comprehensive explanation of the script's functionality, dependencies, execution steps, and breakdown of key functions.

## Functionality

The `test.py` script performs the following actions:

1. **Launches the Docker Container:**
   - It executes necessary commands to launch the Docker container named "spam-classifier".

2. **Sends a Sample Email for Classification:**
   - It constructs a sample email with spammy characteristics.
   - It sends the email to the container's API endpoint (`http://127.0.0.1:5000/score`) for spam classification.

3. **Verifies the API Response Structure:**
   - It processes the response received from the container's API.
   - It asserts that the response structure adheres to expectations, including:
     - Presence of a key named `prediction` with an integer value (0 for Not Spam, 1 for Spam).
     - Presence of a key named `propensity` with a float value representing the spam probability.

4. **Handles Potential Exceptions:**
   - It incorporates exception handling to gracefully handle potential errors during the request process, such as network issues or unexpected responses.

5. **Stops and Removes the Launched Container:**
   - After test completion, the script executes commands to stop and remove the launched container (assuming it exists).

## Dependencies

The script relies on the following external libraries:

- `pytest` (testing framework)
- `joblib` (model persistence/loading)
- `os` (operating system interaction)
- `requests` (HTTP requests)
- `threading` (threading functionalities)
- `subprocess` (subprocess execution)
- `time` (timing functions)
- `score` (custom module for spam classification logic - assumed to be in the same directory)

**Note:** Ensure these libraries are installed in your Python environment before running the tests.



# Explanation of Pre-commit Hook Shell Script

This shell script serves as a pre-commit hook in a Git repository. It ensures that tests are run before any commit is made, but specifically on the "main" branch. Below is a breakdown of its functionality:

1. **Get the Current Active Branch Name:**
   - The script retrieves the name of the currently active branch using the command:
     ```bash
     current_branch=$(git branch | grep '*' | sed 's/* //')
     ```
   - It uses `git branch` to list all branches, `grep` to find the branch marked with '*', indicating the active branch, and `sed` to extract only the branch name.

2. **Check the Current Branch:**
   - The script checks if the current branch is "main" using:
     ```bash
     if [ "$current_branch" = "main" ]; then
     ```
   - This condition ensures that the tests are only run if the current branch is "main".

3. **Informative Message:**
   - Before running the tests, the script prints an informative message indicating the branch being tested:
     ```bash
     echo "Running tests on branch: $current_branch"
     ```

4. **Run Tests:**
   - The script executes the test script (assumed to be named "test.py"):
     ```bash
     python test.py
     ```
   - Replace "test.py" with the actual filename if different.

5. **Handle Test Results:**
   - After executing the tests, the script checks the exit status:
     ```bash
     if [ $? -ne 0 ]; then
     ```
   - If the exit status is non-zero, it means the tests failed. The script prints a warning message and exits with a non-zero status:
     ```bash
     echo "Tests FAILED! Fix errors before committing."
     exit 1
     ```
   - If the exit status is zero, indicating the tests passed, the script prints a success message:
     ```bash
     echo "Tests PASSED."
     ```

**Note:** Ensure that this script is located in the `.git/hooks` directory of your Git repository and is named `pre-commit`. Also, make it executable using `chmod +x pre-commit`.

