from django.db import models
from django import forms

# Create your models here.
class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    birthday = models.CharField(max_length=10)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Expense(models.Model):
    product_title = models.CharField(max_length=255)
    user_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField(default=0)  

class Earning(models.Model):
    earning_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField(default=0)  

class Budget(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField(default=0)  


'''
class LeadDetail(models.Model):
    Lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    files = models.FileField(blank=True, upload_to='media')
    tasks = models.TextField(max_length=1000)

    def __str__(self):
        return self.Lead.first_name 

class Lead(models.Model):
    lead_status = (
        ('Potential', 'Potential'),
        ('Prospect', 'Prospect'),
        ('Negotiation', 'Negotiation'),
        ('Converted', 'Converted'),
        ('Failed', 'Failed')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=25, null=True)
    country = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, choices=lead_status, null=True)
    avatar = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return self.first_name

def eachlead(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    leadinfo = LeadDetail.objects.filter(Lead=lead)
    return render(request, "onelead.html", {'lead': lead, 'leadinfo': leadinfo})'''