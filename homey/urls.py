"""homey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from photologue.sitemaps import GallerySitemap, PhotoSitemap
from listings import views
from django.views.generic import TemplateView
from allauth.account.views import confirm_email
from django.contrib.sitemaps.views import sitemap
from listings.sitemap import PropertyListingsSitemap
from listings.sitemap import StaticViewSitemap
from markets.sitemap import JobPostSitemap
from profiles.sitemap import BusinessProfileSitemap
from resource_center.sitemap import BlogPostSitemap
#from haystack.forms import FacetedSearchForm
#from haystack.views import FacetedSearchView

sitemaps = {
    'property_listings':PropertyListingsSitemap,
    'job_posts':JobPostSitemap,
    'business_profiles':BusinessProfileSitemap,
    'blog_post':BlogPostSitemap,
    'static_content':StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    path('location/', include('location.urls')),
    path('listings/', include('listings.urls')),
    path('mortgage/', include('mortgage.urls')),
    path('contact/', include('contact.urls')),
    path('profile/', include('profiles.urls')),
    path('markets/', include('markets.urls')),
    path('pro/', include('rehgien_pro.urls')),
    path('resources/', include('resource_center.urls')),
    path('partnerships/', include('partnership.urls')),
    path('apis/', include('listings.apis.urls')),
    path('apis/', include('location.api.urls')),
    path('apis/', include('profiles.apis.urls')),
    path('apis/', include('markets.apis.urls')),
    path('apis/', include('contact.apis.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("select2/", include("django_select2.urls")),
    url(r'^apis/rest-auth/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),
    path('r/site/indexing/sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    # path('msg/', TemplateView.as_view(template_name = 'index.html')),
    #url(r'^search/', include('haystack.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('apis/api-auth/', include('rest_framework.urls')),
    url(r'^apis/rest-auth/', include('rest_auth.urls')),
    url(r'^apis/rest-auth/', include('rest_auth.urls')),
    url(r'^apis/rest-auth/registration/', include('rest_auth.registration.urls')),
    # re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name = 'index.html')),
]

sitemaps = {
        'photologue_galleries': GallerySitemap,
        'photologue_photos': PhotoSitemap,
}
