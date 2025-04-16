from django.urls import path
from . import views
from app_cancer.views import LungCancerView

urlpatterns = [
    #path('', views.predict_cancer, name='predict_cancer'),
    path('', LungCancerView.as_view(), name='cancer_list'),
]
