import random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyModel, User, Expense, Earning, Budget
from .forms import MyForm, UserForm, ExpenseForm, EarningForm, BudgetForm


import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


# Create your views here.

def index(request):
    return render(request, "MeBudget/index.html")



def profile(request):
    id = request.session.get('user_id')

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        # Redirect to a custom URL if the user is not found
        return redirect(login_view)

    motivation = get_random_motivation_messages()

    modelBudget = Budget.objects.filter(user_id=id)
    modelExpense = Expense.objects.filter(user_id=id)
    modelEarning = Earning.objects.filter(user_id=id)
    
    budgetform = BudgetForm(request.POST)
    expenseform = ExpenseForm(request.POST)
    earningform = EarningForm(request.POST)


    if request.method == "POST":
        if expenseform.is_valid():
            expense_instance = expenseform.save(commit=False)
            expense_instance.user_id = id  # Assign the user ID to the user_id field
            expense_instance.save()
            modelExpense = Expense.objects.filter(user_id=id)
            expenseform = ExpenseForm()
        else:
            expenseform = ExpenseForm()

        if earningform.is_valid():
            earning_instance = earningform.save(commit=False)
            earning_instance.user_id = id  # Assign the user ID to the user_id field
            earning_instance.save()
            modelEarning = Earning.objects.filter(user_id=id)
            earningform = EarningForm() 
        else:
            earningform = EarningForm() 

        if budgetform.is_valid():
            budget_instance = budgetform.save(commit=False)
            budget_instance.user_id = id  # Assign the user ID to the user_id field
            budget_instance.save()
            modelBudget = Budget.objects.filter(user_id=id)
            budgetform = BudgetForm()  
        else:
            budgetform = BudgetForm()  

    user_budget_amount_list = modelBudget.values_list('total_amount', flat=True)
    user_expense_amounts_list = modelExpense.values_list('user_amount', flat=True)
    user_expense_product_list = modelExpense.values_list('product_title', flat=True)
    user_earning_amounts_list = modelEarning.values_list('earning_amount', flat=True)
    user_budget_amount = sum(user_budget_amount_list)
    user_expense_amounts = sum(user_expense_amounts_list)
    user_earning_amounts = sum(user_earning_amounts_list)
    
    balance = user_budget_amount + user_earning_amounts - user_expense_amounts
    if len(user_budget_amount_list)-1 >= 0:
        budget = user_budget_amount_list[len(user_budget_amount_list)-1]
    else:
        budget = 0

    username = User.objects.get(id=id).username


    return render(request, "MeBudget/profile.html", {"text": motivation, "expenseform": expenseform, "earningform": earningform, "budgetform": budgetform,
    "budget": budget, "expenses": user_expense_amounts, "earnings": user_earning_amounts, "balance": balance, "id": id, "products": modelExpense,
    "user": username
    })


def register_view(request):
    model = User.objects.all()
    form = UserForm(request.POST)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.dict().get("username")
            password = request.POST.dict().get("password")
            if not User.objects.filter(username = username).exists():
                form.save()
                form = UserForm()  
                request.method = "GET"
            else:
                error_msg = "--User already registered--"
                return render(request, "Mebudget/register.html", {'form': form, 'error_msg': error_msg})
            id = User.objects.get(username=username).id
            request.session['user_id'] = id
            form = UserForm()  
            return redirect(profile)
        else:
            form = UserForm()
    error_msg = ""
    return render(request, "Mebudget/register.html", {'form': form, 'error_msg': error_msg})


def login_view(request):
    model = User.objects.all()
    form = UserForm(request.POST)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.dict().get("username")
            password = request.POST.dict().get("password")
            form = UserForm() 
            if User.objects.filter(username = username).exists() and User.objects.filter(password = password).exists():
                request.method = "GET"
                request.session['user_id'] = User.objects.get(username=username).id
                return redirect(profile)
            else:
                error_msg = "--Please enter valid info--"
                return render(request, "Mebudget/login.html", {'form': form, 'error_msg': error_msg})
        else:
            form = UserForm()
    error_msg = ""
    return render(request, "Mebudget/login.html", {'form': form, 'error_msg': error_msg})

def logout_view(request):
    request.session['user_id'] = None
    logout(request)
    return redirect('index')

def Listofname(request):
   model = User.objects.all()
   return render(request, 'MeBudget/listofnames.html', {'Data' : model})

def get_random_motivation_messages():
    motivation_messages = [
        "You're doing great! However, your expenses seem a bit below your budget. Save more to reach bigger goals in the future.",
        "Every step is a big change. Keep your budget under control and move forward on the path to success!",
        "Having a plan is the key to success. Review your expenses and achieve your financial goals!",
        "Managing your money is a way to control your future. Pay attention to your daily expenses and save!",
        "Small steps lead to big success. Track your expenses and be patient to reach your financial goals!",
        "Take a step every day to achieve future successes. Managing your budget correctly is the way to success.",
        "Your future successes depend on your current financial decisions. Keep your expenses under control and reach your goals!",
        "Managing your budget is a step towards building the life of your dreams. Shape your future by saving!",
        "Take small steps to reach your financial goals. Every saving makes your future brighter!",
        "Use your budget to achieve your financial goals. Controlled expenses will lead you to financial success.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
        "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is not in what you have, but who you are. - Bo Bennett",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
        # ... You can add in here
    ]

    selected_message = random.choice(motivation_messages)
    return selected_message


def editProduct(id):
    return 0

    
def deleteProduct(id):
    return 0


#cs50 session stuff / user page authoritize / take data with same id / return same ids (for expense list)
#find a way to make to do app with register login