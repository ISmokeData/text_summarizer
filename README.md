# 📝 AI-Powered Text Summarizer  

A deep learning-based **Text Summarization** tool using **Hugging Face Transformers** and **PyTorch**. This model efficiently generates concise summaries from long texts, making it useful for research, content processing, and automation.  

## 🚀 Features  
- Fine-tuned **Hugging Face Transformer** model for text summarization  
- Utilizes **AutoModelForSeq2SeqLM** and **AutoTokenizer**  
- Experiment tracking with **Weights & Biases (wandb.ai)**  
- Supports both short and long text summarization  

## 📂 Dataset  
The model was trained and fine-tuned using **[Dataset Name]**, ensuring high-quality summaries with minimal loss.  

## 🛠️ Technologies Used  
- **Python**  
- **PyTorch**  
- **Hugging Face Transformers**  
- **Weights & Biases (wandb.ai)**  

## 📌 Installation  
Clone the repository and install dependencies:  
```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
pip install -r requirements.txt
```

## ▶️ Usage  
Run the script to summarize text:  
```python
python summarize.py --text "Your input text here"
```

## 🖥️ Example  
```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = "Long input text that needs summarization..."
inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Summary:", summary)
```

## 📈 Training & Experiment Tracking  
Weights & Biases was used to log training metrics and optimize model performance.  

## 🔗 Links  
- **Model Weights**: [Hugging Face Model](https://huggingface.co/)   

## 🤝 Contributing  
Contributions are welcome! Feel free to open issues or submit pull requests.  
