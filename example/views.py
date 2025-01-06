from django.shortcuts import render
import csv
from django.http import JsonResponse
from django.conf import settings
import os

def get_messages_from_csv(request):
    # Path to the CSV file, make sure to keep it inside the Django project or in a static folder
    file_path = os.path.join(settings.BASE_DIR, 'messages.csv')

    # Check if the file exists
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    messages = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            messages.append({"sender": row["sender"], "text": row["text"]})
    
    return JsonResponse({"messages": messages})


def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')