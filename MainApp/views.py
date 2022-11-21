from django.shortcuts import render, HttpResponse
from django.http import Http404

text_back_to_items = f"<a href = /items>Назад к списку товаров</a><br><br>"

author = {
    'name': 'Tatiana',
    'surname': 'Zubko',
    'second_name': 'Aleksandrovna',
    'phone': '8-923-600-01-02',
    'email': 'trds42@gmail.com'
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    context = {
        "author": author
    }
    return render(request, "about.html", context)


def items_list(request):
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)


def item(request, item_id):
    text = text_back_to_items
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, "item.html", context)
    raise Http404(f"Товар с id={item_id} не найден")
