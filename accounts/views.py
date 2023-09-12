from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def dashboard(request):
    return render(request, 'account/dashboard.html', {})


def register(request):
    user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})