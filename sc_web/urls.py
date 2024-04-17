
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('causes/', views.causes, name='causes'),
    path('signup/', views.signup, name='signup'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contactus, name='contactus'),
    path('donate/', views.donate, name='donate'),
    path('404/', views.pagenotfound, name='404'),
    path('blog_1/', views.blog_1, name='blog-details'),
    path('blog_2/', views.blog_2, name='blog_2'),
    path('blog_3/', views.blog_3, name='blog_3'),
    path('blog_4/', views.blog_4, name='blog_4'),
    path('blog_5/', views.blog_5, name='blog_5'),
    path('blog_6/', views.blog_6, name='blog_6'),
    path('contact-form-submit/', views.contact_form_submit, name='contact_form_submit'),
    # Add more paths as needed
]

