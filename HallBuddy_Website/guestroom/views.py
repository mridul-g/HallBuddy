from django.shortcuts import render, HttpResponse
from datetime import datetime
from guestroom.models import Guestroom, Room
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def guestroom(request):  # student can book the guestroom
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            context = {
                "bookings": Guestroom.objects.filter(username=request.user.username),
                "messages": messages.get_messages(request),
                "rooms": Room.objects.all().order_by("room"),
            }
            # keeps the booking logs updated
            today = datetime.today().date()
            rooms = Guestroom.objects.all()
            for room in rooms:
                out_date = room.checkout_date
                if today > out_date:
                    room.delete()

            # This codes will tackle when the request of booking is made
            if request.method == "POST":
                room = request.POST.get("room")
                checkin_date = request.POST.get("checkin_date")
                checkout_date = request.POST.get("checkout_date")
                room_type=request.POST.get("type")
                price = request.POST.get("price")

                request_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
                request_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

                if request_in_date < request_out_date and request_in_date >= today:
                    rooms = Guestroom.objects.filter(
                        room=room, manager_validation="YES"
                    )
                    if len(rooms) > 0:
                        flag = 1
                        for room_item in rooms:
                            in_date = room_item.checkin_date
                            out_date = room_item.checkout_date

                            request_in_date = datetime.strptime(
                                checkin_date, "%Y-%m-%d"
                            ).date()
                            request_out_date = datetime.strptime(
                                checkout_date, "%Y-%m-%d"
                            ).date()

                            if (
                                request_in_date >= in_date
                                and request_in_date <= out_date
                            ) or (
                                request_out_date >= in_date
                                and request_out_date <= out_date
                            ) or (
                                    in_date >= request_in_date
                                and in_date <= request_out_date
                            ) or (
                                out_date >= request_in_date
                                and out_date <= request_out_date
                            ) :
                                flag = 0
                                break

                        if flag == 1:
                            check_booking = Guestroom.objects.filter(
                                room=room,
                                username=request.user.username,
                                manager_validation="NO",
                            )
                            if len(check_booking) > 0:
                                messages.error(
                                    request,
                                    f"You have already requested this room, please check your booking history.",
                                )
                                return render(request, "guestroom.html", context)
                            else:
                                guestroom_request = Guestroom(
                                    checkin_date=checkin_date,
                                    checkout_date=checkout_date,
                                    type=room_type,
                                    price=price,
                                    date=datetime.today(),
                                    name=request.user.name,
                                    username=request.user.username,
                                    room=room,
                                )

                                guestroom_request.save()
                                messages.success(
                                    request,
                                    f"Your reques thas been sent to the Hall manager, please contact him for further info.",
                                )
                                return render(request, "guestroom.html", context)
                        else:
                            rooms = Guestroom.objects.filter(room=room)
                            for room in rooms:
                                room_r = room
                                break
                            messages.error(
                                request,
                                f"The room you have requested is already booked from {room_r.checkin_date} to {room_r.checkout_date}.",
                            )
                            return render(request, "guestroom.html", context)
                    else:
                        guestroom_request = Guestroom(
                            checkin_date=checkin_date,
                            checkout_date=checkout_date,
                            type=room_type,
                            price=price,
                            date=datetime.today(),
                            name=request.user.name,
                            username=request.user.username,
                            room=room,
                        )

                        guestroom_request.save()
                        messages.success(
                            request,
                            f"Your request for this room has been sent to the Hall manager, Please reach out to him for further details.",
                        )

                else:
                    if request_in_date > today:
                        messages.error(
                            request,
                            f"Checkin date can not be after checkout date, please enter dates correctly again.",
                        )
                    else:
                        messages.error(
                            request,
                            f"Checkin date can not be before today, please enter dates correctly again.",
                        )
            return render(request, "guestroom.html", context)
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")

# this is to see the previous guestroom booking history
def pastbookings(request):
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            context = {
                "bookings": Guestroom.objects.filter(username=request.user.username),
                "messages": messages.get_messages(request)
            }

            return render(request, "pastbookings.html", context)
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")

