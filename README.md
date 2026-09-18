#  Hospital Customer Support Chatbot

This project is a Natural Language Processing (NLP)-based **hospital customer service chatbot**, designed to assist patients and customers with a wide range of inquiries, including appointment details, available doctors details and general inquiries

---

##  Team Members

- **Mahynour Ayman**   
- **Mariam Aly** 
- **Jana Emad**  

---

## ⚙️ Methodology

- **Text Preprocessing**: Clean and prepare user input for better model understanding.
- **Transformer Models**: Leverage pre-trained large language models for generating responses.
- **SQL Database Integration**: Simulate real-time access to patient-related information like appointment schedules.

---

## 📊 Dataset

- **Source**: [Hugging Face – Bitext Customer Support Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset)
- **Size**: ~26,872 records (~19.2 MB)
- **Fields**:
  - `instruction`: user request
  - `category`: high-level topic (e.g., healthcare)
  - `intent`: identified user intent
  - `response`: expected assistant reply
- **Preprocessing**: Filter dataset to focus on relevant domains (healthcare, hospitality, insurance, etc.)

---

## 🚀 Setup & Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg     # ~560 MB, required — not a pip dependency
jupyter notebook NLP_Chatbot.ipynb
```

A few things worth knowing before you run it:

- **`transformers` is pinned to `4.45.2`.** The notebook was built against that
  release; later versions changed the `Trainer` and evaluation APIs, so an
  unpinned install will break the training cells.
- **The spaCy model is a separate download.** `pip install spacy` gives you the
  library but not `en_core_web_lg`, which the preprocessing cells load directly.
- **The SQLite database builds itself.** `clinic.db` (doctors, appointments) is
  created and populated by the notebook at runtime, so there is no database file
  to fetch — just run the cells in order.
- **Outputs are committed**, so you can read every result without executing
  anything.

---

## 🔗 References

- Hugging Face Datasets & Transformers  
- Bitext LLM Chatbot Training Dataset

---

> 💡 _Developed for the Natural Language Processing (IN321) Final Project – College of Artificial Intelligence (El Alamein), Feb 2025_

---

## 📄 License

MIT — see [LICENSE](LICENSE).

> This is a completed university project (NLP IN321, Feb 2025), published to
> GitHub in June 2025. The short commit history reflects that it was uploaded
> at completion rather than developed in the open.
