from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import SurveyViewSet, QuestionViewSet, AnswerViewSet, UserCreate, UserSurveys

router = DefaultRouter()

router.register('api/v1.0/surveys', SurveyViewSet, basename='surveys')
router.register('api/v1.0/questions', QuestionViewSet, basename='questions')
router.register('api/v1.0/answers', AnswerViewSet, basename='answers')


urlpatterns = [
    path('api/v1.0/users/', UserCreate.as_view(), name='user_create'),
    path('api/v1.0/user_surveys/<int:pk>/', UserSurveys.as_view(), name='user_surveys'),
    path('api/v1.0/auth/', obtain_auth_token)
]


urlpatterns += router.urls
