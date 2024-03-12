
from django.urls import path
from . import views

""" path('accounts/', include("django.contrib.auth.urls"))  """
   
urlpatterns = [
    path("accounts/register/",views.register, name="register"),
    path('accounts/login/', views.login_view, name='login')
    

    
]
