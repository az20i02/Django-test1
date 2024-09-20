from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.db.models import Q



def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)


    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))


    return render(request, 'pages/items.html',{
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]

    return render(request, 'pages/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            for img in request.FILES.getlist('images'):
                ItemPhoto.objects.create(item=item, image=img)

            return redirect('item:detail', pk=item.pk)
    else:
        form = NewItemForm()

    return render(request, 'pages/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            for img in request.FILES.getlist('images'):
                ItemPhoto.objects.create(item=item, image=img)

            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'pages/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:indexDash')
