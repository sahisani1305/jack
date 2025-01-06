from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')
from django.http import JsonResponse
from transformers import AutoTokenizer, AutoModelForCausalLM

# Hugging Face API setup
HUGGINGFACE_API_KEY = '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'  # Replace with your Hugging Face API key

# Set the Hugging Face model (Meta's LLaMA)
MODEL_NAME = "meta-llama/Llama-3.3-70B-Instruct"  # Choose the appropriate model you want to use

# Initialize the model and tokenizer globally to avoid re-initializing on every request
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Function to query Hugging Face API with user input
def get_meta_response(user_input):
    # Tokenize input and get the model response
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs)

    # Decode and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Django view to handle the chat request
def chat_view(request):
    # Get user input from request
    user_input = request.GET.get('message', '')

    if user_input:
        # Call the Hugging Face API to get the model's response
        response = get_meta_response(user_input)
        return JsonResponse({"response": response})
    else:
        return JsonResponse({"error": "No message provided"}, status=400)
