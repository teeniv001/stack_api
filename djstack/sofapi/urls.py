from django.urls import path,include
from .views import index,questionsAPI,latest
from rest_framework import routers

router = routers.DefaultRouter()
# .register takes few arguments --> 1} what will be the identification url 
router.register("questions" , questionsAPI)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('latest', latest, name='latest'),
]


# rest api -->http://127.0.0.1:8000/stack/questions/
# database_update --> http://127.0.0.1:8000/stack/latest
# admin --> http://127.0.0.1:8000/admin
# status check for api working or not --> http://127.0.0.1:8000/stack