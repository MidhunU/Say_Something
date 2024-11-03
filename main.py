import streamlit as st
import random

# Set the title of the app
st.title("Say Something App")

# Create a text input for the user's question
user_question = st.text_input("Type your question here:")

# Generate a random response based on user input
if user_question:
    # Simulate an AI response by selecting a random response
    ai_responses = [
        "That's an interesting question!",
        "I'm not sure, but I'll think about it.",
        "Can you ask something else?",
        "Let me get back to you on that."
    ]
    ai_response = random.choice(ai_responses)
    st.write("AI Response:", ai_response)
else:
    st.write("Please enter a question to get a response.")

# Attach the Groq API key
api_key = "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"
st.write("API Key attached successfully.")
# Generate a random funny question
funny_questions = [
    "Why don't scientists trust atoms?",
    "Why did the scarecrow win an award?",
    "Why don't skeletons fight each other?",
    "What do you call fake spaghetti?",
    "Why was the math book sad?"
]

# Generate a random funny answer
funny_answers = [
    "Because they make up everything!",
    "Because he was outstanding in his field!",
    "They don't have the guts.",
    "An impasta!",
    "It had too many problems."
]

if st.button("Ask a random funny question"):
    random_question = random.choice(funny_questions)
    st.write("Question:", random_question)
    random_answer = funny_answers[funny_questions.index(random_question)]
    st.write("Answer:", random_answer)