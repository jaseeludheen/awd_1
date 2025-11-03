from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import Subscriber
from django.contrib import messages
from .utils import send_email_notification

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST, request.FILES)
        if email_form.is_valid():
            email = email_form.save()
            # set an email
            mail_subject = request.POST.get('subject')
            message = request.POST.get('body')
            email_list = request.POST.get('email_list')

            # access the selected email list
            email_list = email.email_list
            print('email list ==>',email_list)

            # Extract email address from the Subscriber model in the selected email list
            subscribers = Subscriber.objects.filter(email_list=email_list)  # email_list is from subscriber model , another is above

            """
            to_email = []
            for email in subscribers:
                to_email.append(email.email_address)
            print('to_email ==>',to_email)
            """
            to_email = [email.email_address for email in subscribers] # list comprehension method

            if email.attachment:
                attachment = email.attachment.path
            else: 
                attachment = None

            email_id = email.id
            # Update the email instance with the email ID

            send_email_notification(mail_subject, message, to_email, attachment, email_id)


            # display success message
            messages.success(request, 'Email sent successfully!')
            return redirect('send_email')
        

    else:
        email = EmailForm()
        context = {
            'email_form': email,
        }
        return render(request, 'emails/send-email.html', context)