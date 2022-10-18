from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def lessons(request):
	return render(request, 'lessons.html')