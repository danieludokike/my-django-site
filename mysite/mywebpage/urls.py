from django.urls import path
from django.contrib.auth.views import (
        LoginView
    )

from .views import (
        home_page_view,
        contact_me_page_view,
        about_me_page_view,
        portfolio_page_view,
    )


template = 'mywebpage-app/login.html'  # Login HTML of the page

app_name = 'mywebpage'
urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_me_page_view, name='contact'),
    path('account/login', LoginView.as_view(template_name=template), name='login'),
    path('about/', about_me_page_view, name='about'),
    path('portfolio/', portfolio_page_view, name='portfolio'),
]
