from discuss.models import Discussion
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from user.forms import ProfileEditForm, RegUserForm

from .models import Profile


def profileUser(request, user_id):
	
	user = get_object_or_404(User, id = user_id)
	user_info = Profile.objects.get(user = user.id)
	discussions = Discussion.objects.filter(author = user_info.user).order_by('-creation_time')


	context= {
		"discussions": discussions,
		"user_info": user_info,
	}


	return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def editProfileUser(request, user_id):
	user = get_object_or_404(User, id = user_id)
	user_info = Profile.objects.get(user = user.id)
	template = 'user/update_profile.html'	

	if user_info.user.id == request.user.id:
		if request.method == 'POST':
			form = ProfileEditForm(request.POST, request.FILES, instance=user_info)
			if form.is_valid:
				form.save()
				return redirect(f'/User/Profile/{user.id}')
		
		context = {
			'form': ProfileEditForm(instance=user_info),
			'user_info': user_info,
			
			}
		
		return render(request, template, context)

	else:
		return HttpResponse("You have no permission")

def registerUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = RegUserForm()
		if request.method == 'POST':
			form = RegUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			

		context = {'form':form}
		return render(request, 'user/registration.html', context)

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'user/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('index')




