from django.urls import path
from Converter.views import Index, Conversion


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('convert/', Conversion.as_view(), name='convert'),
]
