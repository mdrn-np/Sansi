from .views import TodoViewSet, AdminTodoViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("", TodoViewSet, basename="todo")
urlpatterns = router.urls
