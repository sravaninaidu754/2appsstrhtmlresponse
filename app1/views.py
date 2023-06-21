from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def app1_str(request):
    return HttpResponse("<h1>THIS APP1 STRING RESPONSE</h1>")
def app1_html(request):
    return render(request,'app1.html')
