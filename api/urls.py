from django.urls import path, include
from rest_framework import routers
from api import views

# maneja multiples rutas
router = routers.DefaultRouter()
# r para que no mal intermtrete los /1, /n como salto de línea, /t como una tabulación
# programmers para registrar eliminar o actualizar
# views.ProgramerViewSet para manejer las vistas correspondientes relacionadas al programador
router.register(r'programmers', views.ProgramerViewSet)

urlpatterns = [
    # router.urls le otorga todas las rutas creadas en router
    path('', include(router.urls))
]
