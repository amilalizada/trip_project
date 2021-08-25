from django import forms
from Tours.models import TourComments

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = (
            'content',
            # 'post',
        )

        widgets = {
            'content': forms.TextInput(attrs={
                'class':  'form-control',
            }),
            
        }