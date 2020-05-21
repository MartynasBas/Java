from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formView.html/', views.formlist, name='formView'),
    # path('users/login/', views.formlist, name='formView'),
    path('formView/<int:id>/', views.formDetails, name="formDetails"),
    path('formView/<int:id>/pdf-download/', views.actformdetails, name='downloadpdf')
]