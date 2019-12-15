from django import forms
from p_library.models import Author, Book, Friend, Publisher


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = "__all__"


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size':'82'}))
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['ISBN', 'title', 'description', 'year_release',\
        'author', 'in_stock', 'price', 'publisher']


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Publisher
        fields = '__all__'

class FriendForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'
