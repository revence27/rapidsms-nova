RapidSMS Nova
=============

The new RapidSMS, for Rwanda.

- Compatible with Django 1.6.5
- Alternative ORM, with default PostgreSQL adapter.
- Sparse matrix storage for reports, with non-naïve implementation of relational calculus.
- Extensible data-transfer script, for large volumes (e.g., ≅ 13,000,000 entries) with dynamic feedback.
- Available as a RapidSMS installable application.
- Additional SMS processor
- Declarative lexical analyser for parsing SMS message formats, *à la* `lex(1)` and `yacc(1)`.
- Token-based error messaging, with idempotent persistence. Error code tokens have informative names, have a default message, need not be defined before being used to communicate to the user, and can be generated dynamically (with code names specialised for language, *et cetera*).
- The error code tokens can be re-defined by application-level code. Replacement text embeds codes which are processed and replaced by application-context data.
- Online reference for response codes, auto-generated from the configuration files.

TODO:
----
- ORM backward-compatible with Django ORM.
- Speed test and proof.
- Lazy querying.
- Total data transfer.
- All pages load (1).
- Interject our message-handler.
- Online technical documentation and tutorial (HTML and PDF).
- Data-generation.
- Dynamic query optimisation (narrowing the SELECT based on automatic analysis of named queries).
- Ensure that ThouTable implements full relational algebra (5 primitives).
- Ensure that ThouTable implements full monoid algebra.
- Ensure that ThouTable implements co-extensive functor algebra.
- Ensure that ThouTable implements traditional functional morphisms.
- grep -r TODO .

Rapidsmsrw1000
--------------

Below you will find basic setup instructions for the rapidsmsrw1000
project. To begin you should have the following applications installed on your
local development system:

- Python >= 2.6 (2.7 recommended)
- `pip >= 1.1 <http://www.pip-installer.org/>`_
- `virtualenv >= 1.8 <http://www.virtualenv.org/>`_
- MySQL >= 5.1
- git >= 1.7

For Ubuntu:

    sudo apt-get install python-dev

Getting Started
---------------

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    virtualenv --distribute rapidsmsrw1000-env
    source rapidsmsrw1000-env/bin/activate
    cd rapidsmsrw1000
    pip install -r requirements/base.txt

=====In the situation it fails to install distribute, you need to run the following command to rebuild python(Identified in python-2.7.3):
=====sudo apt-get install build-essential


Update your settings file::

    cp local.py.example settings.py

Configure settings as needed for your local environment.

Create the MySQL database and run the initial syncdb/migrate::

    mysql -u root -p
    mysql> CREATE DATABASE rapidsmsrw1000;
    mysql> CREATE USER rapidsmsrw1000 identified by '123456';
    mysql> GRANT ALL ON rapidsmsrw1000.* TO 'rapidsmsrw1000'@'%';
    mysql> GRANT ALL ON test_rapidsmsrw1000.* TO 'rapidsmsrw1000'@'%';
    mysql> FLUSH privileges;
    mysql> quit
    python manage.py syncdb

You should now be able to run the development server::

    python manage.py runserver

Many views in this project return a 404 error unless your user is associated
with a location. To associate a location, navigate to the Django admin and add
a new 'User Location' under the 'Ubuzima' section.
