import urllib

msg_primeiro_ame = """
    Secretaria Municipal de Saúde de Bragança Paulista-SP\n                                            
Informamos que *%s* tem um Exame/Consulta de *%s* no dia *%s* às *%s* agendado no *AME em Atibaia*.
Favor confirmar a presença ou ausência *48 horas antes do agendamento*. Favor chegar com *30 minutos de antecedência*.
E se já está com a guia do agendamento(se acaso não estiver, é só retirar no posto de saúde)
Muito Obrigado.\n
'A sua presença é muito importante para o tratamento da sua patologia e também para diminuir o absenteísmo (falta) no serviço que o SUS oferta.'
"""

msg_aviso_ame = """
    A Secretaria Municipal de Saúde de Bragança Paulista\n
*%s* lembramos que no dia *%s* tem um agendamento no *AME Atibaia*.\n
Por gentileza não se esquecer de levar: o encaminhamento; pedido médico, RG, comprovante de residência, cartão SUS, exames (se tiver) e seguir as orientações dadas pelos profissionais do AME. 
Caso necessário cancelamento, avisar com 48 horas de antecedência.\n
“A sua presença é muito importante para o tratamento da sua patologia e também para diminuir o absenteísmo (falta) no serviço que o SUS oferta".
        """

msg_amb = """
            Secretaria Municipal de Saúde de Bragança Paulista- SP\n
Informamos que *%s* tem uma CONSULTA em *%s* no dia *%s* às *%s* agendado no *Ambulatório de Especialidades*. 
Favor confirmar a presença ou ausência 48 horas antes do agendamento. E se já está com a guia do agendamento.\n

“A sua presença é muito importante para o tratamento da sua patologia e também para diminuir o absenteísmo (falta) no serviço que o SUS oferta".
        """

msg_cancelamento = """
    Secretaria Municipal de Saúde de Bragança Paulista - SP
*%s*,
Informamos que a sua *%s* em *%s* as *%s* foi cancelada. Por favor procurar sua unidade de saúde para remarcar.
"""
'''
nova_menssagem = """
    Texto,
    pula linha\n,
    *texto em negrito*,
    inserir variavel
    por exemplo:
    oi, %s.
"""
'''
def createMessage(messageData, tipo):
    nome = messageData[4]
    especialidade = messageData[2]
    dia = messageData[0]
    hora = messageData[1]
    if(tipo == "Primeiro contato - AME"):
        msg = msg_primeiro_ame  %(nome, especialidade, dia, hora)
    elif tipo == "Aviso - AME":
        msg = msg_aviso_ame  %(nome, dia)
    elif tipo=="Cancelamento":
        msg = msg_cancelamento %(nome, especialidade, dia, hora)
    #elif tipo == "nova menssagem":
    #   msg = nova_menssagem %(nome)
    else:
        msg = msg_amb  %(nome, especialidade, dia, hora)
    msg = urllib.parse.quote(msg)
    return msg

"""class createMessages:
    def _init__(self, messageData, tipo):
        self.messageData = messageData
        self.tipo = tipo
    
    def createMsg():
    if(self.tipo == "Primeiro contato - AME"):
        return 
    elif self.tipo == "Aviso - AME":
        pass
    else:
        pass
"""