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
    marked_dates = list(MarkedDate.objects.filter(User_Name=request.user.username).values('date', 'cleaned'))
    return JsonResponse({'marked_dates': marked_dates})
    # return Json.{'marked_dates': marked_dates}

def mark_date(request):
    # print("inside mark_date")
    # print(request.user.username)
    if request.method == 'POST':
        body = request.body
        decoded_body = json.loads(body)
        # print("inside mark_date: request body : ", decoded_body)
        date_str = decoded_body.get('date')
        # print("inside mark_date : ", date_str)
        room = decoded_body.get('room')
        cleaned = decoded_body.get('cleaned') == True
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        obj = MarkedDate(
            User_Name=request.user.username,
            room=room,
            date=date,
            cleaned = cleaned
        )
        obj.save()
        #MarkedDate.objects.update_or_create(date=date, defaults=None) #{'cleaned': cleaned})
        print("date marked")
        # return JsonResponse({'status': 'ok'})

        return render(request, 'Cleaning_Management.html')
    return JsonResponse({'status': 'error'})

def Complaints_hall(request):
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            return render(request, 'Cleaning_Hall_M.html')
                # request_list =MarkedDate.objects.filter()
                # return render(request, 'Cleaning_Hall_M.html', context= {'records': request_list})
            # All requests made are displayed to the manager
        # else:
        #     return render(request,"Error.html")
    else:
        return render(request,"Error.html")
def get_records(request):
    # Creates a Request object when a complaint request is lodged
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager" :
            if request.method == 'POST' :
                f_date = request.POST.get("filter_date")
                room = request.POST.get("room_num")
                # print("Inside get_records")
                # print("Date:",f_date)
                # print("Room:",room)
                if (f_date=="" and room=="Room Number"):
                    record_list =MarkedDate.objects.filter()
                elif(f_date==""):
                    record_list =MarkedDate.objects.filter(room=room)
                elif(room=="Room Number"):
                    record_list =MarkedDate.objects.filter(date=f_date)
                else:
                    record_list =MarkedDate.objects.filter(room=room,date=f_date)
                return render(request, 'Cleaning_Hall_M2.html', context= {'records': record_list})
        else:
            return render(request,"Error.html")
    else: return render(request,"Error.html")


