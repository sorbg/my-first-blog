#/blog/models.py  class post with atributes and methods for a blog
# note models.Model  this is a django object.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User') # models.ForeignKey – this is a link to another model
    title = models.CharField(max_length=200) # models.CharField – text with a limited number of characters.
    text = models.TextField() # TextField – this is for long text without a limit.
    created_date = models.DateTimeField(
            default=timezone.now)    # models.DateTimeField – this is a date and time.   
    published_date = models.DateTimeField(
            blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
