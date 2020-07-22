from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
        UserContactForm,
        PortfolioDetail,

    )

# Register your models here.

admin.site.register(UserContactForm)
admin.site.register(PortfolioDetail)
# admin.site.unregister(User)
