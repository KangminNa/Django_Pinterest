from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    # form 단에서가 아닌 서버에서 컨트롤 하기 위해 여기서 작성
    def form_valid(self, form):
        # 여기서 커스텀마이징을 하면 됨
        temp_profile = form.save(commit=False) # commit=False 임시 데이터 저장 아직 user 데이터가 아님
        temp_profile.user = self.request.user # 여기서 유저를 저장
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    # 인자를 보내주기 위한 함수 생성 pk를 보내야하는 detail에서 보내기 위한 함수

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    # 인자를 보내주기 위한 함수 생성 pk를 보내야하는 detail에서 보내기 위한 함수