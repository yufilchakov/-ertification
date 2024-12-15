from django.urls import path, include
from rest_framework.routers import DefaultRouter

from network.views import ContactsViewSet, NetworkViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/contacts/<int:pk>/', ContactsViewSet.as_view({'put': 'update'}), name='update'),
    path('api/network/<int:pk>/', NetworkViewSet.as_view({'put': 'update'}), name='update'),
    path('api/products/<int:pk>/', ProductViewSet.as_view({'put': 'update'}), name='update'),
]
