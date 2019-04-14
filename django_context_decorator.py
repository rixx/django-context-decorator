import copy


class context:
    """
    Use this class as a decorator around methods, properties, or cached
    properties to add the wrapped value (or result for callables) to
    the template context. Works for all Django View classes.
    Requires Python 3.6+
    """

    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):

        if hasattr(self.func, '__set_name__'):
            self.func.__set_name__(owner, name)

        if not hasattr(owner, '_context_fields'):
            owner._context_fields = set()
        elif not getattr(owner, '_context_copied', '') == owner.__name__:
            setattr(owner, '_context_copied', owner.__name__)
            owner._context_fields = copy.deepcopy(owner._context_fields)
        owner._context_fields.add(name)

        if not getattr(owner, 'get_context_data', False):

            def get_context_data(_self, **kwargs):
                return super(owner, _self).get_context_data(**kwargs)

            owner.get_context_data = get_context_data

        if not getattr(owner, '_context_patched', False):
            old_get_context_data = owner.get_context_data

            def new_get_context_data(_self, **kwargs):
                result = old_get_context_data(_self, **kwargs)
                for name in _self._context_fields:
                    attr = getattr(_self, name)
                    if callable(attr):
                        attr = attr()
                    result.setdefault(name, attr)
                return result

            owner.get_context_data = new_get_context_data
            owner._context_patched = True

    def __get__(self, instance, cls=None):
        return self.func.__get__(instance, cls) if hasattr(self.func, '__get__') else self.func
