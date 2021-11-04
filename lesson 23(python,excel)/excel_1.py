####
import win32com.client

# создаем объект для работы с excel
xlapp = win32com.client.DispatchEx('Excel.Application')
# открываем файл
path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
wb = xlapp.Workbooks.Open(path)

# открываем нужную страницу
wb.Worksheets('data_1')
# скрываем выпадающие сообщения
xlapp.DisplayAlerts = False
# обновляем всю книгу
wb.RefreshAll()
# сообщаем ,что нужно дождаться выполнения обновления
xlapp.CalculateUntilAsyncQueriesDone()
# сохраняем файл
wb.Save()
# говорим что нужно выходить
xlapp.Quit()
# если объект висит в памяти, убиваем процесс
del xlapp
print('end')
## ОБНОВЛЕНИЕ КНИГИ + ПРОВЕРКА НА РЕДАКТИРОВАНИЕ
import win32com.client
import time
# Тут методы для wb. К примеру RefreshAll
# https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.workbook?view=excel-pia

while True:
    # создаем объект для работы с excel
    xlapp = win32com.client.DispatchEx('Excel.Application')
    # сообщаем ,что нужно дождаться выполнения обновления
    xlapp.CalculateUntilAsyncQueriesDone()
    # открываем файл
    path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
    wb = xlapp.Workbooks.Open(path)
    # скрываем выпадающие сообщения
    xlapp.DisplayAlerts = False
    if wb.ReadOnly:
        # говорим что нужно выходить
        xlapp.Quit()
        # если объект висит в памяти, убиваем процесс
        del xlapp
        print('занят')
    else:
        # открываем нужную страницу
        wb.Worksheets('data_1')
        # обновляем всю книгу
        wb.RefreshAll()
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # сохраняем файл
        wb.Save()
        # говорим что нужно выходить
        xlapp.Quit()
        # если объект висит в памяти, убиваем процесс
        del xlapp
        print('good')
        break
    time.sleep(5)

## ВЫЧИСЛЕНИЕ ФОРМУЛ, КОТОРЫЕ НЕ ВЫЧИСЛЯЮТСЯ АВТОМАТИЧЕСКИ
import win32com.client
import time
# Тут методы для xlapp. К примеру CalculateFull()
# https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel._application?view=excel-pia

while True:
    # создаем объект для работы с excel
    xlapp = win32com.client.DispatchEx('Excel.Application')
    # сообщаем ,что нужно дождаться выполнения обновления
    xlapp.CalculateUntilAsyncQueriesDone()
    # открываем файл
    path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
    wb = xlapp.Workbooks.Open(path)
    # скрываем выпадающие сообщения
    xlapp.DisplayAlerts = False
    if wb.ReadOnly:
        # говорим что нужно выходить
        xlapp.Quit()
        # если объект висит в памяти, убиваем процесс
        del xlapp
        print('занят')
    else:
        # обновляем всю книгу
        xlapp.CalculateFull()
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # сохраняем файл
        wb.Save()
        # говорим что нужно выходить
        xlapp.Quit()
        # если объект висит в памяти, убиваем процесс
        del xlapp
        print('good')
        break
    time.sleep(5)

##ВЗАИМОДЕЙСТВИЕ МЕЖДУ ЯЧЕКАМИ
import win32com.client
import time

#Тут методы для ws. К примеру CalculateFull()
# https://docs.microsoft.com/ru-ru/office/vba/api/excel.worksheet
try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
        wb = xlapp.Workbooks.Open(path)
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:
            # открываем нужную страницу и называем её ws
            ws = wb.Worksheets('data_1')

            # получение знаячения ячейки
            print(ws.Range("A1").Value)

            # получение кол-ва строк
            j = 0
            for i in ws.Range("A:A"):
                if str(i) == '' or str(i) == 'None':
                    print(i)
                    break
                else:
                    j += 1
                    print(i)
            print('кол-ва строк', j)

            # копируем в ней все из столбца E:E в F:F
            ws.Range("A1:E10").Copy(ws.Range("F:F"))

            # сообщаем ,что нужно дождаться выполнения обновления
            xlapp.CalculateUntilAsyncQueriesDone()
            # сохраняем файл
            wb.Save()
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('good')
            break

        time.sleep(5)
