from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput
                                (attrs={'class': 'form-control form-validation-inside',
                                        'id': 'contact-me-name',
                                        'data-constraints': "@Required",
                                        'name': 'firstname'}))
    surname = forms.CharField(widget=forms.TextInput
                              (attrs={'class': 'form-control form-validation-inside',
                                      'id': 'contact-me-last-name',
                                      'data-constraints': "@Required",
                                      'name': 'surname'}))

    phone = forms.CharField(widget=forms.TextInput
                            (attrs={'class': 'form-control form-validation-inside',
                                    'id': 'contact-me-phone',
                                    'data-constraints': "@Required @IsNumeric",
                                    'name': 'phone'}))
    message = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 'form-control form-validation-inside',
                                      'id': 'contact-me-message',
                                      'name': 'message',
                                      'data-constraints': "@Required",
                                      'style': "height: 220px"}))

    email = forms.EmailField(error_messages={'invalid': 'This is my email error msg.'},
                             widget=forms.TextInput(attrs={'class': 'form-control form-validation-inside',
                                                           'type': 'email',
                                                           'id': 'contact-me-email',
                                                           'data-constraints': "@Required",
                                                           'name': 'email'}
                                                    ),
                             required=True
                             )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
