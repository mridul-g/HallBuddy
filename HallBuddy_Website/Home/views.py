from django.shortcuts import render
from django.core.mail import send_mail
from dateutil.rrule import rrule, DAILY
from django.contrib import messages
from datetime import datetime
from Home.models import Announcement

# Create your views here.

def Make_Homepage (request):
    # rendering the home page
    if request.user.is_authenticated:
        if(request.user.designation == 'Student'):
            announcements = Announcement.objects.all().exclude(Item_Name = "").exclude(Item_Name = "None").order_by(
                "-Announcement_Date"
            )  # QuerySet containing all announements

            if request.method == "POST":

                quantity = int(request.POST.get("quantity"))  # number requested
                idt = request.POST.get("identity")
                order = Announcement.objects.filter(id=idt)[0]  # key of the item ordered

            return render(request,"Announcements.html",
                context={
                    "announcements": announcements,
                    "messages": messages.get_messages(request),
                },
            )
        
        # hall manager
        else:
            announcements = Announcement.objects.all().order_by("-Announcement_Date")

            if request.method == "POST":
                
                flag = 0

                if (
                    ("submit" in request.POST)
                    or (
                        "add_hidden_item" in request.POST
                        and "editable_mode" in request.POST
                    )
                    or ("delete" in request.POST and "editable_mode" in request.POST)
                ):
                    # Commits changes to the database

                    for obj in Announcement.objects.all():  # for obj in Announcements
                        
                        announcement_date = request.POST.get("announcement_date" + str(obj.id))
                        if announcement_date is not None:

                            announcement_date = datetime.strptime(str(announcement_date), "%Y-%m-%d")
                            item = request.POST.get("item" + str(obj.id))
                            announcement_items = Announcement.objects.filter(id=obj.id)[0]
                            announcement_items.Announcement_Date = announcement_date
                            announcement_items.Item_Name = item
                            announcement_items.save()
                                
                        else:
                            obj.delete()

                if "add_hidden_item" in request.POST:               # makes an entry which will be filled by hall manager
                    
                    for item1 in Announcement.objects.all():
                        for item2 in Announcement.objects.all():
                            if item1.id != item2.id:

                                if (item1.Announcement_Date == item2.Announcement_Date)  and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break

                    obj = Announcement(Announcement_Date =  datetime.today())
                    obj.save()
                    return render(
                        request,
                        "Announcements_admin.html",
                        context={"announcements": announcements, "status_check": 1},
                    )

                elif "submit" in request.POST:
                    for item1 in Announcement.objects.all():
                        for item2 in Announcement.objects.all():
                            if item1.id != item2.id:
                                if (item1.Announcement_Date == item2.Announcement_Date) and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break
                    if flag:
                        return render(
                            request,
                            "Announcements_admin.html",
                            context={
                                "announcements": announcements,
                                "status_check": 1,
                                "messages": messages.get_messages(request),
                            },
                        )
                    else :
                        messages.success(request, "Changes made successfully.")
                        return render(
                            request,
                            "Announcements_admin.html",
                            context={
                                "announcements": announcements,
                                "status_check": 0,
                                "messages": messages.get_messages(request),
                            },
                        )

                elif "edit" in request.POST:                        # status checks make the menu editable

                    return render(
                        request,
                        "Announcements_admin.html",
                        context={"announcements": announcements, "status_check": 1},
                    )

                elif "delete" in request.POST:
                    # to delete Announcements from the weekly menu
                    idt = request.POST.get(
                        "delete"
                    )  # idt is the key of the object to be deleted
                    if Announcement.objects.filter(id=idt):
                        announcement_items_del = Announcement.objects.filter(id=idt)[0]
                        announcement_items_del.delete()

                    for item1 in Announcement.objects.all():
                        for item2 in Announcement.objects.all():
                            if item1.id != item2.id:
                                if (item1.Announcement_Date == item2.Announcement_Date) and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break

                    messages.success(request, "Deleted Successfully")
                    return render(
                        request,
                        "Announcements_admin.html",
                        context={
                            "announcements": announcements,
                            "status_check": 0,
                            "messages": messages.get_messages(request),
                        },
                    )      
            else:
                return render(
                    request, "Announcements_admin.html", context={"announcements": announcements}
                )
    else:
        return render(request, "Error.html")
    
def map (request):
    # rendering the map page
    if request.user.is_authenticated:
        return render (request, 'Map.html')
    else:
        return render(request, "Error.html")
    
def contact (request):
    # rendering the contact page
    if request.user.is_authenticated:
        return render (request, 'Contact.html')
    else:
        return render(request, "Error.html")

def shop (request):
    # rendering the shop page
    if request.user.is_authenticated:
        return render (request, 'Shop.html')
    else:
        return render(request, "Error.html")

def dues (request):
    # rendering the dues page
    if request.user.is_authenticated:
        return render (request, 'dues.html')
    else:
        return render(request, "Error.html")