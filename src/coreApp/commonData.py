import pycountry

# list of all coutmries


def all_countries():
    countr_list = []

    for e in pycountry.countries:
        countr_list.append((e.name, e.name))
    return countr_list


def fontsize(value_char_len, base_char, field_length, base_font_size=0.37, ):
    each_char_width = field_length/value_char_len
    base_char_width = field_length/base_char
    font_size = (base_font_size/base_char_width) * each_char_width
    return font_size

def max_char_fixed_font(base_char, field_length, base_font_size, target_font):
    base_char_width = field_length/base_char
    each_char_width = (base_char_width/base_font_size) * target_font
    max_char = field_length/each_char_width
    if max_char is float:
        return int(max_char)
    else:
        return max_char


def acropolis_positions():
    Acropolis_positions= {'User.date_joined':(3.2,22.4),'reference_id':((9.9,22.4), 21, 4.6),
                          'User.full_name': ((4.1, 21.6), 48, 10.65), 'full_name2': ((2.55, 13.3), 25, 6),
                          'acropolismodel.date_of_birth':(4.4,20.8),
                          'passport_no':((10.6, 20.8), 17, 3.7), 'passport2':((11.1, 13.3), 19, 4.2),
                          'country_of_residence':((5.9,20.05), 10 , 2.2),
                          'nationality':((10.5,20.05), 18, 3.95),'name_of_the_spouse':((5.7,19.25), 40, 8.85),
                          'acropolismodel.no_of_chldrn_U21':(8.4,18.4),'current_add':((5.1,17.65), 59, 13.1),
                          'permanent_add':((5.6,16.85), 57, 12.65), 'email_add':((4.8,16.1), 25, 5.5),
                          'phone_no':((12.6,16.1), 22, 5.3), 'is_business_set_up':(12.9,15.4),
                          'application_type':((5.75,15.5), (9.35,15.5)),'application_status' :((5.4,14.7), (9,14.7)),}
    return Acropolis_positions


def visa_positions():
    visa_positions={'type_of_pass':((6.1,25),(8.4,25),(10.8,25),(15,25)), # professional, social, business, temp
                    'sarawakmodel.application_category_type': ((8.4,24),(10.8,24)), #new, renewal
                    'User.full_name': ((2.2,21), 60, 13.1),'sarawakmodel.gender': ((5.4,19.9),(8.25,19.9)),# first name, male, female
                    'place_of_birth': ((12.8,19.9), 32, 6.4),'acropolismodel.date_of_birth': (5.3,19.1),
                    'nationality':((12.8,18.8), 32, 6.4), 'trvl_doc_tpe':((6.3,16.25) , 31,6.82),
                    'trvl_doc_no': ((15.3,16.25), 18, 3.91), 'trvl_doc_issue_place': ((6.3,15.3) ,31, 6.82),
                    'strvl_doc_valid_till': (16.3,15.4), 'spnsr_frst_name': ((6.3,12.75) , 59, 13.1),
                    'spnsr_NRIC_no': ((6.3,11.85) , 19, 4.2), 'spnsr_telephone_no': ((15.4, 11.85) , 17, 3.73),
                    'spnsr_add': ((6.3,11.05), (6.3,10.2), (6.3,9.4), (6.3,8.65), 55), # address row 1,2,3,4
                    'spnsr_state': ((6.3,7.9), 28, 6.2),
                    'visa_req': ((8.3,5.6), (12.8,5.6)),# yes, no
                    'visa_tpe': ((8.3,4.5), (12.8,4.5)) # single entry, multiple entry
                     }

def sarawak_positions1():
    sarawak_positions_1={'age':((2.5,20.08), (8.2,20.08)),'application_category_type':((2.5,19.4), (8.2,19.4)), # 50 above, below ,# new , renewal
                       'accompanied_by_spouse':(2.5,17.8), 'accompanied_by_children':(8.2,17.8),
                       'User.full_name': ((8.4,15.4), 36, 10.5 ),
                       'gender': ((10.3,12.8), (13.1,12.8), ), 'marital_status': ((8.4,11.6), (11.1,11.6), (14.1,11.6),
                                                                                  (8.4,10.7), (12.9,10.7),(14.85,10.7), ),
                       'place_of_birth': ((8.4,9.1),24, 10.5 ), 'acropolismodel.date_of_birth': (8.3, 6.8),
                       'acropolismodel.nationality': ((8.5,5.55),24, 10.5 ),
                       'acropolismodel.passport_no': ((8,3.65),12, 10.5 )}
    return sarawak_positions_1



def sarawak_positions2():
    sarawak_positions_2={'sarawakmodel.date_of_expiry_passport': (8,26.7),
                       'permanent_add':((8,25.15), 72, 10.5),'mailling_add': ((8,20.75) ,72, 10.5),
                       'add_in_malaysia': ((8,16.3) ,72,  10.5),'acropolismodel.email_add':((8,11.95),24, 10.5 ),
                       'acropolismodel.country_coode_1':(8,9.65), 'acropolismodel.area_code_1':(10.4,9.65), 'acropolismodel.phone_no_1': (12.9,9.65),
                         'acropolismodel.country_coode_2':(8,8.7), 'acropolismodel.area_code_2':(10.4,8.7), 'acropolismodel.phone_no_2': (12.9,8.7),
                       'current_employment': ((8, 7.45),24, 10.5),'income_per_annum': ((8,5.55), 12, 10.5),
                       'current_organization': ((8,4.5), 36, 10.5)}
    return sarawak_positions_2

def sarawak_positions3():
    sarawak_positions_3={'current_organization_add': ((8,26.5), 36, 10.5),
                       'last_employment': ((8,23.55), 24, 10.5),'pension_recieved_perannum': ((8,21.7), 12,10.5),
                       'last_employer': ((8,20.4), 24, 10.5), 'last_employer_add': ((8,18.35), 36, 10.5),
                       'position1': ((3,8,14), 21, 6.25 ), 'organization1': ((10.46,14), 21, 6.25),
                       'working_year_start1': (16.5, 14 , 'working_year_end1'),
                       'position2': ((3.8,12.9), 21, 6.25), 'organization2': ((10.46, 12.9), 21, 6.25),
                       'working_year_start2': (16.5, 12.9, 'working_year_end2'),
                       'position3': ((3.8,11.7), 21, 6.25), 'organization3': ((10.46,11.7), 21, 6.25),
                       'working_year_start3': (16.5, 11.7, 'working_year_end3'),
                       'position4': ((3.8,10.59), 21, 6.25), 'organization4': ((10.46,10.59), 21, 6.25),
                       'working_year_start4': (16.5,10.59,'working_year_end4'),
                       'position5': ((3.8,9.4), 21, 6.25), 'organization5': ((10.46,9.4), 21, 6.25),
                       'working_year_start5': (16.5,9.4,'working_year_end5'),
                       }
    return sarawak_positions_3