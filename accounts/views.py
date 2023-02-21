from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.

def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    total_customers=customers.count()
    total_orders=orders.count()

    delivered=orders.filter(status='Delivred').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    products=Products.objects.all()
    return render(request,'accounts/products.html',{'products':products})
def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    orders_count=orders.count()
    context={'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method=='POST':
        #print('Printing Post',request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}

    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk):
    
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method=='POST':
        #print('Printing Post',request.POST)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}

    return render(request,'accounts/order_form.html',context)
