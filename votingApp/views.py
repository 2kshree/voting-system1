from django.shortcuts import render,redirect,get_object_or_404
from .forms import num,reg_page,Voteing
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from .models import number1,aadhaarnumber,voteringlist,votedata
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
def home(request):
    
    return render(request,'web/index.html')

def register(request):
    reg=reg_page()
    # print(reg_page)
    if request.method=='POST':
        reg=reg_page(request.POST)
        if reg.is_valid():
            reg.save()
            print("Register Successfully !!!")
            return redirect('login')
    return render(request,'web/reg.html',{'form':reg_page})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=="POST":
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('aadhaar')
            else:
                message="Username are Password incorrect"
                print(message)
                return render(request,'web/login.html',{'message':message})
    return render(request,'web/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        print("Logout")
        return redirect('home')



def send_otp(recipient_email):
    sender_email = 'hariviki7895@gmail.com'
    sender_password = 'kmvw rwph njsf amtu'
    recipient_email = 'matlabfabhost2023@gmail.com'

    otp = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'OTP for Verification'

    body = f"Your OTP is: {otp}. Please use this code to verify your identity."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)

    server.quit()

    return otp



def aadhaar(request):
    if request.user.is_authenticated:
        print("Welcome")
        aadhaar_form = num()
        entered_aadhaar = None
        message = None

        if request.method == "POST":
            aadhaar_form = num(request.POST)
            if aadhaar_form.is_valid():
                aadhaar_instance = aadhaar_form.save(commit=False)
                aadhaar_instance.save()
                message = 'Aadhaar number successfully enrolled.'
                # entered_aadhaar = aadhaar_form.cleaned_data['aadhaar']
                # if number1.objects.filter(aadhaar=entered_aadhaar).exists():
                #     message = 'Aadhaar number already enrolled.'
                    # otp = send_otp(request.user.email)
                    # request.session['otp'] = otp
                    # request.session['aadhaar'] = entered_aadhaar
                    # return redirect('aadhaar1')
                return render(request, 'web/aadhaar_next.html', {'message': message})
                    
            else:
                    
                    # otp = send_otp(request.user.email)
                    # request.session['otp'] = otp
                    # request.session['aadhaar'] = entered_aadhaar
                    # return redirect('aadhaar1')
                aadhaar_instance = aadhaar_form.save(commit=False)
                aadhaar_instance.save()
                message = 'Aadhaar number successfully enrolled.'
            
                return render(request, 'web/aadhaar_next.html', {'message': message})

        return render(request, 'web/aadhaar.html', {'data': aadhaar_form, 'number': entered_aadhaar, 'message': message})
    else:
        print("Please Login")
        message='Login User Account'
        return render(request, 'web/index.html', {'message': message})
    


@csrf_exempt
def aadhaar_next(request):
    if request.method == "POST":
        aadhaar = request.POST.get('number')
        # print(aadhaar)

        data = number1.objects.filter(aadhaar=aadhaar)
        print(data)

        if data:
            num_queryset = number1.objects.filter(aadhaar=aadhaar)
            # print(num_queryset)

            if num_queryset:
                num = num_queryset.first()
                # print(num)
                num_list = list(num_queryset.values())

                request.session['aadhaar'] = num_list

                otp = send_otp(request.user.email)
                request.session['otp'] = otp
                
                print("Hello")
                return render(request, 'web/aadhaar_next.html', {'data': data, 'num': num})
            else:
                message = 'Aadhaar number not found in aadhaarnumber.'
                return render(request, 'web/aadhaar_next.html', {'message': message})
        else:
            message = 'Aadhaar number not found in Database.'
            return render(request, 'web/aadhaar_next.html', {'message': message})
    else:
        return render(request, 'web/aadhaar_next.html')
    

@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        aadhaar = request.session.get('aadhaar')

        print("Entered OTP:", entered_otp)
        print("Stored OTP:", stored_otp)
        print("Aadhaar from session:", aadhaar)
        
        aadhaar_number = aadhaar[0]['aadhaar']

        print("Aadhaar Number:", aadhaar_number)
        
        user_aadhaar = number1.objects.get(aadhaar=aadhaar_number)
        print(user_aadhaar)
        if entered_otp == stored_otp:
            aadhaarnumber.objects.create(useraadhaar=user_aadhaar, otp=stored_otp)

            # Clear session variables
            # del request.session['otp']
            # del request.session['aadhaar']

            return redirect('voters')
        else:
            message = 'Invalid OTP. Please try again.'
            print(message)
            return render(request, 'web/aadhaar_next.html', {'message': message})

    return render(request, 'web/aadhaar_next.html')



def voters(request):
    print("Election team list")

    if request.user.is_authenticated:
        voters_list = voteringlist.objects.all()
        return render(request, 'web/voters.html', {'voters_list': voters_list})
    else:
        message = "Login to Your Account"
        print(message)
        return render(request, 'web/index.html', {'message': message})