# booking manager approval added
def pending(request):  # hall manager
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            context = {
                "query_results_request": Guestroom.objects.filter(
                    manager_validation="NO"
                ),
                "query_results_approved": Guestroom.objects.filter(
                    manager_validation="YES"
                ),
                "messages": messages.get_messages(request),
            }
            if request.method == "POST":
                username = request.POST.get("username")
                room = request.POST.get("room")
                room_type = request.POST.get("type")
                checkin = request.POST.get("checkin_date")
                checkout = request.POST.get("checkout_date")
                action = request.POST.get("action")

                date_format = "%B %d, %Y"
                checkin_date = datetime.strptime(checkin, date_format).date()
                checkout_date = datetime.strptime(checkout, date_format).date()

                get_booking = Guestroom.objects.filter(
                    username=username,
                    room=room,
                    type=room_type,
                    checkin_date=checkin_date,
                    checkout_date=checkout_date,
                )
                get_booking = get_booking[0]
                if action == "Approve":
                    get_booking.manager_validation = "YES"
                    get_booking.save()
                    messages.success(request, "The booking has been validated")

                    #deleting the other booking request for same room between same dates
                    other_bookings = Guestroom.objects.filter(room=room,manager_validation = "NO")
                    for booking in other_bookings:
                        # if booking.checkin_date <= checkin_date <= booking.checkout_date or booking.checkin_date <= checkout_date <= booking.checkout_date:
                        if (booking.id != get_booking.id):
                            if checkin_date <= booking.checkin_date <= checkout_date or checkin_date <= booking.checkout_date <= checkout_date or booking.checkin_date <= checkin_date <= booking.checkout_date or booking.checkin_date <= checkout_date <= booking.checkout_date:
                                booking.delete()
                                #sending mail to the user
                                subject = "Guestroom Booking Rejected"
                                message = f"Dear {booking.username},\n\n Your booking request for Room:{booking.room}, {booking.type} has been rejected by the hall manager. You had requested Room-{booking.room} from {booking.checkin_date} to {booking.checkout_date}\n  This is an auto-generated mail, please do not reply to this mail. \n\nHall Buddy"
                                email_from = settings.EMAIL_HOST_USER
                                recipient_list = [f"{booking.username}@iitk.ac.in"]
                                send_mail(subject, message, email_from, recipient_list)

                    # adding mail for validation of the booking
                    subject = "Guestroom Booking Accepted"
                    message = f"Dear {username},\n\n Your booking request for Room:{room},{room_type} has been accepted by the hall manager. You have booked Room-{room} from {get_booking.checkin_date} to {get_booking.checkout_date}\n This is an auto-generated mail, please do not reply to this mail.\n\nHallBuddy"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [f"{username}@iitk.ac.in"]
                    send_mail(subject, message, email_from, recipient_list)
                else:
                    messages.success(request, "The booking has been rejected")
                    get_booking.delete()

                    # adding mail for rejection of booking
                    subject = "Guestroom Booking Rejected"
                    message = f"Dear {username},\n\n Your booking request for Room:{room},{room_type} has been rejected by the hall manager. You had requested Room-{room} from {get_booking.checkin_date} to {get_booking.checkout_date}\n This is an auto-generated mail, please do not reply to this mail.\n\nHallBuddy"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [f"{username}@iitk.ac.in"]
                    send_mail(subject, message, email_from, recipient_list)

            return render(request, "booking_pending.html", context)
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")

def bookings_aprooved(request):  # hall manager
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            context = {
                "query_results_approved": Guestroom.objects.filter(manager_validation="YES"),
                "messages": messages.get_messages(request),
            }
            return render(request, "booking_aprooved.html", context)
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")

def update_room(request):
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            if request.method == "POST":
                if "add_room" in request.POST:               # makes an entry which will be filled by hall manager

                    obj = Room(price="1000")
                    obj.save()
                    rooms = Room.objects.all().order_by("room")
                    return render(
                        request,
                        "update_room.html",
                        context={"rooms": rooms}
                    )

                elif "delete" in request.POST:
                    # to delete Announcements from the weekly menu
                    idt = request.POST.get(
                        "delete"
                    )  # idt is the key of the object to be deleted
                    if Room.objects.filter(id=idt):
                        room_del = Room.objects.filter(id=idt)[0]
                        room_del.delete()

                    messages.success(request, "Deleted Successfully")
                    rooms = Room.objects.all().order_by("room")
                    return render(
                        request,
                        "update_room.html",
                        context={
                            "rooms": rooms,
                            "messages": messages.get_messages(request),
                        },
                    )

                elif "update" in request.POST:
                    # to delete Announcements from the weekly menu
                    idt = request.POST.get(
                        "update"
                    )  # idt is the key of the object to be deleted
                    if Room.objects.filter(id=idt):
                        room_obj = Room.objects.filter(id=idt)[0]
                        room_obj.price = request.POST.get("price" + str(idt))
                        room_obj.room = request.POST.get("room" + str(idt))
                        room_obj.type=request.POST.get("type" + str(idt))
                        room_obj.save()

                    messages.success(request, "Updated Successfully")
                    rooms = Room.objects.all().order_by("room")
                    return render(
                        request,
                        "update_room.html",
                        context={
                            "rooms": rooms,
                            "messages": messages.get_messages(request),
                        },
                    )


            else:
                rooms = Room.objects.all().order_by("room")
                return render(request, "update_room.html", context={"rooms": rooms})

                return render(request, "Error.html")