# Customer Support Chatbot

This project focuses on fine-tuning a Transformer-based chatbot for customer support interactions. The chatbot is trained using the [Bitext Customer Support LLM Chatbot Training Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset), which contains structured conversations tailored for customer service.

## Features
- Fine-tuned Transformer model for customer support.
- Utilizes NLP evaluation metrics: BLEU, F1-score, perplexity.
- Hyperparameter tuning for optimized performance.
- Model deployment for web applications using HTML CSS Javascript.

## Dataset
- **Source**: [Bitext Customer Support Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset)
- **Description**: A dataset containing customer service queries and responses for training language models.

## Training and Fine-Tuning
- **Model**: Pre-trained Transformer model fine-tuned on the customer support dataset.
- **Hyperparameters Tuned**:
  - Learning rate
  - Batch size
  - Number of epochs
  - Weight decay
- **Evaluation Metrics**:
  - Accuracy
  - Precision, Recall, F1-score
  - BLEU Score
  - Perplexity
  - Qualitative Testing

## Model Evaluation
The chatbot's performance is assessed using multiple NLP metrics:
- **BLEU Score**: Measures the similarity between generated and reference responses.
- **F1-score**: Evaluates precision and recall balance.
- **Perplexity**: Measures the model's confidence in generating coherent responses.
- **Qualitative Testing**: Ensures relevance and coherence in chatbot responses.

## Deployment
The trained model is integrated into a Flutter mobile application for real-time customer interactions. Essential model files used for deployment include:
- `model.safetensors`
- `tokenizer.json`
- `vocab.json`
- `merges.txt`

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Azeezmariam/customer-support-chatbot.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train.py
   ```
4. Evaluate the model:
   ```bash
   python evaluate.py<img width="448" alt="Screen Shot 2025-02-25 at 20 53 10" src="https://github.com/user-attachments/assets/87fb7b5e-d118-48df-97b7-a9b99a34777f" />

   ```
5. Deploy to Web Application.

## Future Improvements
- Optimize model size for low-resource environments.
- Enhance the dataset with more diverse customer support queries.
- Improve response coherence through further fine-tuning.

  ## Model
 - https://drive.google.com/drive/folders/1iiKAlMGFCNmruY5DRslHknUCQ35_vkC8?usp=drive_link


## Chatbox screenshot
   <img width="475" alt="Screen Shot 2025-02-25 at 20 54 16" src="https://github.com/user-attachments/assets/4fc6d2e0-e568-4547-8acf-c7c3311a575e" />
<img width="448" alt="Screen Shot 2025-02-25 at 20 53 10" src="https://github.com/user-attachments/assets/5a44035a-8adc-4d91-9b8d-b109c318aeaa" />

   

## References
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Bitext Customer Support Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset)

