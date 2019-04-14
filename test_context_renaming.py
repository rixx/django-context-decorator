from contextlib import suppress

from django.conf import settings
from django.test import RequestFactory
from django.views.generic import TemplateView

import django_context_decorator

context = django_context_decorator.context

with suppress(RuntimeError):
    settings.configure()


class View(TemplateView):
    template_name = '.html'

    def __init__(self, request, **kwargs):
        self.request = request
        super().__init__(**kwargs)

    @context
    def foo(self):
        return 'foo'


NewView = View


class View(NewView):
    @context
    def data(self):
        return 'data'


OtherView = View


class View(OtherView):
    @context
    def other_data(self):
        return 'data'


def test_view_inheritance_with_renaming():

    view = OtherView(RequestFactory().get(''))
    context = view.get_context_data()
    assert 'data' in context
    assert 'other_data' not in context
