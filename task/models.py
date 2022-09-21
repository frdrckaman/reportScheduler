from django.db import models
from edc_utils import get_utcnow
from simple_history.models import HistoricalRecords

from .choices import REPORT_FREQUENCY
from .mixin import BaseUuidModel


class ScheduleTask(BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )
    report_name = models.CharField(
        verbose_name='Report Name',
        max_length=45,
    )
    report_frequency = models.CharField(
        verbose_name='Report Frequency',
        max_length=20,
        choices=REPORT_FREQUENCY
    )
    search_variable = models.CharField(
        verbose_name='Search variable',
        max_length=45,
    )
    search_operator = models.CharField(
        verbose_name='Search criteria/operators',
        max_length=45,
    )
    search_query = models.TextField(
        verbose_name='Query'
    )

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Task"
        verbose_name_plural = "Task"
