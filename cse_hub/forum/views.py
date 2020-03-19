from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h3> Forum Home Page, returning HttpResponse instead of rendering html page </h3>')
