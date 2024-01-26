"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from .models import QuestionAndAnswer
from .forms import QuestionAndAnswerForm
import random

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def question_view(request):
    question_id = random.choice(QuestionAndAnswer.objects.values_list('id', flat=True))
    question_and_answer = get_object_or_404(QuestionAndAnswer, id=question_id)
    
    if request.method == 'POST':
        form = QuestionAndAnswerForm(request.POST)
        if form.is_valid():
            # Get the submitted answer from the form
            submitted_answer = form.cleaned_data['answer_text']
            # Check if the submitted answer matches the correct one
            if submitted_answer == question_and_answer.answer_text:
                # If the answer is correct, add a success message
                message = "Correct!"
            else:
                # If the answer is incorrect, add an error message
                message = "Incorrect!"
            
            return render(request,  'app/question.html', {'question_text': question_and_answer.question_text, 'form': form, 'message': message})
    else:
        form = QuestionAndAnswerForm(initial={'question': question_and_answer.question_text})

    return render(request,  'app/question.html', {'question_text': question_and_answer.question_text, 'form': form})
