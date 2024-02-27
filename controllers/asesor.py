# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import gluon.contrib.simplejson
import re
import json

@auth.requires_login()
def dashboard():
    response.title        = T("Listado Chats") 
    response.suBtitle     = T("Dashboard Asesor")
    idCliente,idClientHst = setInfoAtencion()
    logsMostrar( 'info', 'dashboard => idCliente '+str(idCliente)+'' )
    logsMostrar( 'info', 'dashboard => idClientHst '+str(idClientHst)+'' )
    # tmp = validateHoraAtencion( '07:00', '19:00','si' )
    return locals()


@auth.requires_login()
def misGestiones():
    response.title        = T("Mis gestiones") 
    response.suBtitle     = T("Mis gestiones")
    infoGestiones         = setGestionesAsesor( idUser )
    return locals()

@auth.requires_login()
def misGestionesMesAntes():
    infoGestiones         = setGestionesAsesorMesAntes( idUser )
    return locals()


@auth.requires_login()
def chatClienteGestion():
    varDatos            = request.vars
    response.suBtitle   = T("Dashboard Asesor")
    response.title      = T(""+str(varDatos.nCustomer).capitalize()+" - Chat Gestiones ") 
    # listadoClientesChat = setDataInfoClienteSmsGestiones( varDatos.numberCustomer, idUser )
    return locals()


@auth.requires_login()
def listaEmpresasAsesor():
    varDatos              = request.vars
    return locals()

# Actualizar Developer
@auth.requires_login()
def listaChatEmpresa():
    response.title                = T("Listado Chats") 
    response.suBtitle             = T("Dashboard Asesor")
    varDatos                      = request.vars
    idCliente,idClientHst         = setInfoAtencion()
    nombreCliente,identificacion, clienteSeg  = setInfoAtencionNomCliente( idCliente )
    listadoClientesChat           = setListChatEmpresa( varDatos.prem, varDatos.atrg )
    return locals()

@auth.requires_login()
def verInfoChatCliente():
    varDatos            = request.vars
    infoClienteSmsDta   = setDataInfoClienteSms( varDatos.idCliente, varDatos.idClientHst, varDatos.idEmpresa, varDatos.idUser )
    for item in infoClienteSmsDta:
        sms = re.sub("(\[\{(\d|[A-Z])+\}\])|(\[<(\d|[A-Z]|-)+>\])",emoj,item['sms'])
        item['sms'] = sms
        pass
    return gluon.contrib.simplejson.dumps(infoClienteSmsDta)


@auth.requires_login()
def smsPrestablecidos():
    varDatos            = request.vars
    infoSmsPrestDta  = setSmsPrestablesidosSeg( varDatos.idCliente )
    return gluon.contrib.simplejson.dumps(infoSmsPrestDta)



@auth.requires_login()
def envioSmsCliente():
    varDatos         = request.vars
    resulSend        = 0
    infoCliente,camposSeg  = infoClienteId( varDatos.idClienteGlb )
    logsMostrar( 'info', 'envioSmsCliente => infoCliente '+str(infoCliente)+'' )
    sms = re.sub("(\[\{(\d|[A-Z])+\}\])|(\[<(\d|[A-Z]|-)+>\])",emoj,varDatos.sms)
    if infoCliente:
        envioSmsWhat = sendSmsAsesor( sms, varDatos.idClienteGlb, varDatos.idClientHstGlb, infoCliente.empresa_strauss, infoCliente.cliente_strauss, infoCliente.segmento_strauss, infoCliente.telefono )
        
        if envioSmsWhat == 0:
            resulSend    = 0
        else:
            resulSend    = recepcionSms( infoCliente.telefono, infoCliente.identificacion, infoCliente.empresa, infoCliente.cliente, infoCliente.segmento,varDatos.sms, 'asesor', 'cliente', 'text', varDatos.idClienteGlb, varDatos.idClientHstGlb )
            pass
        pass
    return str(resulSend)


@auth.requires_login()
def verInfoOfertasCliente():
    varDatos              = request.vars
    infoClienteOfertasDta = []
    infoClienteOfertasDta    = setInfoOfertasTuacuerdo( varDatos.idCliente )
    # logsMostrar( 'info', 'infoClienteOfertasDta => verInfoOfertasCliente '+str(infoClienteOfertasDta)+'' )
    if len(infoClienteOfertasDta) == 0:
        infoCliente,fieldsSeg = infoClienteId( varDatos.idCliente )
        if infoCliente:
            infoClienteOfertasDta = setInfoOfertasCampos( varDatos.idCliente,fieldsSeg,infoCliente.producto )
            pass
        pass
    return gluon.contrib.simplejson.dumps(infoClienteOfertasDta)


