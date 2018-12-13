import pycountry

# list of all coutmries


def all_countries():
    country_list = []

    for e in pycountry.countries:
        country_list.append((e.name, e.name))

    return country_list;