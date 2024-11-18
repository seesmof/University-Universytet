from django.shortcuts import redirect, render
from .models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return redirect('user_dashboard', user_id=user.id)
    return render(request, 'login.html')

def user_dashboard(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_dashboard.html', {'user': user})