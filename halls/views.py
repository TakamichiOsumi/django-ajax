from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Hall
from .forms import SignupForm

# Create your views here.
def home(request):
    return render(request, 'halls/home.html')

def dashboard(request):
    return render(request, 'halls/dashboard.html')

class SignUp(generic.CreateView):
    model = CustomUser
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('home')

class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)

class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'

detail_hall = DetailHall.as_view()
create_hall = CreateHall.as_view()
