from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountap.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountap"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountap/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # 로그인 로그아웃은 뷰에서 따로 함수 만들지 않아도 장고에서 제공

    path('create/', AccountCreateView.as_view(), name='create'),    #회원가입 창
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),#디테일 창 : 몇번 유저 객체에 접근하는지 : <int:pk>
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
