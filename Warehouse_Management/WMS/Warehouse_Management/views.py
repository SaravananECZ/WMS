# In views.py

from django.shortcuts import render, redirect
from .forms import WarehouseDetailsForm
from django.shortcuts import render
from .models import Item  # Import your model here

def search_view(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    results = []

    if query:
        # Perform a search on your model. Modify as needed.
        results = Item.objects.filter(name__icontains=query)  # Example search filter

    return render(request, 'warehouse_management/search.html', {'query': query, 'results': results})

def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page or another view
    else:
        form = WarehouseDetailsForm()
    
    return render(request, 'warehouse_form.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import WarehouseForm

def warehouse_selection_view(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            selected_warehouses = form.cleaned_data['types_of_warehouses']
            # Save selected items to the session or database if needed
            request.session['selected_warehouses'] = selected_warehouses
            return redirect('warehouse_selection')
    else:
        form = WarehouseForm()
        # Load selected items from the session or database if needed
        selected_warehouses = request.session.get('selected_warehouses', [])

    return render(request, 'warehouse_selection.html', {
        'form': form,
        'selected_warehouses': selected_warehouses
    })
