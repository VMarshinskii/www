# coding=utf-8
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template import RequestContext
from django.core.context_processors import csrf
from settings.models import Settings, Contact


def settings(request):
    if request.user.is_authenticated():
        model = Settings.objects.get(id=1)
        args = {}
        if request.POST:
            model.title = request.POST.get('title')
            model.email = request.POST.get('email')
            model.description = request.POST.get('description')
            model.phone_home = request.POST.get('phone')
            model.contacts = request.POST.get('contacts')
            model.odnoklassniki = request.POST.get('odnoklassniki')
            model.twitter = request.POST.get('twitter')
            model.facebook = request.POST.get('facebook')
            model.vk = request.POST.get('vk')
            model.footer = request.POST.get('footer')
            model.footer_link = request.POST.get('footer_link')
            model.save()
            args['message'] = "yes"
        args.update(csrf(request))
        args['model'] = model
        return render_to_response("set.html", args)
    else:
        return redirect('/admin/')


def contacts(request):
    if request.user.is_authenticated():
        model = Contact.objects.get(id=1)
        args = {}
        if request.POST:
            model.text = request.POST.get('text')
            model.map = request.POST.get('map')
            model.save()
            args['message'] = "yes"
        args.update(csrf(request))
        args['model'] = model
        return render_to_response("contacts.html", args)
    else:
        return redirect('/admin/')