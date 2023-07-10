# from django.urls import path
# from .views import index

# urlpatterns = [
#     path('http://127.0.0.1/lesson_4', index)
    
# ]
from django.urls import path
from .views import index

urlpatterns = [
    path('lesson_4/', index, name='index'),
]