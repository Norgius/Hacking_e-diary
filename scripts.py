from datacenter.models import Schoolkid, Subject, Lesson, Mark, Chastisement
from datacenter.models import Commendation
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from random import choice


def get_random_commendation():
    with open('commendations.txt', 'r') as file:
        return choice([commendation for commendation in file])


def fix_marks(child):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
    except ObjectDoesNotExist:
        print('\nОшибка в фамилии или имени\n')
        return
    except MultipleObjectsReturned:
        print('\nПожалуйста, укажите фамилию и имя\n')
        return
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    print('\nПлохие оценки стали пятерками, '
          'проверьте пожалуйста это в журнале\n')


def remove_chastisements(child):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
    except ObjectDoesNotExist:
        print('\nОшибка в фамилии или имени\n')
        return
    except MultipleObjectsReturned:
        print('\nПожалуйста, укажите фамилию и имя\n')
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    print('\nВсе замечания удалены, проверьте пожалуйста это в журнале\n')


def create_commendation(child, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
    except ObjectDoesNotExist:
        print('\nОшибка в фамилии или имени\n')
        return
    except MultipleObjectsReturned:
        print('\nПожалуйста, укажите фамилию и имя\n')
        return
    try:
        Subject.objects.get(title=subject, year_of_study=6)
    except ObjectDoesNotExist:
        print('\nОшибка в названии предмета\n')
        return
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject__title=subject
    )
    sorted_lessons = sorted(
        lessons,
        key=lambda lesson: lesson.date,
        reverse=True
    )
    last_lesson = sorted_lessons[0]
    lesson_date = last_lesson.date
    teacher = last_lesson.teacher
    commendation = Commendation.objects.filter(
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        created=lesson_date,
        teacher=teacher
    )
    if commendation:
        print('\nПохвала от учителя уже есть к последнему '
              f'уроку {subject}, будьте аккуратнее\n')
        return
    commendation = get_random_commendation()
    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        created=lesson_date,
        teacher=teacher,
        text=commendation
    )
    print(f'\nПоявилась похвала к последнему уроку {subject}, '
          'проверьте пожалуйста это в журнале\n')
