from django.urls import path
from users import views


urlpatterns = [
    path('registration/', views.register_view),
    path('authorization/', views.authorize_view)
]