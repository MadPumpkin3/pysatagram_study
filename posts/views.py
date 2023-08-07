from django.shortcuts import render


# Create your views here.
def feeds(request):
    return render(request, "posts/feeds.html")
