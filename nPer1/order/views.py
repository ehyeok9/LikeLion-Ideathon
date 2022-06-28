from django.shortcuts import render, get_object_or_404

from accounts.models import User
from .models import Order, Store, Menu


def board(request):
    orders = Order.objects.all()
    return render(request, 'board.html', {'orders': orders})


def detail(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, 'detail.html', {'order': order})


def joinEnd(request):
    return render(request, 'joinEnd.html')


def menu(request):
    return render(request, 'menu.html')


def stores(request, food):
    stores = Store.objects.all()
    stores = stores.filter(foodCategory=food)
    return render(request, 'stores.html', {'stores': stores})


def order(request, id):
    store = get_object_or_404(Store, pk=id)
    menus = Menu.objects.all()
    menu = menus.filter(store=store)
    return render(request, 'order.html', {'store': store, 'menu': menu})


def orderEnd(request):
    if request.method == 'POST':
        
        host_option = request.POST['host_option']
        option_num = None

        if host_option == "count":
            option_num = request.POST['option_count']
        elif host_option == "time":
            option_num = request.POST['option_time']

        # menu append
        user_menus = []
        for i in range(int(request.POST['total_count'])):
            user_menus.append({'food_id': request.POST['food'+str(i)], 'amount': request.POST['amount'+str(i)]})

        menus = {}
        menus[request.user.id] = user_menus

        order = Order(
            store = get_object_or_404(Store, pk=request.POST['store']),
            host_option = request.POST['host_option'],
            option_num = option_num,
            pay_option = int(request.POST['pay_option']),
            users = {},
            total = 0,
            menus = menus,
            author = get_object_or_404(User, id=request.user.id),
        )
        order.save()
        
        return render(request, 'orderEnd.html')
