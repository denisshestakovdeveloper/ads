from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .ExtraFunctions import get_main_user
import uuid
def main(request):
    return redirect('get-main')

def index(request):
    categories = AdCategory.objects.all()
    ads = AdCard.objects.select_related("category_id").order_by('id')[:20]
    form_find_main = FindFormMain()
    main_user = get_main_user(request)
    context = {'categories':categories, 'ads':ads, 'form_find_main':form_find_main, 'user':request.user, 'main_user':main_user, 'search_query' : ''}
    return render(request,'main\main.html', context)
def magazine(request):
    return render(request,'magazine\magazine.html')

def find_category(request, id):
    ads_by_category = AdCard.objects.filter(category_id=id).order_by('id')
    main_user = get_main_user(request)
    return render(request,'main/ads_by_category.html', {'ads_by_category': ads_by_category, 'main_user':main_user})
def open_ad(request, id):
    ad = AdCard.objects.get(id = id)
    pictures = AdImage.objects.filter(ad = ad)
    categories = AdCategory.objects.all()
    main_user = get_main_user(request)
    context = {'categories': categories, 'ad': ad, 'pictures':pictures, 'main_user':main_user, 'search_query' : ''}
    return render(request, 'main/ad_card.html', context)

def auth(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        user = authenticate(request, username=form.data.get('username'), password=form.data.get('password'))
        if user is not None:
            login(request, user)
            return redirect('get-main')
        else:
            return redirect('get-main')
    form = AuthForm()
    main_user = get_main_user(request)
    return render(request, 'main/auth.html', {'form': form, 'main_user':main_user})

def reguser(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        user = User()
        sys_user = SysUser()
        sys_user.username = form.data.get('username')
        sys_user.first_name = form.data.get('firstname')
        sys_user.set_password(form.data.get("password"))
        sys_user.save()
        user.sys_user = sys_user
        user.firstname = form.data.get('firstname')
        user.lastname = form.data.get("lastname")
        user.save()
        return redirect('get-main')

    form = AuthForm()
    main_user = get_main_user(request)
    return render(request, 'main/reguser.html', {'reguser_form': form, 'main_user':main_user})

def logout_view(request):
    logout(request)
    return redirect('get-main')

def personal_cabinet(request):
    main_user = get_main_user(request)
    if not main_user == None:
        ads_by_user = AdCard.objects.filter(author_id = main_user.id).order_by('id')
    else:
        ads_by_user = {}
    return render(request, 'main/personal_cabinet.html', {'ads_by_user': ads_by_user, "main_user":main_user})

def fast_payment(request):
    return redirect('http://127.0.0.1:5000')

def edit_ad(request, id):
    if request.method == "POST":
        if "button_add_image" in request.POST:
            form = UploadPicture(request.POST, request.FILES)
            if form.is_valid():
                file_name = handle_uploaded_file(form.cleaned_data['file'])
                add_image_to_ad_card(id, file_name)
        if 'button_save_card' in request.POST:
            ad = AdCard.objects.get(id=id)
            form = EditAdCard(request.POST, instance=ad)
            if form.is_valid():
                form.save()
                return redirect('personal_cabinet')

    ad = AdCard.objects.get(id=id)
    pictures = AdImage.objects.filter(ad = ad)
    form_pictures = UploadPicture()
    form_edit_card = EditAdCard(instance = ad)
    main_user = get_main_user(request)
    context = {'ad': ad, 'ad_id' : id, 'pictures':pictures, 'main_user':main_user, 'form_add_picture':form_pictures, 'form_edit_card':form_edit_card}

    return render(request, 'main/edit_card.html', context)

def add_ad(request):
    def_category = AdCategory.objects.get(id = 1)
    def_type = AdType.objects.get(id = 1)
    new_ad = AdCard()
    new_ad.category_id = def_category
    new_ad.type_id = def_type
    new_ad.author_id = get_main_user(request)
    new_ad.price = 0
    new_ad.is_active = False
    new_ad.published = False
    new_ad.save()
    return redirect('edit_ad', id = new_ad.id)

def handle_uploaded_file(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())
    new_file_name = f"{name}_{suffix}{ext}"
    with open(f"D:/_Programs/LearnPython/Ads_TopAcademy/ads_yarko/ads_main/static/ads_images/{new_file_name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return new_file_name

def add_image_to_ad_card(card_id, file_name):
    ad = AdCard.objects.get(id=card_id)
    image = AdImage()
    image.file_name = file_name
    image.ad = ad
    image.save()
    if (ad.main_picture == ''):
        ad.main_picture = file_name
        ad.save()

def delete_image(request, id_card, id_picture):
    AdImage.objects.filter(id = id_picture).delete()
    return edit_ad(request, id_card)

def make_image_main(request, id_card, id_picture):
    picture = AdImage.objects.get(id = id_picture)
    print(picture)
    card = AdCard.objects.get(id = id_card)
    card.main_picture = picture.file_name
    card.save()
    return edit_ad(request, id_card)

def publish_ad(request, id_card):
    card = AdCard.objects.get(id = id_card)
    card.is_active = True
    card.published = True
    card.save()
    return personal_cabinet(request)

def unpublish_ad(request, id_card):
    card = AdCard.objects.get(id = id_card)
    card.is_active = False
    card.save()
    return personal_cabinet(request)

def delete_card(request, id_card):
    AdCard.objects.get(id = id_card).delete()
    return redirect('personal_cabinet')

def search(request):
    if request.method == "POST":
        data = request.POST;
        query_text = data.get('query')
        if (query_text != ''):
            ads = AdCard.objects.all()
            ads = ads.filter(name__icontains=query_text) | ads.filter(decription__icontains=query_text)
            form_find_main = FindFormMain()
            main_user = get_main_user(request)
            context = {'ads': ads, 'form_find_main': form_find_main, 'user': request.user, 'main_user': main_user, 'search_query' : query_text }
            return render(request, 'main\search_result.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')