from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.index,name='index'),
    # path('<str:user_name>/',views.main,name='name'),
    # path('<str:user_name>/<int:pk>/',views.edit,name='edit'),
    # path('<str:user_name>/<str:date>/',views.date,name='date'),
    # path('<str:user_name>/<str:date>/AI_choice',views.AI,name='AI')
]