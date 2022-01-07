from rest_framework.serializers import ModelSerializer

from .models import Question, Quiz


class GetAllQuizSerializer(ModelSerializer):
    """
    This serializer for getting all the quizzed
    """
    class Meta:
        model = Quiz
        fields = "__all__"


class GetQuestionSerializer(ModelSerializer):
    """
    This serializer for getting all the quizzed
    """
    class Meta:
        model = Question
        fields = "__all__"
