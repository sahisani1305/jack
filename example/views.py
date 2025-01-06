from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')

from django.http import JsonResponse
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")

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