except:
    xlapp.Quit()
    del xlapp

## ДОБАВЛЕНИЕ НОВОГО ЛИСТА + НАПОЛНЕНИЕ ДАННЫМИ + try (иссключение)
# https://vremya-ne-zhdet.ru/vba-excel/rabochiy-list-sozdaniye-kopirovaniye-udaleniye/
import pandas as pd
import win32com.client

pd.set_option('display.max_columns', None)
df = pd.read_csv('C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/CSV/tss.csv', usecols=[i for i in range(1, 25)], nrows=5)
print(df)

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
        wb = xlapp.Workbooks.Open(path)
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:

            # создаем нужную страницу и называем её
            wb.Sheets.Add().Name = "data_2"

            # довавляем значения на страницу
            wb.Sheets("data_2").Cells(1, 1).Value = 'номер'
            wb.Sheets("data_2").Cells(1, 2).Value = 'номер заявки/CTN контакта'
            wb.Sheets("data_2").Cells(1, 3).Value = 'формула'
            # wb.Sheets("data_1").Cells(1,7).Value = 'Test'

            # пробегаемся по первым столбцам DF и копируем их на лист data_2
            for index, row in df.iterrows():
                print(index, row['номер'], row['номер заявки/CTN контакта'])
                wb.Sheets("data_2").Cells(index + 2, 1).Value = str(row['номер'])
                wb.Sheets("data_2").Cells(index + 2, 2).Value = str(row['номер заявки/CTN контакта'])
                wb.Sheets("data_2").Cells(index + 2, 3).Formula = f'=A{index + 2}+B{index + 2}'

            # сообщаем ,что нужно дождаться выполнения обновления
            xlapp.CalculateUntilAsyncQueriesDone()
            # сохраняем файл
            wb.Save()
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('good')
            break

        time.sleep(5)
except Exception as ex:
    print('bad', ex)
    xlapp.Quit()
    del xlapp

## ОФОРЛМЕНИЕ ЯЧЕЕК
# https://vremya-ne-zhdet.ru/vba-excel/tsvet-teksta-shrifta-v-yacheyke/
# https://vremya-ne-zhdet.ru/vba-excel/tsvet-yacheyki-zalivka-fon/
# https://webdelphi-ru.turbopages.org/webdelphi.ru/s/2009/09/excel-v-delphi-kak-izmenit-vneshnij-vid-yacheek/
import win32com.client

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
        wb = xlapp.Workbooks.Open(path)
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:
            # меняем цвет фона
            wb.Sheets("data_2").Range("A1:C1").Interior.ColorIndex = 1
            # меняем цвет шрифта
            wb.Sheets("data_2").Range("A1:C1").Font.ColorIndex = 2
            # делаеам автоширину для всех полей под текст
            wb.Sheets("data_2").Columns.AutoFit()

            # делаем внутренюю сетку
            wb.Sheets("data_2").Range("A1:C6").Borders.LineStyle = True
            # делаем жирное обрамление (4) по краям (7 - левый край,10 - правый край, 8 - верх, 9 - низ)
            wb.Sheets("data_2").Range("A1:C6").Borders(7).Weight = 4
            wb.Sheets("data_2").Range("A1:C6").Borders(8).Weight = 4
            wb.Sheets("data_2").Range("A1:C6").Borders(9).Weight = 4
            wb.Sheets("data_2").Range("A1:C6").Borders(10).Weight = 4

            # сообщаем ,что нужно дождаться выполнения обновления
            xlapp.CalculateUntilAsyncQueriesDone()
            # сохраняем файл
            wb.Save()
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('good')
            break

        time.sleep(5)
except Exception as ex:
    print('bad', ex)
    xlapp.Quit()
    del xlapp

