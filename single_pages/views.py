from django.shortcuts import render

def landing(request):
    return runder(
        request,
        'single_pages/landing.html',
    )
