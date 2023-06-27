from django.shortcuts import render
from .models import Software, Plugin, User,Review
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


def search_api(request):
    query = request.GET.get("q")
    softwares = Software.objects.all()
    
    if query:
        softwares = softwares.filter(tags__name__icontains=query).distinct()
        # print(softwares)
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


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User.objects.create_user(username=username, password=password, email=email)
        return redirect("/catalog/login")  # Replace 'login' with your login page URL
    return render(request, "register.html")





@login_required
def profile_view(request):
    user = request.user
    return render(request, "profile.html", {"user": user})


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
