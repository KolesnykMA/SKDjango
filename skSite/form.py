from django.forms import ModelForm, widgets
from .models import Mail


class ContactForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['name', 'email', 'telegram', 'text']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'class': 'name', 'id': 'name', 'name': 'name', 'placeholder': 'Григорій Сковорода'})
        self.fields["email"].widget.attrs.update({'class': 'email', 'id': 'email', 'name': 'email', 'placeholder': 'name.lastname@ukma.edu.ua'})
        self.fields["telegram"].widget.attrs.update({'class': 'tg', 'id': 'telegram', 'name': 'tg', 'placeholder': '@KMA1615'})
        self.fields["text"].widget.attrs.update({'class': 'message', 'id': 'message', 'name': 'message', 'placeholder': 'Було б дуже круто зробити...'})

        self.fields['name'].label = "Ім'я та прізвище"
        self.fields['email'].label = "Електронна пошта"
        self.fields['telegram'].label = "Телеграм"
        self.fields['text'].label = "Повідомлення"


