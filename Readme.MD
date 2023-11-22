# Open Trivia Quiz Game

This is a simple Open Trivia Quiz Game implemented in Python using the Streamlit library. It fetches questions from the Open Trivia Database API, presents them to the user, and provides feedback on their answers.

## Features

- Fetches 10 questions from the Open Trivia Database API.
- Allows the user to choose their answers (True/False) for each question.
- Displays the quiz results, showing the total score and details for each question.
- Provides a "Refresh" button to restart the quiz with new questions.

## Usage

1. Ensure you have Python installed on your machine.
2. Install the required libraries by running:

    ```bash
    pip install requests json streamlit
    ```

3. Run the script:

    ```bash
    streamlit run your_script_name.py
    ```

4. Interact with the quiz, choose your answers, and click the "Submit" button to see the results.
5. Use the "Refresh" button to restart the quiz with new questions.

## Dependencies

- [requests](https://docs.python-requests.org/en/latest/) - For making HTTP requests to fetch quiz questions.
- [json](https://docs.python.org/3/library/json.html) - For working with JSON data.
- [streamlit](https://docs.streamlit.io/en/stable/) - For building interactive web applications with Python.

## Notes

- The background color of the app is set using custom CSS in the `st.markdown` function.
- The quiz results are displayed using Streamlit components like `st.title`, `st.text`, `st.subheader`, and `st.write`.
- The "Refresh" button resets the session state, allowing users to take the quiz again with new questions.

Feel free to modify and customize the code according to your preferences or add more features to enhance the quiz experience!