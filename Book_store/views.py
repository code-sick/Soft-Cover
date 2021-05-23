from django.shortcuts import render
from django.core.mail import send_mail
from Django_Project import settings
from django.contrib.auth.models import User
from Book_store.models import Book




# Create your views here.


def about(request):
	return render(request, "about.html")

def booklist(request):
	books = Book.objects.all()
	return render(request,"booklist.html", {'books' : books})

# def sendmail(request):
# 	subject = "Order successfully palced"
# 	msg = "Your order from SOFTCOVER is on the way"
# 	to = "User."
# 	res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
# 	return render(request, "confirm.html")

def showBooks(request):
	return render(request, "home.html")
def contact(request):
	return render(request,"contact.html")