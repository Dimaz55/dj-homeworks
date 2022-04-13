from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def calc(request):
    dish_name = request.path.strip('/')

    servings = request.GET.get('servings', 1)

    for ingr, amount in DATA[dish_name].items():
        DATA[dish_name][ingr] = round(amount * int(servings), 2)
    context = {'recipe': {'Количество блюд': servings}}
    context['recipe'].update(DATA[dish_name])

    return render(request, 'calculator/index.html', context)
