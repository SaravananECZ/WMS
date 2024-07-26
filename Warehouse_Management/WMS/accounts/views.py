from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Generate OTP
        otp = generate_otp()
        # Example function to send OTP via email
        send_otp_email(email, otp)
        # Store email and OTP in session for verification
        request.session['otp_email'] = email
        request.session['otp'] = otp
        # Redirect to OTP verification page
        return redirect('verify_otp')
    # If GET request or after form submission
    return render(request, 'accounts/register.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        if entered_otp == saved_otp:
            # Clear OTP data from session after successful verification
            email = request.session.get('otp_email')
            del request.session['otp_email']
            del request.session['otp']
            messages.success(request, 'OTP verified successfully. You can now create your account.')
            return redirect('create_account', email=email)
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    # If GET request or after form submission
    return render(request, 'accounts/verify_otp.html')

def create_account(request, email):
    if request.method == 'POST':
        password = request.POST.get('password')
        # Here you can create the account with the provided email and password
        # For demonstration, let's assume account creation was successful
        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('login')  # Redirect to login page after account creation
    return render(request, 'accounts/create_account.html', {'email': email})

def generate_otp():
    length = 6  # Length of the OTP
    letters_and_digits = string.digits  # Using only digits for OTP
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def send_otp_email(email, otp):
    smtp_server = 'smtpout.secureserver.net'
    smtp_port = 465  # For SSL
    sender_email = 'saravanan@ecosoftzolutions.com'
    receiver_email = email
    password = 'Ezsaravanan@2071'
    subject = 'OTP Verification'  # Subject with OTP
    body = f"""
    <html>
    <head></head>
    <body>
        <p>Hello,<br>
           This is an OTP email message.<br>
           Your OTP is: {otp}<br>
           Regards,<br>
           Sender
        </p>
    </body>
    </html>
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    # Send the email using SMTP with SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")

def login(request):
    return render(request, 'accounts/login.html')
