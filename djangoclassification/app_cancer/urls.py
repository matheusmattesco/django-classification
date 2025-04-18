from django.urls import path
from . import views
from django.views.generic import RedirectView
from app_cancer.views import LungCancerView, LungCancerEdit, LungCancerDelete

urlpatterns = [
    path('', RedirectView.as_view(url='list/'), name='index'),
    path('list/', LungCancerView.as_view(), name='list'),
    path('register/', views.LungCancerRegister.as_view(), name='register'),
    path('edit/<int:id>/', LungCancerEdit.as_view(), name='edit'),
    path('delete/<int:id>/', LungCancerDelete.as_view(), name='delete'),
] 
