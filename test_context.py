import pytest
from django.conf import settings
from django.test import RequestFactory
from django.utils.functional import cached_property
from django.views.generic import TemplateView

import django_context_decorator

context = django_context_decorator.context
settings.configure()


class ViewMixin:

    @context
    def mixin(self):
        return 'mixin'

    @context
    @property
    def property_mixin(self):
        return 'mixin property'

    @context
    @cached_property
    def cached_property_mixin(self):
        return 'mixin cached property'


class View(ViewMixin, TemplateView):
    template_name = '.html'

    def __init__(self, request, **kwargs):
        self.request = request
        super().__init__(**kwargs)

    @context
    def data(self):
        return 'data'

    @context
    @property
    def property_data(self):
        return 'data property'

    @context
    @cached_property
    def cached_property_data(self):
        return 'data cached property'


DATA = {
    'data': 'data',
    'property_data': 'data property',
    'cached_property_data': 'data cached property',
    'mixin': 'mixin',
    'property_mixin': 'mixin property',
    'cached_property_mixin': 'mixin cached property',
}

@pytest.mark.parametrize('key,value',((key, value) for key, value in DATA.items()))
def test_context_decorator_view_attributes(key, value):
    view = View(RequestFactory().get(''))
    for _ in range(2):
        attr = getattr(view, key)
        if callable(attr):
            assert attr() == value
        else:
            assert attr == value


@pytest.mark.parametrize('key,value',((key, value) for key, value in DATA.items()))
def test_context_decorator_context_content(key, value):
    view = View(RequestFactory().get(''))
    for _ in range(2):
        assert view.get_context_data()[key] == value
