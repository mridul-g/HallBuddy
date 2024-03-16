# from django.shortcuts import render
# from .models import CleaningStatus

# # Create your views here.
# def Cleaning_Status(request):
#     return render(request,'Cleaning_Management.html')
from django.shortcuts import render
from django.http import JsonResponse
from .models import MarkedDate
from datetime import datetime
import json

def calendar_view(request):
    marked_dates = MarkedDate.objects.all()
    return render(request, 'Cleaning_Management.html', {'marked_dates': marked_dates})

def get_marked_dates(request):
    marked_dates = list(MarkedDate.objects.values('date', 'cleaned'))
    return JsonResponse({'marked_dates': marked_dates})
    # return Json.{'marked_dates': marked_dates}

def mark_date(request):
    print("inside mark_date")
    if request.method == 'POST':
        body = request.body
        decoded_body = json.loads(body)
        print("inside mark_date: request body : ", decoded_body)
        date_str = decoded_body.get('date')
        print("inside mark_date : ", date_str)
        cleaned = decoded_body.get('cleaned') == True
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        obj = MarkedDate(
            date=date,
            cleaned = cleaned
        )
        obj.save()
        #MarkedDate.objects.update_or_create(date=date, defaults=None) #{'cleaned': cleaned})
        print("date marked")
        # return JsonResponse({'status': 'ok'})

        return render(request, 'Cleaning_Management.html')
    return JsonResponse({'status': 'error'})



