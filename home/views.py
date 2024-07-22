from urllib import request
from django.shortcuts import render
from .models import Contact, Reservation
from django.contrib import messages

# Create your views here.



#reservation form
def rev(request):
    if request.method=="POST" and 'Reserve' in request.POST:
        reg_name=request.POST['reg_name']   
        reg_email=request.POST['reg_email']
        reg_phone=request.POST['reg_phone']
        reg_date=request.POST['reg_date']
        reg_time=request.POST['reg_time']
        reg_person =request.POST['reg_person']
        if  len(reg_name)<2 or len(reg_email)<1 or len(reg_phone)<10 or len(reg_date)<2:
            messages.error(request, "Please fill the form correctly")
        else:
            
            reservation=Reservation(reg_name=reg_name, reg_email=reg_email, reg_phone=reg_phone, reg_date=reg_date, reg_time=reg_time, reg_person=reg_person)
            reservation.save()
            messages.success(request, "Thank you for your inquiry we will contact you shortly to confirm this reservation.")






def index(request):
    r=rev(request)
    return render(request,"index.html")


def about(request):
    r=rev(request)

    return render(request,"about-us.html")




def services(request):
    r=rev(request)

    return render(request,"services.html")




def contact(request):

    if request.method=="POST" and 'contact' in request.POST:

            name=request.POST['name']   
            email=request.POST['email']
            phone=request.POST['phone']
            subject=request.POST['subject']
            message =request.POST['message']
            if  len(name)<2 or len(email)<1 or len(phone)<10 or len(subject)<2:
                messages.error(request, "Please fill the form correctly")
            else:
                
                contact=Contact(name=name, email=email, phone=phone, subject=subject, message=message)
                contact.save()
                messages.success(request, "Your message has been successfully sent")
            
    r=rev(request)
    return render(request,"contact.html")
