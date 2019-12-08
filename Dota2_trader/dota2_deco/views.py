from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Decorations, Items

def index(request):
    # latest_item_list = Items.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('dota2_deco/index.html')
    # context = {
    #     'latest_item_list': latest_item_list,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse("hello")

 def detail(request, question_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'dota2_deco/detail.html', {'item': item, 'decoration': item.item_type})