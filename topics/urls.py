from rest_framework import routers
from topics.views import TopicViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"", TopicViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = router.urls
