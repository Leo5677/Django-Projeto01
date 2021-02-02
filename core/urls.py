from django.urls import *
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('produto/<int:pk>', ProdutoView.as_view(), name='produto'),
]
