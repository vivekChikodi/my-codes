from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class addBookmark(models.Model):
    bookmark_tag = models.CharField(max_length=200)
    bookmark_name = models.CharField(max_length=200)
    bookmark_desc = models.CharField(max_length=500)
    def __str__(self):
        return self.bookmark_tag
    

# Create your models here.
