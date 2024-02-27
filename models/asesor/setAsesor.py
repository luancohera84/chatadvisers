# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos
from clientesUsers import ClientesUsers
from conversaCliAdv import ConversClientAdv
from _clasFunt import ConexionWhast, DataGlobal
from interaccionesAsesor import InteraccionesAsesor
from  ofertasTu import ofertasTuacuerdo


def setSmsPrestablesidosSeg( idClientePlf ):

    cliInfo              = ClientesUsers( db )
    cliInfo.idCliPlaf    = idClientePlf
    cliInfo.define_table()
    listSmsPrest         = []
    infoClienteSendSms   = cliInfo.consultingClieTrueId()
    if infoClienteSendSms:
        company              = Empresas( db )
        customers            = Clientes( db )
        segment              = Segmentos( db )
        company.define_table()
        customers.define_table()
        segment.define_table()
        segment.idSegmento  = infoClienteSendSms.segmento
        segment.tipoSmsPr    = 'Asesor'
        listSmsPrestTmp      = segment.setSmssPrebSegId()
        if listSmsPrestTmp:
            for item in listSmsPrestTmp:
                listSmsPrest.append(
                    dict(
                        sms = item.sms
                    )
                )
                pass
            pass
        pass
    return listSmsPrest


def setCamposMostrarOferta( idSegmento ):
    camposList  = []
    return camposList

def setCantidadClienteSms( idClientePlf ):
    convCliAs               = ConversClientAdv( db )
    convCliAs.idCliPlaf     = idClientePlf
    dataClienteSms          = 0
    tiempoEspera            = 0 
    convCliAs.define_table()
    dataClienteSTmp         = convCliAs.countSmsSinLectura()
    if dataClienteSTmp:
        dataClienteSms      = len(dataClienteSTmp)
        for item in dataClienteSTmp:
            tiempoEspera    = str(fechaFormato(item.hora_creacion,'hora'))
            pass
        pass
    return dataClienteSms,tiempoEspera


def empresasChatAsesorAsi( idAsesor ):
    convCliAs             = ConversClientAdv( db )
    convCliAs.idAdvisers  = idAsesor
    convCliAs.define_table()
    listEmpresasAsigChats = convCliAs.empresasClietAsesor()
    # logsMostrar( 'info', 'empresasChatAsesorAsi => listEmpresasAsigChats '+str(listEmpresasAsigChats)+'' )
    return listEmpresasAsigChats

def setInfoAtencion():
    convCliAs            = ConversClientAdv( db )
    varData                = DataGlobal()
    convCliAs.idAdvisers = idUser
    convCliAs.define_table()
    idCliente            = 0
    idClientHst          = 0
    dataClientAten       = convCliAs.consultingAtencionClinAsesor()
    logsMostrar( 'info', 'setInfoAtencion => dataClientAten '+str(dataClientAten)+'' )
    if dataClientAten:
        idCliente        = dataClientAten.id_cliente
        idClientHst      = dataClientAten.id_cliente_histori
        pass

    # emoji  = varData.emojis()
    return idCliente, idClientHst

# Actualizar Developer    
def setInfoAtencionNomCliente( idClientePlf ):
    cliInfo              = ClientesUsers( db )
    cliInfo.idCliPlaf    = idClientePlf
    cliInfo.define_table()
    nombreCliente        = ''
    identificacion       = ''
    clienteSeg           = ''
    infoClienteSendSms   = cliInfo.consultingClieTrueId()
    if infoClienteSendSms:
        identificacion    = infoClienteSendSms.identificacion
        nombreClienteTmp  = str(infoClienteSendSms.name).capitalize()+' '+str(infoClienteSendSms.surname).capitalize()
        clienteSeg        = str(infoClienteSendSms.cliente_strauss)+'-'+str(infoClienteSendSms.segmento_strauss)
        if nombreClienteTmp != " ":
           nombreCliente = nombreClienteTmp
        else:
            nombreCliente  = str(infoClienteSendSms.Nombre).capitalize()
            pass
        pass
    return nombreCliente,identificacion,clienteSeg

def setListChatEmpresa( idEmpresa, idAsesor ):
    convCliAs            = ConversClientAdv( db )
    convCliAs.idAdvisers = idAsesor
    convCliAs.idEmpresa  = idEmpresa
    convCliAs.define_table()
    listChatEmpresa      = convCliAs.clientesAsigEmpresaAsesor()
    return listChatEmpresa


