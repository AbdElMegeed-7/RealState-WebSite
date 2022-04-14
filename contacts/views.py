from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact(listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Have have already made Inquiry')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)

        contact.save()
        # After saving the inquiry
        # Sending Emails
        # from django.core.mail import send_mail
        # send_mail(
        #     'Subject',
        #     'Message',
        #     'From_mail',
        #     ['List of email addresses Recipient_list']
        # )
        messages.success(
            request, 'Your request has been submitted, a realtor will gitback to you soon')

        return redirect('/listings/'+listing_id)
