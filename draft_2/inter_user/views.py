from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            current_username = form.cleaned_data.get('username')

            # CHeck for existing username
            if CustomUser.objects.filter(username=current_username).exists():
                form.add_error('username', 'A user with this username already exists.')
                return render(request, 'inter_user/register.html', {'form': form})

            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inter_user/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    filtered_users = CustomUser.objects.filter(ref_id=user.username)
    fetched = {'filtered_users':filtered_users}
    current = {'user': user}
    
    CONTEXT = {}
    CONTEXT.update(current)
    CONTEXT.update(fetched)

    return render(request, 'inter_user/dashboard.html', CONTEXT)
