from django import forms

from shorty.models import Shortener


class ShortenerForm(forms.ModelForm):

    url = forms.URLField(
        widget=forms.URLInput(
            attrs={"class": "form-control", "placeholder": "Enter URL"}
        )
    )

    class Meta:
        model = Shortener

        fields = ("url",)
