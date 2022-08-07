from django.urls import path
from organizations import views

urlpatterns = [
    path('', views.OrganizationView.as_view()),
    path('<int:id>', views.OrganizationView.as_view())
]

