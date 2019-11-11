django-context-decorator
------------------------

.. image:: https://img.shields.io/travis/rixx/django-context-decorator.svg
   :target: https://travis-ci.org/rixx/django-context-decorator
   :alt: Continuous integration

.. image:: https://img.shields.io/codecov/c/github/rixx/django-context-decorator.svg
   :target: https://codecov.io/gh/rixx/django-context-decorator
   :alt: Coverage

.. image:: https://img.shields.io/pypi/v/django-context-decorator.svg
   :target: https://pypi.python.org/pypi/django-context-decorator
   :alt: PyPI

``django-context-decorator`` is a Python package for Django removing the need
to call ``super().get_context_data(**kwargs)`` in nearly every Django view.

You can also read the `blog post`_ about this package.

Usage
=====

.. code-block:: python

   from django_context_decorator import context
   from django.utils.functional import cached_property
   from django.views.generic import TemplateView

   class MyView(TemplateView):
       template_name = 'path/to/template.html'

       @context
       def context_variable(self):
           return 'context value'

       @context
       @property
       def context_property(self):
           return 'context property'

       @context
       @cached_property
       def expensive_context_property(self):
           return 'expensive context property'

Now you'll have access to ``{{ context_variable }}``, ``{{ context_property }}``
and ``{{ expensive_context_property }}`` in your template.

Please note: While this package works with the ``@cached_property`` decorator,
please make sure to add the ``@context`` decorator **above** the
``@cached_property`` decorator.

This is especially useful when you couple it with inheritance, because it
allows you to re-use parent class variables without having to extract them from
your ``context``. So you could write a long-form like this:

.. code-block:: python

    from django.views.generic import TemplateView

    
    class BaseMixin:

        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx['var_from_base_mixin'] = 'var_from_base_mixin'
            return ctx


    class View1(BaseMixin, TemplateView):

        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx['var_from_view_1'] = 'value_from_view_1'
            return ctx


    class View2(View1):

        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx['var_from_view_2'] = 'value_from_view_2'
            return ctx

instead like this:

.. code-block:: python

    from django.views.generic import TemplateView
    from django_context_decorator import context


    class BaseMixin:

        @context
        def var_from_base_mixin(self):
            return 'var_from_base_mixin'


    class View1(BaseMixin, TemplateView):

        @context
        def var_from_view_1(self):
            return 'value_from_view_1'


    class View2(View1):

        @context
        def var_from_view_2(self):
            return 'value_from_view_2'



Limitations
===========

Due to the usage of ``__set_name__``, this package is limited to Python 3.6+.

Development
===========

All code resides in ``django_context_decorator.py``. Tests are collected by
``pytest`` from all files starting with ``test_``. To run tests, start a
virtual environment, install the dependencies, and run ``pytest``::

    pip install django pytest pytest-cov
    pytest --cov-report term --cov=django_context_decorator

.. _blog post: https://rixx.de/blog/a-context-decorator-for-django/
