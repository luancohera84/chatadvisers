# -*- coding: utf-8 -*-

@auth.requires_login()
def listado():
    if ( ( userType[0] ==  'Developer' ) | ( userType[0] ==  'Administrador' )):
        response.title     = T("Listado empresas") 
        response.suBtitle  = T("Dashboard empresas")
        infoCompany        = setListadoEmpresas()
    elif userType[0] ==  'Director':
        response.title     = T("Listado empresas") 
        response.suBtitle  = T("Dashboard empresas")
        infoCompany        = setListadoEmpresas()
    else:
        redirect(URL('error','pageNoPermitida'))
        pass
    return locals()


@auth.requires_login()
def infoEmpresa():
    response.title     = T("Listado empresas") 
    response.suBtitle  = T("Dashboard empresas")
    data               = request.vars
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
    response.title     = T("Listado empresas") 
    response.suBtitle  = T("Dashboard empresas")
    data               = request.vars
    listadoSegmentos   = []
    listadoSegmentos   = setListadoSegmentosClientes( data.idCliente )
    if data.idSegmento:
        listadoCamposOferta = setConfigSegmento( data.idSegmento )
        pass
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
