# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import gluon.contrib.simplejson



@auth.requires_login()
def dashboard():
    response.title    = T("Dashboard")
    return locals()


@auth.requires_login()
def empresas():
    response.title     = T("Listado empresas") 
    response.suBtitle  = T("Dashboard configuraciones")
    logsMostrar( 'info', 'Lmando controlador empresas => '+str(idUser)+' ')
    infoCompany        = setListadoEmp()
    logsMostrar( 'info', 'empresas nombre_equipo => '+str(infoCompany)+' ' )
    return locals()


@auth.requires_login()
def infoEmpresa():
    data               = request.vars
    logsMostrar( 'info', 'data => '+str(data)+'' )
    listadoClientes    = []
    if data.idEmpresa:
        listadoClientes    = setListadoClientesEmpresas( data.idEmpresa )
        pass
    return locals()

@auth.requires_login()
def infoClientes():
    response.title     = T("Listado empresas") 
    response.suBtitle  = T("Dashboard empresas")
    data               = request.vars
    listadoSegmentos    = []
    if data.idCliente:
        listadoSegmentos = setListadoSegmentosClientes( data.idCliente )
        pass
    return locals()

@auth.requires_login()
def infoSegmento():
    data               = request.vars
    listadoSegmentos   = []
    listadoSegmentos   = setListadoSegmentosClientes( data.idCliente )
    if data.idSegmento:
        listadoCamposOferta = setConfigSegmento( data.idSegmento )
        listadoHorarios     = setConfigSegHorarios( data.idSegmento )
        listadoContextos    = setConfigSegContextos( data.idSegmento )
        listadoSmsPrest     = setConfigSegSmsPrest( data.idSegmento )
        listadoContChatBot  = setcontexChatBot( data.idSegmento )
        listadoContChatAdv  = setcontexChatAdv( data.idSegmento )
        listadoRusltados    = setResultadoSegmentos( data.idSegmento )
        listadoFormularios  = setFormularioSegmentos( data.idSegmento )
        listadoInstancias   = setInstanciasSegmentos( data.idSegmento )
        listadoPunto        = setPuntosPagoSegmentos( data.idSegmento )
        # logsMostrar( 'info', 'infoSegmento => listadoPunto '+str(listadoPunto)+'')
        pass
    return locals()


@auth.requires_login()
def bodyInfoEditarInstancias():
    data              = request.vars
    infoInstancia     = setInstanciasId( data )
    status            = ['success','hotFull','blockFull','standby']
    return locals()



# Contextos chatBot


@auth.requires_login()
def newNodos():
    data                = request.vars
    listadoRusltados    = setResultadoSegmentos( data.idSegmento ) 
    listadoNomNodos     = setListadoNombreNodos()        
    return locals()


@auth.requires_login()
def procesarJson():
    import json
    data           = request.vars
    # logsMostrar( 'info', 'procesarJson => data '+str(data)+'')
    nodos          = json.loads(data.nodos)
    opcionesNodos  = json.loads(data.opcionesNodos)
    compoNodos     = json.loads(data.compoNodos)
    dataEmClSeg    = infoSegClienteEmpresa( data.idSegemnto, 'segment' )
    # logsMostrar( 'info', 'procesarJson => dataE   mClSeg '+str(dataEmClSeg)+'')
    if dataEmClSeg:
        dataJson       = setProcesoJson( nodos, opcionesNodos, compoNodos, data.nomContexto, data.idSegemnto,dataEmClSeg['company'], dataEmClSeg['customers'], dataEmClSeg['segment'], data.canNodos )
        # logsMostrar( 'info', 'procesarJson => dataJson '+str(dataJson)+'')
        # dataJson       = 1
        dataJson  = dict(
            resul = 'success',
            json = dataJson
        )
        return gluon.contrib.simplejson.dumps(dataJson)
    else:
        dataJson  = dict(
            resul = 'error',
            json = ''
        )
        return gluon.contrib.simplejson.dumps(dataJson)
        pass


@auth.requires_login()
def verNodosContexto():
    data            = request.vars
    logsMostrar( 'info', 'verNodosContexto => data '+str(data)+'')
    dataJson       = setInfoDatacontexChatBot( data.idContxChatbot )
    return gluon.contrib.simplejson.dumps(dataJson)

@auth.requires_login()
def changeStatus():
    data            = request.vars
    # logsMostrar( 'info', 'verNodosContexto => data '+str(data)+'')
    dataEmClSeg    = infoSegClienteEmpresa( data.idSegmento, 'segment' )
    resul          = 0
    if dataEmClSeg:
        resul       = setchangeStatus(  data.idContxChatbot,data.nombreContexto, data.idSegmento,dataEmClSeg['company'], dataEmClSeg['customers'], dataEmClSeg['segment'], data.status )
        pass
    return str(resul)

@auth.requires_login()
def probarChatWhas():
    data       = request.vars
    dataJson   = setCamposPruebaContex( data.idContxChatbot )
    return gluon.contrib.simplejson.dumps(dataJson)

# fin contextos chatbot

@auth.requires_login()
def guardarFormPrevio():
    data            = request.vars
    # logsMostrar( 'info', 'guardarFormPrevio => data '+str(data)+'')
    resul           = createFormularioPrevio(  data.idSegmento, data.nomForm, data.canCampos )
    # logsMostrar( 'info', 'guardarFormPrevio => resul '+str(resul)+'')
    return str(resul)


