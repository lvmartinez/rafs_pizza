# rafs_pizza
# Pizza cms using django cms
# django CMS requires Django 1.8, 1.9 or 1.10 and Python 2.7, 3.3 or 3.4.

#create a root folder
mkdir rafs_pizza
cd rafs_pizza

# Install working environment on root folder
pip install --upgrade pip
pip install virtualenv
virtualenv env

# activate environment (for windows)
env\Scripts\activate

# Install django cms framework (if your working from scratch, otherwise just clone this project on the same root folder
pip install djangocms-installer

# Access project folder and run server
cd rafaels_pizza
python manage.py runserver

# More information
#http://docs.django-cms.org/en/release-3.4.x/introduction/install.html