@auth.requires_login()
def cambioEstado():
    varDatos        = request.vars
    tmpCambioEstado = 0
    # logsMostrar( 'info', varDatos )
    tmpCambioEstado = changeStatusAdviser( varDatos.idUserClt,varDatos.statusIngr )
    # print('Salida asesor', tmpCambioEstado)
    return str(tmpCambioEstado)


@auth.requires_login()
def tipificacion():
    varDatos              = request.vars
    tipoTipificaciones    = setListHomologaciones( varDatos )
    return locals()

@auth.requires_login()
def actualizaDatos():
    varDatos              = request.vars
    clienteData           = infoClienteData( varDatos.idClienteGlb )
    return locals()




@auth.requires_login()
def validarPuntosPagoSeg():
    varDatos       = request.vars
    infoPuntoPago  =  setPuntosPagoSegmentos( varDatos.idClienteGlb )
    return gluon.contrib.simplejson.dumps(infoPuntoPago)


@auth.requires_login()
def validarFormularioGestion():
    data            = request.vars
    idFormulario    = validateFormularioId( data.idCliente, data.descripResul, data.idResul )
    if idFormulario > 0:
        listadoCampos   = setCamposForm( idFormulario )
        resul = dict(
            listadoCampos = listadoCampos.as_list(),
            pPagos        = setPuntosPagoSegmentos( data.idCliente )
        )
        return gluon.contrib.simplejson.dumps(resul)
    else:
        resul = dict(
            listadoCampos  =  [],
            pPagos        = []
        )
        return gluon.contrib.simplejson.dumps(resul)
        pass



@auth.requires_login()
def cerrarGestion():
    try:
        varDatos        = request.vars
        # logsMostrar( 'info', varDatos )
        if int(varDatos.idFormResul) > 0:
            idInteraccion           = guardarInteraccion( varDatos, varDatos.idFormResul, varDatos.dataFormExtra )
            liberacionClienteAsesor = setLiberacionAdviACli( varDatos.idCliente, varDatos.idClientHist )
            tipeForm                = setTypeForm( varDatos.idFormResul )
            # logsMostrar( 'info', 'tipeForm cerrarGestion 141 => '+str(tipeForm)+' ' )
            if tipeForm:
                idAcuerdo           = setAcuerdoForm( varDatos.dataFormExtra, idInteraccion )
                # logsMostrar( 'info', 'idAcuerdo cerrarGestion 144 => '+str(idAcuerdo)+' ' )
                functultSmsClienteion( varDatos.idCliente, varDatos.idClientHist )
                return str(idInteraccion)
            else:
                functultSmsClienteion( varDatos.idCliente, varDatos.idClientHist )
                return str(idInteraccion)
                pass
        else:
            idInteraccion   = guardarInteraccion( varDatos,varDatos.idFormResul , {} )
            # logsMostrar( 'info', 'idInteraccion => 141 '+str(idInteraccion)+' ' )
            if idInteraccion > 0:
                liberacionClienteAsesor = setLiberacionAdviACli( varDatos.idCliente, varDatos.idClientHist )
                functultSmsClienteion( varDatos.idCliente, varDatos.idClientHist )
                return str(idInteraccion)
            else:
                idInteraccion = 0
                return str(idInteraccion)
                pass
            pass
    except Exception as e:
        logsMostrar( 'error', 'cerrarGestion Error => '+str(e)+' ' )
        idInteraccion   = 0
        return str(idInteraccion)
        pass
    


def cargaHistorial():
    varDatos            = request.vars
    infoClienteSmsDtaHistory   = setDataInfoClienteSmsHistory( varDatos.idCliente )
    for item in infoClienteSmsDtaHistory:
        sms = re.sub("(\[\{(\d|[A-Z])+\}\])|(\[<(\d|[A-Z]|-)+>\])",emoj,item['sms'])
        item['sms'] = sms
        pass
    return gluon.contrib.simplejson.dumps(infoClienteSmsDtaHistory)