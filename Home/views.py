from django.shortcuts import render, HttpResponse
from datetime import datetime 
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
  return render(request,"index.html")
 # return render(request,"index.html",context)
#   context = {
#       "variable":"hein ji"
#   }
  #  return HttpResponse("Yo")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, "We will contact you soon")
    return render(request,"contact.html")