def voterlist(request):
    if request.method == 'POST':
        form = Voteing(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('voters') 
    else:
        form = Voteing()

    return render(request, 'web/voterlist.html', {'form': form})



def voter_details(request, code):
    voter = get_object_or_404(voteringlist, pk=code)
    return render(request, 'web/voter_details.html', {'voter': voter})


def mine_block(request,code):
    global value
    try:
        latest_block = votedata.objects.last()
        aadhaar = request.session.get('aadhaar')
        # leadername = f"Leader-{latest_block.code + 1}" if latest_block else "Genesis Leader"
        aadhaar_number = aadhaar[0]['aadhaar']

        print("Aadhaar Number:", aadhaar_number)
        new_block = votedata.objects.create(
            leadername=code,
            user =aadhaar_number,
            previous_hash=latest_block.hash if latest_block else None
            
        )
        value=new_block.hash
        print(value)
        send_hash(request.user.email)
        message="Voting Successfully"
        print(message)
        return render(request, 'web/index.html', {'message': message})
    except:
        message='Already Vote for that Aadhaar Number'
        print(message)
        return render(request, 'web/index.html', {'message': message})

def send_hash(recipient_email):
    
    sender_email = 'hariviki7895@gmail.com'
    sender_password = 'kmvw rwph njsf amtu'
    recipient_email = 'matlabfabhost2023@gmail.com'

    otp = value

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Secret Key'

    body = f"Secret key : {otp}. Doesn't Share Any One else."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)

    server.quit()

    return otp

STATIC_USERNAME = 'admin@gmail.com'
STATIC_PASSWORD = '123456'
@csrf_exempt
def admin1(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == STATIC_USERNAME and password == STATIC_PASSWORD:
            # messages.success(request, 'Login successful!')
            return redirect('voterlist')
        else:
            messages.error(request, 'Login failed.')
    
    # return render(request, 'login_app/login.html')
    return render(request,'web/adminpanel.html')


def view_chain(request):
    # Order the blocks in descending order based on total votes
    blocks = votedata.objects.values('leadername').annotate(total_votes=Sum(1)).order_by('-total_votes')

    # Retrieve the leadername with the highest total votes
    winner = blocks.first()

    return render(request, 'web/view_chain.html', {'blocks': blocks, 'winner': winner})






# def view_chain(request):

#     blocks = votedata.objects.values('leadername').annotate(total_votes=Sum(1)).order_by('leadername')
#     print(blocks)
#     return render(request, 'web/view_chain.html', {'blocks': blocks})




# def view_chain(request):
#     blocks = votedata.objects.values('leadername', 'hash', 'previous_hash').annotate(total_votes=Sum('id')).order_by('-hash')
#     for block in blocks:
#         block['leader'] = voteringlist.objects.get(leadername=block['leadername']).image.url if block['leadername'] else ''
#     return render(request, 'web/view_chain.html', {'blocks': blocks})










#-------------------------------------------------------------------Testing Process--------------------------------------------------------

        # Use try-except to handle the case where the Aadhaar number does not exist
        # try:
        #     user_aadhaar = number1.objects.filter(aadhaar=aadhaar)
        # except number1.DoesNotExist:
        #     message = 'Aadhaar number does not exist.'
        #     print(message)
        #     return render(request, 'web/aadhaar_next.html', {'message': message})
        # ---------------------------------------------------

        # print("Welcome")
        # aadhaar_form = num()
        # if request.method == "POST":
        #     aadhaar_form = num(request.POST)
        #     if aadhaar_form.is_valid():
        #         entered_aadhaar = aadhaar_form.cleaned_data['aadhaar']
        #         if number1.objects.filter(aadhaar=entered_aadhaar).exists():
        #             message = 'Aadhaar number already enrolled.'
        #             # otp = send_otp(request.user.email)
        #             # request.session['otp'] = otp
        #             # request.session['aadhaar'] = entered_aadhaar
        #             # return redirect('aadhaar1')
        #             return render(request, 'web/aadhaar_next.html', {'message': message})
        #         else:
        #             print("Please Login")
        #             return redirect('home')


# def aadhaar(request):
#     if request.user.is_authenticated:
#         print("Welcome")
#         aadhaar_form = num()
#         entered_aadhaar = None
#         message = None

#         if request.method == "POST":
#             aadhaar_form = num(request.POST)
#             if aadhaar_form.is_valid():
#                 entered_aadhaar = aadhaar_form.cleaned_data['aadhaar']
#                 if number1.objects.filter(aadhaar=entered_aadhaar).exists():
#                     message = 'Aadhaar number already enrolled.'
#                     return redirect('aadhaar1')
#                 else:
#                     aadhaar_instance = aadhaar_form.save(commit=False)
#                     aadhaar_instance.save()
#                     message = 'Aadhaar number successfully enrolled.'
                
#                     return render(request, 'web/index.html', {'message': message})
                

#         return render(request, 'web/aadhaar.html', {'data': aadhaar_form, 'number': entered_aadhaar, 'message': message})
#     else:
#         print("Please Login")
#         return redirect('home')

# def aadhaar_next(request):
#     a="Welcome"
#     return render(request, 'web/aadhaar_next.html', {'data':a})