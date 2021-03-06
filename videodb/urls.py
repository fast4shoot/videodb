from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	# Examples:
	# url(r'^$', 'videodb.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', 'home.views.index', name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', include('home.urls')),
	url('^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
