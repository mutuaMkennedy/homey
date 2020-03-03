from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'listings'

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^onsale/(?P<listing_id>[0-9]+)/$', views.onsale_detail, name='onsale_detail'),
	url(r'^rental/(?P<listing_id>[0-9]+)/$', views.rental_detail, name='rental_detail'),
	path('on_sale/<int:pk>/edit/', views.for_sale_update, name='update'),
	path('rental/<int:pk>/edit/', views.for_rent_update, name='rental_update'),
	path('<int:pk>/delete/', views.delete_listing, name='delete'),
	url(r'sell/$', views.listing_form, name='sell_listing_form'),
	url(r'list_your_rental/$', views.rental_listing_form, name='rental_listing_form'),
	url(r'^sale_like/$', views.sale_like, name = 'sale_like'),
	# url(r'^directions/$', views.directions, name = 'directions'),
	#url(r'^search/autocomplete/$', views.autocomplete),
    #url(r'^find/', views.FacetedSearchView.as_view(), name='haystack_search'),
	#rl(r'^find/rentals', views.rental_results, name='rental_search'),
	#APis

]
