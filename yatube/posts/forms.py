from django.contrib.auth import get_user_model
from django.forms import ModelForm, Select, Textarea, forms
from posts.models import Post

User = get_user_model()


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

        widgets = {
            'text': Textarea(
                attrs={
                    'name': 'text',
                    'cols': '40',
                    'rows': '10',
                    'class': 'form-control',
                    'required id': 'id_text',
                }
            ),
            'group': Select(
                attrs={
                    'name': 'group',
                    'class': 'form-control',
                    'id': 'id_group',
                }
            ),
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError(
                'Вы ничего не написали и нам нечего сохранять'
            )

        return data
