from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.index,name='index'),
    path('account_create/',views.create,name='create'),
    path('main/',views.main,name='name'),
    path('<int:pk>/',views.edit,name='edit'),
    path('AI_choice/',views.AI,name='AI'),
]