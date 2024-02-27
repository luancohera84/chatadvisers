# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import gluon.contrib.simplejson

@auth.requires_login()
def empresas():
    # import socket
    # nombre_equipo = socket.gethostname()
    # logsMostrar( 'info', 'empresas nombre_equipo => '+str(nombre_equipo).replace('-','')+' ' )
    response.title     = T("Listado empresas") 
    response.suBtitle  = T("Dashboard reportes")
    if ( ( userType[0] ==  'Developer' ) | ( userType[0] ==  'Administrador' )):
        infoCompany        = setListadoEmpresas()
    elif userType[0] ==  'Director':
        infoCompany        = setListadoEmpresas()
    elif userType[0] ==  'Gerente':
        infoCompany        = setListadoEmpresas()
    else:
        redirect(URL('error','pageNoPermitida'))
        pass
    return locals()


@auth.requires_login()
def cuerpoReportEmpresa():
    varDatos       = request.vars
    return locals()


@auth.requires_login()
def cargaChatAsignacion():
    varDatos       = request.vars
    cantidadCerrados, cantidadAsig   = setCargaChatAsignacion( varDatos.idEmpresa, varDatos.nomEmpresa )
    data = dict(
        cantidadCerrados = cantidadCerrados,
        cantidadAsig     = cantidadAsig
    )
    return gluon.contrib.simplejson.dumps(data)


@auth.requires_login()
def cargaChatCola():
    varDatos       = request.vars
    cantidadCola, cantidadAsig   = setCargaChatCola( varDatos.idEmpresa, varDatos.nomEmpresa )
    data = dict(
        cantidadCola = cantidadCola,
        cantidadAsig     = cantidadAsig
    )
    return gluon.contrib.simplejson.dumps(data)


@auth.requires_login()
def cargaPromedioAtencion():
    varDatos   = request.vars
    data       = promedioAtencion( varDatos.idEmpresa, varDatos.nomEmpresa )
    return str(data)


@auth.requires_login()
def cargaAcuerdos():
    varDatos   = request.vars
    data       = acuerdosPago( varDatos.idEmpresa, varDatos.nomEmpresa )
    return str(data)


@auth.requires_login()
def cargaListaAsesorAtencion():
    varDatos       = request.vars
    data       = setAsesoresAtencion( varDatos.idEmpresa, varDatos.nomEmpresa )
    return gluon.contrib.simplejson.dumps(data)


@auth.requires_login()
def buscarReporte():
    varDatos       = request.vars
    data           = setDescargaGestion( varDatos.idEmpresa, varDatos.nomEmpresa )
    if data == '':
        data = dict(
            file = ''
        )
    else:
        data = dict(
            file = data
        )
        pass
    return gluon.contrib.simplejson.dumps(data)

def limpiarReporte():
    varDatos       = request.vars
    logsMostrar( 'info', 'limpiarReporte  varDatos=> '+str(varDatos)+' ' )
    setlimpiarReporte( varDatos.file )
    pass

@auth.requires_login()
def gestionesAsig():
    varDatos   = request.vars
    # logsMostrar( 'info', 'gestionesAsig  varDatos=> '+str(varDatos)+' ' )
    infoGestiones = setGestionesAsig( varDatos.idEmpresa )
    return locals()


@auth.requires_login()
def chatClienteGestion():
    varDatos            = request.vars
    response.suBtitle   = T("Dashboard Asesor")
    response.title      = T(""+str(varDatos.nCustomer).capitalize()+" - Chat Gestiones ") 
    return locals()