def setDataInfoClienteSms( idClientePlf, idClientePlfHist, idCompany, idAsesor ):
    convCliAs               = ConversClientAdv( db )
    convCliAs.idAdvisers    = idAsesor
    convCliAs.idCliPlaf     = idClientePlf
    convCliAs.idCliPlafHist = idClientePlfHist
    dataClienteSms          = []
    convCliAs.define_table()
    idClAdvisersAtencion    = convCliAs.getCreateClienteAdvisersAtencion()
    dataClienteSTmp         = convCliAs.infoClienteSmsAsesor()
    # logsMostrar( 'info', 'setDataInfoClienteSms ASESOR => idClientePlf '+str(idClientePlf)+'' )
    # logsMostrar( 'info', 'setDataInfoClienteSms ASESOR => idAsesor '+str(idAsesor)+'' )
    # logsMostrar( 'info', 'setDataInfoClienteSms ASESOR => dataClienteSTmp '+str(dataClienteSTmp)+'' )
    
    if dataClienteSTmp:
        for item in dataClienteSTmp:
            nameClienteTmp = str(db.info_cliente[item.conversaciones.id_cliente].name).capitalize()+' '+str(db.info_cliente[item.conversaciones.id_cliente].surname).capitalize()
            if nameClienteTmp != " ":
                nameCliente = nameClienteTmp
            else:
                nameCliente = str(db.info_cliente[item.conversaciones.id_cliente].Nombre).capitalize()
                pass
            dataClienteSms.append(
                dict(
                    idSms       = item.mensajes_conversacion.id,
                    tipoUsuario = item.mensajes_conversacion.origen_mensaje,
                    sms         = item.mensajes_conversacion.mensage,
                    estLect     = item.mensajes_conversacion.estado_lectura,
                    idConv      = item.mensajes_conversacion.id_conversacion,
                    horaSms     = str(fechaFormato(item.mensajes_conversacion.hora_creacion,'hora')),
                    fechaSms    = str(fechaFormato(item.mensajes_conversacion.fecha_creacion,'fecha')),
                    textFecSms  = str(textFechaDia(item.mensajes_conversacion.fecha_creacion)),
                    tipoSms     = item.mensajes_conversacion.tipo_mensaje,
                    cliente     = nameCliente,
                    asesor      = infoUsuarioId( item.conversaciones.id_asesor )
                )
            )
            pass
        pass
    return dataClienteSms


def functultSmsClienteion( idClienteGlb, idClientHstGlb ):
    varData                = DataGlobal()
    infoCliente,camposSeg  = infoClienteId( idClienteGlb )
    sms                    = varData.smsFinal
    if infoCliente:
        envioSmsWhat = sendSmsAsesor( sms, idClienteGlb, idClientHstGlb, infoCliente.empresa, infoCliente.cliente, infoCliente.segmento, infoCliente.telefono )
        if envioSmsWhat == 0:
            resulSend    = 0
        else:
            resulSend    = recepcionSms( infoCliente.telefono, infoCliente.identificacion, infoCliente.empresa, infoCliente.cliente, infoCliente.segmento, sms, 'asesor', 'cliente', 'text', idClienteGlb, idClientHstGlb )
            pass
        pass
    pass



def infoClienteId( idClientePlf ):
    from empresas import Empresas, Clientes, Segmentos
    cliInfo            = ClientesUsers( db )
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    cliInfo.idCliPlaf  = idClientePlf
    cliInfo.define_table()
    company.define_table()
    customers.define_table()
    segment.define_table()
    infoClienteSendSms  = cliInfo.consultingClieTrueId()
    fieldsSegmento      = []
    if infoClienteSendSms:
        segment.idSegmento = infoClienteSendSms.segmento
        fieldsSegmento      = segment.getCamposAsigSeg()
        pass
    return infoClienteSendSms,fieldsSegmento

def sendSmsAsesor( sms, idClientePlf, idClientePlfHist, empresaNombre, clienteNombre, segmentoNombre, teleCliente ):
    resulApi = 0
    # empresaNombre   = empresaIdConsulting( idEmpresa )
    # clienteNombre   = clienteIdConsulting( idCliente  )
    # segmentoNombre  = segmentoIdConsulting( idSegmento  )
    conexApiWhat    = ConexionWhast( sms, empresaNombre, clienteNombre, segmentoNombre, teleCliente )
    resulApi        = conexApiWhat.conexionSend()
    return resulApi


