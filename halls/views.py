from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from .models import CustomUser, Hall, Video
from .forms import SignupForm, VideoForm, SearchForm
import urllib

# Create your views here.
def home(request):
    return render(request, 'halls/home.html')

def dashboard(request):
    return render(request, 'halls/dashboard.html')

def add_video(request, pk):

    form = VideoForm()
    search_form = SearchForm()
    hall = Hall.objects.get(pk = pk)

    if not hall.user == request.user:
        raise Http404

    if request.method == 'GET':
        print("request method is GET, just return HttpResponse object")
    elif request.method == 'POST':
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id is not None:
                video.youtube_id = video_id
                video.hall = hall
                video.url = filled_form.cleaned_data['url']
                video.title = "dummy"
                video.save()
                return redirect('detail_hall', pk)
        else:
            print("data in the form was invalid")

    return render(request,
                  'halls/add_video.html',
                  { 'form' : form,
                    'search_form' : search_form,
                    'hall' : hall })

def search_video(request):
    user_input = request.GET.get("search_term")
    return JsonResponse({
        'srv_msg' : f'Server got {user_input} !'
    })

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

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = 'halls/update_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('dashboard')

detail_hall = DetailHall.as_view()
create_hall = CreateHall.as_view()
update_hall = UpdateHall.as_view()
delete_hall = DeleteHall.as_view()
