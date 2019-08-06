from django import template
from qusans.models import Answer

register = template.Library()

@register.simple_tag (name='total_answers_of_this_question', takes_context=True)
def total_answers_of_this_question(context,question_id):
    print("custom tag")
    #print(context)
    print(question_id)
    anslen = None
    try:
        anslen = Answer.objects.filter(id=question_id)
    except Exception:
        return 0
    return len(anslen)