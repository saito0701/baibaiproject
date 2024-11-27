from django.urls import path
from . import views

app_name = 'baibai'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/', views.CreateBaibaiView.as_view(), name='post'),

    path('post_done/',
         views.PostSuccessView.as_view(),
         name ='post_done'),

    path('baibais/<int:category>',
         views.CategoryView.as_view(),
         name ='baibai_cat'),

    path('user-list/<int:user>',
         views.UserView.as_view(),
         name ='user_list'),

    path('baibai-detail/<int:pk>',
         views.DetailView.as_view(),
         name ='baibai_detail'),

    path('mypage/',
         views.MypageView.as_view(),
         name='mypage'),

    path('baibai/<int:pk>/delete/',
         views.BaibaiDeleteView.as_view(),
         name ='baibai_delete'),

    path('baibai/<int:pk>/buy/',
         views.BaibaiBuyView.as_view(),
         name ='baibai_buy'),

    path('baibai/done/',
         views.BuySuccessView.as_view(),
         name ='baibai_done'),
]