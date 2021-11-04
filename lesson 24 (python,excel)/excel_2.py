## СОЗДАНИЕ ТАБЛИЦЫ И ФИЛЬТРАЦИЯ
#  xlSrcRange в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xllistobjectsourcetype?view=excel-pia)
#  xlNo в методе ListObjects.Add, искать в api (пример https://docs.microsoft.com/ru-ru/dotnet/api/microsoft.office.interop.excel.xlyesnoguess?view=excel-pia#Microsoft_Office_Interop_Excel_XlYesNoGuess_xlNo)
# https://vremya-ne-zhdet.ru/vba-excel/sozdaniye-tablitsy/
import win32com.client
import time
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
import time
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
import time
try:
    while True:
        # создаем объект для работы с excel
        xlapp = win32com.client.DispatchEx('Excel.Application')
        # сообщаем ,что нужно дождаться выполнения обновления
        xlapp.CalculateUntilAsyncQueriesDone()
        # открываем файл
        path = 'C:/Users/3com/PycharmProjects/data_engineer_training/lesson 23(python,excel)/EXCEL/test.xlsx'
        wb = xlapp.Workbooks.Open(path)
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