# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos



def setListadoEmpresas():
    company            = Empresas( db )
    customers          = Clientes( db )
    segment            = Segmentos( db )
    company.define_table()
    company.idEmpresa  = 0
    listEmpresasOrd    = company.getListarEmpresas()
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

