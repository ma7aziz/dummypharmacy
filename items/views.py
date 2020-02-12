from django.shortcuts import render
from .models import Item


# Create your views here.



def item_details(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, 'details.html', {'item':item})


def search(request):
    querset_list = Item.objects.order_by('-price')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            querset_list=querset_list.filter(name__icontains=keyword)
            print(querset_list)

    
    context={
        'items': querset_list,
        'count': len(querset_list)
    }
        
    return render(request, 'search.html', context)
