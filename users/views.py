from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .models import Users
# Django convention is to use singular model names (User, not Users)

# View to render the Signup view page 
def signup_view(request):
    if request.method == 'POST':
        response_data = create_user(request.POST)
        return JsonResponse(response_data)
        
    return render(request, 'signup.html', {
        'page_title': 'Sign Up'
    })

# Function to handle the Creation of User logic. First checks if the user already exists if not creates the user
def create_user(data):
    """
    Validates data and creates a new user if validation passes.
    """
    required_fields = ["last_name", "first_name", "phone_number", "email", "password"]
    missing_fields = []
    
    for field in required_fields:
        if not data.get(field):
            missing_fields.append(field)

    if missing_fields:
        return {'status': False, 'message': f"Missing required fields: {', '.join(missing_fields)}"}

    email = data.get('email')
    phone_number = data.get('phone_number')

    if Users.objects.filter(Q(email=email) | Q(phone_number=phone_number)).exists():
        return {'status': False, 'message': 'A user with this email or phone number already exists.'}

    try:
        Users.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=email,
            phone_number=phone_number,
            password=make_password(data.get('password')),
            username=email 
        )
        return {'status': True, 'message': 'Signup successful!'}
    except Exception as e:
        return {'status': False, 'message': f'An error occurred: {str(e)}'}


def launch(request):
    """Launch page view"""
    return render(request, 'launch.html', {
        'page_title': 'Website Launch'
    })
