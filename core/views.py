from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import InvestmentPlan, Property, Investment

# Create your views here.
def index(request):
    # messages.success(request, "Hey bro whats up !")
    return render(request, "core/index.html")


def onboarding(request):
    messages.success(request, "Fix your account!")
    return render(request, "core/onboarding.html")

@login_required
def withdrawal(request):
    user = request.user
    
    messages.success(request, "Fix your account!")
    return render(request, "core/withdraw.html", {
        'user': user,
    })

@login_required
def confirm_withdrawal(request):
    user = request.user
    
    messages.success(request, "Fix your account!")
    return render(request, "core/confirm_withdraw.html", {
        'user': user,
    })

