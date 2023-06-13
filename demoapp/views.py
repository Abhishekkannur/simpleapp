from django.shortcuts import render

# Create your views here.

def demo_app(request):
    return render(request,'index.html')
