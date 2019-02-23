from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('feedbacktypes:list')
    else:
        form = UserCreationForm()
    return render(request, 'feedback/signup.html', {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feedbacktypes:list')
    else:
        form = AuthenticationForm()        
    return render(request, 'feedback/login.html',{'form': form})
    #return HttpResponse("<h1>This is")

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('feedbacktypes:list')