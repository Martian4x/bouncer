from django.shortcuts import render

# Create your views here.
def landing(request):
   """Render the landing Page"""
   return render(request, 'bouncer/index.html')
