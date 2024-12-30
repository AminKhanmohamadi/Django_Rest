from rest_framework.routers import SimpleRouter
from django.urls import path
from config.auths.users.views.admin import AdminLoginView

router = SimpleRouter()

urlpatterns = [
    path('login/', AdminLoginView.as_view()),
]+ router.urls