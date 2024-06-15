# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, Roster, Attendance
from .serializers import UserSerializer, RosterSerializer, AttendanceSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    """
    Register API view
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginView(generics.GenericAPIView):
    """
    Login API view
    """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class IsManager(permissions.BasePermission):
    """
    Permission class to check if requested user is manager or not
    """

    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and request.user.is_manager
        )


class RosterListView(generics.ListCreateAPIView):
    """
    Api to post roster
    """

    queryset = Roster.objects.all()

    serializer_class = RosterSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            return Roster.objects.all()
        return Roster.objects.filter(user=user)


class RosterDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API to get,patch roster details
    """

    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]


class AttendanceCreateView(generics.CreateAPIView):
    """
    Attenndance Create view
    """

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AssignedShiftsView(generics.ListAPIView):
    """
    Get Assigned shifts view
    """

    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Fetch the roster entries for the logged-in user
        user = self.request.user
        print(user)
        return Roster.objects.filter(user=user)
