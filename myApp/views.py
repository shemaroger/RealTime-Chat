from django.shortcuts import render

def chat(request):
     return render(request, 'myApp/chat.html')