def recepcionSms( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, sms, origen, destino, tipo, infoClienteInfo, infoClienteInHist ):
    idConversacion                       = 0
    clienteUsers                         = ConversClientAdv( db )
    clienteUsers.telfonoCliente          = telefonoCliente
    clienteUsers.idetficCliente          = identificaCliente
    clienteUsers.idEmpresa               = companyCliente
    clienteUsers.idCliente               = customersCliente
    clienteUsers.idSegmento              = segmentCliente
    clienteUsers.sms                     = sms
    clienteUsers.tipo                    = tipo
    clienteUsers.origen                  = origen
    clienteUsers.destino                 = destino
    clienteUsers.define_table()
    clienteUsers.idAdvisers             = idUser
    clienteUsers.idCliPlaf              = infoClienteInfo
    clienteUsers.idCliPlafHist          = infoClienteInHist
    idInsertCov,idInsertCovHist         = clienteUsers.consultinIdConvClinUser()
    # logsMostrar( 'info', 'recepcionSms ASESOR => 216 idInsertCov '+str(idInsertCov)+'' )
    # logsMostrar( 'info', 'recepcionSms ASESOR => 217 idInsertCovHist '+str(idInsertCovHist)+'' )
    if idInsertCov:
        if idInsertCovHist:
            # logsMostrar( 'info', 'recepcionSms ASESOR => 220 ambos cumplen' )
            clienteUsers.idInsertCov        = idInsertCov.id
            clienteUsers.idInsertCovHist    = idInsertCovHist.id
        else:
            # logsMostrar( 'info', 'recepcionSms ASESOR => 224 uno de los dos no cumplen' )
            idInsertCov,idInsertCovHist     = clienteUsers.getNewconversacion()
            clienteUsers.idInsertCov        = idInsertCov
            clienteUsers.idInsertCovHist    = idInsertCovHist
            pass
    else:
        # logsMostrar( 'info', 'recepcionSms ASESOR => 230 uno de los dos no cumplen' )
        idInsertCov,idInsertCovHist     = clienteUsers.getNewconversacion()
        clienteUsers.idInsertCov        = idInsertCov
        clienteUsers.idInsertCovHist    = idInsertCovHist
        pass
    idConversacion                      = clienteUsers.getNewSms()
    return idConversacion


def infoClienteData( idClienteGlb ):
    cliInfo              = ClientesUsers( db )
    cliInfo.idCliPlaf    = idClienteGlb
    cliInfo.define_table()
    dataCliente          = cliInfo.consultingClieTrueId()
    return dataCliente


def setListHomologaciones( data ):
    from _clasFunt import ConexionStrauss
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    cliInfo              = ClientesUsers( db )
    cliInfo.idCliPlaf    = data.idClienteGlb
    dataHomologaciones   = []
    company.define_table()
    customers.define_table()
    segment.define_table()
    cliInfo.define_table()
    infoClienteTipi  = cliInfo.consultingClieTrueId()
    # logsMostrar( 'info', 'setListHomologaciones ASESOR => infoClienteTipi '+str(infoClienteTipi)+'' )
    if infoClienteTipi:
        idEmpresa          = infoClienteTipi.empresa
        segment.idSegmento = infoClienteTipi.segmento
        dataResulSegts     = segment.setResultadosSegmento()
        # Validamos los resultados configurados
        if len(dataResulSegts) > 0:
            for item in dataResulSegts:
                dataHomologaciones.append(
                    dict(
                        descripcion = item['resultado'],
                        idResultado = item['id_resultado']
                    )
                )
                pass
        else:
            dataConexion = empresaConsultingConexion( idEmpresa )
            # logsMostrar( 'info', 'setListHomologaciones ASESOR => dataConexion '+str(dataConexion[0]['empresas_base_key'])+'' )
            if len(dataConexion) > 0:
                conexiones                   = ConexionStrauss()
                conexiones.nomEmpresa        = infoClienteTipi.empresa_strauss
                conexiones.nomCliente        = infoClienteTipi.cliente_strauss
                conexiones.nomSegmento       = infoClienteTipi.segmento_strauss
                conexiones.userStaruss       = dataConexion[0]['empresas_base_usuario']
                conexiones.bDStrauss         = dataConexion[0]['empresas_base']
                conexiones.hostStrauss       = dataConexion[0]['empresas_base_dominio']
                conexiones.keyPrivateStrauss = dataConexion[0]['empresas_base_key']
                dataHomologaciones           = conexiones.datosDBHomologa()
                # logsMostrar( 'info', 'setListHomologaciones ASESOR => dataHomologaciones '+str(dataHomologaciones)+'' )
                pass
            pass
        pass
    
    return dataHomologaciones

