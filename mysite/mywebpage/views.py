from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import UserContactForm

from .forms import (
        ContactMeForm
    )

import re  # Regular expression module


def home_page_view(request):
    """Renders the home page on request"""
    template = 'mywebpage-app/index.html'

    context = {
        # Sending data to the page and requested objects

    }
    return render(request, template, context)


def contact_me_page_view(request):
    """Renders the contact me page on request"""
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']

        user_passed_details = UserContactForm(
            full_name=full_name,
            email=email,
            subject=subject,
            text=text,
        )
        user_passed_details.save()
        submission_successful_message = 'Hello ' + full_name + ' thanks for contacting us'
        messages.info(request, submission_successful_message)

        return redirect('mywebpage:contact')

    else:
        template = 'mywebpage-app/contact.html'

        context = {
            # Sending date to page and requested objects
            'form': ContactMeForm
        }
        return render(request, template, context)


def about_me_page_view(request):
    """Renders the about me page"""
    template = 'mywebpage-app/about-me.html'

    context = {
        # Sending data and requested objects to the page
    }
    return render(request, template, context)


def portfolio_page_view(request):
    """Renders the portfolio page"""
    template = 'mywebpage-app/portfolio.html'

    context = {
        # Sending data and requested objects to the page
    }
    return render(request, template, context)
