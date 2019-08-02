from django import forms

class MovieForm(forms.Form):
    movie_name=forms.CharField(
        label="Enter Movie Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Movie Name',
            }
        )

    )

    hero_name = forms.CharField(
        label="Enter Hero Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hero Name',
            }
        )

    )

    heroine_name = forms.CharField(
        label="Enter Heroine Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Heroine Name',
            }
        )

    )

    director_name = forms.CharField(
        label="Enter Director Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Director Name',
            }
        )

    )

    rating = forms.CharField(
        label="Enter Movie Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie Rating',
            }
        )

    )

    release_date = forms.DateField(
        label="Enter Movie Release Date",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie Date',
            }
        )

    )

    budget = forms.IntegerField(
        label="Enter Budget",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Movie Budget',
            }
        )

    )