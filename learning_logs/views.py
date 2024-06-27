from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ Showing all topics """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    enteries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'enteries': enteries}
    
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Add new topic """
    if request.method != 'POST':
        # When no data submitted; create a blank from.
        form = TopicForm()
    else:
        # Post data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form
    context = {'form': form}
    
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """ Adding a new entry for a topic """
    
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
        
    else:
        #Post data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    #Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    # Edit entries 
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST the submitted data; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic':topic, 'form':form}
    
    return render(request, 'learning_logs/edit_entry.html', context)