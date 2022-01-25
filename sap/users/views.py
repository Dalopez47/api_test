from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from users.filters import OrderFilter
from users.forms import PersonaForm
from users.models import User


def listUser(request):
    search_for = request.POST.get("search")
    users = User.objects.all()

    if search_for:
        users = User.objects.filter(
            Q(name__icontains = search_for) |
            Q(lastname__icontains = search_for) |
            Q(company__icontains = search_for) |
            Q(email__icontains = search_for) |
            Q(address__icontains = search_for) |
            Q(city__icontains = search_for)
        ).distinct()

    return render(request, 'list.html', {'user': users})

class list_user(ListView):
    model = User
    template_name = 'list.html'
    context_object_name = 'users'

def detailUser(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'detail.html', {'user': user})



def newUser(request):
    if request.method == 'POST':
         formUser = PersonaForm(request.POST)
         if formUser.is_valid():
             formUser.save()
             return redirect('index')
    else:
         formUser = PersonaForm()

    return render(request, 'new.html', {'formUser' : formUser})


def editUser(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
         formUser = PersonaForm(request.POST, instance=user)
         if formUser.is_valid():
             formUser.save()
             return redirect('index')
    else:
        formUser = PersonaForm(instance=user)

    return render(request, 'edit.html', {'formUser' : formUser})


def deleteUser(request, id):
    user = get_object_or_404(User, pk=id)
    if user:
        user.delete()
        return redirect('index')

def listUsers(request):
    template_name = "list.html"
    users = User.objects.all()

    myFilter = OrderFilter(request.POST, queryset=users)
    client = myFilter.qs
    context = {
        'users':users,
        'user':users,
        'myfilter':myFilter,
        'client': client,

    }
    return render(request, template_name, context)
