from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone

# Create your views here.


def home(request):
    current_time = timezone.now()
    print(current_time,"current_time")
    classes = FitnessClass.objects.filter(datetime__gte=current_time).order_by('datetime')
    return render(request, 'home.html', {'classes': classes})

def success_stories(request):
    return render(request,'success.html')




def get_programs(request):
    if request.method == "POST":
        email=request.POST.get('email',None)
        data=list(Booking.objects.filter(client_email=email).values('id','client_name','client_email','fitness_class__name','fitness_class__datetime','fitness_class__instructor','fitness_class__total_slots','fitness_class__available_slots','fitness_class__instructor_image'))
        return JsonResponse(data,safe=False)
    else:
        return render(request,'search.html')



def booknow(request):
    if request.method == "POST":
        fit_id = request.POST.get('fit_id')
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        if not fit_id or not client_name or not client_email:
            messages.error(request, "Please fill in all required fields.")
            return redirect('home')

        # Get the FitnessClass object safely
        fitness = get_object_or_404(FitnessClass, id=fit_id)
        if fitness.available_slots <= 0:
            messages.error(request, "Sorry, no slots available for this class.")
            return redirect('home')
        Booking.objects.create(
            fitness_class=fitness,
            client_name=client_name,
            client_email=client_email
        )
        fitness.available_slots -= 1
        fitness.save()
        messages.success(request, f"You've successfully booked '{fitness.name}'!")
        return JsonResponse({'status':'success'})
    return JsonResponse({'status': 'invalid method'}, status=405)


 

  