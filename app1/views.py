from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import NewEntry, NewTopic
from django.http import Http404
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'learning_log/homepage.html')

@login_required
def topics(request):
    inf_topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': inf_topics}
    return render(request, 'learning_log/topics.html', context)

@login_required
def topic(request, topic_id):
    inf_topic = Topic.objects.get(id=topic_id)
    if inf_topic.owner != request.user:
        raise Http404
    entries = inf_topic.entry_set.order_by('-date_added')
    context = {'topic': inf_topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = NewTopic()
    else:
        form = NewTopic(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('main:topics')
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = NewEntry()
    else:
        form = NewEntry(data=request.POST)
        if form.is_valid():
            New_Entry = form.save(commit=False)
            New_Entry.topic = topic
            New_Entry.save()
            return redirect('main:topic', topic_id=topic_id)
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_log/new_entry.html', context)

@login_required
def up_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = NewEntry(instance=entry)
    else:
        form = NewEntry(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('main:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/up_entry.html', context)







