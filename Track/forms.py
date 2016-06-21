from django import forms
from Track.models import Track, Genre


class TrackForm(forms.ModelForm):

	class Meta:

		model = Track
		fields = ['trackTitle', 'trackRating', 'trackGenre']


class GenreForm(forms.ModelForm):

	class Meta:

		model = Genre
		fields = ['genreName']




