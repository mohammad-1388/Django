from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def view_home(request):
    return HttpResponseRedirect(reverse('ChatTick:index'))
