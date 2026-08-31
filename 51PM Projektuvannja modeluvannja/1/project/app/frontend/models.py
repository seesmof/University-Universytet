from django.db import models
from django.core.exceptions import ValidationError


def validate_full_name(value: str):
    if not " " in value:
        raise ValidationError(
            "Full name does not contain a space.", params={"value": value}
        )


class Doctor(models.Model):
    full_name = models.CharField(max_length=250, validators=[validate_full_name])

    def __str__(self) -> str:
        return self.full_name.title()
