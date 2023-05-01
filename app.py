import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
from googletrans import LANGUAGES,Translator

def analyze_sentiment(text):
    '''
    Function to analyze the sentiment of the transcribed text
    '''
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def highlight_keywords(text, keywords):
    '''
    Function to highlight specific keywords in the transcribed text
    '''
    formatted_text = text
    for keyword in keywords:
        formatted_text = formatted_text.replace(keyword, f"<span style='background-color: yellow;'>{keyword}</span>")
    return formatted_text

def word_freq(text):
    '''
    Function to count the frequency of each word in the transcribed text
    '''
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def translate_text(text, language):
    '''
    Function to translate the transcribed text into another language
    '''
    translator = Translator()
    translated = translator.translate(text, dest=language)
    return translated.text

def app():
    # Set the title of the app
    st.title("Real-time Speech to Text with Sentiment Analysis, Word Frequency Analysis, and Translation")

    # Get the user's chosen keywords to highlight
    keywords_input = st.text_input("Enter keywords to highlight (comma-separated):")
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    # Get the user's chosen language for translation
    language_input = st.selectbox("Select a language for translation:", list(LANGUAGES.values()))
    # language_dict = {"": "", "Spanish": "es", "French": "fr", "German": "de", "Italian": "it", "Japanese": "ja"}
    # language_code = language_dict[language_input]

    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust the microphone sensitivity
        r.adjust_for_ambient_noise(source)

        # Create a button to start and stop recording
        if st.button("Start Recording"):
            st.write("Speak now...")

            # Continuously listen for audio input
            while True:
                # Listen for audio input
                audio = r.listen(source)

                # Use the speech recognition library to transcribe the audio
                try:
                    text = r.recognize_google(audio)
                    formatted_text = highlight_keywords(text, keywords)
                    st.write(f"Transcription: {formatted_text}", unsafe_allow_html=True)
                    sentiment = analyze_sentiment(text)
                    st.write(f"Sentiment: {sentiment}")

                    if language_input:
                        translated_text = translate_text(text, language_input)
                        st.write(f"Translation: {translated_text}")

                    word_count = word_freq(text)
                    st.write("Word Frequency:")
                    for word, count in word_count.items():
                        st.write(f"{word}: {count}")

                except sr.UnknownValueError:
                    st.write("Sorry, I cannot hear you")
                except sr.RequestError as e:
                     st.write(f"Sorry, there was an error processing your request: {e}")
                if st.button("Stop Recording"):
                    break

if __name__ == '__main__':
    app()