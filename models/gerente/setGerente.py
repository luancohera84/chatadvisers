# -*- coding: utf-8 -*-
from datetime import datetime, time, date, timedelta
from empresas import Empresas, Clientes, Segmentos
from usuariosAsignar import UsuariosAsig
from _clasFunt import ConexionStrauss
import pandas as pd
import numpy as np
import json
import os, sys
import subprocess
# reload(sys)
# sys.setdefaultencoding( "latin-1" )


# Config resultados

def setAsignarResultadoSegmentos( idResultado, resultado, idSegmento ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento   = idSegmento
    segment.idResultadoF = idResultado
    segment.resultadoFor = resultado
    segment.userCreate   = idUser
    setInsertAsig        = segment.getCreateResultadosSegmento()
    return setInsertAsig


def validateResultadoSegmentos( idSegemnto, idResultado ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento   = idSegemnto
    segment.idResultadoF = idResultado
    setCanttAsig        = segment.setCountResultadosSegmento()
    return setCanttAsig



def setListadoEmp():
    logsMostrar( 'info', 'inicia peticiona modelos => ')
    asesorSeg            = UsuariosAsig( db )
    logsMostrar( 'info', 'Modelo asesorSeg asesorSeg =>')
    asesorSeg.idUsuario  = idUser
    logsMostrar( 'info', 'asesorSeg.idUsuario => '+str(asesorSeg.idUsuario)+' ')
    asesorSeg.define_table()
    logsMostrar( 'info', 'Definimos tablas')
    listEmpresasOrd      = asesorSeg.infoEmpresasAsesor()
    logsMostrar( 'info', 'Respuesta modelo listEmpresasOrd => '+str(listEmpresasOrd)+' ')
    return listEmpresasOrd



def setListadoClientesEmpresas( idCompany ):
    company            = Empresas( db )
    customers          = Clientes( db )
    company.define_table()
    customers.define_table()
    customers.idEmpresa = idCompany
    listClientesEmpresasOrd = customers.getListarIdEmpresaClientes()
    return listClientesEmpresasOrd




def setListadoSegmentosClientes( idCustomers ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idCliente = idCustomers
    listSegmentosClientesOrd  = segment.getListarIdClienteSegmentos()
    return listSegmentosClientesOrd



def setConfigSegmento( idSegment ):
    from clientesUsers import ClientesUsers
    cltInfo             = ClientesUsers( db )
    cltInfo.define_table()
    listadoCamposOferta = []
    tmp = db( db.info_cliente.id > 0 )._select( db.info_cliente.ALL )
    tmp2 = str(tmp).replace('SELECT','').replace('FROM `info_cliente` WHERE (`info_cliente`.`id` > 0);','').replace('`info_cliente`.','').replace('`','"').replace('`','"')
    listadoCamposOferta = sorted(tmp2.split(), reverse=False)
    return listadoCamposOferta


def setConfigSegHorarios( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    listadoHorariosSeg  = []
    segment.idSegmento = idSegment
    listadoHorariosSeg  =  segment.setListHorariosSeg()
    return listadoHorariosSeg


def setCreateHorarioSegmento( idSegment,nomHorario,diaIniHr,horaIniHr,horaFinHr,userCreate, diaFestivos, diaLabora ):
    # logsMostrar( 'info', 'setCreateHorarioSegmento 65 => idSegment '+str(idSegment)+'')
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento   = idSegment
    segment.nomHorario   = nomHorario
    segment.diaIniHr     = diaIniHr
    segment.horaIniHr    = horaIniHr
    segment.diaLabora    = diaLabora
    segment.horaFinHr    = horaFinHr
    segment.userCreate   = userCreate
    segment.diaFest      = diaFestivos
    idSegHorario         = segment.getCreateHorarioSegmento()
    return idSegHorario


def setCreateSmsPrestSegmento( idSegment,nomSmsPrest,tipoSmsPrest,smsPrest, userCreate ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento  = idSegment
    segment.nomSms       = nomSmsPrest
    segment.tipoSmsPr    = tipoSmsPrest
    segment.smsPr        = smsPrest
    segment.userCreate   =  userCreate
    idSegSmsPrest        = segment.getCreateSmsPrestbSegmento()
    return idSegSmsPrest




def setEditarSmsPrestSegmento( idSms,nomSmsPrestUp,tipoSmsPrestUp,smsPrestUp, userCreateUp ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSmsPret    = idSms
    segment.nomSms       = nomSmsPrestUp
    segment.tipoSmsPr    = tipoSmsPrestUp
    segment.smsPr        = smsPrestUp
    segment.userCreate   = userCreateUp
    idSegSmsPrestUp      = segment.getUpdateSmsPrestbSegmento()
    return idSegSmsPrestUp




def setEditarHorarioSegmento( idHorario,nomHorarioEditar,diaIniHrEditar,horaIniHrEditar,horaFinHrEditar,diaFestivosEditar, diaLaboraEditar, userCreateUp ):
    logsMostrar( 'info', 'setEditarHorarioSegmento 131 => idHorario '+str(idHorario)+'')
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idHorario    = idHorario
    segment.nomHorario   = nomHorarioEditar
    segment.diaIniHr     = diaIniHrEditar
    segment.horaIniHr    = horaIniHrEditar
    segment.horaFinHr    = horaFinHrEditar
    segment.diaLabora    = diaLaboraEditar
    segment.userCreate   = userCreateUp
    segment.diaFest      = diaFestivosEditar
    idSegHorarioUp       = segment.getUpdateHorarioSegmento()
    return idSegHorarioUp


def setConfigSegContextos( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento = idSegment
    listadoContextosSeg  = []
    return listadoContextosSeg


def setConfigSegSmsPrest( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento = idSegment
    listadoContextosSeg  = segment.setListSmsPrebSeg()
    return listadoContextosSeg


def setValidateCampoAsignado( idSegemnto, campoReal ):
    segment                         = Segmentos( db )
    segment.idSegmento             = idSegemnto
    segment.nomCampoReal            = campoReal
    validaTrueOrFalse,idFielAsig    = segment.getValidateCampoAsig()
    return validaTrueOrFalse

def setAsignarCamposSegmentos( data ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento  = data.idSegmento
    segment.nomCampoReal = data.nomCampoReal
    segment.nomCampoRepr = data.campoRespresenta
    segment.userCreate   = idUser
    setInsertAsig        = segment.getCreateCampoSegmento()
    return setInsertAsig


def setQuuitarCamposSegmentos( data ):
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento  = data.idSegmento
    segment.nomCampoReal = data.nomCampoReal
    segment.nomCampoRepr = data.campoRespresenta
    setDeleteAsig        = segment.deleteAsigFieldSeg()
    return setDeleteAsig


def setListadoEmpresasusuarios( idUser ):
    listEmpresasUser = []
    company            = Empresas( db )
    company.define_table()
    company.idEmpresa  = 0
    infoCompany        = company.getListarEmpresas()
    return listEmpresasUser



def setValidateEmpresasusuarios( idEmpresa, idUser ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idEmpresa  = idEmpresa
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    listEmpresasUser     = asesorSeg.validaAsigbacionEmpresaUsers()
    return listEmpresasUser



def setValidateClienteUsuarios( idCliente, idUser ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idCliente  = idCliente
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    listClienteUser      = asesorSeg.validaAsigbacionCleinteUsers()
    return listClienteUser


def setValidateSegmentoUsuarios( idSegmento, idUser ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idSegmento  = idSegmento
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    listSegmentoUser      = asesorSeg.validaAsigbacionSegmentoUsers()
    return listSegmentoUser


def infoEmpresaListAsigAs( idUser ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    listEmpresas         = []
    listEmpresas         = asesorSeg.infoEmpresasAsesor()
    return listEmpresas

def setListadoEmpresas():
    company            = Empresas( db )
    company.define_table()
    company.idEmpresa  = 0
    listEmpresasOrd    = company.getListarEmpresas()
    return listEmpresasOrd


def setAsignarUsuEmpresa( idEmpresa, idUser, tipoGes, opc ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idEmpresa  = idEmpresa
    idAseAsig            = 0
    if int(opc) == 1:
        clientesAsig  = setListadoClientesEmpresasUsu( idEmpresa )
        if len(clientesAsig) > 0:
            for item in clientesAsig:
                asesorSeg.idCliente  = item.id
                listSegmentos = setListadoSegmentosClientesUsu( item.id )
                if len(listSegmentos) > 0:
                    for seg in listSegmentos:
                        asesorSeg.idSegmento = seg.id
                        asesorSeg.define_table()
                        asesorSeg.idUsuario  = idUser
                        idAseAsig            = asesorSeg.getAsigUsuario()
                        pass
                    pass
                pass
            pass
    elif int(opc) == 2:
        print('Listar clientes')
    else:
        # Desasidnar empresa a usuario
        asesorSeg.define_table()
        asesorSeg.idUsuario  = idUser
        idAseAsig            = asesorSeg.getEliminarUsuario()
        pass
    return idAseAsig



def setListadoClientesEmpresasUsu( idCompany ):
    company            = Empresas( db )
    customers          = Clientes( db )
    company.define_table()
    customers.define_table()
    customers.idEmpresa = idCompany
    listClientesEmpresasOrd = customers.getListarIdEmpresaClientes()
    return listClientesEmpresasOrd



def setListadoSegmentosClientesUsu( idCustomers ):
    segment            = Segmentos( db )
    segment.define_table()
    segment.idCliente = idCustomers
    listSegmentosClientesOrd  = segment.getListarIdClienteSegmentos()
    return listSegmentosClientesOrd


def setAsigClientesSegmentoUsu( idCompany, idCustomers, idSegment, idUser, opcStatus  ):
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idEmpresa  = idCompany
    asesorSeg.idCliente  = idCustomers
    asesorSeg.idSegmento = idSegment
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    if int(opcStatus) == 0:
        #  Asignar segmento a usuario
        insertRegAsi = asesorSeg.getAsigUsuario()
    else:
        #  Desasignar segmento a usuario
        insertRegAsi =  asesorSeg.getEliminarUsuarioSegmento()
        pass
    return insertRegAsi


def listUsersAsig():
    listadoUsers = []
    asesorSeg            = UsuariosAsig( db )
    asesorSeg.idUsuario  = idUser
    asesorSeg.define_table()
    tmpSegAsigUsers      = asesorSeg.infoSegmentosAsigUsers()
    if tmpSegAsigUsers:
        for item in tmpSegAsigUsers:
            asesorSeg.idSegmento = item.id_segmento
            tmpUserAsiSeg = asesorSeg.infoUserAsigSegmento()
            if tmpUserAsiSeg:
                for itemAse in tmpUserAsiSeg:
                    listadoUsers.append(itemAse.id_asesor)
                    pass
                pass
            pass
        pass
    return listadoUsers


def setcontexChatBot( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento = idSegment
    listContexChatBot  = segment.setContextChatbotSegId()
    logsMostrar( 'info', 'setcontexChatBot => listContexChatBot '+str(listContexChatBot)+'')
    return listContexChatBot



def setInfoDatacontexChatBot( idContNodo ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    infoDataContex     = []
    segment.idConChat  = idContNodo
    infoDataChatBot    = segment.setContextChatbotConteId()
    if infoDataChatBot:
        for item in infoDataChatBot:
            infoDataContex.append( 
                dict(
                    nodo_contexto       = item.nodo_contexto,
                    nodo_nombre         = item.nodo_nombre,
                    nodo_mensaje        = item.nodo_mensaje,
                    nodo_mensaje_error  = item.nodo_mensaje_error,
                    nodo_tipo           = item.nodo_tipo,
                    nodo_directo        = item.nodo_directo,
                    nodo_num_opciones   = item.nodo_num_opciones,
                    nodo_opciones       = item.nodo_opciones,
                    nodo_id_resultado   = item.nodo_id_resultado
                )
            )
            pass
        pass
    return infoDataContex


def setcontexChatAdv( idSegment ):
    listContexChatAdv = []
    return listContexChatAdv



def setResultadoSegmentos( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento = idSegment
    dataHomologaciones = []
    dataSegmento = segment.getListarIdSegmento()
    if dataSegmento:
        # logsMostrar( 'info', 'setResultadoSegmentos gerente => dataSegmento.nombre_segmento '+str(dataSegmento.nombre_segmento)+'' )
        dataConexion = empresaConsultingConexion( dataSegmento.empresa_segmento )
        # logsMostrar( 'info', 'setResultadoSegmentos gerente => dataConexion '+str(dataConexion[0])+'' )
        if len(dataConexion) > 0:
            conexiones                   = ConexionStrauss()
            conexiones.nomEmpresa        = empresaIdConsulting( dataSegmento.empresa_segmento )
            conexiones.nomCliente        = clienteIdConsulting( dataSegmento.cliente_segmento )
            conexiones.nomSegmento       = dataSegmento.nombre_segmento
            conexiones.userStaruss       = dataConexion[0]['empresas_base_usuario']
            conexiones.bDStrauss         = dataConexion[0]['empresas_base']
            conexiones.hostStrauss       = dataConexion[0]['empresas_base_dominio']
            conexiones.keyPrivateStrauss = dataConexion[0]['empresas_base_key']
            dataHomologaciones           = conexiones.datosDBHomologa()
            # logsMostrar( 'info', 'setResultadoSegmentos gerente => dataHomologaciones '+str(dataHomologaciones)+'' )
            pass
        pass
    return dataHomologaciones


def setFormularioSegmentos( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    listadoFormulariosSeg  = []
    segment.idSegmento = idSegment
    listadoFormulariosSeg  =  segment.setListFormularioSegmento()
    return listadoFormulariosSeg


def setPuntosPagoSegmentos( idSegment ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    listadoPuntoPagoSeg  = []
    segment.idSegmento   = idSegment
    listadoPuntoPagoSeg  =  segment.getListPuntoSeg()
    return listadoPuntoPagoSeg

def getAgregarPuntoPago( idSegment, puntoPago ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento       = idSegment
    segmentInfo              = segment.getListarIdSegmento()
    segment.idCliente        = segmentInfo.cliente_segmento
    segment.idEmpresa        = segmentInfo.empresa_segmento
    segment.punto_pago       = str(puntoPago).lower()
    segment.userCreate       = idUser
    idSegPunto               = segment.getCreatePuntoSegmento()
    return idSegPunto


def getDeletePuntoPago( idSegment, puntoPago ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento       = idSegment
    segment.punto_pago       = str(puntoPago).lower()
    idSegPunto               = segment.getDeletePuntoSeg()
    return idSegPunto


def setInstanciasSegmentos( idSegment ):
    listadoInstancias  = []
    data  = infoSegClienteEmpresa( idSegment, 'segment' )
    if len(data) > 0:
        from _clasFunt import DataGlobal, ConexionWhast
        conexApiWhat      = ConexionWhast( '', data['company'], data['customers'], data['segment'], '' )
        listadoInstancias  = conexApiWhat.datosBDInstance()
        pass
    return listadoInstancias


def setInstanciasId( data ):
    listadoInstancias  = []
    if data.idIntance:
        from _clasFunt import DataGlobal, ConexionWhast
        conexApiWhat            = ConexionWhast( '', '', '', '', '' )
        conexApiWhat.idInstance = data.idIntance
        infoInstancia           = conexApiWhat.datosBDInstanceId()
        pass
    return infoInstancia



def cantResultadosFormulario( idFormulario ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario = idFormulario
    cantResul            = segment.setCantResulInFormulario()
    return cantResul



def getResultAgregado( idResultado, resultado, idFormulario ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario = idFormulario
    segment.idResultadoF = idResultado
    segment.resultadoFor = resultado
    resulCant = segment.setCountFormularioResul()
    return resulCant


def getAgregarQuitarResultado( idResultado, resultado, idFormulario ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario = idFormulario
    segment.idResultadoF = idResultado
    segment.resultadoFor = resultado
    resulOpFoRes         = segment.setAgregarQuitarResultado()
    return resulOpFoRes


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




def createFormularioPrevio(  idSegment, nombreForm, canCampos ): 
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento         = idSegment
    segment.nomFormulario      = nombreForm
    segment.canCampoFormulario = canCampos
    segment.userCreate         = idUser
    idFormulario  = segment.getCreateFormularioSegmento()
    return idFormulario


def createCampoFormPrevio( idFormulario, tipo_campo, tipo_dato, label, obligatorio, descripcion_campo = '', tamano_texto = 100 ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idFormulario       = idFormulario
    segment.tipo_campo         = tipo_campo
    segment.tipo_dato          = tipo_dato         
    segment.nombre_label       = label
    segment.obligatorio        = obligatorio
    segment.descripcion_campo  = descripcion_campo
    segment.tamano_texto       = tamano_texto
    idCamFormulario            = segment.getCreateCampoForm()
    return idCamFormulario




def setListadoNombreNodos():
    dataNomNodos  = db( db.nombre_nodos.nombre_nodos_estado == True ).select( db.nombre_nodos.ALL )
    return dataNomNodos

def setCamposPruebaContex( idContxChatbot ):
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idConChat  = idContxChatbot
    dataCamps          = []
    dataCTmps          = segment.getCamposPruebaContex()
    if dataCTmps:
        for item in dataCTmps:
            dataCamps.append(
                dict(
                    cantidad_campos = item.cantidad_campos,
                    valores_variables = item.valores_variables
                )
            )
        pass
    return dataCamps
 

def setchangeStatus(  idContxChatbot,nombreContexto, idSegmento,companyText, customersText, segmentText, status ):

    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )

    company.define_table()
    customers.define_table()
    segment.define_table()
    segment.idSegmento = idSegmento
    segment.idConChat  = idContxChatbot
    segment.userCreate = idUser
    statusActiv        = 0
    logsMostrar( 'info', 'int(status) => setchangeStatus 578 '+str(int(status))+'')
    if int(status) ==  0:
        statusActiv = segment.setContextChatbotSegStatus()
        pass
    logsMostrar( 'info', 'statusActiv => setchangeStatus 582 '+str(int(statusActiv))+'')
    if statusActiv == 0:
        dataCont           = segment.setContextChatbotId()
        logsMostrar( 'info', 'dataCont => setchangeStatus 585 '+str(dataCont)+'')
        nameJson           = str(companyText)+'_'+str(customersText)+'_'+str(segmentText)+'.json'
        logsMostrar( 'info', 'nameJson => setchangeStatus 587'+str(nameJson)+'')
        if dataCont:
            resulIdContex  = 1
            if int(status) == 1:
                segment.status  = False
                segment.nameNew = idContxChatbot+'.json'
                resulIdContex   = segment.getchangeStatus()
            else:
                segment.status  = True
                segment.nameNew = nameJson
                resulIdContex   = segment.getchangeStatus()
                pass

            if os.path.exists("/var/www/web2py/applications/init/static/contextosChatbot/"+str(dataCont.contexto_nombre_json)+""):

                subprocess.call(
                    """
                        chmod -R 777 /var/www/web2py/applications/init/static/contextosChatbot/"""+str(dataCont.contexto_nombre_json)+"""
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        mv /var/www/web2py/applications/init/static/contextosChatbot/"""+str(dataCont.contexto_nombre_json)+"""   /var/www/web2py/applications/init/static/contextosChatbot/"""+str(segment.nameNew)+"""
                    """,
                    shell=True
                )


                subprocess.call(
                    """
                        chmod -R 777 /var/www/web2py/applications/init/static/contextosChatbot/"""+str(segment.nameNew)+"""
                    """,
                    shell=True
                )

                if os.path.exists("/opt/chatbot/contextos/"+str(nameJson)+""):
                    subprocess.call(
                        """
                            chmod -R 777 /opt/chatbot/contextos/"""+str(nameJson)+"""
                        """,
                        shell=True
                    )

                    subprocess.call(
                        """
                            rm -r /opt/chatbot/contextos/"""+str(nameJson)+"""
                        """,
                        shell=True
                    )
                    pass
                
                if int(status) == 1:
                    if os.path.exists("/opt/chatbot/contextos/"+str(segment.nameNew)+""):
                        subprocess.call(
                            """
                                chmod -R 777 /opt/chatbot/contextos/"""+str(segment.nameNew)+"""
                            """,
                            shell=True
                        )

                        subprocess.call(
                            """
                                rm -r /opt/chatbot/contextos/"""+str(segment.nameNew)+"""
                            """,
                            shell=True
                        )
                        pass
                else:
                    if os.path.exists("/opt/chatbot/contextos/"+str(dataCont.contexto_nombre_json)+""):
                        subprocess.call(
                            """
                                chmod -R 777 /opt/chatbot/contextos/"""+str(dataCont.contexto_nombre_json)+"""
                            """,
                            shell=True
                        )

                        subprocess.call(
                            """
                                rm -r /opt/chatbot/contextos/"""+str(dataCont.contexto_nombre_json)+"""
                            """,
                            shell=True
                        )
                        pass
                    pass

                subprocess.call(
                    """
                        cp /var/www/web2py/applications/init/static/contextosChatbot/"""+str(segment.nameNew)+"""  /opt/chatbot/contextos/
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        chmod -R 777 /opt/chatbot/contextos/"""+str(segment.nameNew)+"""
                    """,
                    shell=True
                )
            else:
                logsMostrar( 'error', 'no haty infi => setchangeStatus ')
                pass
            pass
        return resulIdContex
    else:
        statusActiv = -1
        return statusActiv
        pass


def setProcesoJson( nodos, opcionesNodos, compoNodos, nomContexto, idSegmento, companyText, customersText, segmentText, canNodos ):
    
    # logsMostrar( 'info', 'setProcesoJson => nodos '+str(nodos)+'')
    # logsMostrar( 'info', 'setProcesoJson => nodos type '+str(type(nodos))+'')
    # logsMostrar( 'info', 'setProcesoJson => opcionesNodos '+str(opcionesNodos)+'')
    # logsMostrar( 'info', 'setProcesoJson => type(opcionesNodos) '+str(type(opcionesNodos))+'')
    # logsMostrar( 'info', 'setProcesoJson => compoNodos '+str(compoNodos)+'')
    # logsMostrar( 'info', 'setProcesoJson => idSegmento '+str(idSegmento)+'')
    # logsMostrar( 'info', 'setProcesoJson => nomContexto '+str(nomContexto)+'')
    # logsMostrar( 'info', 'setProcesoJson => canNodos '+str(canNodos)+'')
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    customers.define_table()
    segment.define_table()
    # nodos = [{'valorCampo': 'Nombre nodo 1', 'identificaCampo': 'nombreNodo1', 'id_nodo': 1}, {'valorCampo': 'Nombre nodo 2', 'identificaCampo': 'nombreNodo2', 'id_nodo': 2}]

    # opcionesNodos = [{'opc': 'Nombre nodo 1', 'nodo': 'inicio'}, {'opc': 'Nombre nodo 2', 'nodo': 'inicio'}, {'opc': 'inicio', 'nodo': 'Nombre_nodo_1'}, {'opc': 'Nombre nodo 2', 'nodo': 'Nombre_nodo_1'}, {'opc': 'despedida', 'nodo': 'Nombre_nodo_1'}, {'opc': 'despedida', 'nodo': 'Nombre_nodo_2'}]


    # compoNodos =  [{'tipoSmsNodo': 'chat', 'resultadoSmsNodo': '70006', 'smsErrorNodo': 'sseeeeeeeeeeeeeeeee', 'directoNodo': '', 'nodo': 'inicio', 'smsNodo': 'sssssssssssssssssssss'}, {'nodo': 'despedida', 'smsNodo': 'rrrrrrrrrrrrrrrrrrrrrrrrr'}, {'tipoSmsNodo': 'chat', 'resultadoSmsNodo': '70014', 'smsErrorNodo': 'tttttttttttttttttttt', 'directoNodo': 'on', 'nodo': 'Nombre_nodo_1', 'smsNodo': 'eeeeeeeeeeeeeeeeeeeeeeeeeeeee'}, {'tipoSmsNodo': 'chat', 'resultadoSmsNodo': '70006', 'smsErrorNodo': 'ttttttttttttttttttttt', 'directoNodo': 'on', 'nodo': 'Nombre_nodo_2', 'smsNodo': 'uuuuuuuuuuuuuuuuuuuuuuuu'}]


    df_compoNodos = pd.DataFrame(compoNodos)

    df_opcionesNodos = pd.DataFrame(opcionesNodos)
    jsonPre = {}

    resulInit = str(companyText)+'_'+str(customersText)+'_'+str(segmentText)+'.json'
    
    segment.idSegmento     =  idSegmento
    segment.nomContBot     =  nomContexto
    segment.cantNodosCont  = int(canNodos) + 2
    segment.nomContBotJson = resulInit
    segment.userCreate     = idUser 
    segment.idConChat      = segment.getCreateContChatBot()
    # logsMostrar( 'info', 'setProcesoJson 532 => segment.idConChat '+str(segment.idConChat)+'')
    resul = str(segment.idConChat)+'.json'
    for index,item in df_compoNodos.iterrows():
        
        data_filter = df_opcionesNodos[df_opcionesNodos['nodo'] == item['nodo']]
        data_filter.reset_index(drop=True, inplace=True)
        # print('data_filter', data_filter)
        dataOpciones = ''
        tmpOpcionesCampo = []
        for indexFil,itemFil in data_filter.iterrows():
            if itemFil['opc'] == 'despedida':
                tmp = itemFil['opc']
            else:
                tmp   = 'nodo_'+str(itemFil['opc']).replace(' ','_').lower()
                pass
            valor = indexFil + 1
            tmpOpcionesCampo.append(tmp)
            finl  = '''''opcion'''+str(valor)+'''' : ' '''+str(tmp)+''' ' ,'''
            
            dataOpciones += finl
            pass
        
        smsNormal = str(item['smsNodo']).split(' ')
        # logsMostrar( 'info', 'smsNormal 758 => smsNormal '+str(smsNormal)+'')
        smsNormalFinal = ''
        for itemNormal in smsNormal:
            # logsMostrar( 'info', 'smsNormal 761 => itemNormal '+str(itemNormal)+'')
            if itemNormal[:2] == '[<':
                emoji_unicode = itemNormal.replace('[<','').replace('>]','')
                emoji_unIni   = emoji_unicode.split("-")
                emoji_chars   = ""
                for i in emoji_unIni:
                    emoji_chars += chr(int(i, 16))
                    pass
                smsNormalFinal = smsNormalFinal+' '+str(emoji_chars)
            elif itemNormal[:2] == '[{':
                emoji_unicode = itemNormal.replace('[{','').replace('}]','')
                emoji_chars = chr(int(str(emoji_unicode), 16))
                smsNormalFinal = smsNormalFinal+' '+str(emoji_chars)
            else:
                smsNormalFinal = smsNormalFinal+' '+str(itemNormal)
                pass
            pass
        smsError = str(item['smsErrorNodo']).split(' ')
        if smsError:
            smsErrorFinal = ''
            for itemErr in smsError:
                if itemErr[:2] == '[<':
                    emoji_unicodeErrN = itemErr.replace('[<','').replace('>]','')
                    emoji_unIniErr   = emoji_unicodeErrN.split("-")
                    emoji_charsErrN   = ""
                    for i in emoji_unIniErr:
                        emoji_charsErrN += chr(int(i, 16))
                        pass
                    smsErrorFinal = smsErrorFinal+' '+str(emoji_charsErrN)
                elif itemErr[:2] == '[{':
                    emoji_unicodeErrE = itemErr.replace('[{','').replace('}]','')
                    emoji_charsErrE = chr(int(str(emoji_unicodeErrE), 16))
                    smsErrorFinal = smsErrorFinal+' '+str(emoji_charsErrE)
                else:
                    smsErrorFinal = smsErrorFinal+' '+str(itemErr)
                    pass
                pass
        else:
            smsErrorFinal = ''
            pass
    
        if item['nodo'] == 'despedida':
            print('smsNormalFinal despedida =>', smsNormalFinal )
            jsonPre[str(item['nodo']).replace(' ','_').lower()] = []
            jsonPre[str(item['nodo']).replace(' ','_').lower()].append({
                'mensaje': smsNormalFinal
            })
            if item['directoNodo'] == 'on':
                directo = 'SI'
            else:
                directo = 'NO'
                pass
        else:
            jsonPre['nodo_'+str(item['nodo']).replace(' ','_').lower()] = []
            # logsMostrar( 'info', 'tem[directoNodo] => 607 '+str(item['directoNodo'])+'')
            if item['directoNodo'] == 'on':
                directo = 'SI'
            else:
                directo = 'NO'
                pass
            jsonPre['nodo_'+str(item['nodo']).replace(' ','_').lower()].append({
                'mensaje':  smsNormalFinal, #replaceAcentos( smsNormalFinal ),
                'mensaje_error': smsErrorFinal, #replaceAcentos( smsErrorFinal ),
                'tipo': item['tipoSmsNodo'],
                'directo': directo,
                'num_opciones':str(len(data_filter)),
                '<>':''+str(dataOpciones)+'',
                'id_resultado':int(item['resultadoSmsNodo'])
            })
            pass
        
        if segment.idConChat:
            segment.nodo_nombre        = item['nodo']
            segment.nodo_mensaje_error = smsErrorFinal, #replaceAcentos( smsErrorFinal )
            segment.nodo_mensaje       = smsNormalFinal, #replaceAcentos( smsNormalFinal )
            segment.nodo_tipo          = item['tipoSmsNodo']
            segment.nodo_directo       = directo
            segment.nodo_num_opciones  = len(data_filter)
            segment.nodo_opciones      = tmpOpcionesCampo
            segment.nodo_id_resultado  = item['resultadoSmsNodo'] if item['resultadoSmsNodo'] else 0
            segment.userCreate         = idUser
            idNodoCreate               = segment.getCreateNodoIdContexto()
            # logsMostrar( 'info', 'setProcesoJson 532 => idNodoCreate '+str(idNodoCreate)+'')
            pass
        pass
        # json.loads(
        #print('jsonPre', str(jsonPre).replace('<>','').replace("'':",'').replace('[','').replace(']','').replace(',"}','}').replace("' ","'").replace(" ',","',").replace(""""'""","").replace("''","'").replace(",  '}","'}").replace(" '","'"))
        nodos          = str(jsonPre).replace('<>','').replace("'':",'').replace('[','').replace(']','').replace(',\",',',').replace("\"''","'").replace(",''",",'").replace(" ' ,","',").replace("' ","'").replace("'",'"').replace(',"}','}').replace(' ",','",').replace(' ":','":')
        #.replace(',"}','}').replace("' ","'").replace(" ',","',").replace(""""'""","").replace("''","'").replace(",  '}","'}").replace(" '","'")
        #.replace("'",'"')
        # print('nodos',json.dumps(json.loads(nodos)))
        dataJson = json.dumps(nodos ,indent=4)
        # logsMostrar( 'info', 'setProcesoJson 851 => dataJson '+str(dataJson)+'')
        text  = str(dataJson).replace('"{','{').replace('}"','}').replace('\\\"','"').replace('\"','"')
        # logsMostrar( 'info', 'setProcesoJson 853 => texto '+str(text)+'')
        tex = json.loads(text)
        # tex = json.loads(r"""{ "entry":{ "etag":"W/\"A0UGRK47eCp7I9B9WiRrYU0.\"" } }""")
        # logsMostrar( 'info', 'setProcesoJson 856 => texto '+str(type(tex))+'')
        texto = text #str(text).replace("u'","'").replace("\\t",'').replace("\\r",'').replace("\\",'').replace("'",'"').replace("*","'")
        # logsMostrar( 'info', 'setProcesoJson 858 => texto '+str(texto)+'')
        with open('/var/www/web2py/applications/init/static/contextosChatbot/'+str(resul)+'', 'w',encoding='latin') as file:
            file.write(texto)
            pass

        # logsMostrar( 'info', 'setProcesoJson 863 => archivo json creado con exito')

        archivoJson = ''

        with open('/var/www/web2py/applications/init/static/contextosChatbot/'+str(resul)+'', "rt",encoding='latin') as file:
            archivoJson = file.read()
            pass

        with open('/var/www/web2py/applications/init/static/contextosChatbot/'+str(resul)+'', "wt",encoding='latin') as file:
            archivoJson = archivoJson.replace("<salto>",'\\n')
            #dataJson = json.dumps(archivoJson)
            #text  = str(dataJson).replace('"{','{').replace('}"','}').replace('\\\"','"').replace('\"','"').replace("'\n'n","'\'n")
            file.write(archivoJson)
            pass

        # logsMostrar( 'info', 'setProcesoJson 878 => archivo json leido y <salto> reemplazado con exito')

        if os.path.exists("/var/www/web2py/applications/init/static/contextosChatbot/"+str(resul)+""):
            subprocess.call(
                """
                    chmod -R 777 /var/www/web2py/applications/init/static/contextosChatbot/"""+str(resul)+"""
                """,
                shell=True
            )
            subprocess.call(
                """
                    cp /var/www/web2py/applications/init/static/contextosChatbot/"""+str(resul)+"""  /opt/chatbot/contextos/contexts/
                """,
                shell=True
            )
            subprocess.call(
                """
                    chmod -R 777 /opt/chatbot/contextos/contexts/"""+str(resul)+"""
                """,
                shell=True
            )
            pass
    return str(resul)