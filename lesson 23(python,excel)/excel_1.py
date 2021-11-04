##
import win32com.client

# создаем объект для работы с excel
xlapp = win32com.client.DispatchEx('Excel.Application')
# открываем файл
wb = xlapp.Workbooks.Open('/Users/dgribanov/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx')

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
    wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
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
    wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
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
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
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
df = pd.read_csv('CSV/tss.csv', usecols=[i for i in range(1, 25)], nrows=5)
display(df)

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
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
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
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

## СОЗДАНИЕ ТАБЛИЦЫ И ФИЛЬТРАЦИЯ
#  xlSrcRange в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xllistobjectsourcetype?view=excel-pia)
#  xlNo в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xlyesnoguess?view=excel-pia#Microsoft_Office_Interop_Excel_XlYesNoGuess_xlNo)
# https://vremya-ne-zhdet.ru/vba-excel/sozdaniye-tablitsy/
import win32com.client

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:
            # создаем объект с полями (для удобства)
            range_ws = wb.Sheets("data_2").Range("A1:C6")
            # создаем пользовательскую таблицу
            wb.Sheets("data_2").ListObjects.Add(1, range_ws, 2).Name = "Таблица_1"
            # фильтруем интереусующие значения во втром поле
            wb.Sheets("data_2").ListObjects('Таблица_1').Range.AutoFilter(Field=2,Criteria1='nan')
            # сбрасываем фильтр
            #wb.Sheets("data_2").ListObjects('Таблица_1').Range.AutoFilter(Field=2)



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
    print('bad',ex)
    xlapp.Quit()
    del xlapp

## ВЗАИМОДЕЙСТВИЕ С ЯЧЕЙКАМИ ЧЕРЕЗ ЦИКЛ
#  xlSrcRange в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xllistobjectsourcetype?view=excel-pia)
#  xlNo в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xlyesnoguess?view=excel-pia#Microsoft_Office_Interop_Excel_XlYesNoGuess_xlNo)
# https://vremya-ne-zhdet.ru/vba-excel/sozdaniye-tablitsy/
import win32com.client

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:
            # удаляем nan
            # цикл по ячекам стобца B
            for i in wb.Sheets("data_2").Range("B:B"):
                if str(i) == '' or str(i) == 'None':
                    break
                elif str(i) == 'nan':
                    wb.Sheets("data_2").Cells(index, 2).Value = ''

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
except Exception as ex:
    print('bad', ex)
    xlapp.Quit()
    del xlapp

## СВОДНАЯ ТАБЛИЦА
# https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.core.xlpivotfieldorientation?view=office-pia
# https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xlconsolidationfunction?view=excel-pia
# https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xlpivotfieldorientation?view=excel-pia#Microsoft_Office_Interop_Excel_XlPivotFieldOrientation_xlDataField
# https://docs.microsoft.com/ru-ru/office/vba/api/excel.pivottable.columnfields
import win32com.client

try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        wb = xlapp.Workbooks.Open('C:/Users/3com/Desktop/Учеба/WorkTraining/EXCEL/test.xlsx')
        # объект моей книги
        ws = wb.Worksheets('data_1')
        # скрываем выпадающие сообщения
        xlapp.DisplayAlerts = False
        if wb.ReadOnly:
            # говорим что нужно выходить
            xlapp.Quit()
            # если объект висит в памяти, убиваем процесс
            del xlapp
            print('занят')
        else:

            # создаем кэш таблицы Указываем тип (1.1 - означает что внутри этой книги), и источник данных
            PTCache = wb.PivotCaches().Create(SourceType=1.1, SourceData='data_1!A1:C11')
            # создаем саму свод. таблицу Указываем где будет таблица, и её название
            PT = PTCache.CreatePivotTable(TableDestination="data_1!R2C11", TableName="Сводная таблица")

            # указываем, что поле idtest, будет строкой и первым
            PT.PivotFields("idtest").Orientation = 1  # xlRowField
            PT.PivotFields("idtest").Position = 1

            # указываем, что поле text_test, будет колонкой и первым
            PT.PivotFields("text_test").Orientation = 2  # xlColumnField
            PT.PivotFields("text_test").Position = 1

            # в качестве данных date_test. !!! Когда мы его туда помещаем , название поля меняется (узнаем по 'str(PT.DataFields.Item(1))')
            PT.PivotFields("date_test").Orientation = 4  # xlDataField
            print(str(PT.DataFields.Item(1)))
            PT.PivotFields(str(PT.DataFields.Item(1))).Function = -4112  # xlCount

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
except Exception as ex:
    print('bad', ex)
    xlapp.Quit()
    del xlapp