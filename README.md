# voice-enabled-cursor

**Voice Enabled Cursor** 🎤🖱️  
A system that takes voice input, changes it to text, uses an LLM to do tasks like read or write files, and speaks the result back.  

---

## 📌 Project Description  

This system provides a **voice-driven interaction loop** for executing tasks via an LLM:  

- 🎤 **Voice Input** – User provides a spoken command.  
- 📝 **Speech-to-Text** – The audio input is transcribed into text.  
- 🤖 **LLM Invocation** – The transcribed text is passed to an LLM, which interprets the command and executes the required task (e.g., reading/writing a file).  
- 📄 **Task Output** – The LLM generates the textual result of the executed task.  
- 🔊 **Text-to-Speech** – The textual output is synthesized into natural speech.  
- 🔁 **Continuous Loop** – The cycle repeats for subsequent commands, enabling hands-free, voice-controlled system interaction.

---

## 🛠️ Tech Stack Used

- **Programming Language:** Python  
- **Libraries / Frameworks:**  
  - `SpeechRecognition` – For converting speech to text  
  - `pyaudio` – For microphone input support  
  - `pyttsx3` – For text-to-speech output  
  - `langchain` – For LLM integration  
  - `langchain-google-genai` – For Google Gemini model access  
  - `langgraph` – For agent task graph orchestration
  - `python-dotenv` – For environment variable management  
  - `pymongo` – For MongoDB checkpointing with LangGraph  

---

## ⚙️ Project Setup

1. **Clone the repository**  

```bash
git clone https://github.com/ayushianand088/voice-enabled-cursor.git
cd voice-enabled-cursor
