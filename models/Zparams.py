# -*- coding: utf-8 -*-

from empresas import Clientes
import re

def logsMostrar( tipo, sms ):
    from _clasFunt import InfoLogs
    logs = InfoLogs( tipo, sms )
    logs.logFile()
    pass


def enviarSmsRT( people, sms ):
    from _clasFunt import RtTonadoWeb
    envRt = RtTonadoWeb( people, sms )
    envRt.rtInfo()
    pass

def conexionBDS( db, host, user, key ):
    from sqlalchemy import create_engine
    engineConexion  = 0
    try:
        engineConexion  = create_engine(
            "mysql+pymysql://"+str(user)+":"+str(key)+"@"+str(host)+"/"+str(db)+""
        )
    except Exception as e:
        logsMostrar( 'info', 'conexionBDS  Error=> '+str(e)+' ' )
        raise e
    return engineConexion


def rederHtmlPrincipal():
    from _clasFunt import PlantillaUser
    plaReder = PlantillaUser( userType[0] )
    plaReder.rederPalntilla()
    return plaReder.rederPalntilla()



def infoSegClienteEmpresa( param, opc ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    data    = {}
    if opc == 'segment':
        segment.idSegmento  = param
        segmentInfo = segment.getListarIdSegmento()
        if segmentInfo:
            customers.idCliente = segmentInfo.cliente_segmento
            company.idEmpresa   = segmentInfo.empresa_segmento
            companyInfo         = company.getListarIdEmpresa()
            customersInfo       = customers.getListarIdCliente()
            if customersInfo:
                if companyInfo:
                    data = dict(
                        company   = companyInfo.nombre_empresa,
                        customers = customersInfo.nombre_cliente,
                        segment   = segmentInfo.nombre_segmento
                    )
                    pass
                pass
            pass
        pass
    return data


def empresaIdConsulting( idCompany ):
    from empresas import Empresas
    company               = Empresas( db )
    company.idEmpresa     = idCompany
    company.define_table()
    infoCompany           = company.getListarIdEmpresa()
    if infoCompany:
        nombreEmpresa  = infoCompany.nombre_empresa
    else:
        nombreEmpresa  = 0
        pass
    return nombreEmpresa


def clienteIdConsulting( idCustomers):
    from empresas import Clientes
    customers               = Clientes( db )
    customers.idCliente     = idCustomers
    customers.define_table()
    infocustomers           = customers.getListarIdCliente()
    if infocustomers:
        nombreCliente       = infocustomers.nombre_cliente
    else:
        nombreCliente  = 0
        pass
    return nombreCliente


def segmentoIdConsulting( idSegment ):
    from empresas import Segmentos
    segment                 = Segmentos( db )
    segment.idSegmnento     = idSegment
    segment.define_table()
    infoSegment           = segment.getListarIdSegmento()
    if infoSegment:
        nombreSegmento  = infoSegment.nombre_segmento
    else:
        nombreSegmento  = 0
        pass
    return nombreSegmento

def empresaConsulting( nombreCompany ):
    from empresas import Empresas
    company               = Empresas( db )
    company.nomEmpresa    = nombreCompany
    company.define_table()
    infoCompany           = company.getListarNomEmpresa()
    if infoCompany:
        idEmpresa  = infoCompany.id
    else:
        idEmpresa  = 0
        pass
    # logsMostrar('info', 'idEmpresa: '+str(idEmpresa)+' ' )
    return idEmpresa


def empresaConsultingConexion( idEmpresa ):
    from empresas import Empresas
    company               = Empresas( db )
    company.idEmpresa     = idEmpresa
    company.define_table()
    infoResul             = []
    infoCompany           = company.getListarIdEmpresa()
    if infoCompany:
        infoResul.append(
            dict(
                empresas_base_usuario  = infoCompany.empresas_base_usuario,
                empresas_base_key      = infoCompany.empresas_base_key,
                empresas_base          = infoCompany.empresas_base,
                empresas_base_dominio  = infoCompany.empresas_base_dominio
            )
        )
        pass
    return infoResul


def clienteConsulting( customersCliente, idCompany ):
    from empresas import Clientes
    customers              = Clientes( db )
    customers.idEmpresa    = idCompany
    customers.nomCliente   = customersCliente
    customers.define_table()
    infoCustomers          = customers.getListarIdEmpresaCliente()
    if infoCustomers:
        idCliente  = infoCustomers.id
    else:
        idCliente  = 0
        pass
    # logsMostrar('info', 'idCliente: '+str(idCliente)+' ' )
    return idCliente


def segmentoConsulting( segmentCliente, idCustomers ):
    from empresas import Segmentos
    segment              = Segmentos( db )
    segment.idCliente    = idCustomers
    segment.nomSegmento  = segmentCliente
    segment.define_table()
    infosegment          = segment.getListarIdClienteSegmento()
    if infosegment:
        idSegmento  = infosegment.id
    else:
        idSegmento  = 0
        pass
    # logsMostrar('info', 'idSegmento: '+str(idSegmento)+' ' )
    return idSegmento


def getNomFormu( idForm ):
    from empresas import Empresas, Clientes, Segmentos
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario   = idForm
    nombreForm             = ''
    infoForm               = segment.setInfoFormulario()
    if infoForm:
        nombreForm         = infoForm.nombre_formulario
        pass 
    return nombreForm


def setTypeForm( idForm ):
    from empresas import Empresas, Clientes, Segmentos
    from _clasFunt import DataGlobal
    varData            = DataGlobal()
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    segment.define_table()
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario   = idForm
    typeFormPDP            = False
    infoForm               = segment.setInfoFormulario()
    logsMostrar( 'info', 'infoForm setTypeForm 181 => '+str(infoForm)+' ' )
    if infoForm:
        logsMostrar( 'info', 'infoForm.nombre_formulario setTypeForm 183 => '+str(infoForm.nombre_formulario)+' ' )
        logsMostrar( 'info', 'infoForm.creador setTypeForm 183 => '+str(infoForm.creador)+' ' )
        if ( ( infoForm.nombre_formulario == varData.formAcuerdos ) & ( infoForm.creador == varData.estadoFalsNum ) ):
            typeFormPDP         = True
            pass
        pass 
    return typeFormPDP

def fechaFormato(valor,opc):
    hora  = '00'
    minu  = '00'
    segun = '00'
    if opc == 'fecha':
        anio = str(valor)[:4]
        mes  = str(valor)[4:-2]
        dia  = str(valor)[6:]
        formato = anio+'-'+str(mes)+'-'+str(dia)
    else:
        if len(str(valor)) == 5:
            hora  = str(valor)[:1]
            minu  = str(valor)[1:3]
            segun = str(valor)[3:]
        elif len(str(valor)) == 6:
            hora  = str(valor)[:2]
            minu  = str(valor)[2:4]
            segun = str(valor)[4:]
            pass
        if hora == '24':
            hora = hora.replace('24','00')
            pass
        formato = hora+':'+str(minu)+':'+str(segun)
        pass
    return formato


def getFotoUsuario(id):
    lastIdUsuer   = db(db.auth_user.id==id).select(db.auth_user.ALL).last()
    if lastIdUsuer:
        if lastIdUsuer.foto:
            resul = URL('default','download/%s' %(empleado.foto))
        else:
            ff = URL('static','template/base/assets/img/avatar/avatar-3.jpg')
            fh = URL('static','template/base/assets/img/avatar/avatar-9.jpg')
            if lastIdUsuer.genero:
                if lastIdUsuer.genero[0] == 'Femenino':
                    resul = ff
                else:
                    resul = fh
            else:
                resul = URL('static','template/base/assets/img/avatar/avatar-9.jpg')
    else:
        resul = URL('static','template/base/assets/img/avatar/avatar-9.jpg')
        pass
    return resul 


def getFotoEmpresa():
    from empresas import Empresas
    company               = Empresas( db )
    company.nomEmpresa    = nombreCompany
    company.define_table()
    if db.empresas[empresaSesion].empresas_logo:
        resul  = URL('default','download/%s' %(db.empresas[empresaSesion].empresas_logo))
    else:
        resul  = URL('static','images/intelibpo-logo.png')
        pass
    return resul
    
def infoUsuarioId( idUser ):
    infoUsuario = ''
    if idUser:
        if db.auth_user[idUser]:
            infoUsuario = db.auth_user[idUser].first_name+' '+str(db.auth_user[idUser].last_name)
            pass
        pass
    return infoUsuario


def utilDesEncry( text, tipo ):
    from _clasFunt import EncryDesCry,DataGlobal
    textRtmp   = EncryDesCry( text )
    textRtmp.generate_key()
    varGl     = DataGlobal()
    if int(tipo) == varGl.estadoIniNum:
        textRes    = textRtmp.EnCry()
    else:
        textRes    = textRtmp.desCry()
        pass
    logsMostrar( 'info', 'textRes => '+str(textRes)+'' )
    return textRes


def textFechaDia( fechaSms ):
    from _clasFunt import DataGlobal
    varGl        = DataGlobal()
    fechaActual  = varGl.fechaIntModels
    operacion    = int(fechaActual) - int(fechaSms)
    if operacion ==  varGl.estadoFalsNum:
        textFecha   = 'Hoy'
    elif operacion ==  varGl.estadoIniNum:
        textFecha   = 'Ayer'
    else:
        if str(fechaActual)[-2:] == '01':
            textFecha   = 'Ayer'
        else:
            textFecha   = str(fechaFormato(fechaSms,'fecha'))
            pass
        pass
    return textFecha


def validateHoraAtencion( horaInicio, horaFin,festivo ):
    from _clasFunt import DataGlobal
    from datetime import date
    #import holidays
    varData = DataGlobal()
    horaInicialBase = int(str(horaInicio).replace(':',''))
    horaFinalBase   = int(str(horaFin).replace(':',''))
    horaActual      = int(varData.horaSinSeg)
    #holidaysCod     = holidays.country_holidays('CO')  # this is a dict
    # logsMostrar('info', 'horaInicialBase: '+str(horaInicialBase)+' ' )
    # logsMostrar('info', 'horaFinalBase: '+str(horaFinalBase)+' ' )
    # logsMostrar('info', 'horaActual: '+str(varData.horaSinSeg)+' ' )
    # logsMostrar('info', 'festivo: '+str(festivo)+' ' )
    #logsMostrar('info', 'holidaysCod: '+str(holidaysCod)+' ' )
    #tmp = date(varData.anioGlb, varData.mesGlb, varData.dayGlb) in us_holidays  # True
    #logsMostrar('info', 'tmp: '+str(tmp)+' ' )
    # tmp = varData.holidays_word()
    # logsMostrar('info', 'tmp 271: '+str(tmp)+' ' )
    if ( ( horaActual >= horaInicialBase) & ( horaActual <= horaFinalBase) ):
        horarioHabil  = varData.StatBoolT
    else:
        horarioHabil  = varData.StatBoolF    
        pass
    # logsMostrar('info', 'horarioHabil: '+str(horarioHabil)+' ' )
    return horarioHabil




def createnombreNodo( nombreNodo, tipo, opc ):
    logsMostrar( 'info', 'createnombreNodo => opc '+str(opc)+'')
    if opc:
        # db( db.nombre_nodos.id > 0 ).delete()
        nombreNodos = [
            { 'nombre': 'autorizo', 'tipo': 'chat' },
            { 'nombre': 'no_autorizo', 'tipo': 'chat' },
            { 'nombre': 'ya_pago_imagen', 'tipo': 'imagen' },
            { 'nombre': 'validacion_comprobante', 'tipo': 'chat' },
            { 'nombre': 'estado_cuenta', 'tipo': 'chat' },
            { 'nombre': 'puntos_pago', 'tipo': 'chat' },
            { 'nombre': 'mecanismos_pago', 'tipo': 'chat' },
            { 'nombre': 'pago_total', 'tipo': 'chat' },
            { 'nombre': 'pago_minimo', 'tipo': 'chat' },
            { 'nombre': 'acepta_compromiso_total', 'tipo': 'chat' },
            { 'nombre': 'acepta_compromiso_minimo', 'tipo': 'chat' },
            { 'nombre': 'asesor', 'tipo': 'asesor' },
        ]
        logsMostrar( 'info', 'createnombreNodo => nombreNodos '+str(nombreNodos)+'')
        for nodo in nombreNodos:
            logsMostrar( 'info', 'createnombreNodo => nodo '+str(nodo)+'')
            idNombreNodo  = db.nombre_nodos.insert(
                nombre_nodos_nombre  = nodo['nombre'],
                nombre_nodos_tipo  = nodo['tipo']
            )
            logsMostrar( 'info', 'createnombreNodo => idNombreNodo '+str(idNombreNodo)+'')
            pass
    else:
        idNombreNodo  = db.nombre_nodos.insert(
            nombre_nodos_nombre  = nombre,
            nombre_nodos_tipo  = tipo
        )
        pass
    return idNombreNodo


def emoj(emoji):
    if emoji.group()[:2] == '[<':
        emoji_unicode = emoji.group().replace('[<','').replace('>]','')
        emoji_unIni   = emoji_unicode.split("-")
        emoji_chars   = ""
        for i in emoji_unIni:
            emoji_chars += chr(int(i, 16))
            pass
    elif emoji.group()[:2] == '[{':
        emoji_unicode = emoji.group().replace('[{','').replace('}]','')
        emoji_chars = chr(int(str(emoji_unicode), 16))
        pass
    return emoji_chars


