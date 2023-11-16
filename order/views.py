from django.shortcuts import render,HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from inventory.models import *

# Create your views here.

def create_order(request, id):
    inventory = Inventory.objects.get(id=id)
    
    if request.method == "POST":
        form = OrderForm(request.POST)  # Bind form data to request.POST
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            create_order = Orders.objects.create(item=inventory, quantity=quantity)
            create_order.save()
            return redirect('order_list')

    else:
        form = OrderForm() 

    return render(request, 'order/index.html', {'form': form})



def order_list(request):  
    orderss = Orders.objects.all()
    return render(request,"order/show.html",{'orderss':orderss})  

def RecivedOrder(request,id):
    orderss = Orders.objects.get(id=id)
    if orderss.is_received == False:
                orderss.is_received = True
                orderss.save()
                quantity = orderss.quantity
                item = orderss.item
                stock = Inventory.objects.filter(name=item).first()
                newstock = int(stock.quantity) + int(quantity)
                stock.quantity = newstock
                stock.save()
                return redirect("order_list")   
    else:
        return HttpResponse("Order Already Recived ")
    

def CancelOrder(request,id):
    orderss = Orders.objects.get(id=id)
    if orderss.is_cancel == False:
                orderss.is_cancel = True
                orderss.save()
                return redirect("order_list")         
    else:
        return HttpResponse("Order Already Cancel ")
    


def sell_order(request, id):
    inventory = Inventory.objects.get(id=id)
    quantity = inventory.quantity
    print(quantity)
    
    if request.method == "POST":
        form = SellForm(request.POST)  
        if form.is_valid():
            quantity_sold = form.cleaned_data['quantity_sold']
            # check for available quantity in the inventory
            if quantity >= quantity_sold :
                inventory.quantity -= quantity_sold
                inventory.quantity_sold += quantity_sold
                inventory.save()
                return redirect('show')
            else:
                return HttpResponse("The quantity you sold is not available.")

    else:
        form = SellForm() 

    return render(request, 'order/sell.html', {'form': form})



def create_trans(request, id):
    inventory = Inventory.objects.get(id=id)
    
    if request.method == "POST":
        form = TransForm(request.POST)  # Bind form data to request.POST
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            create_order = Transaction.objects.create(item=inventory, quantity=quantity)
            create_order.save()
            return redirect('trans_list')

    else:
        form = TransForm() 

    return render(request, 'order/create_trans.html', {'form': form})

def trans_list(request):
    transactions = Transaction.objects.all().order_by('-transactiondttm')
    return render(request,'order/trans.html',{'transactions':transactions})


def ApprovedTrans(request,id):
    transaction = Transaction.objects.get(id=id)
    quantity = transaction.quantity
    item = transaction.item
    stock = Inventory.objects.filter(name=item).first()
    newstock = int(stock.quantity) - int(quantity)
    stock.quantity = newstock
    stock.save()
    return redirect('show')
    #return render(request,'order/trans.html')
    # return redirect("order_list")   
    # else:
    #     return HttpResponse("Order Already Recived ")



# def create_order(request):  
#     if request.method == "POST":  
#         form = OrderForm(request.POST) 
#         if form.is_valid():  
#             try:  
#                 form.save()
#                 return redirect('order_list')  
#             except:  
#                 pass  
#     else:  
#         form = OrderForm()
#     return render(request,'order/index.html',{'form':form})  

# def destroy_order(request, id):  
#     order = Orders.objects.get(id=id)  
#     order.delete()  
#     return redirect("order_list")  


# def create_order(request, id):  
#     if request.method =="POST":
#         inventory = Inventory.objects.get(id=id)
#         quantity = request.POST['quantity']
#         create_order = Orders.objects.create(item=inventory,quantity=quantity)
#         create_order.save()
#         return redirect('order_list')  
#     return render(request, 'order/index.html')  