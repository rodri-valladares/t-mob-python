from django.shortcuts import render

# from django.views.generic import (
#     ListView
# )

from rest_framework.generics import ListAPIView

from .serializers import RedirectSerializer

from .models import Redirect

class RedirectListApiView(ListAPIView):

    serializer_class = RedirectSerializer

    def get_queryset(self):
        return Redirect.objects.all()

class ListRedirectByKey(ListAPIView):
    
    serializer_class = RedirectSerializer

    def get_queryset(self):
        key_date = self.kwargs['key']
        return Redirect.objects.filter(key=key_date)