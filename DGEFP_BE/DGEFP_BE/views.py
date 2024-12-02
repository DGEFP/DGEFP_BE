from django.http import HttpResponse

def Homepage(request): 
         return HttpResponse("Homepage")
     
def Dashboard(request):
         return HttpResponse(" Dashboard _ test")