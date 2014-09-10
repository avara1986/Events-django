.. contents::

======
Events
======

Information
===========

.. image:: https://travis-ci.org/avara1986/Django-rest-AngularJS.svg
    :target: https://travis-ci.org/avara1986/Django-rest-AngularJS

Events is a Django proyect focused on build events

Installation Basics
===================

* In your settings:

::

	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_HOST_USER = 'no-reply@your-domain.es'
	EMAIL_HOST_PASSWORD = '*****'
	EMAIL_USE_TLS = True
	DEFAULT_FROM_EMAIL = 'no-reply@your-domain.es'

Dev & Prod DDBB:
	
::

    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'test-django-cloud-sql-1234:django-test-1234',
            'NAME': 'test_django',
        }
    }

Constant Project:
	
::

	PROJECT_CONSTANTS = {'BASE_URL': 'http://192.168.1.9:999',
						 'RIA_URL': 'http://192.168.1.9:999/' + RIA_URL,
						}


Export Data:

::

	python manage.py dumpdata --indent=2 > data_initial.json
	
Load Data:

::

	python manage.py loaddata data_initial.json

	
Bower on Ubuntu:

:: 
	sudo ln -s /usr/bin/nodejs /usr/bin/node
	
First, lunch virtual env:

::

	source vevents/bin/activate

Stop virtual env:

::

	deactivate
	
if the Software have new dependencies, run:

::

	pip freeze > requirements.txt
	
Install Python Requirements

        pip install -r requirements.txt
        python setup.py develop

Install Bower + Grunt

		npm install -g grunt-cli bower

Install Assets

        #npm install
        sudo bower --allow-root install		
		
Deploy to GoogleAppEngine
===============================

At last, run this command of django-appengine-toolkit (Thanks Massimiliano!! https://github.com/masci/django-appengine-toolkit)

::

	python manage.py collectdeps -r requirements.txt

Deploy to GAE:

::

	appcfg.py update de4g/

Connect to DDBB:

::

	mysql -u root -h 173.194.87.247 -p -D test_django


Import data to DDBB:

::

	mysql -u root -h 173.194.87.247 -p -D test_django < test_django.sql
	
Collect statics:

::

	./manage.py collectstatic
	
Executing the test
==================

You need install project before

::

    python manage.py test revengeapp


Executing the test with tox
===========================

You DON'T need install project before. And you executing the tests with python 2.7/3.3 and Django 1.5/1.6

::

    pip install tox==1.7.1
    tox


Executing the test with tox and coverage
========================================

::

    sudo pip install coveralls==0.4.1
    coverage erase
    tox
    coverage combine
    coverage report -m
    coverage html
    chromium-browser htmlcov/index.html  # or another browser


Requirements
============

::

	Django==1.5
	GoogleAppEngineCloudStorageClient==1.9.0.0
	Pillow==2.4.0
	PyPDF2==1.21
	argparse==1.2.1
	django-appengine-toolkit==0.2.1
	html5lib==1.0b3
	qrcode==4.0.4
	reportlab==3.1.8
	six==1.6.1
	wsgiref==0.1.2
	xhtml2pdf==0.0.6
	
Warnings
========
If you use reportLab, it have an error in version 3.1.8. It was solved in the V. 3.1.10 but it´s not now in Pip. To solved it. you must see this commit:

::

	https://bitbucket.org/rptlab/reportlab/commits/ca6c60fd1f627a0f9c040b370ef52f9f4496d6f5


Reportlab have been modified to run in GAE, **libs/reportlab/rl_config.py - Line 92**

.. code-block:: python

	if '~' in d: d = os.path.expanduser(d)
