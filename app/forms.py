from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import AppliedStudents, UndergraduateCourse
from .choices import COUNTRY_CHOICES, SCHOOL_CHOICES, SOCIAL_STATUS, STUDY_LANGUAGES


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



class AppliedStudentsForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=STUDY_LANGUAGES,
        widget=forms.Select(attrs={
            'class': 'block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'language'
        })
    )
    program = forms.ModelChoiceField(
        queryset=UndergraduateCourse.objects.all(),
        widget=forms.Select(attrs={
            'class': 'block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'language'
        })
    )
    surname = forms.CharField(widget=forms.TextInput
                              (attrs={
                                  'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
                                  'id': 'grid-last-name',
                                  'placeholder': 'Familiya'
                                  }))
    name = forms.CharField(widget=forms.TextInput
                              (attrs={
                                  'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
                                  'id': 'grid-first-name',
                                  'placeholder': 'Ism'
                                  }))
    
    fathers_name = forms.CharField(widget=forms.TextInput
                              (attrs={
                                  'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
                                  'id': 'father-name',
                                  'placeholder': 'Otasini ismi'
                                  }))
    passport_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'passport','placeholder': 
            'Pasport Seriya raqami'
            })
        )
    passport_pdf = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'passport',
            'placeholder': 'Pasport nusxasi',
        })
    )
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'country'
        })
    )
    region = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'placeholder': 'Viloyat'
            })
        )
    district = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'placeholder': 'Tuman'
            })
        )
    schooling = forms.ChoiceField(
        choices=SCHOOL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'schooling'
        })
    )
    
    diploma = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'diploma',
            'placeholder': 'Diplom nusxasi',
        })
    )
    social_status = forms.ChoiceField(
        choices=SOCIAL_STATUS,
        widget=forms.Select(attrs={
            'class': 'block w-full bg-white text-gray-700 border border-gray-200 rounded py-2.5 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'status'
        })
    )
    social_status_file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'id': 'social_status_file',
        }),
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'placeholder': 'Telefon raqam'
            })
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'appearance-none block w-full bg-white text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-gray-50 focus:border-gray-500',
            'placeholder': 'Elektron manzil',
        })
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = AppliedStudents
        fields = [
            "program",
            "language",
            'surname', 
            'name', 
            'fathers_name', 
            'passport_number', 
            'passport_pdf',
            'country',
            'region',
            'district',
            'schooling',
            'diploma',
            'social_status',
            'social_status_file',
            'phone_number',
            'email'
            ]