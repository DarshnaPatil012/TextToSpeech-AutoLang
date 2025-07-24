# TextToSpeech-AutoLang

# 🗣️ Text-to-Speech Converter with Language Auto-Detection

This Python project reads text from a file (`sample.txt`), **automatically detects the language**, and **converts it into speech** using the [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/) library.

🎧 The output is saved as an `MP3` file (`sound.mp3`) and played instantly.

---

## 📌 Features

- ✅ Reads text from a `.txt` file
- 🌐 Detects language automatically using `langdetect`
- 🎤 Converts the detected language text into speech
- 💽 Saves the audio as an MP3 file
- ▶️ Automatically plays the audio on your device
- 🌍 Supports multiple languages (English, Hindi, Marathi, French, German, Gujarati, etc.)

---

## 🛠️ Requirements

Make sure you have Python installed. Then, install the following libraries:

```bash
pip install gTTS langdetect
