from catalog import views as catalog_view
from rest_framework.routers import DefaultRouter

from catalog.views import ProductViewSet

app_name = 'catalog'

router = DefaultRouter()

router.register(r'products', ProductViewSet, base_name='products')

urlpatterns = router.urls
