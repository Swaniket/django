from django.shortcuts import render, redirect
# To hit the db with these data, we need to use a model or write SQL
# In Django, we have build in model for our users
from django.contrib.auth.models import User,auth
# Import for messages
from django.contrib import messages

# Create your views here.
def register(request):
    # If it's a post method that means we are submitting data, according to out HTML
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Creating an object of the model object
        #filtering and checking conditions
        # Check if both password matches
        if password1 == password2:
            # Check if the username already exist
            if User.objects.filter(username = username).exists():
                #print('Username Taken')
                # To print in the same form
                messages.info(request, 'Username is taken')
                # Return to the register page if the registration goes wrong
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email is taken')
                return redirect('register')
            # If both username & email is unique
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                # Save the data
                user.save()
                print('User Created')
                # After the user creation it will redirect to login
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('register')

        return redirect('/')
        
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # If the user exist in the database it will give a user object
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
