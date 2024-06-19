from .views import TodoViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", TodoViewSet, basename="todo")
urlpatterns = router.urls