def setPuntosPagoSegmentos( idClienteGlb ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    cliInfo              = ClientesUsers( db )
    cliInfo.idCliPlaf    = idClienteGlb
    company.define_table()
    customers.define_table()
    segment.define_table()
    cliInfo.define_table()
    listadoPuntoPagoSeg  = []
    infoClienteTipi  = cliInfo.consultingClieTrueId()
    if infoClienteTipi:
        segment.idSegmento = infoClienteTipi.segmento
        listadoPunto       =  segment.getListPuntoSeg()
        if listadoPunto:
            for item in listadoPunto:
                listadoPuntoPagoSeg.append(
                    dict(
                        punto_pago = item.punto_pago
                    )
                )
                pass
            pass
        pass
    return listadoPuntoPagoSeg


def guardarInteraccion( datos, idFormResu, dataExtra  ):
    # logsMostrar( 'info', 'guardarInteraccion 240 => datos '+str(datos)+'' )
    clienteUsers                       = ConversClientAdv( db )
    intAsesor                          = InteraccionesAsesor( db )
    clienteUsers.define_table()
    clienteUsers.idAdvisers            = idUser
    clienteUsers.idCliPlaf             = datos.idCliente
    clienteUsers.idCliPlafHist         = datos.idClientHist
    idInsertCov,idInsertCovHist        = clienteUsers.consultinIdConvClinUser()
    # logsMostrar( 'info', 'idInsertCov => 248 idInsertCov '+str(idInsertCov)+'' )
    nomFormulario                      = getNomFormu(idFormResu)
    # logsMostrar( 'info', 'nomFormulario => 250 nomFormulario '+str(nomFormulario)+'' )
    intAsesor.idAdvisers               = clienteUsers.idAdvisers
    intAsesor.idCliPlaf                = datos.idCliente
    intAsesor.idCliPlafHist            = datos.idClientHist
    intAsesor.id_resultado             = datos.idResul
    intAsesor.descripcion_resultado    = datos.descripResul
    intAsesor.idInsertCov              = idInsertCov.id
    intAsesor.idInsertCovHist          = idInsertCovHist.id
    intAsesor.comentarios              = datos.comentarios
    intAsesor.formulario               = dataExtra
    intAsesor.formulario_id            = idFormResu
    intAsesor.formulario_nombre        = nomFormulario
    intAsesor.define_table()
    idInteraccion                    = intAsesor.insertInteraccion()
    # logsMostrar( 'info', 'guardarInteraccion => 264 idInteraccion '+str(idInteraccion)+'' )
    return idInteraccion


def setLiberacionAdviACli( idCliente, idClienteHist ):
    intAsesor                 = InteraccionesAsesor( db )
    cliInfo                   = ClientesUsers( db )
    intAsesor.define_table()
    cliInfo.define_table()
    intAsesor.idCliPlaf       = idCliente
    intAsesor.idCliPlafHist   = idClienteHist
    cliInfo.idCliPlaf         = idCliente
    intAsesor.deleteClinInfo()
    resulTmp                  = cliInfo.consultingClieTrueId()
    if resulTmp:
        resulLiberacion           = False
    else:
        resulLiberacion           = True
        pass
    return resulLiberacion


def setInfoOfertasCampos( idClientePlaf, fieldsSeg, numProdcuto ):
    # logsMostrar( 'info', 'setInfoOfertasTuacuerdo => idClientePlaf 316 '+str(idClientePlaf)+'' )
    # logsMostrar( 'info', 'setInfoOfertasTuacuerdo => fieldsSeg 317 '+str(fieldsSeg)+'' )
    # logsMostrar( 'info', 'setInfoOfertasTuacuerdo => numProdcuto 318 '+str(numProdcuto)+'' )
    cliInfo                   = ClientesUsers( db )
    cliInfo.define_table()
    dataOfertasFields = []
    cadenaCampos      = ''
    contador          = 1
    for cpms in fieldsSeg:
        if contador == len(fieldsSeg):
            cadenaCampos += cpms.campo_base+' '+'as'+' '+str(cpms.campo_representa)
        else:
            cadenaCampos += cpms.campo_base+' '+'as'+' '+str(cpms.campo_representa)+','
            pass
        contador  = contador + 1
        pass
    
    if cadenaCampos:
        sqlSpeech = """
            SELECT
                """+str(cadenaCampos)+"""
            FROM 
                info_cliente
            WHERE 
                id = """+str(idClientePlaf)+"""
        """
        res           = db.executesql(sqlSpeech)
        if res:
            for item,x in enumerate(res[0]):
                dataOfertasFields.append(
                    dict(
                        campoRespresenta = fieldsSeg[item].campo_representa,
                        valorCampo       = x,
                        numProducto      = numProdcuto,
                        canal            = 'chat'
                    )
                )
                pass
            pass
        pass
    
    return dataOfertasFields



def setInfoOfertasTuacuerdo( idClientePlaf ):
    infoOfertas               = []
    cliInfo                   = ClientesUsers( db )
    cliInfo.define_table()
    cliInfo.idCliPlaf         = idClientePlaf
    infoCliente               = cliInfo.consultingClieTrueId()
    if infoCliente:
        oferTu                = ofertasTuacuerdo( infoCliente.empresa_strauss, infoCliente.cliente_strauss, infoCliente.segmento_strauss, infoCliente.identificacion, infoCliente.token )
        infoOfertas           = oferTu.ordenamiento()
        pass
    return infoOfertas



def setDataInfoClienteSmsHistory( idClientePlf ):
    cliInfo                 = ClientesUsers( db )
    cliInfo.define_table()
    cliInfo.idCliPlaf       = idClientePlf
    infoCliente             = cliInfo.consultingClieTrueId()
    dataClienteSmsHistory   = ''
    if infoCliente:
        # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => infoCliente.empresa '+str(infoCliente.empresa)+'' )
        # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => infoCliente.cliente '+str(infoCliente.cliente)+'' )
        # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => infoCliente.segmento '+str(infoCliente.segmento)+'' )
        # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => infoCliente.identificacion '+str(infoCliente.identificacion)+'' )
        # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => infoCliente.telefono '+str(infoCliente.telefono)+'' )
        cliInfo.telfonoCliente   = infoCliente.telefono
        cliInfo.idetficCliente   = infoCliente.identificacion
        cliInfo.idEmpresa        = infoCliente.empresa
        cliInfo.idCliente        = infoCliente.cliente
        cliInfo.idSegmento       = infoCliente.segmento
        idsHistoryCliente        = cliInfo.consultingClieHist()
        idCliPlafLits            = []
        if idsHistoryCliente:
            for items in idsHistoryCliente:
                idCliPlafLits.append(items.id)
                pass
            # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => idCliPlafLits '+str(str(idCliPlafLits).replace('[','(' ).replace(']',')' ))+'' )
            # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => idCliPlafLits '+str(tuple(idCliPlafLits))+'' )
            convCliAs               = ConversClientAdv( db )
            convCliAs.idCliPlafs    = str(idCliPlafLits).replace('[','(' ).replace(']',')' )
            convCliAs.define_table()
            dataClienteSmsHistory         = convCliAs.infoClienteSmsHistory()
            # logsMostrar( 'info', 'setDataInfoClienteSmsHistory 324 => dataClienteSmsHistory '+str(dataClienteSmsHistory)+'' )
            # if dataClienteSTmp:
            #     for item in dataClienteSTmp:
            #         dataClienteSmsHistory.append(
            #             dict(
            #                 idSms       = item.mensajes_conversacion_historica.id,
            #                 tipoUsuario = item.mensajes_conversacion_historica.origen_mensaje,
            #                 sms         = item.mensajes_conversacion_historica.mensage,
            #                 estLect     = item.mensajes_conversacion_historica.estado_lectura,
            #                 idConv      = item.mensajes_conversacion_historica.id_conversacion,
            #                 horaSms     = str(fechaFormato(item.mensajes_conversacion_historica.hora_creacion,'hora')),
            #                 fechaSms    = str(fechaFormato(item.mensajes_conversacion_historica.fecha_creacion,'fecha')),
            #                 textFecSms  = str(textFechaDia(item.mensajes_conversacion_historica.fecha_creacion)),
            #                 tipoSms     = item.mensajes_conversacion_historica.tipo_mensaje,
            #                 cliente     = str(db.info_cliente_historica[item.conversaciones_historica.id_cliente].name).capitalize()+' '+str(db.info_cliente_historica[item.conversaciones_historica.id_cliente].surname).capitalize(),
            #                 asesor      = infoUsuarioId( item.conversaciones_historica.id_asesor )
            #             )
            #         )
            #         pass
            #     pass
            pass
        pass
    # logsMostrar( 'info', 'setDataInfoClienteSmsHistory => dataClienteSmsHistory '+str(dataClienteSmsHistory)+'' )
    return dataClienteSmsHistory



def setGestionesAsesor( idAsesor ):
    intAsesor            = InteraccionesAsesor( db )
    intAsesor.define_table()
    infoGestiones        = ''   
    intAsesor.idAdvisers = idAsesor
    infoGestiones        = intAsesor.gestionesAsesor()
    # logsMostrar( 'info', 'setGestionesAsesor => infoGestiones '+str(infoGestiones)+'' )
    return infoGestiones


def setGestionesAsesorMesAntes( idAsesor ):
    intAsesor               = InteraccionesAsesor( db )
    intAsesor.define_table()
    infoGestionesFecha      = ''
    intAsesor.idAdvisers    = idAsesor
    infoGestionesFecha      = intAsesor.gestionesAsesorFechas()
    # logsMostrar( 'info', 'setGestionesAsesorMesAntes => infoGestionesFecha '+str(infoGestionesFecha)+'' )
    return infoGestionesFecha



def setDataInfoClienteSmsGestiones( idClientePlf, idAsesor ):
    convCliAs               = ConversClientAdv( db )
    convCliAs.idAdvisers    = idAsesor
    convCliAs.idCliPlaf     = idClientePlf
    convCliAs.idCliPlafHist = idClientePlf
    dataClienteSms          = []
    convCliAs.define_table()
    idClAdvisersAtencion    = convCliAs.getCreateClienteAdvisersAtencion()
    dataClienteSTmp         = convCliAs.infoClienteSmsIdCov()
    # logsMostrar( 'info', 'setDataInfoClienteSmsGestiones ASESOR => idClientePlf '+str(idClientePlf)+'' )
    # logsMostrar( 'info', 'setDataInfoClienteSmsGestiones ASESOR => idAsesor '+str(idAsesor)+'' )
    # logsMostrar( 'info', 'setDataInfoClienteSmsGestiones ASESOR => dataClienteSTmp '+str(dataClienteSTmp)+'' )
    
    if dataClienteSTmp:
        for item in dataClienteSTmp:
            nameClienteTmp = str(db.info_cliente[item.conversaciones.id_cliente].name).capitalize()+' '+str(db.info_cliente[item.conversaciones.id_cliente].surname).capitalize()
            if nameClienteTmp != " ":
                nameCliente = nameClienteTmp
            else:
                nameCliente = str(db.info_cliente[item.conversaciones.id_cliente].Nombre).capitalize()
                pass
            dataClienteSms.append(
                dict(
                    idSms       = item.mensajes_conversacion.id,
                    tipoUsuario = item.mensajes_conversacion.origen_mensaje,
                    sms         = item.mensajes_conversacion.mensage,
                    estLect     = item.mensajes_conversacion.estado_lectura,
                    idConv      = item.mensajes_conversacion.id_conversacion,
                    horaSms     = str(fechaFormato(item.mensajes_conversacion.hora_creacion,'hora')),
                    fechaSms    = str(fechaFormato(item.mensajes_conversacion.fecha_creacion,'fecha')),
                    textFecSms  = str(textFechaDia(item.mensajes_conversacion.fecha_creacion)),
                    tipoSms     = item.mensajes_conversacion.tipo_mensaje,
                    cliente     = nameCliente,
                    asesor      = infoUsuarioId( item.conversaciones.id_asesor )
                )
            )
            pass
        pass
    return dataClienteSms


def setChatGestiones( idClienPlaf ):
    from clientesUsers import ClientesUsers
    from conversaCliAdv import ConversClientAdv
    cliInfo                    = ClientesUsers( db )
    clienteUsers               = ConversClientAdv( db )
    clienteUsers.idAdvisers    = idUser
    clienteUsers.idCliPlaf     = idClienPlaf
    clienteUsers.idCliPlafHist = idClienPlaf
    idAsigCli,idAsigCliHist    = clienteUsers.getCreateClienteAdvisers()
    idClAdvisersAtencion       = clienteUsers.getCreateClienteAdvisersAtencion()
    infoChatCliente    = []
    cliInfo.define_table()
    infoClienteSendSms  =  db( db.info_cliente.id == idClienPlaf ).select( db.info_cliente.ALL ).last()
    if infoClienteSendSms:
        infoChatCliente.append(
            dict(
                empresa   = str(infoClienteSendSms.empresa_strauss).capitalize(),
                idUser    = idUser,
                idEmpresa = infoClienteSendSms.empresa
            )
        )
        pass
    return infoChatCliente



def validateFormularioId( idClientePlf, descripcion_resultado, id_resultado ):
    company                 = Empresas( db )
    customers               = Clientes( db )
    segment                 = Segmentos( db )
    cliInfo                 = ClientesUsers( db )
    varData                 = DataGlobal()
    company.define_table()
    customers.define_table()
    segment.define_table()
    cliInfo.define_table()
    cliInfo.idCliPlaf       = idClientePlf
    resulResulForm          = 0
    infoCliente             = cliInfo.consultingClieTrueId()
    if infoCliente:
        # logsMostrar( 'info', 'validateFormularioId => infoCliente.empresa '+str(infoCliente.empresa)+'' )
        segment.idSegmento     = infoCliente.segmento
        listFormularios        = segment.setFormulariosSegId()
        if listFormularios:
            for item in listFormularios:
                # logsMostrar( 'info', 'validateFormularioId => item.id '+str(item.id)+'' )
                segment.idFormulario  = item.id
                segment.resultadoFor  = descripcion_resultado
                segment.idResultadoF  = id_resultado
                cantFormResul         = segment.setCountFormularioResul()
                # logsMostrar( 'info', 'validateFormularioId => cantFormResul '+str(cantFormResul)+'' )
                if cantFormResul == varData.estadoIniNum:
                    resulResulForm = item.id
                    break
                    pass
                pass
            pass
        pass
    return resulResulForm


def setCamposForm( idFormulario ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario = idFormulario
    camposResul          = segment.setCamposFormulario()
    return camposResul


def setAcuerdoForm( data, id_interacion ):
    import json
    res = json.loads(data)
    intAsesor     = InteraccionesAsesor( db )
    varData            = DataGlobal()
    # logsMostrar( 'info', 'setAcuerdoForm => 539 '+str(type(res))+'' )
    # logsMostrar( 'info', 'setAcuerdoForm => 540 '+str(res)+'' )
    intAsesor.define_table()
    intAsesor.id_interacion = id_interacion
    intAsesor.telefono          = 0
    intAsesor.numero_producto   = 0
    intAsesor.valor_acordado    = 0
    intAsesor.cuotas_acordadas  = 0
    intAsesor.interes_acordados = 0
    intAsesor.fecha_pago        = 0
    intAsesor.punto_pago        = 0
    for item in res:
        # print( item['nombreCampo']+' => '+str(item['valorCampo']) )
        if item['nombreCampo'] == varData.telefonoPD:
            intAsesor.telefono   = item['valorCampo']
        elif item['nombreCampo'] == varData.valor_acordadoPD:
            intAsesor.valor_acordado   = item['valorCampo']
        elif item['nombreCampo'] == varData.cuotas_acordadasPD:
            intAsesor.cuotas_acordadas   = item['valorCampo']
        elif item['nombreCampo'] == varData.interes_acordadosPD:
            intAsesor.interes_acordados   = item['valorCampo']
        elif item['nombreCampo'] == varData.fecha_pagoPD:
            intAsesor.fecha_pago   = item['valorCampo']
        elif item['nombreCampo'] == varData.numero_productoPD:
            intAsesor.numero_producto   = item['valorCampo']
        else:
            intAsesor.punto_pago   = item['valorCampo']
            pass
        pass
    idAcuerdoForm  = intAsesor.saveAcuerdosInteraccion()
    # logsMostrar( 'info', 'setAcuerdoForm => 572 '+str(idAcuerdoForm)+'' )
    return idAcuerdoForm
