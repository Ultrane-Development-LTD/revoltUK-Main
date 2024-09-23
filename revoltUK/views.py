from django.shortcuts import render, redirect, get_object_or_404
from .models import Legislation, Category, VotingSession, Vote
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def home(request):
    categories = Category.objects.all()
    current_time = timezone.now()

    # Fetch active and closed voting sessions with related legislation and category
    active_sessions = VotingSession.objects.filter(start_time__lte=current_time, end_time__gte=current_time).select_related('legislation__category')
    closed_sessions = VotingSession.objects.filter(end_time__lt=current_time)

    # Calculate ratings for each session
    session_ratings = {}
    for session in active_sessions:
        votes = Vote.objects.filter(session=session)
        total_votes = votes.count()
        print(f"Session ID: {session.id}, Total Votes: {total_votes}")  # Debug output

        if total_votes > 0:
            avg_rating = votes.aggregate(Avg('rating'))['rating__avg']
            session_ratings[session.id] = avg_rating
        else:
            session_ratings[session.id] = 0  # No votes, set rating to 0

    print(f"Session Ratings: {session_ratings}")  # Debug output

    return render(request, 'index.html', {
        'categories': categories,
        'active_sessions': active_sessions,
        'closed_sessions': closed_sessions,
        'session_ratings': session_ratings,  # Pass session ratings
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