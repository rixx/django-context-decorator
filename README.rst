django-context-decorator
------------------------

``django-context-decorator`` is a Python package for Django removing the need
to call ``super().get_context_data(**kwargs)`` in nearly every Django view.

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

Limitations
===========

Due to the usage of ``__set_name__``, this package is limited to usage with Python 3.6+.
