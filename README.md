# Взламываем электронный дневник
Данный скрипт позволяет с помощью `Django shell` работать с базами данных электронного дневника. С его помощью плохие оценки (2, 3) можно заменить пятёрками (5), удалить замечания, а также для отдельно взятого предмета, его последнего урока, создать похвалу от учителя.

## Где разместить скрипт?
Файлы `scripts.py` и `commendations.txt` необходимо поместить в корневую папку `Django проекта - электронный дневник`.

## Если Django проекта нет?
Загрузите его с [Github](https://github.com/devmanorg/e-diary/tree/master) и следуйте предоставленной инструкции.

Для работы с проектом тебе понадобится доступ к `базе данных электронного дневника`.
## Запускаем скрипт в работу
При запущенном `электронном дневнике` необходимо открыть новую консоль и запустить `Django shell`
```
python manage.py shell
```
Далее необходимо импортировать скрипт в сам `shell`
```
import scripts
```
## Работа с электронным дневником
Поправим немного дневник `Фролова Ивана`.

Заменим все плохие оценки на пятёрки (5):
```
scripts.fix_marks('Фролов Иван')
```
В случае успеха скрипт сообщит вам:
```
Плохие оценки стали пятерками, проверьте пожалуйста это в журнале
```
У вас могут возникнуть ошибки, если допустите ошибки в написании фамилии или имени.

#### **Важно**: Порядок ввода данных должен быть `Фамилия Имя`, если вы его поменяете, то получите ошибку.
Теперь удалим все замечания:
```
scripts.remove_chastisements('Фролов Иван')
```
И последнее, создадим похвалу Ване на его недавнем уроке Литературы:
```
scripts.create_commendation('Фролов Иван', 'Литература')
```
Если всё сделано правильно, то консоль выведет на экран:
```
Появилась похвала к последнему уроку Литература, проверьте пожалуйста это в журнале
```
Если же похвала к последнему уроку Литературы есть, то скрипт сообщит нам:
```
Похвала от учителя уже есть к последнему уроку Литература, будьте аккуратнее
```
#### **Важно**: Все названия предметов пишем с Большой буквы (Музыка, Русский язык и т.д.)
Если вы допустили ошибку в названии предмета скрипт также вам сообщит об этом:
```
Ошибка в названии предмета
```
