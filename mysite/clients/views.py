from django.shortcuts import render_to_response
from clients.models import Client, Company
from django.http import Http404, HttpResponse


# Create your views here.
def client_galery(request):
    clients = Client.objects.all()
    companies = Company.objects.all()
    return render_to_response("clients.html", {
                                  'clients': clients,
                                  'companies': companies
                              })