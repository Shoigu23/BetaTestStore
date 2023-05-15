from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from users.models import User
from django.contrib import auth, messages
from main.models import Basket

# Create your views here.

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегестрированы!!!'
    title = 'Store-Регистрация'

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store-Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context