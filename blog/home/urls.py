from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('post/<int:id>/',views.post,name='post'),
    path('delete/<int:post_id>/',views.delete,name='delete'),
    path('update/<int:post_id>/',views.update,name='update'),
    path('singlepost',views.singlepost,name='singlepost'),
    path('register',views.register,name='register'),
]
