from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))

speciality_list = (('1', 'Allergy & Immunology'), 
                    ('2', 'Anesthesia'),
                    ('3', 'Cardiology (Heart, Cardiac Surgery, Cardiovascular, Hypertension, Blood Pressure)'),
                    ('4', 'Colorectal Surgery (Surgery of Anal Canal, Rectum, etc.)'),
                    ('5', 'Dentistry (Dental, Orthodontics, Maxillofacial Surgery, Scaling)'),
                    ('6', 'Dermatology (Skin, Venereology, Sexual, Hair, Allergy)'),
                    ('7', 'Endocrinology (Diabetes, Hormones, Thyroid, etc.)'),
                    ('8', 'ENT (Ear, Nose & Throat, Otorhinolaryngology)'),
                    ('9', 'Gastroenterology (Stomach, Pancreas and Intestine)'),
                    ('10', 'General Physician (All or any common diseases and health issues)'),
                    ('11', 'General Surgery (Incision, Operation)'),
                    ('12', 'Gynaecologic Oncology (Cancer of Female Reproductive System)'),
                    ('13', 'Gynaecology and Obstetrics (Pregnancy, Menstrual, Uterus, Female)'),
                    ('14', 'Haematology (Blood related diseases)'),
                    ('15', 'Hepato-Biliary- Pancreatic Surgery'),
                    ('16', 'Hepatology (Liver, Gallbladder, Biliary system)'),
                    ('17', 'Infectious Diseases'),
                    ('18', 'FemaNephrology (Kidney, Ureter, Urinary Bladder)le'),
                    ('19', 'Neuromedicine (Brain, Spinal Cord, Nerve)'),
                    ('20', 'Neurosurgery (Surgery of Brain, Spinal Cord and Nerve)'),
                    ('21', 'Nutritionist (Food, Diet, Weight Management)'),
                    ('22', 'Oncology (Cancer)'),
                    ('23', 'Ophthalmology (Eye, Vision, Cataracts, etc.)'),
                    ('24', 'Orthopaedics (Bone, Joint, Fractures)'),
                    ('25', 'Other Speciality (not mentioned in the list)'),
                    ('26', 'Paediatric Surgery (Surgery for Children)'),
                    ('27', 'Paediatrics (Child or Infant any disease)'),
                    ('28', 'Physical Medicine (Paralysis, Pain Management)'),
                    ('29', 'Physiotherapy'),
                    ('30', 'Plastic Surgery, Reconstruction or Cosmetic Surgery'),)


class EmployeeRegistrationForm(UserCreationForm):
    # gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    speciality = forms.ChoiceField(choices=speciality_list)

    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        # self.fields['gender'].widget = forms.CheckboxInput()


        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )


        self.fields['title_or_designation'].widget.attrs.update(
            {
                'placeholder': '(e.g. Professor / Consultant with hospital name)',
            }
        )
        self.fields['bmdc_reg_no'].widget.attrs.update(
            {
                'placeholder': '(BMDC Registration No.)',
            }
        )
        self.fields['degree_specification'].widget.attrs.update(
            {
                'placeholder': '(Detail of the degree, institute and other specification as to appear on the profile)',
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'placeholder': '(Work phone numbers)',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': '(Detail of the specialties, experiences and expertise as to appear on the profile)',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 
        'password1', 'password2',
        'title_or_designation','speciality','image', 'bmdc_reg_no',
        'description', 'degree_specification',
         'gender', 'phone',]
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            },
            'phone': {
                'required': 'Phone is required',
                'max_length': 'Phone number is too long'
            },
            'title_or_designation': {
                'required': 'Title/Designation is required',
                'max_length': 'Title/Designation is too long'
            },
            'speciality': {
                'required': 'Speciality is required',
            },
            'bmdc_reg_no': {
                'required': 'BMDC reg. no. is required',
                'max_length': 'BMDC number is too long'
            },
            'description': {
                'required': 'Description is required',
                'max_length': 'Description is too long'
            },
            'degree_specification': {
                'required': 'Degree/specification is required',
                'max_length': 'Degree/specification is too long'
            }
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")

        return gender

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "doctor"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(EmployerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Company Name"
        self.fields['last_name'].label = "Company Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Address',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(email)
        print(password)
        print(User.objects.get(id=1))
        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class DoctorProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DoctorProfileUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 
        'title_or_designation','speciality','image', 'bmdc_reg_no',
        'description', 'degree_specification',
         'gender', 'phone',]