@auth.requires_login()
def guardarCamposFormPrevio():
    data            = request.vars
    # logsMostrar( 'info', 'guardarCamposFormPrevio => data '+str(data)+'')
    resul           = createCampoFormPrevio( data.idFomulario, data.tipo_campo, data.tipo_campo, data.label, data.obligatorio, '', 100 )
    # logsMostrar( 'info', 'guardarCamposFormPrevio => resul '+str(resul)+'')
    return str(resul)


@auth.requires_login()
def verCamposFormulario():
    data            = request.vars
    listadoCampos   = setCamposForm( data.idFomulario )
    return gluon.contrib.simplejson.dumps(listadoCampos.as_list())


@auth.requires_login()
def resultadoHomologa():
    data                = request.vars
    listadoResultados   = setResultadoSegmentos( data.idSegmento )
    return gluon.contrib.simplejson.dumps(listadoResultados)



@auth.requires_login()
def resultAgregado():
    data       = request.vars
    # logsMostrar( 'info', 'agregarQuitarResultado => data '+str(data)+'')
    resul      = getResultAgregado( data.resultadoId, data.resultado, data.idFomulario )
    # logsMostrar( 'info', 'agregarQuitarResultado => resul '+str(resul)+'')
    return str(resul)


@auth.requires_login()
def agregarQuitarResultado():
    data        = request.vars
    resul       = getAgregarQuitarResultado( data.idResultado, data.resultado, data.idFomulario )
    return str(resul)

@auth.requires_login()
def agregarQuitarResultadoConf():
    data        = request.vars
    # logsMostrar( 'info', 'agregarQuitarResultadoConf => data '+str(data)+'')
    resul       = setAsignarResultadoSegmentos( data.idResultado, data.resultado, data.idSegmento )
    # logsMostrar( 'info', 'agregarQuitarResultadoConf => resul '+str(resul)+'')
    return str(resul)


@auth.requires_login()
def cuerpoFormulario():
    varDatos     = request.vars
    dbConfigForm = db.configuracion_formularios_segmento
    dbCampFor    = db.configuracion_campos_formulario
    cambio       = str(varDatos.idResultado)+' '+'-'+' '
    resultado    = str(varDatos.resultado).replace(cambio,'')
    
    return locals()



@auth.requires_login()
def asignarCamposSegmentos():
    data        = request.vars
    insertAsig  = setAsignarCamposSegmentos( data )
    return str(insertAsig)


@auth.requires_login()
def quitarCamposSegmentos():
    data        = request.vars
    deleteAsig  = setQuuitarCamposSegmentos( data )
    return str(deleteAsig)



@auth.requires_login()
def chatsSearchs():
    response.title    = T("Buscar chats")
    return locals()


@auth.requires_login()
def agregarPuntoPagoSeg():
    data        = request.vars
    logsMostrar( 'info', 'agregarPuntoPagoSeg => data '+str(data)+'')
    insertAsig  = getAgregarPuntoPago( data.idSegment,data.nomPuntoPago )
    logsMostrar( 'info', 'agregarPuntoPagoSeg => insertAsig '+str(insertAsig)+'')
    return str(insertAsig)


@auth.requires_login()
def agregarHorarioSeg():
    data        = request.vars
    # logsMostrar( 'info', 'agregarHorarioSeg => data '+str(data)+'')
    insertAsig  = setCreateHorarioSegmento( data.idSegment,data.nomHorario,data.diaIniHr,data.horaIniHr,data.horaFinHr,idUser,data.diaFestivos,data.diaLaborable )
    # logsMostrar( 'info', 'agregarHorarioSeg => insertAsig '+str(insertAsig)+'')
    return str(insertAsig)


@auth.requires_login()
def agregarSmsPrestSeg():
    data        = request.vars
    # logsMostrar( 'info', 'agregarSmsPrestSeg => data '+str(data)+'')
    insertAsig  = setCreateSmsPrestSegmento( data.idSegment,data.nomSmsPrest,data.tipoSmsPrest,data.smsPrest,idUser )
    # logsMostrar( 'info', 'agregarSmsPrestSeg => insertAsig '+str(insertAsig)+'')
    return str(insertAsig)



@auth.requires_login()
def actualizarSmsPrest():
    data        = request.vars
    # logsMostrar( 'info', 'actualizarSmsPrest => data '+str(data)+'')
    editSmsId  = setEditarSmsPrestSegmento( data.idSms,data.nomSmsPrestEdit,data.tipoSmsPrestEdit,data.smsPrestEdit,idUser )
    # logsMostrar( 'info', 'actualizarSmsPrest => editSmsId '+str(editSmsId)+'')
    return str(editSmsId)



@auth.requires_login()
def actualizarHorario():
    data        = request.vars
    # logsMostrar( 'info', 'actualizarHorario => data '+str(data)+'')
    editHorarioId  = setEditarHorarioSegmento( data.idHorario,data.nomHorarioEditar,data.diaIniHrEditar,data.horaIniHrEditar,data.horaFinHrEditar,data.diaFestivosEditar,data.diaLaboraEditar,idUser )
    # logsMostrar( 'info', 'actualizarHorario => editHorarioId '+str(editHorarioId)+'')
    return str(editHorarioId)
