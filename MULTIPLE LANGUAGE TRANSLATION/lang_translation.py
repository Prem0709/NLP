import streamlit as st
import pandas as pd
import os
import base64
import pyttsx3
from mtranslate import translate
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# Download NLTK data
nltk.download('punkt')
nltk.download('words')

# Load language dataset
def load_language_data():
    df = pd.read_csv(r'C:\Users\pawar\data_science\Project\NLP project\.MULTIPLE LANGUAGE TRANSLATION\language.csv')
    df.dropna(inplace=True)
    lang = df['name'].to_list()
    lang_code = df['iso'].to_list()
    lang_dict = {lang[i]: lang_code[i] for i in range(len(lang_code))}
    return lang, lang_code, lang_dict

# Generate download link for audio
def generate_audio_download_link(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

# Text-to-Speech with gender selection
def read_aloud(text, language='en', voice_gender='female'):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        # Select voice based on gender (fallback to default if not available)
        if voice_gender.lower() == 'male' and len(voices) > 0:
            engine.setProperty('voice', voices[0].id)  # Typically male voice
        elif len(voices) > 1:
            engine.setProperty('voice', voices[1].id)  # Typically female voice
        
        # Set speech properties
        engine.setProperty('rate', 150)  # Speech speed
        engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # Save audio to file
        audio_file_path = "translated_audio.mp3"
        engine.save_to_file(text, audio_file_path)
        engine.runAndWait()
        
        with open(audio_file_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
        
        return audio_bytes, audio_file_path
    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")
        return None, None

# Translate and generate audio
def translate_and_generate_audio(input_text, target_language_code, gender='female'):
    try:
        translated_text = translate(input_text, target_language_code)
        audio_bytes, audio_file_path = read_aloud(translated_text, language=target_language_code, voice_gender=gender)
        return translated_text, audio_bytes, audio_file_path
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None, None, None

# Generate Word Cloud
def generate_word_cloud(text):
    try:
        # Tokenize and filter English words (or use all words if non-English)
        english_words = set(words.words())
        tokens = word_tokenize(text.lower())
        filtered_words = [word for word in tokens if word.isalpha() and (word in english_words or not text.isascii())]
        filtered_text = ' '.join(filtered_words) if filtered_words else text

        # Generate word cloud with enhanced styling
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis',
            max_words=100,
            font_path=None,  # Use default font or specify path if needed
            min_font_size=10,
            max_font_size=100
        ).generate(filtered_text)

        # Create plot
        buffer = BytesIO()
        plt.figure(figsize=(8, 4), dpi=100)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(buffer, format='png', bbox_inches='tight')
        plt.close()
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"Error generating word cloud: {str(e)}")
        return None

# Main app
def main():
    st.set_page_config(page_title="Globalize: Language Translation", layout="wide")
    st.title("🌍 Globalize: Language Translation + TTS + Word Cloud")

    lang, lang_code, lang_dict = load_language_data()

    input_text = st.text_area("Enter text to translate", height=80)
    selected_language = st.sidebar.selectbox("🌐 Select target language", lang)
    gender_choice = st.sidebar.radio("🔈 TTS Voice", ['Female', 'Male'])

    if input_text:
        target_lang_code = lang_dict[selected_language]
        translated_text, audio_bytes, audio_file_path = translate_and_generate_audio(input_text, target_lang_code, gender_choice)

        if translated_text and audio_bytes:
            st.subheader("✅ Translated Text")
            st.text_area("", translated_text, height=150)

            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("🔉 Audio Output")
                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(generate_audio_download_link(audio_file_path, 'Audio File'), unsafe_allow_html=True)

            with col2:
                st.subheader("☁️ Word Cloud")
                img_buffer = generate_word_cloud(translated_text)
                if img_buffer:
                    st.image(img_buffer, use_column_width=True)
        else:
            st.error("❌ Error occurred during translation or audio generation.")

if __name__ == "__main__":
    main()