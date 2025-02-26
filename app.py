from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (restrict if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the fine-tuned model and tokenizer
MODEL_PATH = "./customer_care_chatbot_model"  
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

class Query(BaseModel):
    question: str

@app.post("/predict/")
async def predict(query: Query):
    try:
        # Tokenize the input query
        inputs = tokenizer(query.question, return_tensors="pt", padding="max_length", truncation=True, max_length=512)

        # Generate model output
        outputs = model.generate(inputs["input_ids"], max_length=512)
        predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {"response": predicted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
