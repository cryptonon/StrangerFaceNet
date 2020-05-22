from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='classify-home'),
    path('about/', views.about, name='classify-about'),
    # path('prediction/', views.predict, name='prediction')
]
