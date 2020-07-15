from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ar', views.ARViewSet)
router.register(r'smg', views.smgViewSet)
router.register(r'dmr', views.dmrViewSet)
router.register(r'sniper', views.sniperViewSet)
router.register(r'lmg', views.lmgViewSet)
router.register(r'pistol', views.pistolViewSet)
router.register(r'shotgun', views.shotgunViewSet)
router.register(r'other', views.otherViewSet)
router.register(r'health', views.healthViewSet)
router.register(r'grip', views.gripViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
     path('',views.home,name='home'),
    #  path('contact',views.contact,name='contact'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

