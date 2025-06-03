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

## 🔗 References

- Hugging Face Datasets & Transformers  
- Bitext LLM Chatbot Training Dataset

---

> 💡 _Developed for the Natural Language Processing (IN321) Final Project – College of Artificial Intelligence (El Alamein), Feb 2025_
