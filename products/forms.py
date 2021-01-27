from django import forms
from .models import Album, Genre, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        genre_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = genre_names


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('album', 'author', 'created_on',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels.
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Write a review..',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['title'] = 'Review content'
            self.fields[field].label = False
