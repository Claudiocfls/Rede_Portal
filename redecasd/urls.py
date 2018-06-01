from django.urls import path, include
from . import views

app_name = 'redecasd'
urlpatterns = [
    path('', views.index, name='index'),
    path('membros/', views.member, name='member'),
    path('reservas/', views.schedule, name='schedule'),
    path('membros/update/<int:pk>', views.problem_report_update, name='problem_report_update'),

    path('reservas/create/<slug:date>', views.reservations_create, name='reservations_create'),
    # path('reservas/update/<int:pk>', views.reservations_update, name='reservations_update'),
    path('reservas/events/', views.reservations_events, name='reservations_events'),

]