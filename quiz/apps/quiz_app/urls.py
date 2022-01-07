from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GetAllQuizView, GetQuestionsForQuizView
router = DefaultRouter()
router.register("getallquiz", GetAllQuizView)   

urlpatterns = router.urls + [
    path("getquestions/<int:qid>", GetQuestionsForQuizView.as_view({'get' : "list"}))
]
