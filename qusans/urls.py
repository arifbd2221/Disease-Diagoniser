from django.urls import path
from .views import *

urlpatterns = [
    path('q-a/', questionAnswer, name='qusans'),
    path('ask/question/', QuestionCreateView.as_view(), name='makequestion'),
    path('answer/<int:q_id>/', AnswerCreateView.as_view(), name='makeanswer'),
]