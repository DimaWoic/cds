from django.shortcuts import render, render_to_response
from .models import Company, CompanyUnit, Transport, Graphic, Worker, Position
from django.views.generic import DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Depot, Route, RouteParam, RollingStock


def index(requests):
    return render(requests, 'cds/base/base.html')


class TransportIndex(ListView):
    template_name = 'cds/transport.html'
    context_object_name = 'transport'

    def get_queryset(self):
        return Transport.objects.all()


class EditTransport(CreateView, ListView):
    model = Transport
    success_url = reverse_lazy('transport')
    fields = ['transport']
    template_name_suffix = '_add'
    context_object_name = 'transport'

    def get_queryset(self):
        return Transport.objects.all()

    def form_invalid(self, form):
        return render_to_response('cds/exists.html')


class DelTransport(DeleteView):
    model = Transport
    success_url = reverse_lazy('transport')


class GraphicIndex(ListView):
    template_name = 'cds/graphic.html'
    context_object_name = 'graphic'

    def get_queryset(self):
        return Graphic.objects.all()


class CreateGraphic(CreateView, ListView):
    model = Graphic
    success_url = reverse_lazy('graphic')
    fields = ['graphic']
    template_name_suffix = '_add'
    context_object_name = 'graphic'

    def get_queryset(self):
        return Graphic.objects.all()

    def form_invalid(self, form):
        return render_to_response('cds/exists.html')


class DelGraphic(DeleteView):
    model = Graphic
    success_url = reverse_lazy('graphic')


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


class CompanyUnitCreate(CreateView, ListView):
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
    context_object_name = 'company_unit'


class PositionIndex(ListView):
    template_name = 'cds/position_index.html'
    context_object_name = 'position'
    template_name_suffix = '_index'

    def get_queryset(self):
        return Position.objects.all()


class PositionCreate(CreateView, ListView):
    model = Position
    success_url = reverse_lazy('positions')
    fields = ['name']
    template_name_suffix = '_add'
    context_object_name = 'position'

    def get_queryset(self):
        return Position.objects.all()


class DelPosition(DeleteView):
    model = Position
    success_url = reverse_lazy('positions')
    context_object_name = 'position'


class WorkerIndex(ListView):
    template_name = 'cds/worker_index.html'
    context_object_name = 'worker'
    template_name_suffix = '_index'

    def get_queryset(self):
        return Worker.objects.all()


class WorkerCreate(CreateView, ListView):
    model = Worker
    success_url = reverse_lazy('worker_index')
    fields = ['name_surname', 'sex', 'birthday', 'working_place', 'position', 'address', 'telephone']
    template_name_suffix = '_add'
    context_object_name = 'worker'

    def get_queryset(self):
        return Worker.objects.all()


class DelWorker(DeleteView):
    model = Worker
    success_url = reverse_lazy('worker_index')
    context_object_name = 'worker'


class ScheduleIndex(ListView):
    template_name = 'cds/schedule_index.html'
    template_name_suffix = '_index'
    queryset = RollingStock.objects.all()
    context_object_name = 'rs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['depot'] = Depot.objects.all()
        context['transport'] = Transport.objects.all()
        context['route'] = Route.objecta.all()
        context['rp'] = RouteParam.objects.all()
        return context
