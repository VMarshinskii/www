from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.core.context_processors import csrf


def settings(request):
    return render_to_response("settings.html")