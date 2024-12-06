from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('tasks/past-week', views.TaskPastWeekView.as_view()),
    path('tasks/past-month', views.TaskPastMonthView.as_view()),
    path('tasks/past-3-months', views.TaskPast3MonthsView.as_view()),
    path('tasks/<str:start_date>/<str:end_date>/', views.TaskDateRangeView.as_view(), name='task-date-range'),

]

urlpatterns += router.urls