Helpful commands:
python manage.py runserver - run server
python manage.py shell - run shell
python manage.py startapp <Name of app> - creating folder with application files
python manage.py syncdb - creating tables in database(using models sructure)
python manage.py dbshell - using sql in python shell

----------------------------------------------------------------------------------------
Installing additional apps:
pip install sorl-thumbnail - for images resizing

----------------------------------------------------------------------------------------
Maybe should be need for media url schema:
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'site_media')
url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
MEDIA_URL = '/site_media/'
url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}), 
----------------------------------------------------------------------------------------

Items for future:
1) Enable email sending for button
2) Enable email sending in contact form
3) Make site map as dynamic feature
4) Improving url schema
5) Adding text to the foto fields
6) Updating all text information for seo optimization
7) Adding sections with text content for seo
8) Improving css styles and improving web site templates
9) Change ceny.html template with Anna
10) Make hyperlink to odnoklassniki page
11) To order 3 slide image at ui designer
