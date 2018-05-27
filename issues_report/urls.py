from django.urls import path
from . import views

app_name = 'issues_report'
urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<slug:ticket_id>', views.ticket, name='detail'),
]