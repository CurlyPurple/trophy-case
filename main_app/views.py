from django.shortcuts import render
from .models import Goal

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def goal_index(request):
  goals = Goal.objects.all()
  return render(request, 'goals/index.html', { 'goals': goals})

def goal_detail(request):
  goal = Goal.objects.get(id=goal_id)
  return render(request, 'goals/detail.html', { 'goal': goal })