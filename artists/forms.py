from django import forms


class ArtistForm(forms.Form):
    stage_name = forms.CharField(
        min_length=10, max_length=50
    )
    social_link_field = forms.URLField(
    )
