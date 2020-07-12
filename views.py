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

def company_form(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cds/done.html')
        context = {'form': form}
        return render(request, 'cds/company.html', context)
    else:
        form = CompanyForm()
        context = {'form': form}
        return render(request, 'cds/company.html', context)