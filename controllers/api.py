# -*- coding: utf-8 -*-
from _clasFunt import DataGlobal, ConexionWhast
import time
dict_d = ""

@request.restful()
def companyCreate():

    def POST(*args,**vars):
        data = request.vars
        # logsMostrar( 'info', data)
        if data.empresa != '':
            idCompany = createCompany( data.empresa )
            if idCompany > 0:
                if data.cliente != '':
                    idCustomers  = createCustomers( idCompany, data.cliente, data.id_cliente )
                    if idCustomers > 0:
                        if data.segmento != '':
                            idSegment = createSegment( idCustomers, data.segmento, data.id_segmento, idCompany )
                            if idSegment > 0:
                                usariosCreate = createUsersApi( idCompany, idCustomers, idSegment, data.empresa )
                                if usariosCreate:
                                    varGl     = DataGlobal()
                                    sms = 'rTime.newCompanyInfo('+str(idCompany)+',"'+str(data.empresa).capitalize()+'","'+str(fechaFormato(varGl.fechaIntModels,'fecha'))+'","'+str(fechaFormato(varGl.horaIntModels,'hora'))+'");'
                                    #enviarSmsRT( 'admin_chatbot', sms )
                                    sResul = dict(resultado = 'success', sms = 'Empresa: '+str(data.empresa).capitalize()+' creada con exito. Cliente: '+str(data.cliente).capitalize()+'  creado con exito. Segmento: '+str(data.segmento).capitalize()+'  creado con exito. Usuarios creados: '+str(usariosCreate)+'.')
                                else:
                                    sResul = dict(resultado = 'error', sms = 'No se puede crear usuarios ocurrio un error en el proceso.')
                                    pass
                            else:
                                sResul = dict(resultado = 'error', sms = 'No se puede crear segmento ocurrio un error en el proceso.')
                                pass
                        else:
                            sResul = dict(resultado = 'error', sms = 'No se puede crear segmento por que faltan parametros. Parametro: segmento.')
                            pass
                    else:
                        sResul = dict(resultado = 'error', sms = 'No se puede crear cliente ocurrio un error en el proceso.')
                        pass
                else:
                    sResul = dict(resultado = 'error', sms = 'No se puede crear cliente por que faltan parametros. Parametro: cliente.')
                    pass
            else:
                sResul = dict(resultado = 'error', sms = 'No se puede crear empresa ocurrio un error en el proceso.')
                pass
        else:
            sResul = dict(resultado = 'error', sms = 'No se puede crear empresa por que faltan parametros. Parametro: empresa.')
            pass
        return sResul

    return locals()



@request.restful()
def seachUsersAdv():
    def GET(*args,**vars):
        data = request.vars
        logsMostrar( 'info', 'seachUsersAdv => '+str(data)+'')
        if ( ( data.empresa != '' )  & ( data.cliente != '' ) & ( data.segmento != '' ) & ( data.identificacion != '' ) & ( data.telefono != '' ) ):
            logsMostrar('info','Todo esta marchando bajo ruedas')
            asesor   =  consultingClAdvCov ( data.telefono, data.identificacion, data.empresa, data.cliente, data.segmento )
            sResul  = dict( resultado = 'Info', sms = 'Asesor: '+str(idAsigCli)+' ' )
        else:
            sResul  = dict( resultado = 'Error', sms = 'Faltan parametros para iniciar la ejecucion' )
            # logsMostrar('error','Faltan parametros para la ejecucion')
            pass
        return sResul

    return locals()

def convert(data):
    global dict_d
    dict_d = data

def envioSmsAlert( telefono, empresa, cliente, segmento ):
    time.sleep( 5 )
    # logsMostrar( 'info', 'envioSmsAlert API => 77 Esperando 5 segundos' )
    sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
    conexApiWhat    = ConexionWhast( sms, empresa, cliente, segmento, telefono )
    resulApi        = conexApiWhat.conexionSend()
    # logsMostrar( 'info', 'envioSmsAlert API => resulApi 81 '+str(resulApi)+'' )
    pass

