from django.shortcuts import render, redirect
from django.http import HttpResponse
from HallBuddy_Soft import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if password != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        #Welcome Email
        subject = 'Welcome to HallBuddy'
        message = f'Hi {myuser.first_name}, thank you for registering in HallBuddy. We hope you have a great time here.\nWe havee also sent you a confirmation email, please confirm your email to activate your account. \n\nThank you\nHallBuddy Team'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Confirmation mail
        curent_site = get_current_site(request)
        conf_subject = 'Activate your HallBuddy account'
        conf_message = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': curent_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': account_activation_token.make_token(myuser),
        })
        email = EmailMessage(
            conf_subject, conf_message, settings.EMAIL_HOST_USER, [myuser.email]
        )
        email.fail_silently = True
        email.send()


        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')
    
    return render(request, 'authentication/signin.html')

def signout(request):
    pass

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
