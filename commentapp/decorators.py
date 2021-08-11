from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):   #아티클 작성자가 요청유저인지 검사
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated