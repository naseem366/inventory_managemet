from django import forms  
from .models import *
import uuid


class InventoryForm(forms.ModelForm):  
    class Meta:  
        model = Inventory  
        fields = ['name','cost','selling_price']

    def clean(self):
 
        # data from the form is fetched using super function
        super(InventoryForm, self).clean()
         
        # extract the name and cost field from the data
        name = self.cleaned_data.get('name')
        cost = self.cleaned_data.get('cost')
        selling_price = self.cleaned_data.get('selling_price')
        # conditions to be met for the  length
        if name is None:
        #if len(name) < 4:
            self._errors['name'] = self.error_class([
                'Name is required'])
        if cost is None :
            self._errors['cost'] = self.error_class([
                'Cost Quntity is required'])
        if cost >= selling_price :
            self._errors['selling_price'] = self.error_class([
                'Selling price is grater than Cost ']) 
        #qs = Inventory.objects.create(name=name,cost=cost,selling_price=selling_price,inn=uuid.uuid4[0:6])
        # return any errors if found
        return self.cleaned_data
    
    def save(self, commit=True):
        instance = super(InventoryForm, self).save(commit=False)
        
        # Generate a random mixed with number and string to in field.
        # instance.random_number = random.randint(1, 1000)  # Adjust the range as needed.
        instance.iin = uuid.uuid4().hex[0:6]  # Adjust the range as needed.
       
        if commit:
            instance.save()
        return instance
    

# # Your Inventory model and other imports...

# class InventoryForm(forms.ModelForm):
#     class Meta:
#         model = Inventory
#         fields = ['item_name']  # Include any other fields you want to capture in the form.

#     def save(self, commit=True):
#         instance = super(InventoryForm, self).save(commit=False)
        
#         # Generate a random number and save it to the 'random_number' field.
#         instance.random_number = random.randint(1, 1000)  # Adjust the range as needed.
        
#         if commit:
#             instance.save()
#         return instance

