from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Shout
from .forms import ShoutForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        form = ShoutForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                shout = form.save(commit=False)
                shout.user = request.user
                shout.save()
                messages.success(request, ("You posted a Shout!"))
                return redirect('home')

        shouts = Shout.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"shouts":shouts, "form":form})
    else:
        shouts = Shout.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"shouts":shouts})


def profile_list(request):
        if request.user.is_authenticated:
            profiles = Profile.objects.exclude(user=request.user)
            return render(request, 'profile_list.html', {"profiles":profiles})
        else:
            messages.success(request, ("You must login to see this page..."))
            return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        shouts = Shout.objects.filter(user_id=pk).order_by("-created_at")

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST ['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()


        return render(request, "profile.html", {"profile":profile, "shouts":shouts})
    else:
        messages.success(request, ("You must login to see this page..."))
        return redirect('home')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("WROOOONG! Try again!"))
            return redirect('login')

    else:    
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out!"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            #second_name = form.cleaned_data['second_name']
            #email = form.cleaned_data['email']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("You are now registered!"))
            return redirect('home')

    return render(request, "register.html", {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("Your information is now updated!"))
            return redirect('home')

        return render(request, "update_user.html", {'user_form':user_form, 'profile_form':profile_form})
    else:
        messages.success(request, ("You must be logged in!"))
        return redirect('home')    
    
def shout_like(request, pk):
    if request.user.is_authenticated:
        shout = get_object_or_404(Shout, id=pk)
        if shout.likes.filter(id=request.user.id):
            shout.likes.remove(request.user)
        else:
            shout.likes.add(request.user)

        return redirect('home')


    else:
        messages.success(request, ("You must be logged in!"))
        return redirect('home')   