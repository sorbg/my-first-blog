# blog/admin.py 

# Register your models here.

# To add, edit and delete the posts we've just modeled, we will use Django admin.

from django.contrib import admin
from .models import Post

admin.site.register(Post)
