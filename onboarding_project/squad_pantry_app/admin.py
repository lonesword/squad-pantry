from django import forms
from django.forms import BaseInlineFormSet
from django.contrib import admin
from squad_pantry_app.models import Dish, Order, OrderDishRelation, SquadUser


class BaseOrderDishFormset(BaseInlineFormSet):
    def clean(self):
        try:
            filled_form = [form for form in self.forms if form.cleaned_data]
        except AttributeError:
            # if a subform is invalid Django explicity raises
            # an AttributeError for cleaned_data
            pass
        else:
            if len(filled_form) < 1:
                raise forms.ValidationError('Enter at least One Dish')


class OrderDishInline(admin.StackedInline):
    model = OrderDishRelation
    formset = BaseOrderDishFormset
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDishInline,]


admin.site.register(Dish)
admin.site.register(Order, OrderAdmin)
admin.site.register(SquadUser)
