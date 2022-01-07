from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Question, Quiz

from .serializers import GetAllQuizSerializer, GetQuestionSerializer

"""
1. Get all quiz
2. Get All Questions for that quiz
3. Get all choices for that question
4. Get all Answers for that question
5. Get questions of a particular user
"""

class GetAllQuizView(ListAPIView, GenericViewSet):
    """
    This view is to get all quizes
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetAllQuizSerializer
    queryset = Quiz.objects.all()

class GetQuestionsForQuizView(ListAPIView, GenericViewSet):
    """
    Get all the questions for particular quiz
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetQuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        return Question.objects.filter(quiz = Quiz.objects.get(pk = self.kwargs['qid']))