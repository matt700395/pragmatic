from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView   #뷰에서 만든 class 갖고옴

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),    #프로필 생성 경로
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]