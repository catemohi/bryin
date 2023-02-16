from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "dashboard/dashboard.html", context=context)
