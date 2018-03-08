from django.db import models
from django.utils.translation import ugettext as _


class RuleReference(models.Model):
    """
    A ``RuleReference`` is an source that can be used to justify a specified value.

    As each instance needs to provide enough information to allow for a manual cross reference/fact
    validation.
    """

    title = models.CharField(max_length=200, help_text=_("The references full title."))
    shorthand = models.CharField(max_length=10, help_text=_("The references common shorthand."))
    edition = models.PositiveIntegerField(help_text=_("Number of the referenced edition"))
    year_published = models.PositiveIntegerField(help_text=_(
        "Year in which this reference has been published."))

    class Meta:
        ordering = ('title', 'year_published')
        unique_together = (('title', 'edition', 'year_published'),)
