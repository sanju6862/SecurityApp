from django.shortcuts import render, redirect
from .forms import FoundItemForm
from .models import Item
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
def lost_and_found(request):
    return render(request, 'LostFound/lost_and_found.html')

def report_found_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            if item.item_type == 'other':
                item.item_type  = 'Other'
            item.user = request.user
            item.save()
            form.save_m2m()  # Save many-to-many fields if any
            messages.success(request, 'Item reported successfully!')
            return render(request, 'LostFound/successreport.html', {'item': item})
    else:
        form = FoundItemForm()
    return render(request, 'LostFound/report_found_item.html', {'form': form})



def item_search(request):
    search_query = request.GET.get('search', '')
    filter_option = request.GET.get('filter_option', 'all')
  
    if filter_option == 'recovered':
        items = Item.objects.filter(is_recovered=True)
    elif filter_option == 'not_recovered':
        items = Item.objects.filter(is_recovered=False)
    else:
        items = Item.objects.all()

    if search_query:
        try:
            search_query = int(search_query)
            items = items.filter(
                Q(id=search_query) |
                Q(item_type__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        except ValueError:
            items = items.filter(
                Q(item_type__icontains=search_query) |
                Q(description__icontains=search_query)
            )

    items = items.order_by('-date_time')

    context = {
        'items': items,
        'filter_option': filter_option,
        'search_query': search_query
    }

    return render(request, 'LostFound/item_search.html', context)
def item_recovery(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'GET':
        # Perform the recovery process
        item.recovered_by = request.user
        item.is_recovered = True
        item.save()

        # Redirect to the recovery success page
        return render(request, 'LostFound/recovery_success.html',{'item' : item})
    item = Item.objects.order_by('date_time')
    return render(request, 'LostFound/item_search.html', {'items': item})
