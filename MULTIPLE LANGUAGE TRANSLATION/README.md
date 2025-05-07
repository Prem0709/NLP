### 📄 `README.md`

```markdown
# 🌍 MultiLingo

**MultiLingo** is an interactive web application that allows users to translate text into multiple languages,
 generate audio output using text-to-speech (TTS), and visualize translated content using Word Clouds.
 Built using Python and Streamlit, this tool is ideal for learners, travelers, educators,
 and anyone needing fast multilingual translation with audio and visual enhancements.

---

## 📌 Features

- 🔤 **Multiple Language Translation** using `mtranslate`
- 🔊 **Text-to-Speech (TTS)** with gender selection using `pyttsx3`
- ☁️ **Word Cloud Visualization** using `wordcloud` and `matplotlib`
- 💾 **Downloadable Audio Output** as MP3
- 📄 **Streamlit Interface** for ease of use

---

## 🛠️ Tech Stack

| Component         | Description                                |
|------------------|--------------------------------------------|
| `Streamlit`      | Frontend Web App Framework                 |
| `mtranslate`     | Lightweight translation API wrapper        |
| `pyttsx3`        | Offline text-to-speech engine              |
| `NLTK`           | Natural Language Toolkit for tokenizing    |
| `WordCloud`      | Generates word clouds from translated text |
| `Matplotlib`     | Used to render word clouds as images       |
| `Pandas`         | Loads language data from CSV               |
| `Base64`         | Encodes audio for download link generation |

---

## 📁 File Structure

```

.
├── app.py                   # Main Streamlit app file
├── language.csv             # Language name and ISO code dataset
├── translated\_audio.mp3     # Generated audio file (runtime)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

````

---

## 📌 How It Works

### 1. **Load Language Dataset**
- Reads `language.csv` containing language names and ISO codes.
- Constructs a language dictionary for dropdown selection.

### 2. **Translate Text**
- Uses `mtranslate.translate()` to convert input text into the selected language.

### 3. **Generate Audio**
- Uses `pyttsx3` to convert translated text to audio.
- User can select male/female TTS voice.
- Audio is saved as `translated_audio.mp3`.

### 4. **Generate Word Cloud**
- Tokenizes translated text using `nltk`.
- Filters meaningful words (English or unicode).
- Generates and displays a styled word cloud.

---

## ✅ Usage Guide

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
````

### Step 2: Run the App

```bash
streamlit run app.py
```

### Step 3: Interact

* Enter text to translate.
* Choose a target language.
* Pick a voice (male/female).
* View translated text, listen to audio, and visualize a word cloud.
* Download the audio file if needed.

---

## 🧠 Notes & Considerations

* **Offline TTS**: `pyttsx3` works offline, but voices depend on OS support.
* **Translation Accuracy**: `mtranslate` uses unofficial APIs; may vary in quality.
* **Unicode Support**: Non-English text may render inconsistently in word cloud.
* **Voice IDs**: Voice selection may differ across systems (Windows/Linux/Mac).
* **Audio Format**: Only `.mp3` is used. Other formats require TTS engine changes.

---

## 📌 Future Enhancements

* 🔗 Switch to official Google Translate or DeepL API for reliable translations.
* 🎙️ Use cloud TTS (Google, Amazon Polly) for multilingual speech support.
* 🧠 Add language detection using `langdetect` or `TextBlob`.
* 📱 Make responsive for mobile using Streamlit’s layout enhancements.
* 📝 Enable saving translation history.

---

## 🙌 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [NLTK](https://www.nltk.org/)
* [WordCloud](https://github.com/amueller/word_cloud)
* [pyttsx3](https://pyttsx3.readthedocs.io/)
* [mtranslate](https://pypi.org/project/mtranslate/)

---

## ✨ Project By

**Prem Pawar**
B.Tech | Data Science & Prompt Engineering
GitHub: [Prem0709](https://github.com/Prem0709)

```
