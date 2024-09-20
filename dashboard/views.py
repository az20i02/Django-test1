from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from item.models import Item, ItemPhoto


@login_required
def indexDash(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'pages/indexDash.html',{
        'items': items,
    })

