# attendance/urls.py
from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    RosterListView,
    RosterDetailView,
    AttendanceCreateView,
    AssignedShiftsView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("rosters/", RosterListView.as_view(), name="roster-create"),
    path("rosters/<int:pk>/", RosterDetailView.as_view(), name="roster-detail-patch"),
    path("attendance/", AttendanceCreateView.as_view(), name="attendance-create"),
    path("assigned-shifts/", AssignedShiftsView.as_view(), name="assigned-shifts"),
]
