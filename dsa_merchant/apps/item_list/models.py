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

    def __str__(self):
        """Return string representation."""
        return self.title


class TradeRegion(models.Model):
    """A ``TradeRegion represents an area where an item is manufactured and/or exported to."""

    name = models.CharField(max_length=200, unique=True)
    shorthand = models.CharField(max_length=10, unique=True)
    # Due to how django handles reflexive m2m relations with intermediate
    # classes we need to specify ``symmetrical=False`` despite the fact that
    # these relations are in fact symmetrical!
    trade_routes = models.ManyToManyField('self', through='TradeRoute', symmetrical=False)
    danger_level_spring = models.PositiveIntegerField(default=0,
        help_text=_("The danger level during spring."))
    danger_level_summer = models.PositiveIntegerField(default=0,
        help_text=_("The danger level during summer."))
    danger_level_autumn = models.PositiveIntegerField(default=0,
        help_text=_("The danger level during autumn."))
    danger_level_winter = models.PositiveIntegerField(default=0,
        help_text=_("The danger level during winter."))
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        """Return string representation."""
        return '{s.name} ({s.shorthand})'.format(s=self)


class TradeRoute(models.Model):
    """
    This intermediate model represents routes from and to ``TradeRegions``.

    Note:
        These routes are un-directed. That is there is not dedicated ``start``
        or ``end``. It is for that reason that we add the ``unique_together``
        constraint.
    """

    point_a = models.ForeignKey('TradeRegion', related_name='trade_routes_point_a',
        on_delete=models.CASCADE)
    point_b = models.ForeignKey('TradeRegion', related_name='trade_routes_point_b',
        on_delete=models.CASCADE)
    is_sea_route = models.BooleanField(default=False)

    class Meta:
        ordering = ('point_a', 'is_sea_route')
        unique_together = (('point_a', 'point_b'),)

    def __str__(self):
        """Return string representation."""
        return 'Trade route between {s.point_a} and {s.point_b}.'.format(s=self)
