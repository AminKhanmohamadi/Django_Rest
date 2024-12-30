from rest_framework.routers import SimpleRouter
from ..views.admin import CategoryViewSet
router = SimpleRouter()
router.register('categories' , CategoryViewSet , basename='category')

urlpatterns = router.urls