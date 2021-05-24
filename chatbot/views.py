import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

def index(request):
  return render(request, "chatbot/index.html")

@csrf_exempt
def response(request):
  global bot
  if request.method == 'POST':
    data = json.loads(request.body)
    user_input = data.get("message","")
    response = str(bot.get_response(user_input))
    return JsonResponse({"reply":response})
  return JsonResponse("POST is required", status=400)