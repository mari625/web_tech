from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm

import math


def info(request):
    mydata = {"name": "Корнева Мария Михайловна",
              "photo": "/images/chinchilla.jpg",
              "email": "mymail@mail.ru",
              "phone": "89654739708"}
    leader = {"name": "Скрипченко Александра Сергеевна",
              "photo": "/images/director.jpg",
              "email": "mail_1@mail.ru"}
    manager = {"name": "Асцатурян Лаура Кареновна",
               "photo": "/images/manager.png",
               "email": "mail_2@mail.ru"}
    description = ("Программа «Математика» дает всестороннюю современную фундаментальную математическую подготовку."
                   " На старших курсах индивидуальный учебный план позволяет уделить большое внимание специализации,"
                   " выбрав ее из всего спектра актуальных направлений математики, смежных дисциплин или приложений."
                   " Благодаря этому выпускники, нацеленные на академическую карьеру, поступают в лучшие аспирантуры"
                   " и магистратуры мира в области математики, физики и экономики, а остальные неизменно находят спрос"
                   " в IT, финансах и других наукоемких приложениях. Тем не менее для успешного освоения программы"
                   " важен интерес к математике как таковой, не обусловленный важностью математической подготовки"
                   " для приложений.")
    program = {"name": "Математика", "description": description, "leader": leader, "manager": manager}
    student_1 = {"photo": "/images/parrot.jpg",
                 "email": "mail_3@mail.ru",
                 "phone": "89654739709"}
    student_2 = {"photo": "/images/beaver.jpg",
                 "email": "mail_4@mail.ru",
                 "phone": "89654739809"}
    students = {"student_1": student_1, "student_2": student_2}
    context = {"mydata": mydata, "program": program, "students": students}
    return render(request, "info.html", context)


def hello(request):
    return HttpResponse('Hello world!')


def calc(a):
    if a < 10:
        result = str((a**4).__round__(3))
    elif a > 61:
        result = str(a)
    else:
        result = str((a - math.sin(a**2)).__round__(3))
    return result


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        context = {'form': form, 'flag': True}
        try:
            a = float(request.POST.get("a_value"))
        except ValueError:
            context['flag'] = False
            return render(request, 'task.html', context)
        result = calc(a)
        context['a'] = a
        context['result'] = result
    else:
        form = TaskForm()
        print(form)
        context = {'form': form, 'flag': True}
    return render(request, 'task.html', context)


def home(request):
    return render(request, 'home.html')


def page_1(request):
    arka = [
        {
            "id": "1",
            "img": "/images/arka1.jpg",
            "price": 1001
        },
        {
            "id": "2",
            "img": "/images/arka2.jpg",
            "price": 1002
        },
        {
            "id": "3",
            "img": "/images/arka3.jpg",
            "price": 1003
        },
        {
            "id": "4",
            "img": "/images/arka4.jpg",
            "price": 1004
        },
        {
            "id": "5",
            "img": "/images/arka5.jpeg",
            "price": 1005
        },
        {
            "id": "6",
            "img": "/images/arka6.jpg",
            "price": 1006
        },
        {
            "id": "7",
            "img": "/images/arka7.jpg",
            "price": 1007
        },
    ]
    dvuscat = [
        {
            "id": "1",
            "img": "/images/dvuscat1.jpg",
            "price": 2001
        },
        {
            "id": "2",
            "img": "/images/dvuscat2.jpg",
            "price": 2002
        },
        {
            "id": "3",
            "img": "/images/dvuscat3.jpg",
            "price": 2003
        },
        {
            "id": "4",
            "img": "/images/dvuscat4.jpg",
            "price": 2004
        },
        {
            "id": "5",
            "img": "/images/dvuscat5.jpg",
            "price": 2005
        },
    ]
    drop = [
        {
            "id": "1",
            "img": "https://rus-teplici.ru/upload/iblock/55b/1talc2640696qibgly75hr6dsqzgxryo/image%2017-min.jpg",
            "price": 3001
        },
        {
            "id": "2",
            "img": "https://www.vseteplichky.ru/img/teplica-strelka1.jpg",
            "price": 3002
        },
        {
            "id": "3",
            "img": "https://www.ogorod.ru/images/cache/460x345/crop/images%7Ccms-image-000027464.jpg",
            "price": 3003
        },
        {
            "id": "4",
            "img": "https://srsu-9.ru/wp-content/uploads/2020/05/teplica_kapelka_preimuschestva_i_harakteristika"
                   "_konstrukcii_1-4.jpg",
            "price": 3004
        },
        {
            "id": "5",
            "img": "https://www.2dum.ru/upload/iblock/0ee/0eec7454d957699e74ce94afaf53632e.jpg",
            "price": 3005
        },
        {
            "id": "6",
            "img": "https://lubosad.ru/image/catalog/ladoga-25/ladoga-25-8.jpg",
            "price": 3006
        },
    ]
    straight = [
        {
            "id": "1",
            "img": "https://td-urojay.ru/upload/iblock/396/0lk2fdge6gkg0l3hytpv3or41hfd4jy5.jpg",
            "price": 2101
        },
        {
            "id": "2",
            "img": "https://dobrye-teplicy.ru/wp-content/uploads/2020/12/5-2.png",
            "price": 2102
        },
        {
            "id": "3",
            "img": "https://voronezh.галерея-теплиц.рф/wp-content/uploads/sites/8/2021/08/%D0%BF%D1"
                   "%80%D1%8F%D0%BC%D0%BE%D1%81%D1%82-3%D0%BC-%D0%B1%D0%BE%D0%BB%D1%82.jpg",
            "price": 2103
        },
        {
            "id": "4",
            "img": "https://lubosad.ru/image/catalog/seliger-25/seliger25-5.jpg",
            "price": 2104
        },
        {
            "id": "5",
            "img": "https://rus-teplici.ru/upload/resize_cache/iblock/5d2/btmotkom6d9c0z7vwin1f4sn51edwnhn/450_9999_0/skazka-3.jpg",
            "price": 2105
        },
    ]
    mitlaider = [
        {
            "id": "1",
            "img": "https://www.2dum.ru/upload/resize_cache/iblock/c8f/290_188_1/q22887bnunm1no22gvztb3j66wpwtujp.jpg",
            "price": 4001
        },
        {
            "id": "2",
            "img": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_6553912d50c5111fe1ae3cdc_6553915211b02f6"
                   "338b0b96f/scale_1200",
            "price": 4002
        },
        {
            "id": "3",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR__jplliKu7Ky-mOhmGil3D7BcqdhwLFPQnA&usqp=CAU",
            "price": 4003
        },
        {
            "id": "4",
            "img": "https://remontpro.pro/files/site/photo/view/108297_57639_3.jpg",
            "price": 4004
        },
    ]
    data = {'arka': arka, 'dvuscat': dvuscat, 'drop': drop, 'straight': straight, 'mitlaider': mitlaider}
    context = {'data': data}
    return render(request, 'page_1.html', context)


def other(request):
    data = {'telephone': '89274891283', 'mail': 'greenmail@mail.ru', 'master': '89648239410', 'adress': 'г.'
            'Москва, ул. Малая Никитинская, 48'}
    context = {'data': data}
    return render(request, 'other.html', context)
