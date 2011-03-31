from django.conf.urls.defaults import *
from katok.main.views import pages, comment, view_gallery
from katok.main import views

#current_datetime
from django.conf import settings
if settings.DEBUG:


# Uncomment the next two lines to enable the admin:
    from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^katok/', include('katok.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     
     (r'^admin/', include(admin.site.urls)),
     
     #(r'^time/$', current_datetime),
     
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
            
        (r'^robots.txt$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'path': "robots.txt"}),
            
        (r'^favicon.ico$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'path': "favicon.ico"}),
            
 #       (r'^media/(?P<path>.*)$', 'django.views.static.serve',(r'^gallery/$', pages, {'template_name': 'gallery.html'}),
 #           {'document_root': settings.MEDIA_ROOT}),
     
     
     
     
     (r'^$', pages, {'template_name': 'index.html'}),
     (r'^index/$', pages, {'template_name': 'index.html'}),
     (r'^index.htm/$', pages, {'template_name': 'index.html'}),
     (r'^index.html/$', pages, {'template_name': 'index.html'}),
     (r'^price/$', pages, {'template_name': 'price.html'}),
     (r'^gallery/$', view_gallery),       
     (r'^contacts/$', pages, {'template_name': 'contacts.html'}),       
     (r'^comment/$', comment),
     
     
     
 #        (r'^search-form/$', views.search_form),
 #   (r'^search/$', views.search),    
)
