from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("onboarding/", views.onboarding, name="onboarding"),
    
    path("withdrawal/", views.withdrawal, name="withdrawal"),
    path("confirm_withdrawal/", views.confirm_withdrawal, name="confirm_withdrawal"),

]












