from django import forms
from .models import Album, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()

        self.fields['genre'].choices = genres
