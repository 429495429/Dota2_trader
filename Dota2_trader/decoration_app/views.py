from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Decorations, Items

def index(request):
    latest_item_list = Items.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

 def detail(request, question_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'decoration_app/detail.html', {'item': item, 'is_recent': item.was_published_recently()})
