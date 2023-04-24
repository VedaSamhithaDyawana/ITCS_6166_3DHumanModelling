import streamlit as st
import speech_recognition as sr

def app():
    # Set the title of the app
    st.title("Speech to Text")

    # Create a button to start recording
    if st.button("Start Recording"):
        # Initialize the recognizer
        r = sr.Recognizer()

        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            # Adjust the microphone sensitivity
            r.adjust_for_ambient_noise(source)

            # Prompt the user to speak
            st.write("Speak now...")

            # Listen for audio input
            audio = r.listen(source)

        # Use the speech recognition library to transcribe the audio
        try:
            text = r.recognize_google(audio)
            keywords = ["important", "highlight", "focus"]  # List of keywords to highlight
            formatted_text = text
            for keyword in keywords:
                formatted_text = formatted_text.replace(keyword, f"<span style='background-color: yellow;'>{keyword}</span>")
            st.write(f"Transcription: {formatted_text}", unsafe_allow_html=True)
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            st.write(f"Sorry, there was an error processing your request: {e}")
if __name__ == '__main__':
    app()