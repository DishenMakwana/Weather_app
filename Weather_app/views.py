from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from Weather_app.forms import SignUpForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm
        return render(request, 'registration/login.html', {'form': form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm
        return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    return render(request, 'registration/logout.html')