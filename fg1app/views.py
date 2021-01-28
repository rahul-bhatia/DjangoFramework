from django.shortcuts import render

# Create your views here.
def home(request):
	if request.POST.get('num') :
		num=int(request.POST.get('num'))
		if num>80:
			msg="Grade : A"
		elif num>60:
			msg="Grade : B"
		elif num>40:
			msg="Grade : C"
		else:
			msg="Fail"
		return render(request,'home.html',{'msg':msg})
	return render(request,'home.html')