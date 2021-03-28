from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from .models import Work
import requests
import os
import json

cwd = os.getcwd()
secret_file = cwd + '/work/secret.json'
with open(secret_file) as f:
    secrets = json.loads(f.read())
url = secrets['url']

embed = {
    "description": "text in embed",
    "title": "embed title"
    }

data = {
    "content": f"임기홍 님이 출근했습니다.",
    "embeds": [
        # embed
        ],
}

headers = {
    "Content-Type": "application/json"
}


class IndexView(generic.ListView):
    template_name = 'work/index.html'
    context_object_name = 'works' 
    
    def get_queryset(self):
        works = Work.objects.filter(created_time__lte=timezone.now()).order_by('created_time')
        return works


def new_view(request):
    new = Work(person='who2')
    new.save()
    # requests.post(url, json=data, headers=headers)
    return render(request, 'work/new.html')

    # work = get_object_or_404(Work, pk=pk)
    # return render(request, 'work/new.html', {'work': 'work'})

