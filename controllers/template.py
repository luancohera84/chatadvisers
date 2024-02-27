#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

import gluon.contrib.simplejson
from _clasFunt import DataGlobal

@auth.requires_login()
def cambioEstado():
    varGl          = DataGlobal()
    varDatos       = request.vars
    idRegistro     = 0
    logsMostrar( 'info', varDatos )
    if session.auth.user.tipo == ['Asesor']:
        tmpCambioEstado = changeStatusAdviser( varGl.estadoFin,varDatos.idUserClt )
        print('Salida asesor', tmpCambioEstado)
        # idCambioEstado = estadoEmpresaAsesor( varDatos.estado, varDatos.empresaClt,varDatos.idUserClt, varDatos.idUserClt )
        # datosAsesor    = datosEmpleado( session.auth.user.id )
        # print('datosAsesor colaborador', datosAsesor)
        # sms = "rTime.notifyMe('Notificacion de prueba');" 
        # print('sms', sms)
        # setRtime(sms,'gerente_'+str(session.auth.user.empresa)+'_'+str(session.auth.user.cliente)+'_'+str(session.auth.user.sucursal))
        # print("idCambioEstado ", idCambioEstado)
        # enviarSmsRT( 'admin_chatbot', sms )
        idCambioEstado = 1
    else:
        idCambioEstado = 1
        pass
    # sms = "rTime.notifyMe('Notificacion de prueba');"
    # enviarSmsRT( 'admin_chatbot', sms )
    if idCambioEstado:
        idRegistro = idCambioEstado
        return str(idRegistro)
    else:
        return str(idRegistro)
    pass


@auth.requires_login()
def updateEstado():
    varDatos       = request.vars
    idRegistro     = 0
    logsMostrar( 'info', 'updateEstado => '+str(varDatos)+'' )
    if varDatos.opc == 'empresa':
        idRegistro = setUpEstadoCompany( varDatos.idParm, varDatos.estadoActual )
    elif varDatos.opc == 'cliente':
        idRegistro = setUpEstadoCustomer( varDatos.idParm, varDatos.estadoActual )
    elif varDatos.opc == 'segmento':
        idRegistro = setUpEstadoSegment( varDatos.idParm, varDatos.estadoActual )
    elif varDatos.opc == 'horario':
        idRegistro = setUpEstadoHorario( varDatos.idParm, varDatos.estadoActual )
    elif varDatos.opc == 'smsPrest':
        idRegistro = setUpEstadoSmsPrest( varDatos.idParm, varDatos.estadoActual )
    else:
        idRegistro = setUpEstadoUsers( varDatos.idParm, varDatos.estadoActual )
        pass
    return str(idRegistro)


@auth.requires_login()
def updateNombre():
    varDatos       = request.vars
    idRegistro     = 0
    # logsMostrar( 'info', 'updateNombre => '+str(varDatos)+'' )
    if varDatos.opc == 'empresa':
        idRegistro = setUpNombreCompany( varDatos.idParm, varDatos.nombreCambioPaVal )
    elif varDatos.opc == 'cliente':
        idRegistro = setUpNombreCustomer( varDatos.idParm, varDatos.nombreCambioPaVal )
    elif varDatos.opc == 'segmento':
        idRegistro = setUpNombreSegment( varDatos.idParm, varDatos.nombreCambioPaVal )
    else:
        idRegistro = setUpNombreUsers( varDatos.idParm, varDatos.emailUsuarioUp, varDatos.passwordUsuarioUp  )
        pass
    return str(idRegistro)

@auth.requires_login()
def chatServicio():
    varDatos  = request.vars
    datos     = setChatServicio( varDatos.idClientePlaf )
    return gluon.contrib.simplejson.dumps(datos)