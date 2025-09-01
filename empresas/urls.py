from django.urls import include, path

from .views import EmpresaCreate

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
]