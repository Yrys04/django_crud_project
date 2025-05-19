from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import CarViewSet, UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.views.decorators.cache import never_cache
from rest_framework import permissions

# Создаем базовое представление схемы без неподдерживаемых параметров
schema_view = get_schema_view(
   openapi.Info(
      title="Car API",
      default_version='v1',
   ),
   public=True,
   patterns=[
        path('api/', include('cars.urls')),
    ],
   permission_classes=[permissions.AllowAny],
)

# Применяем декоратор never_cache к представлениям схемы
swagger_view = never_cache(schema_view.with_ui('swagger', cache_timeout=0))
redoc_view = never_cache(schema_view.with_ui('redoc', cache_timeout=0))

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.car_list, name='car_list'),
    # Используем представления с примененным декоратором
    path('swagger/', swagger_view, name='schema-swagger-ui'),
    path('redoc/', redoc_view, name='schema-redoc'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='cars/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.car_create, name='car_create'),
    path('update/<int:pk>/', views.car_update, name='car_update'),
    path('delete/<int:pk>/', views.car_delete, name='car_delete'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]