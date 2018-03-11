from django.contrib import admin

from . import models


class TradeRouteInlineAdmin(admin.TabularInline):
    """Inline trade route admin representation."""

    model = models.TradeRoute
    fk_name = 'point_a'
    extra = 1


class TradeRegionAdmin(admin.ModelAdmin):
    """Admin model for trade routes."""

    list_display = ('name', 'shorthand', 'danger_level_spring', 'danger_level_summer',
        'danger_level_autumn', 'danger_level_winter')
    list_editable = ('danger_level_spring', 'danger_level_summer', 'danger_level_autumn',
        'danger_level_winter')
    inlines = (TradeRouteInlineAdmin,)


admin.site.register(models.RuleReference)
admin.site.register(models.TradeRegion, TradeRegionAdmin)
