from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Projects(models.Model):
    project_title = models.CharField( max_length=50)
    project_desc = models.CharField(max_length=50)
    project_img = models.FileField(upload_to='projects/', max_length=250, null=True, default=None)
    project_link = models.CharField( max_length=100)
    project_title_slug = AutoSlugField(populate_from="project_title",unique=True,null=True,default =None)