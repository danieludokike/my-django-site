from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
        UserContactForm
    )

# Register your models here.

admin.site.register(UserContactForm)
# admin.site.unregister(User)
