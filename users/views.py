from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash    #kullanıcı şifreyi değiştirdikten sonra oturumda kalmasını sağlıyor.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import UserCreatForm, LoginForm, UserProfileEdit, UserPasswordChangeForm, UserUploadPhotoForm
from yonetim.models import Task


@login_required(login_url='/users/login/')
def user_create(request):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect(reverse('yonetim:task_list'))

    form = UserCreatForm(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        yetkiliMi = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        if yetkiliMi:

            return HttpResponseRedirect(reverse('yonetim:task_list'))

    return render(request, 'users/user_create.html', context={'form':form})


def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('yonetim:task_list'))

    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('yonetim:task_list'))
        else:
            hata_mesaji = 'Lütfen kullanıcı adını veya şifrenizi doğru giriniz!'
            return render(request, 'users/user_login.html', context={'form': form, 'hata_mesaji':hata_mesaji})

    return render(request, 'users/user_login.html', context={'form':form})


def user_logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:user_login'))
    logout(request)
    return HttpResponseRedirect(reverse('users:user_login'))


@login_required(login_url='/users/login/')
def user_edit_profile(request):
    data= {'cinsiyet':request.user.userprofile.cinsiyet, 'dogum':request.user.userprofile.dogum, 'telefon_numarasi':request.user.userprofile.telefon_numarasi}
    user_profile_form=UserProfileEdit(request.POST or None, instance=request.user, initial=data) #instance kısmını yazmasaydık o kişinin bilgileri gelmicekti. initial kısmı da güncelleme yapılacağı için kullanıldı.

    if request.method=="POST":
        if user_profile_form.is_valid():
            user_profile_form.save(commit=True)
            dogum = user_profile_form.cleaned_data['dogum']
            telefon = user_profile_form.cleaned_data['telefon_numarasi']
            cinsiyet = user_profile_form.cleaned_data['cinsiyet']

            request.user.userprofile.cinsiyet= cinsiyet
            request.user.userprofile.telefon_numarasi= telefon
            request.user.userprofile.dogum= dogum
            request.user.userprofile.save()

            messages.success(request,'Kullanıcı bilgileriniz güncellendi!')
            return HttpResponseRedirect(reverse('yonetim:task_list'))

    return render(request, 'users/user_edit_profile.html', context={'form':user_profile_form})


@login_required(login_url='/users/login/')
def user_change_password(request):
    form = UserPasswordChangeForm(request.user, request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user = form.save(commit=True)
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değiştirildi')
    return render(request, 'users/password_change.html', context={'form': form})


def user_list(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('yonetim:task_list'))
    users_list = User.objects.all()
    return render(request, 'users/user_list.html', context={'users_list': users_list})


def user_delete(request, username):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('yonetim:task_list'))
    try:
        user = User.objects.get(username=username)
        user.delete()
        messages.warning(request, "Kullanıcı silindi", extra_tags='danger')

        return HttpResponseRedirect(reverse('users:user_list'))

    except User.DoesNotExist:
        return render(request, 'users/user_list.html')


def user_upload_photo(request):
    if request.method == "POST":
        form = UserUploadPhotoForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if form.is_valid():
            userprofile = form.save(commit=True)
            data = {'is_valid': True, 'image-url':userprofile.profil_photo.url, 'success':'Profil Fotoğrafı Güncellendi'}
            return JsonResponse(data=data)
        else:
            return JsonResponse(data={'is_valid': False})
    else:
        return HttpResponseRedirect(reverse('users:user_edit_profile'))


def user_profile(request,username):
    user = get_object_or_404(User, username=username)
    task_list = Task.objects.filter(worker=user)
    return render(request, 'users/user_profile.html', context={'task_list': task_list, 'user': user})