from django.urls import path
from . import views
urlpatterns=[
    path('todo/',views.todo,name='todo'),
    path('add/',views.add,name='add'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
]