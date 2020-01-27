# Overview

This is a web app to automate the form fill up process of a company for its for its clients.
Users can create account and fill three forms. In the admin site, informations of the clients are available
for editing and the generate pdf to print them on forms. The informations will fill the empty blanks
and reduce its fontsize or create a second line so that it fits in the space provided by the form.
This is an incomplete project. Please read the Usage below to see how it works

# Requirements

conda(4.5.11) (https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

python(3.5.6) (provided in the Usage section below)

Django(2.1.1) (provided in the Usage section below)

Reportlab(3.5.12) (https://docs.djangoproject.com/en/3.0/howto/outputting-pdf/#install-reportlab)

Django rest-framwork(3.9.0) (https://www.django-rest-framework.org/#installation)

widget-tweaks (https://pypi.org/project/django-widget-tweaks/)

django-filters (https://django-filter.readthedocs.io/en/master/guide/install.html)

django_countries (https://pypi.org/project/django-countries/#installation)

# Usage

Firts install conda from the above link. Then Create an environment using the following command:

	conda create --name testenv python=3.5.6 django=2.1.1
	
activate the environment

	source activate testenv
  
install the following packages

	python -m pip install reportlab

	pip install djangorestframework

	pip install django-filter

	pip install django-countries

	pip install django-widget-tweaks
  
Now got src directory in which manage.py file is located. Run
	
	python manage.py runserver

login as user

	acrotasif@gmail.com
	korra1korra2

logout and go back to Navigation Page

	http://127.0.0.1:8000/

login as admin
	
	adminone@gmail.com
	korra1korra2

if the list of clients dont appear change the link

	http://127.0.0.1:8000/superAdmin/dashboard/
	
to

	localhost:8000/superAdmin/dashboard/

you might have to login again as admin

go to this url to see a clients profile
	
	http://localhost:8000/superAdmin/client/8

scroll down and click on print Sarawak form and you will see a PDF generated

press back to go to admin dashboard and logout.






	
