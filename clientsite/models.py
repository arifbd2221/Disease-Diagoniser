from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

gender_list = (('male', 'Male'), ('female', 'Female'),)

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

class Speciality(models.Model):
    name = models.CharField(max_length=100, default='Speciality')

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })

    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    title_or_designation = models.CharField(max_length=100, blank=True, null=True)
    speciality = models.ManyToManyField(Speciality, related_name='speciality')
    gender = models.CharField(max_length=10, choices=gender_list, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    bmdc_reg_no = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    degree_specification = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __unicode__(self):
        return self.email
    
    objects = UserManager()

