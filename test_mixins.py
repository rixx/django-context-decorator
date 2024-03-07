from django.views.generic import TemplateView

import django_context_decorator

context = django_context_decorator.context


class ViewMixin:
    @context
    def mixin_field(self):
        return "mixin"


class BaseView(TemplateView):
    @context
    def base_field(self):
        return "base"


class View(ViewMixin, BaseView):
    pass


def test_mixin_fields():
    view = View()
    context = view.get_context_data()

    assert "mixin_field" in context
    assert "base_field" in context
