# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos
from usuariosAsignar import UsuariosAsig


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
                        asesorSeg.tipoUser   = db.auth_user[idUser].tipo[0]
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