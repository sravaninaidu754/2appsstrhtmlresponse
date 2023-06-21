from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def app2_str(request):
    return HttpResponse("<h1>THIS APP2 STRING RESPONSE</h1>")
def app2_html(request):
    return render(request,'app2.html')
