from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from api.models import Task
from api.serializers import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class BaseTaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer

class TaskPastWeekView(BaseTaskListAPIView):
    queryset = Task.objects.filter(created__gte=timezone.now() - timedelta(days=7))

class TaskPastMonthView(BaseTaskListAPIView):
    queryset = Task.objects.filter(created__gte=timezone.now() - timedelta(days=30))

class TaskPast3MonthsView(BaseTaskListAPIView):
    queryset = Task.objects.filter(created__gte=timezone.now() - timedelta(days=90))

class TaskDateRangeView(BaseTaskListAPIView):
    """
    API view to filter tasks within a given date range.
    """

    def get_queryset(self):
        """
        Filter tasks based on the date range provided in the URL.
        """
        user = self.request.user
        start_date_str = self.kwargs.get('start_date')
        end_date_str = self.kwargs.get('end_date')

        # Parse dates
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if not start_date or not end_date:
            raise ValidationError("Invalid date format. Please use 'YYYY-MM-DD'.")

        if start_date > end_date:
            raise ValidationError("Start date cannot be later than end date.")

        # Use the correct field for filtering (e.g., `created`)
        return Task.objects.filter(user=user, created__date__range=[start_date, end_date])