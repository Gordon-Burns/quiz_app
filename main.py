import requests
import json
import streamlit as st


def fetch_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean')
    response_text = response.text
    return json.loads(response_text).get('results', [])


def quiz_app():
    st.title("Open Trivia Quiz Game")

    # Check if questions are already in session state, if not, fetch them
    if 'questions' not in st.session_state:
        st.session_state.questions = fetch_questions()

    score = 0
    user_choices = []

    for i, question in enumerate(st.session_state.questions, 1):
        st.subheader(f"Question {i}: {question['question']}")
        user_choice = st.radio("Choose your answer:", ["True", "False"], key=f"question{i}")
        user_choices.append({'question': question['question'], 'user_choice': user_choice,
                             'correct_answer': question['correct_answer']})

    # Display submit button
    if st.button("Submit"):
        st.empty()
        # Calculate the score
        for choice in user_choices:
            if choice['user_choice'] == choice['correct_answer']:
                score += 1

        # Display results
        st.warning('Scroll down to see your results')
        st.title("Quiz Results")
        st.text(f"Total Score: {score}/{len(st.session_state.questions)}")

        st.subheader("Details:")
        for i, choice in enumerate(user_choices, 1):
            st.write(f"Question {i}: {choice['question']}")
            st.write(f"Your Answer: {choice['user_choice']}")
            st.write(f"Correct Answer: {choice['correct_answer']}")
            st.write("---")

        # Mark quiz as completed
        st.session_state.quiz_completed = True



if __name__ == "__main__":
    # Set the background color
    st.set_page_config(page_title="Open Trivia Quiz", page_icon="✅", layout="centered", initial_sidebar_state="expanded")
    # Custom CSS for setting the background color



    # Check if the "Refresh" button was clicked
    refresh_button_clicked = st.sidebar.button("Refresh")

    # Reset session_state to restart the quiz if "Refresh" is clicked
    if refresh_button_clicked:
        st.session_state.pop('questions', None)
        st.session_state.pop('quiz_completed', None)

    # Run the quiz app
    quiz_app()
