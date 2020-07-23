from django.urls import include, path
from rest_framework import routers
from listings import views as listing_views
from accounts import views as acc_views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'listings', listing_views.ListingViewSet)
router.register(r'listingRatings', listing_views.ListingRatingViewSet)
router.register(r'realtors', acc_views.RealtorViewSet)
router.register(r'realtorRatings', acc_views.RealtorRatingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]