from django.contrib import admin

# Register your models here.
from .models import Comments
from .models import Replies

admin.site.register(Comments)
admin.site.register(Replies)