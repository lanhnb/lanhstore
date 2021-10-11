from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from cffi.cffi_opcode import CLASS_NAME
from django import forms
from .models import Comment
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User

class RegistrationForm( forms.Form ):
    username = forms.CharField( label='Tài khoản', max_length=30 )
    email = forms.CharField( label='Email' )
    password1 = forms.CharField( label='Mật khẩu', widget=forms.PasswordInput() )
    password2 = forms.CharField( label='Nhập lại mật khẩu', widget=forms.PasswordInput() )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError( "Mật khẩu không hợp lệ" )

    def cleaned_username(self):
        username = self.cleaned_data( 'username' )
        if re.search( r'^\w+$', username ):
            raise forms.ValidationError( "Tên Tài khoản có ký tự đặt biệt" )
        try:
            User.objects.get( username=username )
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError( "Tài khoản đã tồn tại" )

    def save(self):
        User.objects.create_user( username=self.cleaned_data['username'], email=self.cleaned_data['email'],
                                  password=self.cleaned_data['password1'] )


# sendemail/forms.py



class ContactForm( forms.Form ):
    from_email = forms.EmailField( required=True )
    subject = forms.CharField( required=True )
    message = forms.CharField( widget=forms.Textarea, required=True )


class CommentForm( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__( *args, **kwargs )

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]
