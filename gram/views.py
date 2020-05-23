from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import ImageUpload,ReplyForm
from .models import Gram,Reply

# Create your views here.

class UploadImages(LoginRequiredMixin,CreateView):
    model = Gram
    fields = ("Photo","comment",)
    template_name = "upload.html"
    login_url = "login"


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DisplayImages(LoginRequiredMixin,ListView):
    model = Gram
    template_name = "display.html"
    login_url = "login"


class EditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Gram
    template_name = "edit.html"
    login_url = "login"
    fields = ("comment",)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Gram
    template_name = "delete.html"
    success_url = reverse_lazy("display")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ReplyView(LoginRequiredMixin,CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = "reply.html"
    login_url = "login"


    def form_valid(self,form):
        reply = form.save(commit=False)
        reply.post = Gram.objects.get(id=self.kwargs["pk"])
        reply.save()
        form.instance.author = self.request.user
        return super().form_valid(form)

class MyPageView(ListView):
    model = Gram
    template_name = "mypage.html"
