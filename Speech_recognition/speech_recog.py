import streamlit as st
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        st.info("Listening... Speak for up to 1 minute.")
        audio = r.listen(source, timeout=60)  # Set a timeout of 60 seconds (1 minute)
    return audio

def convert_voice_to_text(audio, language="en-US"):
    st.info("Transcribing speech...")
    try:
        text = r.recognize_google(audio, language=language)
        st.success("Transcription complete!")
        st.write("Transcribed Text:")
        st.write(text)  # Display the transcribed text

        if st.button("Save to Text File"):
            save_text_to_file(text)

    except sr.UnknownValueError:
        st.error("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Web Speech API; {e}")

def save_text_to_file(text):
    with st.file_uploader("Save the transcription as a text file", type=["txt"], key="text_file") as text_file:
        if text_file:
            text_file.write(text)

def main():
    st.title("Voice to Text Conversion")
    st.write("Click the 'Start' button to convert your voice to text.")
    st.write("You have 1 minute to speak. Click 'Stop' to end the recording.")
    st.info("Select the language (if known).")

    language = st.selectbox("Select language", ["en-US", "es-ES", "fr-FR"])
    audio = None

    if st.button("Start"):
        audio = capture_voice_input()
        convert_voice_to_text(audio, language)

if __name__ == "__main__":
    main()
