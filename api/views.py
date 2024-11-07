from django.shortcuts import render
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json
from flipbook.models import PdfFlipbook
from django.conf import settings

BACKEND_HOST = settings.BACKEND_HOST


@csrf_exempt
def register(request):
    if request.method == 'POST':

        print(request.body)
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)

        form = CustomUserCreationForm(data)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'User registered successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return JsonResponse({'success': False, 'message': f'Invalid request method: {request.method}'}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        username = data.get('username')  # Extract username
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return JsonResponse({'success': True, 'message': 'User logged in successfully!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)




@csrf_exempt
def get_books(request):
    documents = PdfFlipbook.objects.all()
    json_data = []
    for doc in documents:
        json_data.append({
            'id': doc.id,
            'book_title': doc.flipbook_title,
            'document_url': f'{BACKEND_HOST}{doc.flipbook_document.url}',
            'thumbnail': f'{BACKEND_HOST}{doc.flipbook_image.url}',
        })
    return JsonResponse(json_data, safe=False)


@csrf_exempt
def years_list(request):
    years = PdfFlipbook.objects.values('year').distinct().order_by('year')
    unique_years = years.values_list('year', flat=True)
    return JsonResponse(list(unique_years), safe=False)



@csrf_exempt
def filter_documents(request):
    print(request.body)
    data = json.loads(request.body)
    print(data)
    year = data.get('year')

    documents = PdfFlipbook.objects.filter(year=year)
    json_data = []
    for doc in documents:
        json_data.append({
            'id': doc.id,
            'book_title': doc.flipbook_title,
            'document_url': f'{BACKEND_HOST}{doc.flipbook_document.url}',
            'thumbnail': f'{BACKEND_HOST}{doc.flipbook_image.url}',
            'year':doc.year,
        })
    return JsonResponse(json_data, safe=False)
