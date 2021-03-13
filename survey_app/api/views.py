from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Survey, Question, Answer
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, UserSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserSurveys(APIView):
    def get(self, request, pk):
        answers = Answer.objects.filter(user_id=pk)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
