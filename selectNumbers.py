import xlrd
import re
import sendMessage
#RegEx
padrao = '(((\()\d{2}(\))\s?)?(\d{4,5}\-?\d{4}))'
padraoHorario = '((\d{1,2}:\d{1,2}))'
padraoData = '((\d{1,2}\/\d{1,2}\/\d{1,4}))'
'''
    ['nome_paciente','prestador', 'procedimento','data','horario(-30min)',[numero1, numero2]]
'''

import datetime


def selectMessageDataAmb(arquivo):
    book = xlrd.open_workbook(arquivo)
    sh = book.sheet_by_index(0)
    
    numbers = []
    for rx in range(sh.nrows):
        if sh.cell_value(rowx=rx,colx=0) == '':
            num = str(sh.row_values(rx)[6])
            datahora = str(sh.row_values(rx)[0])
            res = re.findall(padrao,num)
            data = re.findall(padraoData, datahora)
            hora = re.findall(padraoHorario, datahora)
            for r in res:
                numbers.append([
                    data[0][0],
                    hora[0][0],
                    numbers[len(numbers)-1][2],
                    numbers[len(numbers)-1][3],
                    numbers[len(numbers)-1][4],
                    r[0][0]
                ])
        else:
            num = str(sh.row_values(rx)[6])
            res = re.findall(padrao,num)
            datahora = str(sh.row_values(rx)[0])
            data = re.findall(padraoData, datahora)
            hora = re.findall(padraoHorario, datahora)
            dataa = datetime.datetime.strptime(data[0][0],"%d/%M/%Y")
            print("data",dataa)
            for r in res:
                numbers.append([
                data[0][0],#data [0]
                hora[0][0],#hora [1]
                str(sh.row_values(rx)[2]),#especialidade [2]
                int(sh.row_values(rx)[3]),#codigo? [3]
                str(sh.row_values(rx)[4]),#paciente [4]
                r[0]#numero [5]
                ])


    return numbers


def CancelamentoDaAgenda(arquivo):
    book = xlrd.open_workbook(arquivo)
    sh = book.sheet_by_index(0)
    
    numbers = []
    for rx in range(sh.nrows):
        if sh.cell_value(rowx=rx,colx=0) == '':
            num = str(sh.row_values(rx)[21])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                    numbers[len(numbers)-1][6],
                    numbers[len(numbers)-1][7],
                    numbers[len(numbers)-1][3],
                    numbers[len(numbers)-1][0],
                    numbers[len(numbers)-1][10],
                    r[0][0]
                ])
        else:
            num = str(sh.row_values(rx)[21])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                str(sh.row_values(rx)[6]),#data [6]
                float(sh.row_values(rx)[7]),#hora [7]
                str(sh.row_values(rx)[3]),#especialidade [3]
                int(sh.row_values(rx)[0]),#codigo? [0]
                str(sh.row_values(rx)[10]),#paciente [10]
                r[0]#numero []
                ])


    return numbers

def selectMessageData(arquivo):
    book = xlrd.open_workbook(arquivo)
    sh = book.sheet_by_index(0)
    
    numbers = []
    for rx in range(sh.nrows):
        if sh.cell_value(rowx=rx,colx=0) == '':
            num = str(sh.row_values(rx)[6])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                    numbers[len(numbers)-1][0],
                    numbers[len(numbers)-1][1],
                    numbers[len(numbers)-1][2],
                    numbers[len(numbers)-1][3],
                    numbers[len(numbers)-1][4],
                    r[0][0]
                ])
        else:
            num = str(sh.row_values(rx)[6])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                int(sh.row_values(rx)[0]),#data [0]
                float(sh.row_values(rx)[1]),#hora [1]
                str(sh.row_values(rx)[2]),#especialidade [2]
                int(sh.row_values(rx)[3]),#codigo? [3]
                str(sh.row_values(rx)[4]),#paciente [4]
                r[0]#numero [5]
                ])


    return numbers

#Preciso da planilha para conferir o formato dos numeros
def formatNumbers(messegeData):
    messegeDataFormat = []
    for data in messegeData:
        number = data[5]
        number = number.replace('(','')
        number = number.replace(')','')
        number = number.replace('-','')
        number = number.replace('\xa0','')
        number = number.replace(" ","")
        number = number.replace("/","")
        if len(number) == 9:
            number = "11%s" %number
        number = "55%s" % number
        if messegeDataFormat != []:
            if number == messegeDataFormat[len(messegeDataFormat)-1][5]:
                continue
        if len(number) == 13:
            data[5] = number
            try:
                data[0] = datetime.datetime.fromordinal(datetime.date(1900,1,1).toordinal()+data[0]-2).strftime('%d/%m/%Y')
                data[1] = xlrd.xldate_as_datetime(data[1],0).strftime("%H:%M")
            except:
                data[1] = xlrd.xldate_as_datetime(data[1],0).strftime("%H:%M")
            messegeDataFormat.append(data)
        else:
            sendMessage.listarNumerosComErro(number, data[4])
    return messegeDataFormat
'''
def selectMessageData(arquivo):
    book = xlrd.open_workbook(arquivo)
    sh = book.sheet_by_index(0)
    
    numbers = []
    for rx in range(sh.nrows):
        if sh.cell_value(rowx=rx,colx=0) == '':
            num = str(sh.row_values(rx)[posicao_da_coluna_referente_ao_numero_de_telefone])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                    numbers[len(numbers)-1][0],
                    numbers[len(numbers)-1][1],
                    numbers[len(numbers)-1][2],
                    numbers[len(numbers)-1][3],
                    numbers[len(numbers)-1][4],
                    r[0][0]
                ])
        else:
            num = str(sh.row_values(rx)[posicao_da_coluna_referente_ao_numero_de_telefone])
            res = re.findall(padrao,num)
            for r in res:
                numbers.append([
                int(sh.row_values(rx)[0]),#data [0]
                float(sh.row_values(rx)[1]),#hora [1]
                str(sh.row_values(rx)[2]),#especialidade [2]
                int(sh.row_values(rx)[3]),#codigo? [3]
                str(sh.row_values(rx)[4]),#paciente [4]
                r[0]#numero [5]
                ])


    return numbers'''