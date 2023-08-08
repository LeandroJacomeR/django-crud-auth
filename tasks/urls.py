from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.task, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:id>', views.task_detail, name='task_detail'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
