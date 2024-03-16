from django.shortcuts import render
from Complaints.models import Complaint_Request
from datetime import datetime
from django.contrib import messages


def Past_Request(request):
    # Displays completed complaint requests raised by a user in the past
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            user_history = Complaint_Request.objects.filter(Done=True)
            # user_history is a QuerySet storing requests from the user
            return render(request, 'Past_Request.html', context= {'lodging': user_history})
        else:
            # If the user is not a student
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")
    
def Pending_Request(request):
    # Used to mark pending requests as complete
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            pending_list = Complaint_Request.objects.filter(Done = False)
            if request.method == 'POST':
                x = request.POST.get('identity')
                # used to identify which request is being marked as complete
                req=Complaint_Request.objects.filter(id = int(x))[0]
                if(req.User_Name==request.user.username):
                    req.Done = True
                    req.save()
                    messages.success(request, "Your request has been removed from pending requests successfully")
                else:
                    messages.error(request, "You are unauthorised to mark the status of this request.")

            # After updating the database, the page reloads.
            return render(request, 'Pending_Request.html', context= {'lodging': pending_list, "messages": messages.get_messages(request)})

        else:
            return render(request,"Error.html")
    else: 
        return render(request,"Error.html")


def Lodge_Request(request):
    # Creates a Request object when a complaint request is lodged
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            if request.method == 'POST' :
                place = request.POST.get("place")
                username =request.user.username
                location = request.POST.get('location')
                category=request.POST.get('category')  
                sub_category=request.POST.get('sub_category')  
                comments=request.POST.get('comment')
                
                if Complaint_Request.objects.filter(User_Name=username, Place=place, location=location, comments=comments,category=category,sub_category=sub_category, Done = False):
                    messages.error(request, "You have already applied a similar request. Contact Hall manager directly.")
                else:
                    req_object = Complaint_Request( 
                        User_Name=username,
                        Place=place,
                        location=location,
                        comments=comments,
                        category=category,
                        sub_category=sub_category,
                        Complaint_DateTime=datetime.now() )
                    req_object.save()   
                    messages.success(request, "Your request has been sent!")
                return render(request, "Lodge_Request.html", context={"messages": messages.get_messages(request)})
            return render(request, "Lodge_Request.html")
        else:
            return render(request,"Error.html")
    else: return render(request,"Error.html")


def Complaints_hall(request):
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            request_list = Complaint_Request.objects.filter( Done=False )
            return render(request, 'Complaints_hall.html', context= {'lodging': request_list})
            # All requests made are displayed to the manager
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")
