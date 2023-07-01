from django.shortcuts import render
from .models import Software, Plugin, User,Review,Payment
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    softwares = Software.objects.all()
    paginator = Paginator(softwares, per_page=4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # software = Software.objects.get(id=software_id)
    # total_views = Software.views.count()
    # context = {"softwares": softwares}
    return render(request, "index.html", {"page_obj": page_obj})


from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string


def search_api(request):
    from django.core.paginator import Paginator


from django.shortcuts import render
from django.http import JsonResponse

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

def search_api(request):
    query = request.GET.get("q")
    subscription = request.GET.get("subscription")
    license = request.GET.get("license")

    softwares = Software.objects.all()

    if query:
        softwares = softwares.filter(Q(name__icontains=query) | Q(tags__name__icontains=query)).distinct()

    if subscription:
        if subscription == "true":
            softwares = softwares.filter(
                Q(subscription__name="Standard") | Q(subscription__name="Premium")
            ).distinct()
        elif subscription == "false":
            softwares = softwares.filter(subscription__name="Free")



    if license:
        softwares = softwares.filter(license=license)

    paginator = Paginator(softwares, per_page=4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Construct the pagination information
    pagination = {
        "has_previous": page_obj.has_previous(),
        "has_next": page_obj.has_next(),
        "previous_page_number": page_obj.previous_page_number()
        if page_obj.has_previous()
        else None,
        "next_page_number": page_obj.next_page_number()
        if page_obj.has_next()
        else None,
        "current_page_number": page_obj.number,
        "page_range": list(page_obj.paginator.page_range),
    }

    # Construct the JSON response
    response = {
        "html": render(
            request, "software_gallery.html", {"page_obj": page_obj}
        ).content.decode("utf-8"),
        "pagination": pagination,
    }

    return JsonResponse(response)

# def search_api(request):
#     query = request.GET.get("q")
#     softwares = Software.objects.all()
    
#     if query:
#         softwares = softwares.filter(tags__name__icontains=query).distinct()
#         # print(softwares)
#     paginator = Paginator(softwares, per_page=4)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     # Construct the pagination information
#     pagination = {
#         "has_previous": page_obj.has_previous(),
#         "has_next": page_obj.has_next(),
#         "previous_page_number": page_obj.previous_page_number()
#         if page_obj.has_previous()
#         else None,
#         "next_page_number": page_obj.next_page_number()
#         if page_obj.has_next()
#         else None,
#         "current_page_number": page_obj.number,
#         "page_range": list(page_obj.paginator.page_range),
#     }

#     # Construct the JSON response
#     response = {
#         "html": render(
#             request, "software_gallery.html", {"page_obj": page_obj}
#         ).content.decode("utf-8"),
#         "pagination": pagination,
#     }

#     return JsonResponse(response)

from django.db.models import Avg
from django.shortcuts import render
from django.db.models import Count
from .models import Review
@login_required
def softwaredetails(request, software_id):
    user = request.user
    software = Software.objects.get(id=software_id)
    if user in software.views.all():
        # User has already viewed the software
        # Handle the logic accordingly
        pass
    else:
        # User is viewing the software for the first time
        software.views.add(user)
        software.save()
        # Increment the views count and perform other operations
    reviews = Review.objects.filter(software__id=software_id)
    avg=Review.objects.filter(software__id=software_id).aggregate(Avg('rating'))

    total_reviews = reviews.count()
    # Calculate the count and percentage for each rating category
    rating_counts = reviews.values('rating').annotate(count=Count('rating')).order_by('rating')
    rating_data = []
    for rating_count in rating_counts:
        rating_percentage = (rating_count['count'] / total_reviews) * 100
        rating_data.append({
            'rating': rating_count['rating'],
            'count': rating_count['count'],
            'percentage': rating_percentage,
        })

   
    related_software = get_related_software(software_id)
    print(related_software)
    return render(request, "softwaredetails.html", context={"software": software,"related":related_software,"ratings":avg,"rating_context":rating_data})


def plugins(request):
    plugins = Plugin.objects.all()
    paginator = Paginator(plugins, per_page=1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "plugins.html", {"page_obj": page_obj})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                "catalapp:home"
            )  # Replace 'home' with your desired homepage URL
        else:
            error_message = "Invalid credentials. Please try again."
    else:
        error_message = ""
    return render(request, "login.html", {"error_message": error_message})

from django.shortcuts import render, redirect
from .models import UserRequest
# from .forms import UserRequestForm


from django.shortcuts import render, redirect
from .models import Technology,Industry,TechStackList
@login_required
def request_view(request):
    if request.method == 'POST':
        software_name = request.POST.get('name')
        description = request.POST.get('description')
        industry_id = request.POST.get('industry')
        technologies = request.POST.getlist('technologies')
        techstacks = request.POST.getlist('techstacks')

        user_request = UserRequest(
            user=request.user,
            software_name=software_name,
            description=description,
           

            # Add other fields here
        )
        user_request.save()
        user_request.industry_specific.set([industry_id])
        technology_objs = Technology.objects.filter(id__in=technologies)
        user_request.technologies.set(technology_objs)
        user_request.techstacks.set(techstacks)
        # user_request.techstacks.set(techstacks)
        user_requests = UserRequest.objects.all()
        context = {
            'user_requests': user_requests
        }
        return render(request, 'profile.html', context)  # Replace 'success.html' with your success page template
    else:
        technologies = Technology.objects.all()
        industries=Industry.objects.all()
        tech_stacks=TechStackList.objects.all()
        return render(request, 'request.html', {'technologies': technologies,"industries":industries,"tech_stacks":tech_stacks})
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User.objects.create_user(username=username, password=password, email=email)
        return redirect("/catalog/login")  # Replace 'login' with your login page URL
    return render(request, "register.html")




from django.db.models import Prefetch
from .models import Subscription
from datetime import datetime, timedelta,timezone
@login_required
def profile_view(request):
    user = request.user
    payments = Payment.objects.filter(user=user).prefetch_related(
        Prefetch('software', queryset=Software.objects.all()),
        Prefetch('subscription', queryset=Subscription.objects.all())
    )
    purchased_date = payments[0].payment_date
    # purchased_date = datetime.strptime(purchased_date_str, '%Y-%m-%d')

# Example free subscription duration in days
    for payment in payments:
        purchased_date = payment.payment_date
        subscription = payment.subscription
        free_subscription_duration_str = subscription.duration[:2]
        
        if free_subscription_duration_str.isdigit():
            free_subscription_duration = int(free_subscription_duration_str)
            remaining_days = free_subscription_duration - (datetime.now(timezone.utc) - purchased_date).days
            payment.remaining_days=remaining_days
            payment.save()
        else:
            remaining_days = None  # Invalid subscri
    user_requests = UserRequest.objects.all()
 
            
     
    return render(request, "profile.html", {"user": user,'payments': payments,'user_requests': user_requests})


from django.db.models import Count

def get_related_software(current_software_id, num_recommendations=4):
    # Get the current software
    current_software = Software.objects.get(id=current_software_id)

    # Get the users who viewed the current software
    users_viewed_current_software = current_software.views.all()

    # Get the related software viewed by those users and annotate with the count of views
    related_software = Software.objects.filter(views__in=users_viewed_current_software)\
                                       .exclude(id=current_software_id)\
                                       .annotate(view_count=Count('views'))\
                                       .order_by('-view_count')[:num_recommendations]

    return related_software




from django.shortcuts import render, redirect
from .models import Subscription
import stripe

def subscription_view(request,software_id):
    subscriptions = Subscription.objects.all()
    soft_id= Software.objects.get(id=software_id)
    context = {
        'subscriptions': subscriptions,
        "software":soft_id
    }
    return render(request, 'subscription.html', context)



# from django.conf import settings
# def create_subscription(request):
#     if request.method == 'POST':
#         subscription_id = request.POST.get('subscription')
#         subscription = Subscription.objects.get(id=subscription_id)

#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         # Create a customer in Stripe
#         customer = stripe.Customer.create(
#             email=request.user.email,
#         )
#         # Create a subscription in Stripe
#         stripe.Subscription.create(
#             customer=customer.id,
#             items=[
#                 {
#                     'price': "price_1NNRD5FQ7fQ9eiOGo4J7N9uZ",
#                 },
#             ],
#             trial_period_days=14,  # Set the trial period duration in days
#         )
#         # Save the subscription details in your database
#         # You can associate the subscription with the user who initiated the subscription

#         return redirect('catalapp:success')
from django.shortcuts import render

def success_view(request):
    return render(request, 'success.html')
# from django.shortcuts import render
# from django.conf import settings
# import stripe

# def payment_view(request):
#     if request.method == 'POST':
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         # Create a customer in Stripe
#         customer = stripe.Customer.create(
#             email=request.user.email,
#         )
#         # Create a payment method using the card element
#         payment_method = stripe.PaymentMethod.create(
#             type='card',
#             card={
#                 'number': request.POST['card_number'],
#                 'exp_month': request.POST['exp_month'],
#                 'exp_year': request.POST['exp_year'],
#                 'cvc': request.POST['cvc'],
#             },
#         )
#         # Attach the payment method to the customer
#         stripe.PaymentMethod.attach(
#             payment_method.id,
#             customer=customer.id,
#         )
#         # Set the default payment method for the customer
#         stripe.Customer.modify(
#             customer.id,
#             invoice_settings={
#                 'default_payment_method': payment_method.id,
#             },
#         )
#         # Create a subscription in Stripe
#         stripe.Subscription.create(
#             customer=customer.id,
#             items=[
#                 {
#                     'price': 'your_stripe_price_id',
#                 },
#             ],
#             trial_period_days=14,  # Set the trial period duration in days
#         )
#         # Save the subscription details in your database
#         # You can associate the subscription with the user who initiated the subscription

#         return redirect('success')
#     else:
#         return render(request, 'payment.html')


import stripe
from django.contrib.auth.models import User
from .models import Software, Subscription

def retrieve_payment_information(event):
    # global user, software, subscription, amount
    session = event.data.object
    session = event.data.object
    client_reference_id = session.get('client_reference_id')
    software = Software.objects.get(id=client_reference_id)
    # print(software.name)
    metadata = event.data.object.metadata
    subscription_type = metadata.get('subscription_type')
    sub_id=Subscription.objects.get(name=subscription_type)
    return software,sub_id

def retrieve_user_information(event):
    # global user, software, subscription, amount
    session = event.data.object
    customer_mail = session.billing_details.email
    user = User.objects.get(email=customer_mail)
    subscription = None

    if session.amount==100:
        subscription = Subscription.objects.get(id=4)
        # software = subscription.software
    elif session.amount==5000:
        subscription = Subscription.objects.get(id=5)
        # software = subscription.software
    elif session.amount==8000:
        subscription = Subscription.objects.get(id=6)
        # software = subscription.software
    elif session.amount==10000:
        subscription = Subscription.objects.get(id=6)
        # software = subscription.software
    # Retrieve payment amount
    amount = session.amount
    return user,amount
    
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
user = None
software = None
subscription = None
amount = None
@csrf_exempt
def webhook(request):
    global user, software, subscription, amount
    payload = request.body
    event = None
    # software,user,subscription, amount=False,False,False,False
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    
    # Handle specific event types
    if event.type == 'checkout.session.completed':
        # Retrieve the relevant information for the payment
        print(event.type)
        software,subscription= retrieve_payment_information(event)

    if event.type == 'charge.succeeded':
        print(event.type)
        user, amount=retrieve_user_information(event)
        # Create a new Payment object and save it to the database
    import time
    
    if user is not None and software is not None and subscription is not None and amount is not None :
        print("payment should be created now!!!")
        print(user,software) 
        if not Payment.objects.filter(user=user, software=software).exists():
            payment = Payment(
                        user=user,
                        software=software,
                        subscription=subscription,
                        amount=amount,
                        is_successful=True
                    )
            payment.save()
            return HttpResponse(status=200)

        # Update user's subscription status, if applicable
            # user.subscription = subscription
            # user.save()

        # Additional actions (e.g., send confirmation email, update inventory, etc.)
        # ...
    return HttpResponse("Not all info")

    
import stripe
from django.contrib.auth.models import User
from .models import Software, Subscription

def create_payment_link(user, software,subscription,price):
    stripe.api_key = "sk_test_51NNQNSFQ7fQ9eiOGNU27BidquzSvmBAC4FztWt8jroHqHQ2QyTwCx7BBpjksldu7ZBnxRazcOWCVVcOZExG0Ajvt00rmvFR3A5"
    payment_session = stripe.checkout.Session.create(
        customer="cus_OANDy4jNYPGat0",
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': price * 100,  # Price in cents
                    'product_data': {
                        'name': software.name,
                        # 'images': [software.images.url],
                    },
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://192.168.1.79/catalog/profile/',  # Replace with your success URL
        # cancel_url='https://example.com/cancel',  # Replace with your cancel URL
        client_reference_id=str(software.id),  # Pass software ID as the client reference ID
        # subscription_data=str(subscription)
        metadata={
            'subscription_type': subscription  # Include the subscription type in the metadata
        }
    )

    return payment_session.url

# Example usage when redirecting user to the payment link
def redirect_to_payment(request, software_id,subscription,price):
    user = request.user
    software = Software.objects.get(id=software_id)
    payment_link = create_payment_link(user, software,subscription,price)
    return redirect(payment_link)
