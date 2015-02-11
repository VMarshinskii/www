from django.shortcuts import render_to_response
from pages.models import Page, Section
from django.http import Http404


# Create your views here.
def section(request, section_url=1):
    try:
        page_current = Section.objects.get(url=section_url)
    except Section.DoesNotExist:
        raise Http404
    return render_to_response("page.html", {'page': page_current})


def page(request, section_url=1, page_url=1):
    try:
        section_current = Section.objects.get(url=section_url)
        page_current = Page.objects.get(url=page_url, section=section_current)
    except Section.DoesNotExist:
        raise Http404
    except Page.DoesNotExist:
        raise Http404
    return render_to_response("page.html", {'page': page_current})