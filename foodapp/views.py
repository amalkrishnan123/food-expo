# import razorpay
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.mail import send_mail
from django.shortcuts import render,redirect
from . forms import RegistrationForm,PartnerForm
from django.contrib import messages





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def partner_register(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('home') 
    else:
        form = PartnerForm()

    return render(request, 'home.html', {'form': form})

# # from .forms import RegistrationForm
# # from .models import Registration


# # # ---------- STEP 1: CREATE RAZORPAY ORDER ----------
# # def register_ajax(request):
# #     if request.method == 'POST':
# #         form = RegistrationForm(request.POST)
# #         if form.is_valid():

# #             category = form.cleaned_data['category']
# #             amount = 499 if category == 'student' else 999

# #             client = razorpay.Client(
# #                 auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
# #             )

# #             order = client.order.create({
# #                 'amount': amount * 100,   # paise
# #                 'currency': 'INR',
# #                 'payment_capture': '1'
# #             })

# #             return JsonResponse({
# #                 'status': 'success',
# #                 'order_id': order['id'],
# #                 'amount': amount,
# #                 'key': settings.RAZORPAY_KEY_ID
# #             })

# #         return JsonResponse({
# #             'status': 'error',
# #             'errors': form.errors
# #         })


# # # ---------- STEP 2: PAYMENT SUCCESS + EMAIL ----------
# # @csrf_exempt
# # def payment_success(request):
# #     if request.method == 'POST':

# #         # Razorpay response data
# #         razorpay_payment_id = request.POST.get('razorpay_payment_id')
# #         razorpay_order_id = request.POST.get('razorpay_order_id')
# #         razorpay_signature = request.POST.get('razorpay_signature')

# #         # VERIFY PAYMENT SIGNATURE (VERY IMPORTANT)
# #         client = razorpay.Client(
# #             auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
# #         )

# #         try:
# #             client.utility.verify_payment_signature({
# #                 'razorpay_payment_id': razorpay_payment_id,
# #                 'razorpay_order_id': razorpay_order_id,
# #                 'razorpay_signature': razorpay_signature
# #             })
# #         except razorpay.errors.SignatureVerificationError:
# #             return JsonResponse({'status': 'signature_failed'})

# #         # SAVE REGISTRATION
# #         form = RegistrationForm(request.POST)
# #         if not form.is_valid():
# #             return JsonResponse({'status': 'invalid_form', 'errors': form.errors})

# #         reg = form.save()

# #         # Fee logic
# #         amount = 499 if reg.category == 'student' else 999

# #         # EMAIL CONTENT
# #         subject = "Kerala Food Startup Expo 2026 – Registration Confirmed"

# #         message = f"""
# # Dear {reg.name},

# # Thank you for registering for the Kerala Food Startup Expo 2026.

# # EVENT DETAILS
# # -------------
# # 📅 Date   : 8th April 2026
# # 📍 Venue : Gokulam Convention Center, Kochi

# # PAYMENT DETAILS
# # ---------------
# # Category    : {reg.get_category_display()}
# # Amount Paid : ₹{amount}
# # Order ID    : {razorpay_order_id}
# # Payment ID  : {razorpay_payment_id}

# # Your registration and payment have been successfully completed.

# # For any assistance, contact us at:
# # 📞 +91 8848798607

# # Warm regards,
# # Kerala Food Startup Expo Team
# # Building the Future of Food
# # """

# #         send_mail(
# #             subject,
# #             message,
# #             settings.EMAIL_HOST_USER,
# #             [reg.email],
# #             fail_silently=False
# #         )

# #         return JsonResponse({'status': 'success'})

# #     return JsonResponse({'status': 'invalid_request'})


# # ---------- HOME ----------
def food_home(request):
    return render(request, 'home.html')


# # # ---------- UTILITY ----------
# # def get_fee(category):
# #     return 499 if category == 'student' else 999
