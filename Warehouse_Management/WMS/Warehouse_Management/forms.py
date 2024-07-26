from django import forms
from .models import WarehouseDetails

class WarehouseDetailsForm(forms.ModelForm):
    class Meta:
        model = WarehouseDetails
        fields = ['Warehouse_Name', 'Warehouse_location', 'no_of_floors_available', 'Warehouse_square_feet','ground_floor_square_feet', 'first_floor_square_feet', 'Warehouse_amount', 'Warehouse_image', 'Additional_amount', 'permitted_items', 'prohibited_items']
      

class WarehouseForm(forms.Form):
    TYPES_OF_WAREHOUSES = [
        ('cold_storage', 'Cold Storage'),
        ('distribution_center', 'Distribution Center'),
        ('fulfillment_center', 'Fulfillment Center'),
        ('bulk_warehouse', 'Bulk Warehouse'),
        ('custom', 'Custom Type'),
    ]
    
    types_of_warehouses = forms.MultipleChoiceField(
        choices=TYPES_OF_WAREHOUSES,
        widget=forms.CheckboxSelectMultiple
    )