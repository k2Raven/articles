from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


def at_last_10(value):
    if len(value) < 10:
        raise ValidationError('Длина поля должна быть не менее 10 символов')

@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Значение "%(value)s" слишком короткое. Оно должно содержать не менее %(limit_value)d символов.'
    code = 'too_short'

    def clean(self, x):
        return len(x)

    def compare(self, a, b):
        return a < b
