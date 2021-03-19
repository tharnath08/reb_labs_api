from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse, render, redirect

from django.forms import ModelForm
from django import forms
from .models import Post

# define the class of a form
class PostForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	 

		# Custom fields
		fields =["username", "gender", "text"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		text = self.cleaned_data.get('text')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['text'] = self.error_class([
				'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data

def home(request):
 
    # check if the request is post 
    if request.method =='POST':  
 
        # Pass the form data to the form class
        details = PostForm(request.POST)
 
        # In the 'form' class the clean function 
        # is defined, if all the data is correct 
        # as per the clean function, it returns true
        if details.is_valid():  
 
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database   
            post = details.save(commit = False)
 
            # Finally write the changes into database
            post.save()  
 
            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponse("data submitted successfully")
             
        else:
         
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "home.html", {'form':details})  
    else:
 
        # If the request is a GET request then,
        # create an empty form object and 
        # render it into the page
        form = PostForm(None)   
        return render(request, 'home.html', {'form':form})