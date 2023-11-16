from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
from django.conf import settings
import json

#managementjson = settings.MEDIA_ROOT / 'report' / 'management.json'
managementjson = settings.MEDIA_ROOT + 'report/management.json'
print(managementjson)

def management(request):
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except:
        data = {}
    
    jsonData = json.dumps(data)

    context = {'jsonData':jsonData}
    context.update(data)

    #return render(request,'ims/management.html')
    return render(request,'inventory/header.html')


def index(request):
   
    if request.method == "POST":  
        form = InventoryForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()
                return redirect('show')  
            except:  
                pass  
    else:  
        form = InventoryForm()
    return render(request,'inventory/index.html',{'form':form})  

def show(request):  
    inventorys = Inventory.objects.all()
    return render(request,"inventory/show.html",{'inventorys':inventorys})  

def edit(request, id):  
    inventory = Inventory.objects.get(id=id)
    form = InventoryForm()
    return render(request,'inventory/edit.html', {'inventory':inventory,'form':form})  

def update(request, id):  
    inventory = Inventory.objects.get(id=id)  
    print("Hello Update",inventory)
    form = InventoryForm(request.POST, instance = inventory)  
    if form.is_valid():  
        form.save()  
        return redirect('show')  
    return render(request, 'inventory/edit.html', {'inventory': inventory,'form':form})  

def destroy(request, id):  
    inventory = Inventory.objects.get(id=id)  
    inventory.delete()  
    return redirect("show")  