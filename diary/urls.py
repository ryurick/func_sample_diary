from django.urls import path
from .import views

app_name = 'diary'

urlpatterns = [
    path('',views.index, name='index'), #diary/
    path('add/',views.add, name='add'), #diary/add
    #ある特定のデータを取り出す<int:pk>　pk:primarykey modelsでmodelを作成した際、djangoが自動的に振るid。1,2,3…のように増加する
    path('update/<int:pk>/',views.update, name='update'), #diary/update/1
    path('delete/<int:pk>/',views.delete, name='delete'), #diary/delete/1
    path('detail/<int:pk>/',views.detail, name='detail'), #diary/detail/1
]