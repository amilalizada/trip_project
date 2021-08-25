from django import forms
from Restaurants.models import ReviewRestaurant

class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewRestaurant
        fields = ('comment', 'food_rating', 'service_rating', 'value_rating', 'atmosphere_rating',)
        widgets = {
            'comment': forms.Textarea(attrs={
                    'class' : 'form-control mb-2',
                    'placeholder': 'Add your Comment',
                    'rows'  : '2',
                    'cols' : '10',
                }),

        }