from django.apps import apps

from django.urls import include, re_path, path  # > Django-2.0
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from oscar.views import handler403, handler404, handler500


admin.autodiscover()
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0
    re_path(r'^django-admin/', admin.site.urls),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    path('', include(apps.get_app_config('oscar').urls[0])),  # > Django-2.0
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        re_path(r'^403$', handler403, {'exception': Exception()}),
        re_path(r'^404$', handler404, {'exception': Exception()}),
        re_path(r'^500$', handler500),
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
