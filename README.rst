.. contents::

======
Events
======

Information
===========

.. image:: https://travis-ci.org/avara1986/Events-django.svg?branch=master
    :target: https://travis-ci.org/avara1986/Events-django

.. image:: https://coveralls.io/repos/avara1986/Events-django/badge.png?branch=master
  :target: https://coveralls.io/r/avara1986/Events-django?branch=master



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

	
Bower on Ubuntu:

:: 
	sudo ln -s /usr/bin/nodejs /usr/bin/node
	
First, lunch virtual env:

::

	source vevents/bin/activate

Stop virtual env:

::

	deactivate
	
Install Python Requirements

        pip install -r requirements.txt

Install Bower + Grunt

		npm install -g grunt-cli bower

Install Assets

        #npm install
        sudo bower --allow-root install		
		
	
Executing the test
==================

You need install project before

::

    python manage.py test events


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

	Django==1.6
	Pillow==2.4.0
	PyPDF2==1.23
	South==0.8.4
	argparse==1.2.1
	diff-match-patch==20121119
	dj-database-url==0.3.0
	dj-static==0.0.6
	django-extensions==1.4.0
	django-grappelli==2.4.5
	django-import-export==0.2.3
	django-toolbelt==0.0.1
	djangorestframework==2.4.2
	gunicorn==19.1.1
	html5lib==1.0b3
	httplib2==0.9
	psycopg2==2.5.4
	qrcode==5.0.1
	reportlab==3.1.8
	six==1.7.3
	static3==0.5.1
	tablib==0.10.0
	wsgiref==0.1.2
	xhtml2pdf==0.0.6
