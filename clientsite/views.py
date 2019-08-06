from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView,UpdateView
from django.http import HttpResponseRedirect
from .forms import *
from .models import User
from django.contrib import messages, auth
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.conf import settings # new
from django.views.generic.base import TemplateView
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY # new

def home(request):
    model = User.objects.all()
    print("hello")
    print(model)
    return render(request, 'clientsite/index.html', {})


def about(request):
    return render(request, 'clientsite/about.html', {})

def doctor(request):
    return render(request, 'clientsite/doctor.html', {})

def department(request):
    return render(request, 'clientsite/department.html', {})

def contact(request):
    return render(request, 'clientsite/contact.html', {})


class RegisterEmployeeView(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'clientsite/appointment.html'
    success_url = 'login'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method =='POST':
            form = self.form_class(data=request.POST)
            print('before valid')
            if form.is_valid():
                print('after valid')
                user = form.save(commit=False)
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password1")
                user.email = email
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                return render(request, 'clientsite/appointment.html', {'form': form})

class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = 'pricing'
    form_class = UserLoginForm
    template_name = 'clientsite/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        
        print(form.get_user())
        auth.login(self.request, form.get_user())
        if form.get_user().role != 'doctor':
            self.success_url = 'admin'
            return redirect('admin')
        else:
            return redirect('pricing')
            

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(User.objects.all())
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)

def pricing(request):
    return render(request, 'clientsite/pricing.html', {})


from django.shortcuts import render
from django.conf import settings # new
from django.views.generic.base import TemplateView
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY # new


class SubscriptionFee(TemplateView):
    template_name = 'clientsite/checkout.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['cost'] = self.kwargs['cost']
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
    
    for key in request.session.keys():
        del request.session[key]

        return render(request, 'clientsite/charge.html')

class EditProfileView(UpdateView):
    model = User
    form_class = DoctorProfileUpdateForm
    context_object_name = 'doctor'
    template_name = 'clientsite/profile.html'
    success_url = reverse_lazy('update-profile')

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('login')
        if self.request.user.is_authenticated and self.request.user.role != 'doctor':
            return reverse_lazy('login')
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Doctor doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        if obj is None:
            raise Http404("Doctor doesn't exists")
        return obj
