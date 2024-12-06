from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, logout_user, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path("register/", RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name="task"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name="task-delete"),
]
