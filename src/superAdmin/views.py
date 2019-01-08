from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from userProfileApp.forms import AcropolisForm, SarawakForm, VisaForm
from coreApp.commonData import visa_positions, sarawak_positions1, sarawak_positions2, sarawak_positions3, acropolis_positions
from coreApp.commonData import fontsize, max_char_fixed_font

from coreApp.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm

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
            acropolis_form = AcropolisForm(request.POST,instance=user.acropolismodel)
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

# -------------------------------view for each client-----------------------


def print_visa_form(request, client_id):
    client = get_object_or_404(User, id=client_id)
    pdfmetrics.registerFont(TTFont('hack.bold', 'hack.bold.ttf'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disvition'] = 'filename="somefilename.pdf"'
    p = canvas.Canvas(response, pagesize=A4)
    textobject = p.beginText()

    for k, v in visa_positions.items():
        p.setFont("hack.bold", size=0.37 * cm)
        if k == 'type_of_pass':
            if client.visamodel.type_of_pass == 'professional':
                p.drawString(v[0][0] * cm, v[0][1] * cm, 'X')
            elif client.visamodel.type_of_pass == 'social':
                p.drawString(v[1][0] * cm, v[1][1] * cm, 'X')
            elif client.visamodel.type_of_pass == 'business':
                p.drawString(v[2][0] * cm, v[2][1] * cm, 'X')
            elif client.visamodel.type_of_pass == 'temp':
                p.drawString(v[3][0] * cm, v[3][1] * cm, 'X')
        elif k == 'sarawakmodel.application_category_type':
            if client.k == 'new_application':
                p.drawString(v[0][0] * cm, v[0][1] * cm, 'X')
            elif client.k == 'renewal_application':
                p.drawString(v[1][0] * cm, v[1][1] * cm, 'X')
        elif k == 'sarawakmodel.gender':
            if client.k == 'male':
                p.drawString(v[0][0] * cm, v[0][1] * cm, 'X')
            elif client.k == 'female':
                p.drawString(v[1][0] * cm, v[1][1] * cm, 'X')
        elif k == 'acropolismodel.date_of_birth':
            p.drawString(v[0]*cm, v[1]*cm, client.k)
        elif k == 'trvl_doc_valid_till':
            p.drawString(v[0]*cm, v[1]*cm, client.visamodel.trvl_doc_valid_till)
        elif k == 'visa_req':
            if client.visamodel.visa_req == 'yes':
                p.drawString(v[0][0] * cm, v[0][1] * cm, 'X')
            elif client.visamodel.visa_req == 'no':
                p.drawString(v[1][0] * cm, v[1][1] * cm, 'X')
        elif k == 'visa_tpe':
            if client.visamodel.k == 'single entry':
                p.drawString(v[0][0] * cm, v[0][1] * cm, 'X')
            if client.visamodel.k == 'multiple entry':
                p.drawString(v[1][0] * cm, v[1][1] * cm, 'X')
        elif k == 'spnsr_add':
            add = client.visamodel.k
            value_length = len(client.visamodel.k)
            if  value_length > v[4]:
                first_line = add[:55]
                first_break = first_line.rfind(' ')
                if first_break == -1:
                    p.drawString(v[0][0] * cm, v[0][1] * cm, first_line)
                    second_line = add[55:]
                else:
                    first_line = add[:first_break]
                    p.drawString(v[0][0] * cm, v[0][1] * cm, first_line)
                    second_line = add[first_break:]
                if len(second_line) > v[4]:
                    second_break = second_line.rfind(' ')
                    if second_break == -1:
                        second_line = add[:55]
                        p.drawString(v[1][0] * cm, v[1][1] * cm, second_line)
                        third_line = second_line[55:]
                    else:
                        second_line = second_line[:second_break]
                        p.drawString(v[1][0] * cm, v[1][1] * cm, second_line)
                        third_line = second_line[second_break:]
                    if len(third_line) > v[4]:
                        third_break = third_line.rfind(' ')
                        if third_break == -1:
                            third_line = second_line[:55]
                            p.drawString(v[1][0] * cm, v[1][1] * cm, third_line)
                            fourth_line = second_line[55:]
                        else:
                            third_line = third_line[:third_break]
                            p.drawString(v[2][0] * cm, v[2][1] * cm, third_line)
                            fourth_line = third_line[third_break+1:]
                        p.drawString(v[3][0] * cm, v[3][1], fourth_line)
                    else:
                        p.drawString(v[2][0] * cm, v[2][1] * cm, third_line)
                else:
                    p.drawString(v[1][0] * cm, v[1][1] * cm, second_line)
            else:
                p.drawString(v[0][0] * cm, v[0][1], client.visamodel.k)
        else:
            if k == 'User.full_name':
                value = client.k
            else:
                value = client.visamodel.k
            if len(value) > v[1]:
                font_size = fontsize(value_char_len=len(value), base_char=v[1], field_length=v[2],
                                     base_font_size=0.37)
                if font_size <0.25:
                    max_char_one_line = max_char_fixed_font(base_char=v[1], field_length=v[2], base_font_size=0.37,
                                                            target_font=0.25)
                    p.setFont("hack.bold", size=0.25 * cm)
                    if value[max_char_one_line] != ' ':
                        first_line = value[:max_char_one_line] + '-'
                    else:
                        first_line = value[:max_char_one_line]
                    second_line = value[max_char_one_line:]

                    textobject.setTextOrigin(v[0][0] * cm, v[0][1]+0.27 * cm)
                    textobject.setFont("hack.bold", 0.25 *cm,0.27)
                    p.drawText(first_line + '\n' + second_line)
                else:
                    textobject.setTextOrigin(v[0][0] * cm, v[0][1] * cm)
                    textobject.setFont("hack.bold", font_size * cm, 0.27)


            else:
                p.drawString(v[0][0] * cm, v[0][1] * cm, value)


def print_sarawak_form(request, client_id):
    client = get_object_or_404(User, id=client_id)
    age = client.acropolismodel.his_age
    pdfmetrics.registerFont(TTFont('hack.bold', 'hack.bold.ttf'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disvition'] = 'filename="somefilename.pdf"'
    p = canvas.Canvas(response, pagesize=A4)
    textobject = p.beginText()
    date_of_birth = client.acropolismodel.date_of_birth
    date_of_expiry_of_passport = client.sarawakmodel.date_of_expiry_passport.strftime("%d %m %Y")

    for k,v in sarawak_positions1.items():
        if k is True:
            if k == 'age':
                if age >= 50:
                    p.setFont("Courier", size=0.5 * cm)
                    p.drawString(2.5 * cm, 20.8 * cm, "\u2713")  # 50 years and above
                else:
                    p.drawString(8.2 * cm, 20.8 * cm, "\u2713")  # 50 below
            elif k == 'application_category_type':
                p.setFont("Courier", size=0.5 * cm)
                if client.sarawakmodel.k == 'new_application':
                    p.drawString(2.5 * cm, 19.4 * cm, "\u2713")  # new
                elif k == 'renewal_application':
                    p.drawString(8.2 * cm, 19.4 * cm, "\u2713")  # renew
            elif k =='gender':
                p.setFont("Courier", size=0.5 * cm)
                if client.sarawakmodel.gender == 'male':
                    p.drawString(v[0][0]* cm, v[0][1]*cm, "\u2713")
                elif client.sarawakmodel.gender == 'female':
                    p.drawString(v[1][0]* cm , v[1][1],"\u2713")
            elif k == 'marital_status':
                p.setFont("Courier", size=0.5 * cm)
                if client.sarawakmodel.marital_status== 'single':
                    p.drawString(v[0][0], v[0][1],"\u2713")
                elif client.sarawakmodel.marital_status== 'married':
                    p.drawString(v[1][0], v[1][1], "\u2713")
                elif client.sarawakmodel.marital_status == 'divorced':
                    p.drawString(v[2][0], v[2][1], "\u2713")
                elif client.sarawakmodel.marital_status == 'widow/widower':
                    p.drawString(v[3][0], v[3][1], "\u2713")
                elif client.sarawakmodel.marital_status == 'other':
                    p.drawString(v[4][0], v[4][1], "\u2713")
                    p.setFont("hack.bold", size=0.5 * cm)
                    p.drawString(v[5][0]*cm, v[5][1]*cm, client.sarawakmodel.marital_status_other)
            elif k == 'accompanied_by_spouse' or k == 'accompanied_by_children':
                p.drawString(v[0], v[1], "\u2713")
            elif k == 'acropolismodel.date_of_birth':
                p.drawString(v[0], v[1], date_of_birth)
            else:
                value = client.sarawakmodel.k
                textobject.setTextOrigin(v[0][0] * cm, v[0][1] * cm)
                if len(value) > v[1]:
                        textobject.setFont("hack.bold", 0.5 * cm)
                        textobject.setCharSpace(0*cm)
                        if len(value[:]) > 34:
                            if value[34] != ' ':
                                first_line = value[:34] + '-'
                            else:
                                first_line = value[:34]
                            if len(value[34:]) > 34:
                                if value[68] != ' ':
                                    second_line = value[34:68] + '-'
                                else:
                                    second_line = value[34:68]
                                third_line = value[68:]
                                textobject.textLines(first_line+'\n'+second_line+'\n'+third_line)
                                p.drawText(textobject)
                            else:
                                second_line = value[34:]
                                textobject.textLines(first_line+'\n'+second_line)
                        else:
                            textobject.textLines(value)
                            p.drawText(textobject)
                else:
                    textobject.setFont("hack.bold", 0.5 * cm)
                    textobject.setCharSpace(0.63 * cm)
                    if len(client.sarawakmodel.k)> 12:
                        first_line = value[:12]
                        if len(value[12:]) >12:
                            second_line = value[12:24]
                            third_line = value[24:]
                            textobject.textLines(first_line+'\n'+second_line+'\n'+third_line)
                        else:
                            second_line = value[12:]
                            textobject.textLines(first_line+'\n'+second_line)
                            p.drawText(textobject)
                    else:
                        first_line = value[:]
                        textobject.textLines(first_line)
                        p.drawText(textobject)

        else:
            continue

    p.showPage()

    for k2, v2, in sarawak_positions2.items():
        if k2 is True:
            if k2 == 'acropolismodel.country_coode_1' or\
                    k2 == 'acropolismodel.area_code_1' or k2 == 'acropolismodel.phone_no_1' or\
                    k2 == 'acropolismodel.country_coode_2' or k2 == 'acropolismodel.area_code_2' or\
                    k2 == 'acropolismodel.phone_no_2':
                p.drawString(v2[0] * cm, v2[1] * cm, client.k)
            elif k2 == 'sarawakmodel.date_of_expiry_passport':
                p.drawString(v2[0] * cm, v2[1] * cm, date_of_expiry_of_passport)
            else:
                value = client.sarawakmodel.k
                textobject.setTextOrigin(v2[0][0]*cm,v2[0][1]*cm)
                if len(value) > v2[1]:
                    textobject.setFont("hack.bold", 0.5 * cm, 0.6 * cm)
                    textobject.setCharSpace(0 * cm)
                    if len(value[:])>34:
                        if value[34] != ' ':
                            first_line = value[:34] + '-'
                        else:
                            first_line = value[:34]
                        if len(value[34:])>34:
                            if value[68] != ' ':
                                second_line = value[34:68] + ' '
                            else:
                                second_line = value[34:68]
                            if len(value[68:])>34:
                                if value[102] != ' ':
                                    third_line = value[68:102] + '-'
                                else:
                                    third_line = value[68:102]
                                if len(value[102:])>34:
                                    if value[136]!= ' ':
                                        fourth_line = value[102:136] + '-'
                                    else:
                                        fourth_line = value[102:136]
                                    if len(value[136:])>34:
                                        if value[170] != ' ':
                                            fifth_line = value[136:170] + '-'
                                        else:
                                            fifth_line = value[136:170]
                                        if len(value[170:])>34:
                                            sixth_line =  value[170:]
                                            textobject.textLines(first_line + '\n' + second_line + '\n' + third_line +
                                                                 '\n' + fourth_line + '\n'+ fifth_line + '\n'+ sixth_line)
                                    else:
                                        fifth_line = value[136:]
                                        textobject.textLines(
                                            first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line +
                                            '\n'+ fifth_line)
                                else:
                                    fourth_line = value[102:]
                                    textobject.textLines(first_line +'\n'+ second_line +'\n'+ third_line+'\n'+fourth_line)
                            else:
                                third_line = value[68:]
                                textobject.textLines(first_line+'\n'+second_line+'\n'+third_line)
                        else:
                                second_line = value[34:]
                                textobject.textLines(first_line +'\n'+second_line)
                    else:
                        textobject.textLines(value)
                    p.drawText(textobject)
                else:            #  else if the length is less then base_char
                    textobject.setFont("hack.bold", 0.5 * cm, 0.6 *cm)
                    textobject.setCharSpace(0.63 * cm)
                    if len(value)>12:
                        first_line = value[:12]
                        if len(value[12:]) > 12:
                            second_line = value[12:24]
                            if len(value[24:])>12:
                                third_line = value[24:36]
                                if len(value[36:])>12:
                                    fourth_line = value[36:48]
                                    if len(value[48:])>12:
                                        fifth_line = value[48:60]
                                        sixth_line = value[60:]
                                        textobject.textLines(
                                            first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line +
                                            '\n' + fifth_line + '\n' + sixth_line)
                                        p.drawText(textobject)
                                    else:
                                        fifth_line = value[48:]
                                        textobject.textLines(
                                            first_line + '\n' + second_line + '\n' + third_line + '\n' +
                                            fourth_line + '\n' + fifth_line)
                                        p.drawText(textobject)
                                else:
                                    fourth_line = value[36:]
                                    textobject.textLines(first_line + '\n' + second_line + '\n' + third_line + '\n'+ fourth_line)
                                    p.drawText(textobject)
                            else:
                                third_line = value[24:]
                                textobject.textLines(first_line + '\n' + second_line+'\n'+third_line)
                                p.drawText(textobject)
                        else:
                            second_line = value[12:]
                            textobject.textLines(first_line+'\n'+second_line)
                            p.drawText(textobject)
                    else:
                        textobject.textLines(value)
                        p.drawText(textobject)

        else:
            continue

    p.showPage()

    for k3, v3 in sarawak_positions3.items():
        if k3 is True:
            if k3 == 'working_year_start1' or k3 == 'working_year_start2' or k3 == 'working_year_start3' or \
                    k3 == 'working_year_start4' or k3 == 'working_year_start5':
                p.setFont("hack.bold", size=0.4 * cm)
                p.drawString(v3[0], v3[1], client.sarawakmodel.k3 + '-' + client.sarawakmodel.v3[2])
            elif k3 == 'date_of_expiry_passport':
                p.setFont("hack.bold", size=0.5 * cm)
                p.drawString(v3[0], v3[1], client.sarawakmodel.k3)
            elif k3 == 'position1' or k3 == 'position2' or k3 == 'position3' or k3 == 'position4' or k3 == 'position5' or \
                    k3 == 'organization1' or k3 == 'organization2' or k3 == 'organization3' or k3 == 'organization4' \
                    or k3 == 'organization5':
                value = client.sarawakmodel.k3
                if len(value) > v3[1]:
                    font_size = fontsize(value_char_len=len(value), base_char=v3[1], field_length=v3[2],
                                         base_font_size=0.5)
                    if font_size < 0.35:
                        max_char_one_line = max_char_fixed_font(base_char=v3[1], field_length=v3[2], base_font_size=0.5,
                                                                target_font=0.35)

                        if value[max_char_one_line] != ' ':
                            first_line = value[:max_char_one_line] + '-'
                        else:
                            first_line = value[:max_char_one_line]

                        second_line = value[max_char_one_line:]
                        textobject.setTextOrigin(v3[0][0] * cm, v3[0][1] + 0.2 * cm)
                        textobject.setLeading(0.4)
                        textobject.setFont("hack.bold", font_size)
                        textobject.textLines(first_line + '\n' + second_line)
                        p.drawText(textobject)
                    else:
                        p.setFont("hack.bold", size=font_size * cm)
                        p.drawString(v3[0][0] * cm, v3[0][1] * cm, value, )
                else:
                    p.setFont("hack.bold", size=0.5 * cm)
                    p.drawString(v3[0][0] * cm, v3[0][1] * cm, value)
            else:
                value = client.sarawakmodel.k
                textobject.setTextOrigin(v3[0][0] * cm, v3[0][1] * cm)
                if len(value) > v3[1]:
                    textobject.setFont("hack.bold", 0.5 * cm, 0.6 * cm)
                    textobject.setCharSpace(0 * cm)
                    if len(value[:]) > 34:
                        if value[34] != ' ':
                            first_line = value[:34] + '-'
                        else:
                            first_line = value[:34]
                        if len(value[34:]) > 34:
                            if value[68] != ' ':
                                second_line = value[34:68] + ' '
                            else:
                                second_line = value[34:68]
                            third_line = value[68:]
                            textobject.textLines(first_line + '\n' + second_line + '\n' + third_line)
                        else:
                            second_line = value[34:]
                            textobject.textLines(first_line + '\n' + second_line)
                    else:
                        textobject.textLines(value)
                    p.drawText(textobject)
                else:
                    textobject.setFont("hack.bold", 0.5 * cm, 0.6 * cm)
                    textobject.setCharSpace(0.63 * cm)
                    if len(value) > 12:
                        first_line = value[:12]
                        if len(value[12:]) > 12:
                            second_line = value[12:24]
                            third_line = value[24:]
                            textobject.textLines(first_line + '\n' + second_line + '\n' + third_line)
                        else:
                            second_line = value[12:]
                            textobject.textLines(first_line + '\n' + second_line)

                    else:
                        textobject.textLines(value)
                    p.drawText(textobject)
        else:
            continue
    p.showPage()
    p.save()

    return response

def print_acropolis_form(request, client_id):
    client = get_object_or_404(User, id=client_id)
    pdfmetrics.registerFont(TTFont('hack.bold', 'hack.bold.ttf'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disvition'] = 'filename="somefilename.pdf"'
    p = canvas.Canvas(response, pagesize=A4)
    textobject = p.beginText()


    p.setFont("Helvetica", size=0.4 * cm)
    p.drawString(13.45 * cm, 15.2 * cm, "Business Set-up")  # Business set up text
    p.setFont("hack.regular", size=0.4 * cm,)
    p.drawString(13 * cm, 15.2 * cm, "\u25A1")  # Business set up check box
    for k, v in acropolis_positions.items():
        p.setFont("Helvetica", size=0.37 * cm)
        if k is True:
            if k == 'application_type':
                if client.acropolismodel.k == 'mm2h_peninsular':
                    p.drawString(v[0][0] * cm, v[0][1] * cm, "\u2713")
                elif client.acropolismodel.k == 'mm2h_sarawak':
                    p.drawString(v[1][0] * cm, v[1][1] * cm, "\u2713")
            elif k == 'application status':
                if client.acropolismodel.k == 'single_application':
                    p.drawString(v[0][0] * cm, v[0][1] * cm, "\u2713")
                elif client.acropolismodel.k == 'family_application':
                    p.drawString(v[1][0] * cm, v[1][1] * cm, "\u2713")
            elif k == 'is_business_set_up' and 'is_business_set_up' is True:
                p.drawString(v[0] * cm, v[1] * cm, "\u2713")
            elif k == 'User.date_joined' or k == 'acropolismodel.date_of_birth' or k == 'acropolismodel.no_of_chldrn_U21':
                p.drawString(v[1] * cm, v[2] * cm, client.k)
            else:
                if k == 'User.full_name':
                    value = client.k
                elif k == 'full_name2':
                    value = client.User.full_name
                else:
                    value = client.acropolismodel.k
                if len(value) > v[1]:
                    font_size = fontsize(value_char_len=len(value), base_char=v[1], field_length=v[2],
                                         base_font_size=0.37)
                    if font_size < 0.25:
                        max_char_one_line = max_char_fixed_font(base_char=v[1], field_length=v[2], base_font_size=0.37,
                                                                target_font=0.25)
                        p.setFont("hack.bold", size=0.25 * cm)
                        if value[max_char_one_line] != ' ':
                            first_line = value[:max_char_one_line] + '-'
                        else:
                            first_line = value[:max_char_one_line]
                        second_line = value[max_char_one_line:]

                        textobject.setTextOrigin(v[0][0] * cm, v[0][1] + 0.27 * cm)
                        textobject.setFont("hack.bold", 0.25 * cm, 0.27)
                        p.drawText(first_line + '\n' + second_line)
                    else:
                        textobject.setTextOrigin(v[0][0] * cm, v[0][1] * cm)
                        textobject.setFont("hack.bold", font_size * cm, 0.27)
                        textobject.textLines(value)
                else:
                    p.drawString(v[0][0] * cm, v[0][1] * cm, value)
        else:
            continue
    return response