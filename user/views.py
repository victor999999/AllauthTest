from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from user.forms import ProfileForm


class ProfileView(LoginRequiredMixin, View):
    """展示个人信息"""
    login_url = "/accounts/login/"

    def get(self, request):
        user = request.user
        return render(request, 'user/profile.html', {'user': user})


class ChangeProfile(LoginRequiredMixin, View):
    """更改个人信息"""
    login_url = "/accounts/login/"

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'user/change_profile.html', context={'form': form})

    def post(self, request):
        # instance参数表示用model实例来初始化表单，这样就可以达到通过表单来更新数据
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # 添加一条信息，表单验证成功就重定向到个人信息页面
            messages.add_message(request, messages.SUCCESS, '个人信息更新成功！')
            return redirect('user:profile')
        else:
            return render(request, 'user/change_profile.html', context={'form': form})
