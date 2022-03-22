from pyexpat.errors import messages
from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def regi(request):
      if request.method == 'POST':
            fm = StudentRegistration(request.POST)
            if fm.is_valid():
                  fm.save()
                  messages.add_message(request, messages.SUCCESS,'your account has benn created')
                  messages.info(request,'You Can Login Now !!')
                  messages.warning(request,' warning messages')
            
      else:
            fm= StudentRegistration()
      return render (request, 'enroll/reg.html',{'form': fm})
