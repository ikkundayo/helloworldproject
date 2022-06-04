from http.client import HTTPResponse


from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>happy</h1>')
    return returnedobject

class HelloworldClass(TemplateView):
    template_name = 'hello.html'