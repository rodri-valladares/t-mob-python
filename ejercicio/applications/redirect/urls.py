from django.urls import path


from . import views

urlpatterns = [
    path('key-list/', views.RedirectListApiView.as_view()),
    path('key-list/<str:key>/', views.ListRedirectByKey.as_view()),
]