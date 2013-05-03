from django.shortcuts import render_to_response

def landingpage(request):
	return render_to_response("landing_page.html")

def about(request):
	return render_to_response("about.html")

def involved(request):
	return render_to_response("involved.html")


