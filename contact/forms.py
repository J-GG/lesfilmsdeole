from django import forms


class ContactForm(forms.Form):
    """Form of the contact section."""

    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title
