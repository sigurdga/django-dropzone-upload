Django dropzone upload
======================

Example project for integrating [Dropzone.js](http://www.dropzonejs.com) with
[Django](https://www.djangoproject.com/).

Introduction
------------

[Dropzone.js](http://www.dropzonejs.com) by [Matias
Meno](https://github.com/enyo) is a javascript library for drag and drop file
uploading. It is very light and simple to configure and extend.

I have earlier created
[django-jquery-file-upload](https://github.com/sigurdga/django-jquery-file-upload),
which integrates [jquery-file-upload](https://github.com/blueimp/jquery-file-upload) by
[Sebastian Tschan](https://github.com/blueimp) with Django. That project has a
lot of functionality and tries to be a complete package of all you need. It also works on older browsers.

Django-dropzone-upload tries to be as minimal and simple to understand as
possible, as it should be fairly easy to with Dropzone.js functionality.

Howto
-----

We assume you have git, python and python-virtualenv already installed.

* Clone this repository: git clone https://github.com/sigurdga/django-dropzone-upload.git
* Change directory: cd django-dropzone-upload
* Create virtualenv: virtualenv venv
* Activate virtualenv: source venv/bin/activate
* Install dependencies into virtualenv: pip install -r requirements.txt
* Setup database: python manage.py syncdb
* Run development server: python manage.py runserver
* Open browser at localhost:8000

Limitations
-----------

Dropzone.js claims to work for modern browsers:

* Chrome 7+
* Firefox 4+
* IE 10+
* Opera 12+ (Version 12 for MacOS is disabled because their API is buggy)
* Safari 6+

Django-dropzone-upload does not try to do anything more than Dropzone in
its simplest form, so no delete, no listing of already uploaded, etc. in this
project.

Credits
-------

* [Sigurd Gartmann](https://github.com/sigurdga) for initial setup
* [João Paulo Dubas](https://github.com/joaodubas) created the `fileupload/response.py` initially for django-jquery-file-upload.

License
-------

Released under the [MIT license](https://github.com/sigurdga/django-dropzone-upload/blob/master/LICENSE)
