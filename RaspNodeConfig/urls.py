from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Form-based interface: server-side only
    path('', views.node_form, name="node_form"),
    path('rooms/', views.room_view, name='room_view'),
    path('<int:node_id>/<slug:capability>', views.capability_form, name="capability_form"),
]
