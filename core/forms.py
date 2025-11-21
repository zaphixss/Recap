from django import forms
from .models import Blog, Category, Author

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2'
            }
        )
    )

 

    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2'
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset= Category.objects.all(),
        empty_label="Select category",
        widget=forms.Select(
            attrs={
                'class': 'w-full border rounded px-3 py-2'
            }
        )
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'category' ]



class AuthorForm(forms.ModelForm):
    
    fullname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    headline = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    bio = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    bio = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    bio = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    country = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'w-[50%] border rounded px-3 py-2 text-sm'
            }
        )
    )

    youtube = forms.URLField(
        widget= forms.URLInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2 text-sm'
            }
        )
    )

    linkedin = forms.URLField(
        widget= forms.URLInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2 text-sm'
            }
        )
    )

    facebook = forms.URLField(
        widget= forms.URLInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2 text-sm'
            }
        )
    )

    twitter = forms.URLField(
        widget= forms.URLInput(
            attrs={
                'class': 'w-full border rounded px-3 py-2 text-sm'
            }
        )
    )

    class Meta:
        model = Author
        fields = [
            "fullname",
            "headline",
            "bio",
            "country",
            "image",
            "youtube",
            "linkedin",
            "facebook",
            "twitter",
        ]