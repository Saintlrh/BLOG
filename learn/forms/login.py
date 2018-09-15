from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, min_length=6, required=True, error_messages={"required": '用户账户不能为空',
    'invalid':'格式错误'}, widget=forms.TextInput(attrs={"class": "c", "placeholder": "Username"}))

    passwd = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput(attrs={"class": "c",
    "placeholder": "Password"}))


class UserRegister(forms.Form):
    username = forms.CharField(max_length=12, min_length=6, widget=forms.TextInput(attrs={"class": "c", "placeholder": "Username"}))
    password1 = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput(attrs={"class": "c", "placeholder": "Password"}))
    password2 = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput(attrs={"class": "c", "placeholder": "Repeat-Password"}))
    phonenum = forms.CharField(max_length=11, min_length=11, widget=forms.TextInput(attrs={"class": "c", "placeholder": "PhoneNumber"}))
    email = forms.EmailField(label='电子邮件', widget=forms.TextInput(attrs={"class": "c", "placeholder": "E-mail"}))

    def phone_validate(self, phonenum):
        a = 1
        return type(phonenum) == type(a)
    def pwd_validate(self, p1, p2):
        return p1 == p2
