# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.core.context_processors import csrf
from settings.models import Contact


def map(request):
    return render_to_response("map.html")


def mail(request):
    args = {}
    errors = []
    form = {}
    if request.POST:

        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')

        if not form['name']:
            errors.append(u'Заполните имя')
        if '@' not in form['email']:
            errors.append(u'Введите корректный e-mail')
        if not form['message']:
            errors.append(u'Введите сообщение')

        if not errors:
            return HttpResponse(u'Спасибо за ваше сообщение!')

    args.update(csrf(request))
    args['errors'] = errors
    args['form'] = form

    return render_to_response('mail_form.html', args)


def main(request):
    args = {}
    errors = []
    form = {}
    model = Contact.objects.get(id=1)
    if request.POST:
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')
        if not form['name']:
            errors.append(u'Заполните имя')
        if '@' not in form['email']:
            errors.append(u'Введите корректный e-mail')
        if not form['message']:
            errors.append(u'Введите сообщение')
        if not errors:
            return HttpResponse(u'Спасибо за ваше сообщение!')

    args.update(csrf(request))
    args['errors'] = errors
    args['form'] = form
    args['model'] = model

    return render_to_response('contact.html', args)