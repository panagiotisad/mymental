from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('rating page/', views.rating_page, name='rating_page'),
    path('statistics page/', views.statistics_page, name='statistics_page'),
    path('rating/', views.get_statistics, name='rating'),
    path('register page/', views.register_page, name='register_page'),
    path('logout/', views.log_out, name='logout'),
    path('to do list page/', views.to_do_list_page, name='to_do_list'),
    path('change_task_condition/<int:task_id>/',
         views.to_do_list_checkbox, name='to_do_list_checkbox'),
    path('task_delete/<int:task_id>', views.task_delete_view, name='task_delete')
]
