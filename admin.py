from django.contrib import admin
from .models import Transport, Graphic, Company, CompanyUnit, Sex, Position, Worker


admin.site.register(Transport)
admin.site.register(Graphic)
admin.site.register(Company)
admin.site.register(CompanyUnit)
admin.site.register(Sex)
admin.site.register(Position)
admin.site.register(Worker)