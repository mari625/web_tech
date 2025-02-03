from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import TaskForm, TaskModelForm
from .models import TaskModel

import math


def home(request):
    return render(request, 'home.html')


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


def task_form(request):
    task_form = TaskForm()
    print('Task Form')
    print(task_form)
    return render(request, 'task_form.html', {'task_form': task_form})


def task_get(request):
    print(request.GET)
    task_value = (request.GET.get("task"))
    a_value = float(request.GET.get("a"))
    print('task value:', task_value, 'a_value:', a_value)
    new_obj = TaskModel(task=task_value, a=a_value)
    print(new_obj.task, new_obj.a, new_obj.result, new_obj.current_date)
    new_obj.save()
    print('Get')
    return redirect("app_1:task_result")


def task_model_form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("app_1:task_result")
    else:
        form = TaskModelForm()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "task_model_form.html", context)


def solution(a: float):
    if a < 10:
        result = str((a**4).__round__(3))
    elif a > 61:
        result = str(a)
    else:
        result = str((a - math.sin(a**2)).__round__(3))
    return result


def task_result(request):
    object_list = TaskModel.objects.all().order_by("-id")
    print('\nobjects_list: ', object_list)
    last_object = object_list.values('task', 'a')[0]
    print('\nlast_object: ', last_object)
    task_formulation = object_list.values('task')[0]
    task_id = object_list.values('id')[0]['id']
    print('\ntask id: ', task_id, 'task_formulation: ', task_formulation)

    result = solution(last_object['a'])
    print('\nresult: ', result)

    update_obj = TaskModel.objects.filter(id=task_id)
    update_result = result
    update_obj.update(result=update_result)

    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    task_formulation = values_list[1]
    print("\ntask_formulation: ", task_formulation)
    last_values = [values_list[1], values_list[2], values_list[3], values_list[4]]
    print("\nlast_values:", last_values)

    context = {
        "last_object": last_object,
        "task_formulation": task_formulation,
        "last_values": last_values,
        "result": result,
        "data": values_list[4],
    }
    return render(request, "task_result.html", context)


def table(request):
    objects_values = TaskModel.objects.values()
    print("\nobjects_values:", objects_values)
    objects_values_list = (
        TaskModel.objects.values_list().filter(id__gte=5).order_by("-id")
    )
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Count("a")),
        cur_objects.aggregate(Avg("a")),
        cur_objects.aggregate(Min("a")),
        cur_objects.aggregate(Max("a")),
        cur_objects.aggregate(StdDev("a")),
        cur_objects.aggregate(Sum("a")),
    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    fields = TaskModel._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)
