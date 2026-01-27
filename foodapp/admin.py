from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Registration, Partners


def export_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    p = canvas.Canvas(response)
    y = 800

    for obj in queryset:
        # works for both models
        p.drawString(50, y, f"Name: {obj.name}")
        y -= 15
        p.drawString(50, y, f"Email: {obj.email}")
        y -= 15
        p.drawString(50, y, f"Mobile: {obj.mobile}")
        y -= 25

        if y < 100:
            p.showPage()
            y = 800

    p.save()
    return response


export_pdf.short_description = "Download selected as PDF"


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'category', 'created_at')
    search_fields = ('name', 'email', 'mobile')
    list_filter = ('category',)
    ordering = ('-created_at',)
    actions = [export_pdf]   # ✅ PDF for Registration


@admin.register(Partners)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile')
    search_fields = ('name', 'email', 'mobile')
    actions = [export_pdf]   # ✅ PDF for Partners
