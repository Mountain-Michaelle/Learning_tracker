from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/new-topic/', views.new_topic, name='new_topic'),
    path('topics/new-entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]