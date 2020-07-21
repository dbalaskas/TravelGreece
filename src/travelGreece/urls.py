from django.urls import include, path
from rest_framework import routers
from listings import views as lviews
from ratings import views as rviews
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'listings', lviews.ListingViewSet)
router.register(r'listing_ratings', rviews.ListingRatingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]