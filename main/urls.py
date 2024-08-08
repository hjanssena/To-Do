from django.urls import path
from .views import new_entry

urlpatterns = [
    path('newentry/', new_entry, name="newentry")
]