from django.urls import path
from .views import index,detailed_task,todo_by_status,Createtodo,Createcategory,delete_task,update_task


urlpatterns=[

path('',index,name='home'),
path('detailed/<int:pk>',detailed_task,name='detail'),
path('todosstatus/<str:st>',todo_by_status,name='status'),
path('todo/create',Createtodo,name='createtodo'),
path('category/create',Createcategory,name='createcategory'),
path('todo/update/<int:id>' , update_task , name ="updatetask"),
path('todo/delete/<int:id>' , delete_task , name ="deletetask"),


]