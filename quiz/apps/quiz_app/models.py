from django.db import models
from django.contrib.auth import get_user_model



user_model = get_user_model()

class Quiz(models.Model):
    """
    This is a `quiz` model for Quiz app\n
    Fields:
    1. quiz_name -> Charfield
    2. created_user -> FK -> USER
    """
    quiz_name = models.CharField(max_length = 100)
    created_user = models.ForeignKey(user_model, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.quiz_name + " " + str(self.created_user)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"


class Question(models.Model):
    """
    This is a question model
    """
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return str(self.quiz) + " " + self.title

class Choice(models.Model):
    """
    This is a choice model
    """
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_1 = models.CharField(max_length = 140)
    choice_2 = models.CharField(max_length = 140)
    choice_3 = models.CharField(max_length = 140)
    choice_4 = models.CharField(max_length = 140)

    def __str__(self) -> str:
        return "Choices for question: " + str(self.question)


class Answer(models.Model):
    """
    Answer model of every question
    """
    answer = models.CharField(max_length = 140)
    answered_by = models.ForeignKey(user_model, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.answer + " " + str(self.answered_by)

