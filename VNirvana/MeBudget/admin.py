from django.contrib import admin
from .models import MyModel, User, Expense, Earning, Budget

# Register your models here.

 
@admin.register(MyModel)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
MyModel._meta.get_fields()]

@admin.register(User)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
User._meta.get_fields()]

@admin.register(Expense)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Expense._meta.get_fields()]

@admin.register(Earning)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Earning._meta.get_fields()]

@admin.register(Budget)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Budget._meta.get_fields()]

