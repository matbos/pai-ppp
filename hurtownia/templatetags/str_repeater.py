from django import template
from django.template import Library

register = Library()


class RangeNode(template.Node):
    def __init__(self, times, string, context_name):
        if not self._isint(times):
            self.times = 1
        else:
            self.times = times
        if not self._isstr(string):
            self.string = " "
        else:
            self.string = string

        self.context_name = context_name

    def _isint(self, value):
        return isinstance(value, int)

    def _isstr(self, value):
        return isinstance(value, str)

    def _resolveint(self, value, context):
        if self._isint(value):
            return value
        return int(value.resolve(context))

    def render(self, context):
        times = self._resolveint(self.times, context)

        return self.string * times


@register.tag
def str_repeater(parser, token):
    """
        str_repeater
    """
    bits = token.contents.split()
    len_bits = len(bits)

    # DEFAULTS
    times = bits[1]
    string = bits[2]
    context_name = bits[-1]

    return RangeNode(times, string, context_name)
