from django_tables2 import SingleTableView
from apps.core import forms, models
from django.views import generic
from crispy_forms.helper import FormHelper
from django.forms import modelform_factory
from crispy_forms.helper import FormHelper
from django.db.models import Sum
from django.db.models import F


class BaseListView(SingleTableView):
    template_name = "includes/list.html"
    segment = None
    filter_class = None
    create_url = None
    show_only_filtered = False

    def get_queryset(self):
        if self.filter_class:
            self.filter = self.filter_class(self.request.GET, queryset=super().get_queryset())
            if self.show_only_filtered and not self.request.GET:
                return self.model.objects.none()
            return self.filter.qs
        if self.model == models.Inventory and not 'pk' in self.kwargs:
            return models.Inventory.objects.all().values('product').\
                annotate(stock_Quantity=Sum('quantity'),
                         product_name=F('product__product_name')).order_by('product')
        return super().get_queryset()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.filter_class:
            form = forms.FilterForm(self.filter.form)
            context.update({
                'filter': self.filter,
                'helper': form.helper,
                'create_url': self.create_url
            })
        else:
            context.update({
                'create_url': self.create_url
            })
        context.update({
            'segment': self.segment
        })
        return context


class FormViewMixin(generic.FormView):
    widgets = {}
    exclude = None

    def get_form(self, form_class=None):
        if self.form_class is None:
            form_class = modelform_factory(self.model, fields=self.fields, exclude=self.exclude, widgets=self.widgets)
        form = super().get_form(form_class=form_class)
        form.helper = forms.FormHelper()
        form.helper.form_tag = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'segment': self.segment
        })
        return context
