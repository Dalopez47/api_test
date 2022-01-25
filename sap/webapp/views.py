from django.shortcuts import render
from users.models import User


def welcome(request):
    no_users_var = User.objects.count()
    users = User.objects.order_by('id')

    return render(request, 'welcome.html',{'no_users':no_users_var,
                                              'users':users})


