from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth.context_processors import PermWrapper

# Create your views here.

def is_superuser(user):
    return user.is_superuser

@login_required
def accounts(request):
    users = User.objects.all()
    context = {
        'users':users,
        'usernow':PermWrapper(request.user),
    }
    return render(request, 'accounts/users-page.html', context)

@login_required
def details(request, id):
    user = User.objects.get(pk=id)
    context = {
        'userx':user
    }
    return render(request, 'accounts/user-details.html', context)

@login_required
@user_passes_test(is_superuser)
def addUser(request):
    return render(request, 'accounts/add-user.html')

@login_required
@user_passes_test(is_superuser)
def add(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    userCheck = User.objects.filter(username=username)
    flag = False
    for i in userCheck:
        if i.username == username:
            flag = True
    if flag == True:
        return HttpResponse('User already exists')
    else:
        if password1==password2:
            password = password1
            newUser = User.objects.create_user(username=username, password=password, email=email)
            newUser.first_name = first_name
            newUser.last_name = last_name
            newUser.save()
            return redirect('/accounts')
        else: 
            return HttpResponse('Password Mismatch')

@login_required
@user_passes_test(is_superuser)
def deleteUser(request, id):
    user = User.objects.get(pk=id)
    context = {'user':user}
    return render(request, 'accounts/delete-user.html', context)

@login_required
@user_passes_test(is_superuser)
def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/accounts')
    
@login_required
@user_passes_test(is_superuser)
def editUser(request, id):
    user = User.objects.get(pk=id)
    context = {'user':user}
    return render(request, 'accounts/edit-user.html', context)

@login_required
@user_passes_test(is_superuser)
def edit(request, id):
    user = User.objects.get(pk=id)
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1==password2:
        password = password1
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    return redirect('/accounts')

def cancel(request):
    return redirect('/accounts')



def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Correct')
            next_page = request.POST.get('next', '/') # get next page
            # login_url = reverse('login') + '?next=' + next_page # generate login url
            print(next_page)
            login_url = next_page
            return redirect(login_url)
        
        else:
            print('Wrong Username or Password')
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login credentials'})
    else:
        next_url = request.GET.get('next', '/') # get next page
        context = {'next_url':next_url}
        print(next_url)
        return render(request, 'accounts/login.html', context)
    
@login_required
def logoutView(request):
    logout(request)
    return redirect('/')