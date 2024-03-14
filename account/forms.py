from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError, ModelForm
from django.contrib.auth import authenticate
from account.models import Message, Profile, Address, City


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='نام کاربری :')
    password1 = forms.CharField(label='رمز عبور :', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز عبور :', widget=forms.PasswordInput)
    email = forms.CharField(label='ایمیل :', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, label='نام کاربری :')
    password = forms.CharField(max_length=50, label='رمز عبور :', widget=forms.PasswordInput)

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('نام کاربری یا رمز عبور اشتباه می باشد', code='invalid_ingo')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body',)
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        labels = {
            'subject': 'موضوع:',
            'body': 'متن پیام:',
        }
        attrs = {
            'body': {'class': 'requiredd'},
        }


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='پست الکترونیک', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('کاربری با ایمیل وارد شده پیدا نشد', code='invalid_email')

        return email


class ForgetPasswordForm(forms.Form):
    new_password = forms.CharField(
        label='رمزعبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='تکرار رمزعبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise ValidationError('لطفا با دقت فیلد ها رو وارد کنید', code='invalid_password')


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='رمزعبور قدیمی',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password = forms.CharField(
        label='رمزعبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='تکرار رمزعبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise ValidationError('لطفا با دقت فیلد ها رو وارد کنید', code='invalid_password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        user = authenticate(username=self.request.user.username, password=password)
        if user is None:
            raise ValidationError('رمز عبور قدیمی اشتباه است.')
        return password


class EditProfileUser(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'first_name': 'نام:',
            'last_name': 'نام خانوادگی:',
            'email': 'ایمیل:',
            'username': 'نام کاربری:',

        }


class EditImageUser(ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'hidden': 'true', 'id': 'upload', }),
        }
        labels = {
            'image': 'عکس پروفایل:',
        }

    def __init__(self, *args, **kwargs):
        super(EditImageUser, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('state','city','fullname', 'phone', 'email','default', 'address',)
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', }),
            'state': forms.Select(attrs={'class': 'form-control',}),
            'city': forms.Select(attrs={'class': 'form-control',}),
            'default': forms.CheckboxInput(attrs={'class': 'form-check-input',}),

        }
        help_texts = {
            'address': 'لطفا آدرس را به طور دقیق وارد کنید',
            'default':'در نظر داشته باشید شما فقط میتوانید یک آدرس را به عنوان پیش‌فرض تنظیم کنید'
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)



        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')



    def clean_state(self):
        state = self.cleaned_data.get('state')
        if state is None:
            raise ValidationError('لطفا مقدار درست را وارد کنید')
        return state

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city is None:
            raise ValidationError('لطفا مقدار درست را وارد کنید')
        return city

    def clean_default(self):
        cleaned_data = self.cleaned_data
        user = self.request.user
        default_count = Address.objects.filter(user=user, default=True).exclude(pk=self.instance.pk).count()

        if cleaned_data.get('default') and default_count >= 1:
            raise forms.ValidationError('شما از قبل آدرسی را به عنوان پیش‌فرض تنظیم کرده اید.')

        return cleaned_data['default']

