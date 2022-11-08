from django.urls import path

from . import views

urlpatterns = [
    path('area', views.AreaApiView.as_view()),
    path('area/<int:pk>',views.AreaDetailView.as_view())
]
