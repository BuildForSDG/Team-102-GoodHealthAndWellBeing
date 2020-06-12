from django.shortcuts import render

# Create your views here.


def admin(request):
    return render(request, 'admin/')