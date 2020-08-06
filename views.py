from django.shortcuts import render
from .models import Company, CompanyUnit, Transport, Graphic, Worker
from .forms import CompanyForm
from django.views.generic import DeleteView, CreateView, ListView
from django.urls import reverse_lazy


def index(requests):
    return render(requests, 'cds/base/base.html')


def transport_index(request):
    transport = Transport.objects.all()
    context = {'transport': transport}
    template = 'cds/transport.html'
    return render(request, template_name=template, context=context)


def graphic_index(request):
    graphic = Graphic.objects.all()
    context = {'graphic': graphic}
    template = 'cds/graphic.html'
    return render(request, template_name=template, context=context)

class CompanyIndex(ListView):
    template_name = 'cds/company.html'
    context_object_name = 'company'

    def get_queryset(self):
        return Company.objects.all()


class CompanyCreate(CreateView, ListView):
    model = Company
    success_url = reverse_lazy('company')
    fields = ['name', 'address', 'email', 'telephone']
    template_name_suffix = '_add'
    context_object_name = 'company'

    def get_queryset(self):
        return Company.objects.all()


class DelCompany(DeleteView):
    model = Company
    success_url = reverse_lazy('company')


class CompanyUnitsIndex(ListView):
    template_name = 'cds/companyunit.html'
    context_object_name = 'company_units'

    def get_queryset(self):
        return CompanyUnit.objects.all()


class CompanyUnitCreate(CreateView):
    model = CompanyUnit
    success_url = reverse_lazy('company_units')
    fields = ['company', 'name', 'full_name']
    template_name_suffix = '_add'
    context_object_name = 'company_units'

    def get_queryset(self):
        return CompanyUnit.objects.all()


class DelCompanyUnit(DeleteView):
    model = CompanyUnit
    success_url = reverse_lazy('company_units')