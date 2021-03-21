from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма написания отзыва к товару"""
    class Meta:
        model = Reviews
        fields = ('text',)

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'comment', 'rows': 3})}
