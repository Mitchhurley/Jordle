"""
Definition of models.
"""

from django.db import models

# Basic question and answer models
class QuestionAndAnswer(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer_text = models.CharField(max_length=200)
