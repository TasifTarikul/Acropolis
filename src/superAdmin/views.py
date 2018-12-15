from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from userProfileApp.forms import AcropolisForm, SarawakForm, VisaForm

from coreApp.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.

# ----------------------sign in view----------------------


def sign_in(request):
    if request.user.is_authenticated:
        # print(request.user)
        return HttpResponseRedirect(reverse('superAdmin:dashboard'))
    # print('amar', request.user)
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            try:
                user = auth.login(request, form.get_user())
                # print(user)
                # print(form.get_user())
                return HttpResponseRedirect(reverse('superAdmin:signin'))
            except Exception as e:
                print('user can\'t logged in after register')

        else:
            print('error ase ', form.errors.as_data())

    else:
        form = AuthenticationForm()

    return render(request, 'superAdmin/signIn.html', {'form': form})

# -----------------------dashboard---------------------------


@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('superAdmin:signin'))
    else:
        all_clients = User.objects.all()
        # print(all_clients)

    context = {
        'all_clients': all_clients
    }

    return render(request, 'superAdmin/dashboard.html', context)

# -------------------------------view for each client-----------------------


def client(request, client_id):
    client = get_object_or_404(User, id=client_id)

    acropolis_form = AcropolisForm(instance=client.acropolismodel)
    sarawak_form = SarawakForm(instance=client.sarawakmodel)
    visa_form = VisaForm(instance=client.visamodel)

    # print(client.acropolismodel.user_profile.first_name)
    if request.method == 'POST':
        if request.POST['submit'] == 'AcropolisForm':                               # if acropolis form is submitted
            user = client  # get current user
            acropolis_form = AcropolisForm(request.POST,instance=user.acropolismodel )
            if acropolis_form.is_valid():
                acropolis_form.save(commit=True)

        elif request.POST['submit'] == 'SarawakForm':                               # if sarawak form is submitted
            user = client
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            if sarawak_form.is_valid():
                sarawak_form.save(commit=True)

        elif request.POST['submit'] == 'VisaForm':                               # if Visa form is submitted
            user = client
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if visa_form.is_valid():
                visa_form.save(commit=True)
                visa_form = VisaForm()
            

        elif request.POST['submit'] == 'AllForm':
            user = client
            acropolis_form = AcropolisForm(request.POST, instance=user.acropolismodel)
            sarawak_form = SarawakForm(request.POST, instance=user.sarawakmodel)
            visa_form = VisaForm(request.POST, instance=user.visamodel)
            if acropolis_form.is_valid() and sarawak_form.is_valid() and visa_form.is_valid():
                acropolis_form.save()
                sarawak_form.save()
                visa_form.save()

    context = {
        'user': client,
        'acropolis_form': acropolis_form,
        'sarawak_form': sarawak_form,
        'visa_form' : visa_form
    }

    return render(request, 'superAdmin/clientProfile.html', context)