@request.restful()
def sendSms():
    def POST(*args,**vars):
        try:
            data = request.vars
            # print('data => API 87', data)
            # logsMostrar( 'info', 'sendSms API => data 88 '+str(data)+'' )
            if data:
                if ( ( data.empresa != '' )  & ( data.cliente != '' )  & ( data.telefono != '' )  ):
                    logsMostrar( 'info', 'sendSms API => data.segmento 90 '+str(data.segmento)+'' )
                    if data.segmento == '':
                        # logsMostrar( 'error', 'sendSms API => data.segmento vaciooooooooooo 92')
                        sResul = sinSegmenoApi( data )
                    else:
                        # logsMostrar( 'error', 'sendSms API => data.segmento no vacioo 95')
                        horarioAtencion,smsHorario  = setAtencionHorario( data.empresa, data.cliente, data.segmento )
                        # logsMostrar( 'info', 'sendSms API => Informacion 98 '+str(horarioAtencion)+'' )
                        # # Pruebas horarios
                        # logsMostrar( 'info', 'sendSms API => Telefono 100 '+str(data.telefono)+'' )
                        if data.telefono == '573015237437dddddddd':
                            # logsMostrar( 'info', 'sendSms API => Telefono 103 INGRESO ACA' )
                            # sms = """Buen dia Gracias por comunicarte con nuestro chat de """+str(data.empresa).capitalize()+""". El horario de atencion es de lunes a sabado de 9:00 am a 6:00 pm por whatsapp. Escribenos en ese horario para resolver todas tus inquietudes 🕐🕐🕐 🤝🤝🤝🤝."""
                            # # envioSmsAlert( , , , data.segmento )
                            # conexApiWhat    = ConexionWhast( sms, data.empresa, data.cliente, data.segmento, data.telefono )
                            # resulApi        = conexApiWhat.conexionSend()
                            # logsMostrar( 'info', 'sendSms API => resulApi 107 '+str(resulApi)+'' )
                            # sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                            sResul = setApiPrueba( data.empresa, data.cliente, data.segmento )
                        else:
                            # horarioAtencion = True
                            if horarioAtencion:
                                aseDispone  = advisersOnLine( data.empresa, data.cliente, data.segmento )
                                # logsMostrar( 'error', 'sendSms API 116 => '+str(aseDispone)+'')
                                if  aseDispone > 0:
                                    # logsMostrar( 'error', 'sendSms API 97 => '+str(aseDispone)+'')
                                    if data.data:
                                        dat  = response.json(request.vars)
                                        dat  = json.loads(dat)
                                        exec ("convert("+dat['data']+")")
                                        global dict_d
                                        # Inicio de conversacion de cliente & asesor
                                        idClientePlf,idClientePlfHist          =  consultingInfoClTrue ( data.telefono, data.identificacion, data.empresa, data.cliente, data.segmento, dict_d )
                                        # logsMostrar( 'error', 'idClientePlf API  105 => '+str(idClientePlf)+'')
                                        # logsMostrar( 'error', 'idClientePlfHist API 106 => '+str(idClientePlfHist)+'')
                                        # print('idClientePlf API => 98', idClientePlf)
                                        if idClientePlf > 0:
                                            asesor,idAsigCli,idAsigCliHist     =  consultingClAdvCov ( data.telefono, data.identificacion, data.empresa, data.cliente, data.segmento, idClientePlf, idClientePlfHist)
                                            # print('idAsigCli => idAsigCliHist => asesor', idAsigCli,idAsigCliHist,asesor)
                                            # logsMostrar( 'info', 'sendSms API => asesor 108 '+str(asesor)+'' )
                                            if asesor > 0:
                                                idConversacion                 = recepcionSms( data.telefono, data.identificacion, data.empresa, data.cliente, data.segmento, 'Inicio de conversacion', 'cliente', 'asesor', data.tipo , asesor,idAsigCli,idAsigCliHist )
                                                # logsMostrar( 'info', 'sendSms API => idConversacion 114 '+str(idConversacion)+'' )
                                                if idConversacion > 0: 
                                                    sResul  = dict( resultado = 'Info', sms = 'Recibir sms para seguir con la conversacion cliente & asesor', status = 200, asesor = 1 )
                                                else:
                                                    sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                                                    # envioSmsAlert( data.telefono, data.empresa, data.cliente, data.segmento )
                                                    sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                                    pass
                                            else:
                                                sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                                                # envioSmsAlert( data.telefono, data.empresa, data.cliente, data.segmento )
                                                sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                                pass
                                        else:
                                            sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                                            envioSmsAlert( data.telefono, data.empresa, data.cliente, data.segmento )
                                            sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                            pass
                                    else:
                                        if  data.sms:
                                            # Sms de conversacion ya establecida
                                            idConversacion = recepcionSms( data.telefono, data.identificacion, data.empresa, data.cliente, data.segmento, data.sms, 'cliente', 'asesor', data.tipo, 0, 0, 0  )
                                            # logsMostrar( 'info', 'sendSms API => idConversacion 157 '+str(idConversacion)+'' )
                                            if idConversacion > 0: 
                                                sResul  = dict( resultado = 'Info', sms = 'Recibir sms para seguir con la conversacion cliente & asesor', status = 200, asesor = 1 )
                                            else:
                                                sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                                                if  data.sms != '':
                                                    sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                                else:
                                                    envioSmsAlert( data.telefono, data.empresa, data.cliente, data.segmento )
                                                    sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                                    pass
                                                pass
                                        else:
                                            sResul  = dict( resultado = 'Error', sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia', status = 200, asesor = 0 )
                                            pass
                                        pass
                                else:
                                    sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                                    envioSmsAlert( data.telefono, data.empresa, data.cliente, data.segmento )
                                    sResul  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                    pass
                            else:
                                #sms = """Buen dia Gracias por comunicarte con nuestro chat de """+str(data.empresa).capitalize()+""". El horario de atencion es de lunes a sabado de 9:00 am a 6:00 pm por whatsapp. Escribenos en ese horario para resolver todas tus inquietudes 🕐🕐🕐 🤝🤝🤝🤝."""
                                conexApiWhat    = ConexionWhast( smsHorario, data.empresa, data.cliente, data.segmento, data.telefono )
                                resulApi        = conexApiWhat.conexionSend()
                                sResul  = dict( resultado = 'Error', sms = smsHorario, status = 200, asesor = 0 )
                                pass
                            pass
                        pass
                else:
                    sResul  = dict( resultado = 'Error', sms = 'Faltan parametros como la empresa/cliente/segmento/telefono para iniciar la ejecucion', status = 404, asesor = 0 )
                    pass
            else:
                sResul  = dict( resultado = 'Error', sms = 'No enviasteis ningun parametro para el inicio de las validaciones', status = 404, asesor = 0)
                pass
        except Exception as e:
            logsMostrar( 'error', 'sendSms API => Error 192 '+str(e)+'' )
            sResul  = dict( resultado = 'Error', sms = e, status = 404, asesor = 0)
            pass
        logsMostrar( 'info', 'sendSms API => sResul 188 '+str(sResul)+'' )
        return sResul

    return locals()



def sinSegmenoApi( data ):
    resulSinSeg      = ''
    segmento         = consultingInfoSinSeg ( data.telefono, data.identificacion, data.empresa, data.cliente )
    # logsMostrar( 'info', 'sendSms API => Informacion 204 '+str(segmento)+'' )
    horarioAtencion,smsHorario = setAtencionHorario( data.empresa, data.cliente, segmento )
    # logsMostrar( 'info', 'sendSms API => Informacion 201 '+str(horarioAtencion)+'' )
    if data.telefono == '573015237437ddddddddd':
        resulSinSeg  = setApiPrueba( data.empresa, data.cliente, segmento ) 
    else:
        # horarioAtencion  = True
        if horarioAtencion:
            if segmento:
                
                # Cliente con conversa Activa y asesor en modo BackOfficce
                clienteEnConversa = setClienteInConversaAsesor( data.empresa, data.cliente, segmento, data.telefono, data.identificacion )
                # logsMostrar( 'info', 'sinSegmenoApi API => clienteEnConversa 215 '+str(clienteEnConversa)+'' )
                if  clienteEnConversa > 0:
                    if  data.sms:
                        # Sms de conversacion ya establecida
                        idConversacion = recepcionSms( data.telefono, data.identificacion, data.empresa, data.cliente, segmento, data.sms, 'cliente', 'asesor', data.tipo, 0, 0, 0  )
                        # logsMostrar( 'info', 'sinSegmenoApi API => idConversacion '+str(idConversacion)+'' )
                        if idConversacion > 0: 
                            resulSinSeg  = dict( resultado = 'Info', sms = 'Recibir sms para seguir con la conversacion cliente & asesor', status = 200, asesor = 1 )
                        else:
                            sms = 'Por favor escribe "*Menu Inicial*" para seguir interactuando con nuestro chatbot.'
                            # logsMostrar( 'info', 'sinSegmenoApi API => sms '+str(sms)+'' )
                            if  data.sms != '':
                                resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                            else:
                                envioSmsAlert( data.telefono, data.empresa, data.cliente, segmento )
                                resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                pass
                            pass
                    else:
                        resulSinSeg  = dict( resultado = 'Error', sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia', status = 200, asesor = 0 )
                        pass
                else:
                    if advisersOnLine( data.empresa, data.cliente, segmento ) > 0:
                        if  data.sms:
                            # Sms de conversacion ya establecida
                            idConversacion = recepcionSms( data.telefono, data.identificacion, data.empresa, data.cliente, segmento, data.sms, 'cliente', 'asesor', data.tipo, 0, 0, 0  )
                            # logsMostrar( 'info', 'sinSegmenoApi API => idConversacion '+str(idConversacion)+'' )
                            if idConversacion > 0: 
                                resulSinSeg  = dict( resultado = 'Info', sms = 'Recibir sms para seguir con la conversacion cliente & asesor', status = 200, asesor = 1 )
                            else:
                                sms = 'Por favor escribe "*Menu Inicial*" para seguir interactuando con nuestro chatbot.'
                                # logsMostrar( 'info', 'sinSegmenoApi API => sms '+str(sms)+'' )
                                if  data.sms != '':
                                    resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                else:
                                    envioSmsAlert( data.telefono, data.empresa, data.cliente, segmento )
                                    resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                                    pass
                                pass
                        else:
                            resulSinSeg  = dict( resultado = 'Error', sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia', status = 200, asesor = 0 )
                            pass
                    else:
                        sms = 'En el momento no hay asesores disponibles, por favor comunicate mas tarde o escribe "*Menu Inicial*" para seguir interactuando con nuestro Chatbot.\n\nMuchas gracias por interactuar con nosotros, te deseamos que tengas un feliz dia'
                        # envioSmsAlert( data.telefono, data.empresa, data.cliente, segmento )
                        resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                        pass
                    pass
            else:
                sms = 'Por favor escribe "*Menu Inicial*" para seguir interactuando con nuestro chatbot.'
                resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
                pass
        else:
            #sms = """Buen dia\nGracias por comunicarte con nuestro chat de """+str(data.empresa).capitalize()+""".\nEl horario de atencion es de lunes a sabado de 9:00 am a 6:00 pm por whatsapp.\nEscribenos en ese horario para resolver todas tus inquietudes 🕐🕐🕐 🤝🤝🤝🤝."""
            # conexApiWhat    = ConexionWhast( sms, data.empresa, data.cliente, segmento, data.telefono )
            # resulApi        = conexApiWhat.conexionSend()
            resulSinSeg  = dict( resultado = 'Error', sms = smsHorario, status = 200, asesor = 0 )
            pass
        pass
    return resulSinSeg



def setApiPrueba( empresa, cliente, segmento ):
    horarioAtencion  = setAtencionHorario( empresa, cliente, segmento )
    logsMostrar( 'info', 'setApiPrueba API => horarioAtencion 249 '+str(horarioAtencion)+'' )
    sms = """Buen dia\nGracias por comunicarte con nuestro chat de """+str(empresa).capitalize()+""".\nEl horario de atencion es de lunes a sabado de 9:00 am a 6:00 pm por whatsapp.\nEscribenos en ese horario para resolver todas tus inquietudes 🕐🕐🕐 🤝🤝🤝🤝."""
    resulSinSeg  = dict( resultado = 'Error', sms = sms, status = 200, asesor = 0 )
    return resulSinSeg


@request.restful()
def listTemplatesCompany():
    def GET(*args,**vars):
        data = request.vars
        if ( ( data.empresa != '' )  & ( data.cliente != '' )  & ( data.segmento != '' )  ):
            data = lisTemplatesLast( data.empresa, data.cliente, data.segmento )
            if len(data) > 0:
                sResul  = { "status": "success" ,"sms": "Empresa - Cliente - Segmento con informacion", "data": data}
            else:
                sResul  = { "status": "warning" ,"sms": "Empresa - Cliente - Segmento sin informacion", "data": []}
                pass
        else:
            sResul  = { "status": "error" ,"sms": "Faltaran parametro de recepcion", "data": []}
            pass
        return sResul
    return locals()




@request.restful()
def idTemplatesInsertCompany():
    def POST(*args,**vars):
        data = request.vars
        if ( ( data.empresa != '' )  & ( data.cliente != '' )  & ( data.segmento != '' ) & ( data.idTemplate != '' ) ):
            data = idTemplatesInsert( data.empresa, data.cliente, data.segmento , data.idTemplate)
            if data > 0:
                sResul  = { "status": "success" ,"sms": "Empresa - Cliente - Segmento - idTemplate agregado/actualizado correctamente"}
            else:
                sResul  = { "status": "warning" ,"sms": "Empresa - Cliente - Segmento sin informacion", "data": []}
                pass
        else:
            sResul  = { "status": "error" ,"sms": "Faltaran parametro de recepcion", "data": []}
            pass
        return sResul
    return locals()