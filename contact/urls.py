from django.urls import path
from .views import list_contact_view, create_contact_view, update_contact_view, delete_contact_view

urlpatterns = [
    path("", list_contact_view.as_view(), name="contact_list"),
    path("create/", create_contact_view.as_view(), name="contact_create"),
    path("update/<int:pk>/", update_contact_view.as_view(), name="contact_update"),
    path("delete/<int:pk>/", delete_contact_view.as_view(), name="contact_delete")
]
