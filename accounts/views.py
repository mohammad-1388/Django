from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import ProfileForm, MyUserForm
from accounts.models import Profile


def login1(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('ErrorHome'))
    context = {}
    if request.method == "POST":
        try:
            username = request.POST['username']
            assert username, "نام کاربری خود را وارد کنید"
            password = request.POST['password']
            assert password, "گذرواژه خود را وارد کنید"
            user = authenticate(username=username, password=password)
            if user:
                # Successful Login
                login(request, user)
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return HttpResponseRedirect(reverse('ErrorHome'))
            else:
                assert 1 == 2, "کاربری با این مشخصات وجود ندارد"
        except Exception as e:
            context['error'] = e
            return render(request, 'accounts/login.html', context=context)
    else:
        context = {}
        return render(request, 'accounts/login.html', context=context)


@login_required
def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


@login_required
def show_profile(request):
    return render(request, 'accounts/show_profile.html')


@login_required
def change_password(request):
    context = {}
    if request.method == "POST":
        try:
            old_password = request.POST["OPassword"]
            new_password = request.POST["NewPassword"]
            recent_new_password = request.POST["RNewPassword"]
            assert old_password != "", "لطفا رمز فعلی را وارد کنید"
            assert request.user.check_password(old_password), "رمز شما همخوانی ندارد"
            assert new_password != "" and recent_new_password != "", "رمز جدید را وارد کنید"
            assert new_password == recent_new_password, "رمز جدید با تکرارش مطابقت ندارد"
            request.user.set_password(new_password)
            request.user.save()
            return HttpResponseRedirect(reverse('accounts:show_profile'))
        except Exception as e:
            context['error'] = e
            return render(request, 'accounts/chnage_password.html', context)
    else:
        return render(request, 'accounts/chnage_password.html', context)


@login_required
def profile_edit(request):
    # if 'profile_picture' in request.POST:
    #     del request.POST['profile_picture']
    user_form = MyUserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = MyUserForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:show_profile'))
        else:
            print(user_form.is_valid(), profile_form.is_valid())
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)


def signup(request):
    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect(reverse("ErrorHome"))
    context = {}
    if request.method == 'POST':
        try:
            assert 'username' in request.POST, "شما نام کاربری وارد نکرده اید پس وارد کنید"
            assert 'email' in request.POST, "شما ایمیل خودرا وارد نکرده اید. به ما چه"
            assert 'password' in request.POST and 'rpassword' in request.POST, \
                "شما گذرواژه یا تکرار آن را وارد نکرده اید"
            assert 'id' in request.POST, "شما آی دی خود را وارد کنید"
            assert request.session.get('is_signup') == "YES", ["شما مسدود شده اید پس بروید"][0]
            username = request.POST["username"]
            password = request.POST["password"]
            repassword = request.POST["rpassword"]
            email = request.POST["email"]
            assert password == repassword, "گذرواژه با تکرارش مطابقت ندارد"
            idUser = request.POST['id']
            assert User.objects.filter(username=username).count() + Profile.objects.filter(
                idUser=idUser).count() == 0, "نام کاربری یا آی دی یا ایمیل تکراری می باشد"
            user = User.objects.create_user(username, email, password)
            user: User
            user.profile = Profile.objects.create(idUser=idUser, user=user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:show_profile'))

        except Exception as e:
            if e == "شما مسدود شده اید پس بروید":
                request.session['blocked'] = 'YES'
            context['error'] = e
    else:
        if request.session.get('blocked') != 'YES':
            request.session['is_signup'] = "YES"
        else:
            return HttpResponse('شما مسدود شده اید', status=403)
    return render(request, 'accounts/signup.html', context)
