from django.core.cache import cache
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

        #verifico primero si se encuentra en cache
        querysetKeyEnCache = cache.get(self.kwargs['key'])
        
        if querysetKeyEnCache:
            print(f'-->Encontrado en cache {querysetKeyEnCache}')
            return querysetKeyEnCache
        
        key_date = self.kwargs['key']
        return Redirect.objects.filter(key=key_date)