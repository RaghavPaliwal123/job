from django.shortcuts import render
from .models import Job
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def job_listings(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_listings.html', {'jobs': jobs})

@csrf_exempt
def add_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Job.objects.create(
            title=data['title'],
            company_name=data['company_name'],
            location=data['location'],
            employment_type=data['employment_type'],
            posted_date=data['posted_date'],
            description=data['description'],
            url=data['url'],
        )
        return JsonResponse({'message': 'Job added successfully!'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)
