from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, OrderForm
from .models import Order
from .utils import send_telegram_message
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'orders/home.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('orders:create_order')
    return render(request, 'orders/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('orders:create_order')
    return render(request, 'orders/login.html')

def logout_view(request):
    logout(request)
    return redirect('orders:home')

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders:profile')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

@login_required
def profile(request):
    orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'orders/profile.html', {'orders': orders})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    if request.method == 'POST':
        oid = request.POST.get('order_id')
        status = request.POST.get('status')
        o = Order.objects.get(pk=oid)
        o.status = status
        o.save()
    return render(request, 'orders/admin_orders.html', {'orders': orders})

@login_required
def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    form = OrderForm(request.POST or None, request.FILES or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('orders:profile')
    return render(request, 'orders/create_order.html', {'form': form})

@login_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:profile')
    return render(request, 'orders/delete_confirm.html', {'order': order})
