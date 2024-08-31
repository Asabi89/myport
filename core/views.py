from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

def base(request):
    return render(request, 'base.html')


def send_emaile(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Compose email
        email_subject = f"New contact form submission: {subject}"
        email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        
        # Send email
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        # Redirect after successful submission
        return redirect(thank_you)  # Create a thank you page
    
    return render(request, 'thank.html')

def thank_you(request):
    return render(request, 'thank.html')