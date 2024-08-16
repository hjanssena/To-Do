from django.urls import path
from .views import new_entry, new_tag, active_task_view, done_task_view

urlpatterns = [
    path('newentry/', new_entry, name="newentry"),
    path('newtag/', new_tag, name="newtag"),
    path('', active_task_view, name="taskview"),
    path('donetasks/', done_task_view, name="donetaskview"),
]