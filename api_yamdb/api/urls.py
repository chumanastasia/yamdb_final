from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('titles', views.TitleViewSet, basename='titles')
router.register('genres', views.GenreViewSet, basename='genres')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewset,
    basename='reviews'
)
router.register(
    'users',
    views.UserViewSet,
    basename='users')

auth = [
    path('signup/', views.register, name='register'),
    path('token/', views.get_jwt_token, name='token'),
]
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth))
]
