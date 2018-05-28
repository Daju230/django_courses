
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    data = {'courses': Course.objects.all()}
    return render(request, 'index.html', data)

def add_course(request):
	name = request.POST['name']
	desc = request.POST['description']

	errors = Course.objects.validate_form(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/')
	else: 
		description = Description.objects.create(description=desc)
		Course.objects.create(name=name, description=description)

	return redirect('/')

def confirm_delete(request, id):
	data = {'course': Course.objects.get(id=id)}
	return render(request, 'delete.html', data)

def destroy(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	return redirect('/')