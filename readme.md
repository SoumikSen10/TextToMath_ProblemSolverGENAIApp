```md
# 🧮 Text to Math Problem Solver & Reasoning Assistant

A modern **GenAI-powered Streamlit application** that can:
- Solve **mathematical word problems**
- Answer **logical and reasoning-based questions**
- Fetch **factual information from Wikipedia**

This project is built using **Groq’s LLaMA model**, **LangChain’s Runnable architecture**,
and avoids all deprecated APIs such as `LLMChain`, `LLMMathChain`, and legacy agents.

---

## 🚀 Features

- ✅ Math problem solving with step-by-step explanations
- ✅ Logical and reasoning-based question answering
- ✅ Wikipedia-based factual search
- ✅ Smart routing without LangChain agents (stable & future-proof)
- ✅ Clean Streamlit chat-style interface
- ✅ Compatible with latest LangChain versions

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain (Runnable-based API)**
- **Groq LLM (LLaMA 3.1 – 8B Instant)**
- **Wikipedia API**
- **dotenv**

---

## 📂 Project Structure

```

├── app.py
├── requirements.txt
├── .env
└── README.md

````

---

## 🔑 Prerequisites

- Python 3.9+
- A **Groq API Key**  
  Get it from 👉 https://console.groq.com

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/text-to-math-problem-solver.git
cd text-to-math-problem-solver
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

Instead of deprecated LangChain agents, the app uses **explicit routing logic**:

* **Math questions** → Handled by a math-focused LLM prompt
* **Fact-based questions** → Answered using Wikipedia API
* **Reasoning questions** → Solved using a reasoning LLM chain

This approach is:

* More stable
* Easier to debug
* Interview & production friendly

---

## 📝 Example Questions

* *“I have 5 bananas and 7 grapes. How many fruits do I have after eating some?”*
* *“Who is A. P. J. Abdul Kalam?”*
* *“Explain the solution to this logic puzzle step by step.”*

---

## ⚠️ Important Notes

* This project **does NOT use deprecated LangChain APIs**
* No `initialize_agent`, `LLMMathChain`, or `LLMChain`
* Built using **Runnable pipelines (`prompt | llm | parser`)**

---

## 📌 Future Enhancements

* Conversation memory
* Tool-usage visualization
* PDF-based math problem solving
* Multi-model support (Gemma, Mixtral)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* LangChain
* Groq
* Streamlit
* Wikipedia API

