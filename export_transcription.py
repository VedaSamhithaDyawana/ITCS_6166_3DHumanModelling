import streamlit as st
import speech_recognition as sr
from io import BytesIO

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
            st.write(f"You said: {text}")
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            st.write(f"Sorry, there was an error processing your request: {e}")
        
        # Create a button to export the transcription
        if st.button("Export Transcription"):
            # Create a file name for the export file
            file_name = "transcription.txt"

            # Create a BytesIO object to hold the transcription text
            buffer = BytesIO()
            buffer.write(text.encode())

            # Set the cursor position to the beginning of the buffer
            buffer.seek(0)

            # Send the buffer to the browser with appropriate headers
            st.download_button(
                label="Download Transcription",
                data=buffer,
                file_name=file_name,
                mime="text/plain"
            )
if __name__ == '__main__':
    app()