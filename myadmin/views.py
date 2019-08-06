from django.shortcuts import render,HttpResponse, redirect
from clientsite.models import User as loginuser
from django.views.generic import FormView, RedirectView
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from clientsite.forms import UserLoginForm
from .models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def myadmin(request):
    users = User.objects.all()
    return render(request, 'myadmin/admin.html', {'users': users})
    
@login_required(login_url='login')    
def addDoctor(request):
    if request.method == 'POST':
        user = User(role='doctor',email=request.POST.get('email'),gender=request.POST.get('gender'),name=request.POST.get('name'),chamber=request.POST.get('chamber'),speciality=request.POST.get('speciality'),password=request.POST.get('password'))
        user.save()
        return render(request, 'myadmin/admin.html', {})

    return render(request, 'myadmin/add_doctor.html', {})

@login_required(login_url='login')
def detailsDoctor(request, id):
    user = User.objects.get(id=id)
    return render(request, 'myadmin/details_doctor.html', {'user': user})

@login_required(login_url='login')
def deleteDoctor(request, id):
    deleted = User.objects.get(id=id)
    deleted.delete()
    return render(request, 'myadmin/admin.html', {})

@login_required(login_url='login')
def editDoctor(request, id):
    user = User.objects.get(id=id)

    return render(request, 'myadmin/update_doctor.html', {'user': user})


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = 'admin'
    form_class = UserLoginForm
    template_name = 'login.html'

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
        return redirect('pricing')

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(loginuser.objects.all())
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = 'clientsite/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)