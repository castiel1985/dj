from django.http import HttpResponse

def test(request):
    return HttpResponse("this is a test") 
