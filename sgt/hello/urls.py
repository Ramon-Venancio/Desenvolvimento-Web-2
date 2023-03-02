from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello,name='hello'),
    path('<str:name>', views.greet, name='greet'),
    path('greet-html/<str:name>', views.html, name='html'),
    path('tia/<str:name>', views.tia_zap, name='tia_zap'),
]