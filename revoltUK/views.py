from django.shortcuts import render, redirect, get_object_or_404
from .models import Legislation, Category, VotingSession
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import VotingSession, Vote
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    current_time = timezone.now()

    # Fetch active voting sessions
    active_sessions = VotingSession.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    # Fetch closed voting sessions
    closed_sessions = VotingSession.objects.filter(end_time__lt=current_time)

    return render(request, 'index.html', {
        'categories': categories,
        'active_sessions': active_sessions,
        'closed_sessions': closed_sessions,
    })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def submit_vote(request, session_id):
    if request.method == 'POST':
        session = get_object_or_404(VotingSession, id=session_id)
        rating = int(request.POST['rating'])
        vote, created = Vote.objects.update_or_create(
            user=request.user,
            session=session,
            defaults={'rating': rating}
        )
        return redirect('home')  # Or wherever you want to redirect after voting