from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):   #유저가 수정할 정보나 탈퇴하려는 유저가 요청한 유저이닞 검사
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated