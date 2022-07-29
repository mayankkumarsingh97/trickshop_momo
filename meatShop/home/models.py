from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
from colorfield.fields import ColorField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import date
import django_filters

from django.dispatch import receiver
# from allauth.account.signals import user_signed_up
from django.db.models.signals import m2m_changed
from django.utils.text import slugify
# from .views import *
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator,MaxValueValidator

from django.utils.safestring import mark_safe

# Create your models here.

# The content of Front Page that consits of Pic and one line title

class subcategory(models.Model):
    # avatar = models.ImageField(upload_to='avatars/',blank=True, null=True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='subCategory',blank=False,null=False)
    name = models.CharField(max_length=200, null=False,default="None", blank=False,verbose_name="Sub-category Name")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=55, blank=True, null=True)

    def get_slug(self):

        slug = self.name
        return slugify(slug)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.get_slug()
        super(subcategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def Sub_parent(self):
        return "\n,".join([p.name for p in self.subparent.all()])

class category(models.Model):
    id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=200, null=False,default="None", blank=False,verbose_name="Category Name")
    SubcatName = models.ManyToManyField(subcategory,related_name='subcat', blank=False,verbose_name="Sub-category Name")
    slug = models.SlugField(max_length=55, blank=True, null=True)

    def get_slug(self):

        slug = self.CategoryName
        return slugify(slug)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.get_slug()
        super(category, self).save(*args, **kwargs)

    def __str__(self):
        return self.CategoryName

    def Sub_category(self):
        return "\n,".join([p.name for p in self.SubcatName.all()])




class product(models.Model):
    image = models.ImageField(upload_to='mainMenu',blank=False,null=False)
    title = models.CharField(max_length=100)
    upload_date=models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=55, blank=True, null=True)
    category=models.ForeignKey(category,blank=True,on_delete=models.CASCADE, null=True ,related_name='category')

    def __str__(self):
        return self.title


