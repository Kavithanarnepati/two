from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def String_Response(request):
    return HttpResponse('<h1><marquee>This is my first string hlo saru</h1></marquee>')
def String_Two(request):
    return HttpResponse('<h1>hlo world</h1>')
