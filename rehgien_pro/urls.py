from django.urls import path
from . import views
from profiles import pro_profile_setup_forms as pro_setup_forms

app_name = 'rehgien_pro'

urlpatterns = [
	path('', views.homepage, name = 'rehgien_pro_homepage'),

	path('home/', views.dashboard_home, name = 'dashboard_home'),
	path('insights/', views.dashboard_insights, name = 'dashboard_insights'),
	path('myproperties/', views.dashboard_properties, name = 'dashboard_properties'),
	path('jobs/', views.dashboard_jobs, name = 'dashboard_jobs'),

	path('join/', views.pro_join_landing, name = 'pro_join_landing'),
	path('onboarding/', views.ProSetupWizardView.as_view(views.FORMS), name='ProSetupWizardView'),
	path('find_customers/jobs/list/', views.jobs_list, name = 'jobs_list'),
	path('find_customers/jobs/<int:pk>/', views.job_detail, name = 'job_detail'),
	path('resources/blog/', views.blog_posts, name = 'blog_posts'),
	path('resources/blog/<slug:slug>/', views.blog_detail, name = 'blog_detail'),
	path('resources/blog/ajax_autocomplete/', views.ajax_blog_post_autocomplete, name = 'ajax_blog_post_autocomplete'),

	# Rehgien Agency Url Paths
	path('rehgien_agency/', views.r_agency_home, name = 'r_agency_home'),
]
