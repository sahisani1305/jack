from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
import json

# Predefined key-pair values for responses
KEY_PAIR_RESPONSES = {
    "hello": "Hello!| How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great, thank you!",
    "what can you do": "I'm here to help you with any questions you have. Just ask me anything!",
    "who are you": "I'm a bot created by Mohammed Shaik Sahil. Nice to meet you!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm a bot, you can call me Jack.",
    "help": "I'm here to help you! Just ask me anything."
}

@csrf_exempt
@require_POST
def get_bot_response(request):
    try:
        # Get the message sent from the frontend
        data = json.loads(request.body)
        user_message = data.get('message')

        # Normalize the message (convert to lowercase to make it case-insensitive)
        user_message = user_message.strip().lower()

        # Default response in case no match is found
        bot_response = "Sorry, I couldn't understand that. Could you please rephrase?"

        # Check if the user message matches any predefined key
        if user_message in KEY_PAIR_RESPONSES:
            bot_response = KEY_PAIR_RESPONSES[user_message]

        # Return the response in JSON format
        return JsonResponse({'response': bot_response})

    except Exception as e:
        # In case of any errors, send a failure response
        return JsonResponse({'error': 'An error occurred while processing your request. Please try again later.'}, status=500)


def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')