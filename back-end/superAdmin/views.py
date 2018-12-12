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
        print(request.user)
        return HttpResponseRedirect(reverse('superAdmin:dashboard'))
    print('amar', request.user)
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            try:
                user = auth.login(request, form.get_user())
                print(user)
                print(form.get_user())
                return HttpResponseRedirect(reverse('superAdmin:signin'))
            except Exception as e:
                print('user can\'t logged in after register')

        else:
            print('error ase ', form.errors.as_data())

    else:
        form = AuthenticationForm()

    return render(request, 'signIn.html', {'form': form})

# -----------------------dashboard---------------------------


@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('superAdmin:signin'))
    else:
        all_clients = User.objects.all()
        print(all_clients)
    return render(request, 'dashboard.html', {'all_clients': all_clients})

# -------------------------------view for each client-----------------------


def client(request, client_id):
    client = get_object_or_404(User, id=client_id)

    if request.method == 'POST':
        if request.POST['submit'] == 'AcropolisForm':  # if acropolis form is submitted
            acropolis_form = AcropolisForm(request.POST)
            if acropolis_form.is_valid():
                acropolis_form.save(commit=True)
                acropolis_form = AcropolisForm(instance=client.acropolismodel)
                sarawak_form = SarawakForm(instance=client.sarawakmodel)
                visa_form = VisaForm(instance=client.visamodel)
                context = {
                    'user': client,
                    'acropolis_form': acropolis_form,
                    'sarawak_form': sarawak_form,
                    'visa_form': visa_form
                }
                return HttpResponseRedirect(reverse('superAdmin:client', args=(client.id,)), context)

        elif request.POST['submit'] == 'SarawakForm':  # if sarawak form is submitted
            sarawak_form = SarawakForm(request.POST)
            if sarawak_form.is_valid():
                sarawak_form.save(commit=True)
                acropolis_form = AcropolisForm(instance=client.acropolismodel)
                sarawak_form = SarawakForm(instance=client.sarawakmodel)
                visa_form = VisaForm(instance=client.visamodel)
                context = {
                    'user': client,
                    'acropolis_form': acropolis_form,
                    'sarawak_form': sarawak_form,
                    'visa_form': visa_form
                }
                return HttpResponseRedirect(reverse('superAdmin:client', args=(client.id,)), context)

        elif request.POST['submit'] == 'VisaForm':  # if Visa form is submitted
            user = request.user
            visa_form = VisaForm(request.POST)
            if visa_form.is_valid():
                visa_form.save(commit=True)
                acropolis_form = AcropolisForm(instance=client.acropolismodel)
                sarawak_form = SarawakForm(instance=client.sarawakmodel)
                visa_form = VisaForm(instance=client.visamodel)
                context = {
                    'user': user,
                    'acropolis_form': acropolis_form,
                    'sarawak_form': sarawak_form,
                    'visa_form': visa_form
                }
                return HttpResponseRedirect(reverse('superAdmin:client', args=(client.id,)), context)

        elif request.POST['submit'] == 'AllForm':
            acropolis_form = AcropolisForm(request.POST)
            sarawak_form = SarawakForm(request.POST)
            visa_form = VisaForm(request.POST)
            if acropolis_form.is_valid() & sarawak_form.is_valid() & visa_form.is_valid():
                acropolis_form = AcropolisForm(instance=client.acropolismodel)
                sarawak_form = SarawakForm(instance=client.sarawakmodel)
                visa_form = VisaForm(instance=client.visamodel)
                context = {
                    'user': client,
                    'acropolis_form': acropolis_form,
                    'sarawak_form': sarawak_form,
                    'visa_form': visa_form
                }
                return HttpResponseRedirect(reverse('superAdmin:client', args=(client.id,)), context)
    else:
        acropolis_form = AcropolisForm(instance=client.acropolismodel)
        sarawak_form = SarawakForm(instance=client.sarawakmodel)
        visa_form = VisaForm(instance=client.visamodel)
        context = {
            'user': client,
            'acropolis_form': acropolis_form,
            'sarawak_form': sarawak_form,
            'visa_form': visa_form
        }
        return render(request, 'clientProfile.html', context)
