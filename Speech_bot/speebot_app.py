import streamlit as st
import speech_recognition as sr
import random

def speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("Please speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Google Speech Recognition could not understand the audio.")
    except sr.RequestError:
        st.write("Could not request results from Google Speech Recognition service.")

PATTERNS = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "how are you": ["I'm a computer program, so I don't have feelings, but thanks for asking!", "I'm doing well, how can I assist you today?"],
    # Add more patterns here...
}

# Tokenizing function
def preprocess_text(text):
    return text.lower().split()

def chatbot_function(user_input):
    tokenized_input = preprocess_text(user_input)
    for pattern, responses in PATTERNS.items():
        tokenized_pattern = preprocess_text(pattern)
        if any(word in tokenized_input for word in tokenized_pattern):
            return random.choice(responses)
    return "I'm sorry, I didn't understand that. Could you rephrase, please?"

st.title('Speebot: Speech-Enabled Chatbot')
user_input = ""

st.sidebar.write("Choose Input Method:")
option = st.sidebar.radio('', ('Text', 'Speech'))

if option == 'Text':
    user_input = st.text_input("You:")
    if st.button('Send'):
        response = chatbot_function(user_input)
        st.write(f"Bot: {response}")
elif option == 'Speech':
    if st.button('Start Speaking'):
        user_input = speech_to_text()
        st.write(f"You said: {user_input}")
        response = chatbot_function(user_input)
        st.write(f"Bot: {response}")