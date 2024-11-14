from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


from .qa_chatbot import chatbot_api

import json
# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines('<h1>Hello</h1>')
    response.write('This is chatbot')

    return response


@csrf_exempt
def process_message(request):
    if request.method == "POST":
        data = json.loads(request.body)

        question = data.get('message')
        id = data.get('id')

        response = chatbot_api(question, id)

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)