from django.shortcuts import render, redirect,get_object_or_404
from .forms import BillForm
from .models import Bill
from .forms import CustomerForm
from .models import Customer


def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bill_list.html', {'bills': bills})

def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'add_bill.html', {'form': form})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list page
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})




def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list page
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form})



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


