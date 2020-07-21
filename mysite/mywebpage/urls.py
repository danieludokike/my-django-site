from django.urls import path

from .views import (
        home_page_view,
        contact_me_page_view,
        about_me_page_view,
        portfolio_page_view,
    )


app_name = 'mywebpage'
urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_me_page_view, name='contact'),
    path('about/', about_me_page_view, name='about'),
    path('portfolio/', portfolio_page_view, name='portfolio'),
]
