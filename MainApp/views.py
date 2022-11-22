from django.shortcuts import render
from django.http import Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, 'index.html')


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)


def item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={item_id} не найден")
    context = {
        "item": item
    }
    return render(request, "item.html", context)

