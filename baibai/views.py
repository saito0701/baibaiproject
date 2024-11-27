from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BaibaiPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import BaibaiPost
from django.views.generic import DetailView
from django.views.generic import DeleteView


class IndexView(ListView):
    template_name ='index.html'
    queryset = BaibaiPost.objects.order_by('-posted_at')
    paginate_by = 9
@method_decorator(login_required, name='dispatch')

class CreateBaibaiView(CreateView):
    form_class = BaibaiPostForm
    template_name = "post_baibai.html"
    success_url = reverse_lazy('baibai:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name ='post_success.html'

class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
      category_id = self.kwargs['category']
      categories = BaibaiPost.objects.filter(
        category=category_id).order_by('-posted_at')
      return categories

class UserView(ListView):
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
      user_id = self.kwargs['user']
      user_list = BaibaiPost.objects.filter(
        user=user_id).order_by('-posted_at')
      return user_list

class DetailView(DetailView):
    template_name ='detail.html'
    model = BaibaiPost

class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 9

    def get_queryset(self):
      queryset = BaibaiPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      return queryset
  
class BaibaiDeleteView(DeleteView):
    model = BaibaiPost
    template_name ='baibai_delete.html'
    success_url = reverse_lazy('baibai:mypage')
    def delete(self, request, *args, **kwargs):
      return super().delete(request, *args, **kwargs)
    
class BaibaiBuyView(ListView):
   template_name ='baibai_buy.html'
   model = BaibaiPost
   queryset = BaibaiPost.objects.order_by('-posted_at')
   success_url = reverse_lazy('baibai:baibai_done')

class BuySuccessView(TemplateView):
   template_name ='buy_success.html'


