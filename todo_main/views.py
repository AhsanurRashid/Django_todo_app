from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to the Todo App!</h1><p>This is the home page.</p>')