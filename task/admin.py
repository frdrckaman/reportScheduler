from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from .models import ScheduleTask

admin.site.enable_nav_sidebar = False


@admin.register(ScheduleTask)
class ScheduleTaskAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("report_datetime",)}),
        (
            "SCHEDULE DETAILS",
            {
                "fields": (
                    "report_name",
                    "report_frequency",
                    "search_variable",
                    "search_operator",
                    "search_query",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "report_name",
        "report_frequency",
        "search_variable",
        "search_query",
    )

    list_filter = (
        "report_datetime",
        "report_name",
        "report_frequency",
    )

    search_fields = (
        "report_name",
    )

    radio_fields = {
        "report_frequency": admin.VERTICAL,
    }
