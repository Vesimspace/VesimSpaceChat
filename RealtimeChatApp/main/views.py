from django.shortcuts import render

def HomeScreenView(request, *args, **kwargs):
    context = {}
    return render(request, "main/home.html", context)

