from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('personal/', views.personal, name='personal'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
]
