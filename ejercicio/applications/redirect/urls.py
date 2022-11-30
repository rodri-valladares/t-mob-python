from django.urls import path


from . import views

urlpatterns = [
    #path('buscar-key/', views.ListRedirectByKey.as_view()),
    path('buscar-key/', views.RedirectListApiView.as_view()),
]