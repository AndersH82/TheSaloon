from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Shout, UploadedImage
from .forms import ShoutForm, SignUpForm, ProfilePicForm, UploadImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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
        return render(request, 'home.html', {"shouts": shouts, "form": form})
    else:
        shouts = Shout.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"shouts": shouts})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("You must login to see this page..."))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user_id=pk)
        except ObjectDoesNotExist:
            messages.error(request, "Profile not found.")
            return redirect('home')

        shouts = Shout.objects.filter(user_id=pk).order_by("-created_at")

        if request.method == "POST":
            if not hasattr(request.user, 'profile'):
                missing_profile = Profile(user=request.user)
                missing_profile.save()

            current_user_profile = request.user.profile
            action = request.POST.get('follow', '')
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile, "shouts": shouts})
    else:
        messages.success(request, "You must login to see this page...")
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
    return redirect('login')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You are now registered!"))
            return redirect('home')

    return render(request, "register.html", {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        user_form = SignUpForm(request.POST or None,
                               request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(
            request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)
            messages.success(request, ("Your information is now updated!"))
            return redirect('home')

        return render(request, "update_user.html",
                               {'user_form': user_form,
                                'profile_form': profile_form})
    else:
        messages.success(request, ("You must be logged in!"))
        return redirect('login')


def shout_like(request, pk):
    if request.user.is_authenticated:
        shout = get_object_or_404(Shout, id=pk)
        if shout.likes.filter(id=request.user.id):
            shout.likes.remove(request.user)
        else:
            shout.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("You must be logged in to like/unlike!"))
        return redirect('home')


def delete_shout(request, pk):
    if request.user.is_authenticated:
        shout = get_object_or_404(Shout, id=pk)
        if request.user.username == shout.user.username:
            shout.delete()
            messages.success(request, ("The Shout has been deleted"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("This is not your Shout"))
            return redirect('home')
    else:
        messages.success(request, ("Please log in to continue..."))
        return redirect(request.META.get("HTTP_REFERER"))


def edit_shout(request, pk):
    if request.user.is_authenticated:
        shout = get_object_or_404(Shout, id=pk)
        if request.user.username == shout.user.username:
            form = ShoutForm(request.POST or None, instance=shout)
            if request.method == "POST":
                if form.is_valid():
                    shout = form.save(commit=False)
                    shout.user = request.user
                    shout.save()
                    messages.success(request, ("Your Shout has been updated!"))
                    return redirect('home')
            else:
                return render(request, "edit_shout.html", {'form': form,
                                                           'shout': shout})
        else:
            messages.success(request, ("This is not your Shout!"))
            return redirect('home')
    else:
        messages.success(request, ("Please log in to continue..."))
        return redirect('home')


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
    else:
        form = UploadImageForm()
    images = UploadedImage.objects.filter(user=request.user)
    return render(request, 'upload_image.html', {'form': form, 'images': images})


def delete_image(request, pk):
    if request.method == 'POST':
        image = get_object_or_404(UploadedImage, pk=pk, user=request.user)
        image.delete()
        messages.success(request, "Image deleted successfully.")
        return redirect('upload_image')
    else:
        return redirect('upload_image')


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.profile.delete()
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')
    else:
        return redirect('profile')
