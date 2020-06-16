from django.http import HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from account.models import User


def smoke(request):
    return HttpResponse('Hello from account')


# 1
# class UpdateUserView(LoginRequiredMixin, UpdateView):
#     queryset = User.objects.all()
#     template_name = 'my-profile.html'
#     fields = ('email', 'first_name', 'last_name')
#     success_url = reverse_lazy('rate:list')
#
#     def get_queryset(self):
#         query = super().get_queryset()
#         return query.filter(id=self.request.user.id)


# 2
class UpdateUserView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    fields = ('email', 'first_name', 'last_name')
    success_url = reverse_lazy('rate:list')

    # a
    # def get_object(self, queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #
    #     object = get_object_or_404(queryset, id=self.request.user.id)
    #     return object

    # b
    def get_object(self, queryset=None):
        self.kwargs[self.pk_url_kwarg] = self.request.user.id
        return super().get_object(queryset)
