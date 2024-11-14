from django import forms
from django.core.exceptions import ValidationError


def validate_not_only_spaces_or_tabs(value):
    trimmed_value = value.strip()
    if len(trimmed_value) < 30:
        raise ValidationError("Post body most be more then 30 characters long.")


class PostForm(forms.Form):
    post_body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control mb-1", "rows": "3", "id": "post_body"}
        ),
        min_length=30,
        max_length=300,
        required=True,
        validators=[validate_not_only_spaces_or_tabs],
    )
