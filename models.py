from django.db import models
from django.contrib.auth.models import User as SysUser

class User(models.Model):
    id = models.AutoField(primary_key = True)
    firstname = models.CharField(max_length=100, null = True)
    secondname = models.CharField(max_length=100, null = True)
    surname = models.CharField(max_length=100, null = True)
    phone = models.CharField(max_length=15, null = True)
    email = models.CharField(max_length=150, null = True)
    logo = models.CharField(max_length=150, null = True)
    sys_user = models.ForeignKey(SysUser, on_delete=models.CASCADE)

class AdType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class AdCategory(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class AdImage(models.Model):
    id = models.AutoField(primary_key = True)
    file_name = models.CharField(max_length=255)
    ad = models.ForeignKey('AdCard', on_delete=models.CASCADE)

class AdCard(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    decription = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField()
    main_picture = models.CharField(max_length=100)
    published = models.BooleanField()
    type_id = models.ForeignKey('AdType', on_delete=models.PROTECT, null=False)
    category_id = models.ForeignKey('AdCategory', on_delete=models.PROTECT, null=False)
    author_id = models.ForeignKey('User', on_delete=models.PROTECT, null=False)

    @staticmethod
    def init_empty_fields():
        empty_fields = {}
        empty_fields['id'] = -1
        empty_fields['name'] = ''
        empty_fields['decription'] = ''
        empty_fields['price'] = 0
        empty_fields['is_active'] = False
        empty_fields['published'] = False
        empty_fields['main_picture'] = ''
        empty_fields['type_id'] = None
        empty_fields['category_id'] = None
        empty_fields['author_id'] = None
        return empty_fields




