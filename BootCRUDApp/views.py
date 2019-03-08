from django.shortcuts import render, redirect, get_object_or_404
from .models import GarageSaleModel
from .forms import GarageSaleForm


# Create your views here.
# view to print all items in the model form as well as to add the form into the index html
def index(request):
    allItems = GarageSaleModel.objects.all()
    form = GarageSaleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    context = {
        "allItems": allItems,
        "form": form,
    }
    return render(request, 'BootCRUDApp/index.html', context)

# view to edit form
def edit(request, id):
    item = get_object_or_404(GarageSaleModel, pk=id)
    editItem = GarageSaleForm(request.POST or None, instance=item)
    if editItem.is_valid():
        editItem.save()
        return redirect('index')
    context = {
        'form': editItem
    }
    return render(request, 'BootCRUDApp/editItem.html', context)
