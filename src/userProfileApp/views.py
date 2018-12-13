from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, AcropolisForm, SarawakForm, VisaForm
from django.contrib import auth


@login_required
def usr_profile(request):
    if request.user.is_superuser:  # checks wether the user is a superuser.
        return HttpResponseRedirect(reverse('superAdmin:dashboard'))

    acropolis_form = AcropolisForm(instance=request.user.acropolismodel)
    sarawak_form = SarawakForm(instance=request.user.sarawakmodel)
    visa_form = VisaForm(instance=request.user.visamodel)

    # print(request.user.acropolismodel.user_profile.first_name)
    if request.method == 'POST':
        if request.POST['submit'] == 'AcropolisForm':                               # if acropolis form is submitted
            user = request.user  # get current user
            acropolis_form = AcropolisForm(request.POST,instance=user.acropolismodel )
            if acropolis_form.is_valid():
                acropolis_form.save(commit=True)

        elif request.POST['submit'] == 'SarawakForm':                               # if sarawak form is submitted
            user = request.user
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            if sarawak_form.is_valid():
                sarawak_form.save(commit=True)

        elif request.POST['submit'] == 'VisaForm':                               # if Visa form is submitted
            user = request.user
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if visa_form.is_valid():
                visa_form.save(commit=True)
                visa_form = VisaForm()
            

        elif request.POST['submit'] == 'AllForm':
            user = request.user
            acropolis_form = AcropolisForm(request.POST, instance=user.acropolismodel)
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if acropolis_form.is_valid() and sarawak_form.is_valid() and visa_form.is_valid():
                acropolis_form.save()
                sarawak_form.save()
                visa_form.save()

    context = {
        'user': request.user,
        'acropolis_form': acropolis_form,
        'sarawak_form': sarawak_form,
        'visa_form' : visa_form
    }
    return render(request, 'userProfileApp/userProfilePage.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            try:
                print("form is saved")
                auth.login(request, user)
                if request.user.is_authenticated:
                    return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
            except Exception as e:
                print('user can\'t logged in after register')
    else:
        form = UserSignUpForm()

    return render(request, 'userProfileApp/signUpPage.html', {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        print(request.user)
        return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
    print('amar', request.user)
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            try:
                user = auth.login(request, form.get_user())
                print(user)
                print(form.get_user())
                return HttpResponseRedirect(reverse('userProfileApp:usrProfile'))
            except Exception as e:
                print('user can\'t logged in after register')

        else:
            print('error ase ', form.errors.as_data())

    else:
        form = AuthenticationForm()

    return render(request, 'userProfileApp/signInPage.html', {'user_signinform': form})


