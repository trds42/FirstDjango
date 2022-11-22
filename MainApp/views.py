from django.shortcuts import render
from django.http import Http404
from MainApp.models import Item


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
        context = {
            "item": item
        }
        return render(request, "item.html", context)
    except Item.DoesNotExist:
        raise Http404(f"Товар с id={item_id} не найден")
