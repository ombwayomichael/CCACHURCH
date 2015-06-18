from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(self,request, user):
		return '/church/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exam1.views.home', name='home'),
    url(r'^church/', include('church.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/(.*)',admin.site.root),
    url(r'^photologue/',include('photologue.urls',namespace='photologue')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    #url(r'^church/comments/', include('fluent_comments.urls')),
)+ static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
