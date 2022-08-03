from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import reverse
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.db.models import Avg
import json



# Create your views here.

def homepage(request):
    context = {}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context, request))


def rest_list(request):
    restaurant_list = Restaurant.objects.all()
    return render(request, 'restaurant/list.html', {'restaurant_list': restaurant_list})


def empl_list(request):
    employee_list = Employee.objects.all()
    return render(request, 'employee/list.html', {'employee_list': employee_list})


def rat_list(request):
    rating_list = Ratings.objects.all()
    return render(request, 'ratings/list.html', {'rating_list': rating_list})


def rest_detail(request, rest_name):
    try:
        all_restaurants = Restaurant.objects.get(r_name=rest_name)
        mean = all_restaurants.ratings_set.all().aggregate(Avg('rating'))
        str_mean = json.dumps(mean)
        split_mean = str_mean.split(":")
        str_mean = split_mean[1][:-1]
        float_mean = float(str_mean)
        mean = round(float_mean,2)


    except Restaurant.DoesNotExist:
        raise Http404("Nous n'avons pas trouvé le restaurant demandé")
    return render(request, 'restaurant/detail.html', {'all_restaurants': all_restaurants, 'mean': mean})


def empl_detail(request, empl_name):
    try:
        all_employees = Employee.objects.get(e_name=empl_name)

    except Employee.DoesNotExist:
        raise Http404("Nous n'avons pas trouvé l'employé' demandé")
    return render(request, 'employee/detail.html', {'all_employee': all_employees})


def register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = UserCreationForm()
    except Users.DoesNotExist:
        raise Http404("Register does not exist")
    return render(request, 'register.html', {'form': form})


@login_required
def login_1(request):
    return render(request, 'login_1.html')


@login_required
def rate(request, rest_pk):
    if request.method == 'POST':
        form = signInForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            time = datetime.now()
            comment = form.cleaned_data['comment']
            r_rated = Restaurant.objects.get(pk=rest_pk)
            newrating = Ratings(rating=rating, comment=comment, time=time, r_rated=r_rated)
            newrating.save()

            return HttpResponseRedirect(reverse('rest_detail', args=(r_rated,)))
    else:
        form = signInForm()
        restaurant = Restaurant.objects.get(pk=rest_pk)
    return render(request, 'ratings/new.html', {'form': form, 'restaurant': restaurant})


class RatingsForm(ModelForm):
    class Meta:
        model = Ratings
        fields = ['rating', 'comment']
