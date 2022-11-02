# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

import emoji
import calendar
a = int(input('Напишите год: '))
b = int(input('Напишите цифру месяца: ')) 
calendar.TextCalendar().prmonth(a, b)
print(emoji.emojize('Введите цифру дня недели:calendar:'))
a = int (input())
if a > 7 or a < 1:
    print(emoji.emojize('Некорректный ввод:cross_mark:'))
elif a == 6 or a == 7:
    print(emoji.emojize('Отдыхай!:wolf:'))
else:
    print(emoji.emojize('Работай!:anxious_face_with_sweat:'))
print(emoji.emojize('Python is :thumbs_up:'))

