from django.shortcuts import render
from .models import Company, CompanyUnit, Transport, Graphic, Worker
from .forms import CompanyForm


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


def company(request):
    company = Company.objects.all()
    context = {'company': company}
    return render(request, 'cds/company.html', context)


def add_company(request):
    company = Company.objects.all()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cds/done.html')
        context = {'form': form}
        return render(request, 'cds/add_company.html', context)
    elif request.method == 'DELETE':
        company = Company.objects.get(id=id)
        company.delete()
        context = {'company': company}
        return render(request, 'cds/add_company.html', context)
    else:
        form = CompanyForm()
        context = {'form': form, 'company': company}
        return render(request, 'cds/add_company.html', context)


def company_units(request):
    company_unit = CompanyUnit.objects.all()
    context = {'company_units': company_unit}
    template = 'cds/companyunit.html'
    return render(request, template, context)
