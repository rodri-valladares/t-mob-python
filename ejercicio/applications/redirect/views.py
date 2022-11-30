from django.shortcuts import render

# from django.views.generic import (
#     ListView
# )

from rest_framework.generics import ListAPIView

from .serializers import RedirectSerializer

from .models import Redirect

# class ListRedirectByKey(ListView):
#     template_name = 'home.html'
#     context_object_name = 'redirect_date'

#     def get_queryset(self):
#         key_date = self.request.GET.get("kword", '')
#         lista = Redirect.objects.filter(key=key_date)
#         return lista

class RedirectListApiView(ListAPIView):

    serializer_class = RedirectSerializer

    def get_queryset(self):
        # key_date = self.request.GET.get("kword", '')
        # lista = Redirect.objects.filter(key=key_date)
        # return lista
        return Redirect.objects.all()