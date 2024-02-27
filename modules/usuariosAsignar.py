from cmath import log
from email.policy import default
from gluon import *
from _clasFunt import InfoLogs
from _clasFunt import DataGlobal
from empresas import Empresas, Clientes, Segmentos

class UsuariosAsig:
    
    def __init__( self, db ):
        self.db               = db
        self.idUsuario        = 0
        self.tipoUser         = ''
        self.idEmpresa        = ''
        self.idCliente        = ''
        self.idSegmento       = ''

    def define_table( self ):
        try:
            varGl     = DataGlobal()
            db = self.db
            db.define_table('asesores_empresas',
                Field('id_empresa','integer'),
                Field('id_cliente','integer'),
                Field('id_segmento','integer'),
                Field('id_asesor','integer'),
                Field('tipo_usuario'),
                Field('estado',default=True),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer')
            )

            db.define_table('asesores_bolsa',
                Field('id_segmento','integer'),
                Field('id_asesor','integer'),
                Field('fecha_asignacion','integer',default=varGl.estadoIniNum),
                Field('hora_creacion','integer',default=varGl.estadoIniNum)
            )

            db.define_table('asesores_bolsa_historica',
                Field('id_segmento','integer'),
                Field('id_asesor','integer'),
                Field('fecha_asignacion','integer',default=varGl.estadoIniNum),
                Field('hora_creacion','integer',default=varGl.estadoIniNum)
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table asesores_empresas asesores_bolsa asesores_bolsa_historica => '+str(e)+'' )
            # logs.logFile()
            return False
            pass
    
    def getAsigUsuario( self ):
        db = self.db
        try:
            varGl     = DataGlobal()
            idAsigAsesor = db.asesores_empresas.insert(
                id_empresa       = self.idEmpresa,
                id_cliente       = self.idCliente,  
                id_segmento      = self.idSegmento,
                id_asesor        = self.idUsuario,
                tipo_usuario     = self.tipoUser,
                hora_creacion    = varGl.fechaIntModels,
                fecha_creacion   = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se crear el registro de asignacion empresa asesor para el idAsesor: '+str(self.idUsuario)+'  con id: '+str(idAsigAsesor)+' ' )
            logs.logFile()
        except Exception as e:
            idAsigAsesor  = varGl.estadoFalsNum
            logs = InfoLogs( 'error', 'Error en: getAsigUsuario => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigAsesor


    def getEliminarUsuario( self ):
        db = self.db
        try:
            if db(  ( db.asesores_empresas.id_empresa == self.idEmpresa ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).count() > 0:
                idAsigAsesorDelete = db(  ( db.asesores_empresas.id_empresa == self.idEmpresa ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).delete()
                pass
        except Exception as e:
            idAsigAsesorDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarUsuario => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigAsesorDelete


    def getEliminarEmpresaAs( self ):
        db = self.db
        try:
            if db(  db.asesores_empresas.id_empresa == self.idEmpresa  ).count() > 0:
                idAsigEmpresaDelete = db(  db.asesores_empresas.id_empresa == self.idEmpresa  ).delete()
                pass
        except Exception as e:
            idAsigEmpresaDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarEmpresaAs => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigEmpresaDelete


    def getEliminarUsuarioCliente( self ):
        db = self.db
        try:
            if db(  ( db.asesores_empresas.id_cliente == self.idCliente ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).count() > 0:
                idAsigAsesorClienteDelete = db(  ( db.asesores_empresas.id_cliente == self.idCliente ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).delete()
                pass
        except Exception as e:
            idAsigAsesorClienteDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarUsuarioCliente => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigAsesorClienteDelete


    def getEliminarClienteSegAs( self ):
        db = self.db
        try:
            if db(  db.asesores_empresas.id_cliente == self.idCliente  ).count() > 0:
                idAsigClienteDelete = db(  db.asesores_empresas.id_cliente == self.idCliente  ).delete()
                pass
        except Exception as e:
            idAsigClienteDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarClienteSegAs => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigClienteDelete


    def getEliminarUsuarioSegmento( self ):
        db = self.db
        try:
            if db(  ( db.asesores_empresas.id_segmento == self.idSegmento ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).count() > 0:
                idAsigAsesorSegmentoDelete = db(  ( db.asesores_empresas.id_segmento == self.idSegmento ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).delete()
                pass
        except Exception as e:
            idAsigAsesorSegmentoDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarUsuarioSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigAsesorSegmentoDelete


    def getEliminarSegmentoAs( self ):
        db = self.db
        try:
            if db(  db.asesores_empresas.id_segmento == self.idSegmento  ).count() > 0:
                idAsigSegmentoDelete = db(  db.asesores_empresas.id_segmento == self.idSegmento  ).delete()
                pass
        except Exception as e:
            idAsigSegmentoDelete  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarSegmentoAs => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsigSegmentoDelete

    
    def validaAsigbacionEmpresaUsers( self ):
        db = self.db
        resulEmpUsr   = db(  ( db.asesores_empresas.id_empresa == self.idEmpresa ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).count()
        return resulEmpUsr


    def infoEmpresasAsesor( self ):
        db = self.db
        company           = Empresas( db )
        company.define_table()
        print('Iniciando consulta para el usuario =>', self.idUsuario)
        resulEmpresasAs   = db(  db.asesores_empresas.id_asesor == self.idUsuario  ).select( db.asesores_empresas.fecha_creacion,db.asesores_empresas.hora_creacion,db.asesores_empresas.id_empresa, db.empresas.nombre_empresa,db.empresas.id,db.empresas.estado_empresa,left = ( db.empresas.on( db.empresas.id ==  db.asesores_empresas.id_empresa) ), groupby= db.empresas.nombre_empresa )
        print('resulEmpresasAs =>', resulEmpresasAs)
        return resulEmpresasAs


    def validaAsigbacionCleinteUsers( self ):
        db = self.db
        resulCliUsr   = db(  ( db.asesores_empresas.id_cliente == self.idCliente ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).select( db.asesores_empresas.ALL ).last()
        return resulCliUsr


    def infoClienteEmpresa( self ):
        db = self.db
        customers    = Clientes( db )
        customers.define_table()
        resulClientesAs   = db(  ( db.asesores_empresas.id_empresa == self.idEmpresa ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).select( db.asesores_empresas.fecha_creacion,db.asesores_empresas.hora_creacion,db.asesores_empresas.id_cliente,db.asesores_empresas.id_empresa, db.clientes.nombre_cliente,left = ( db.clientes.on( db.clientes.id ==  db.asesores_empresas.id_cliente ) ), groupby= db.clientes.nombre_cliente )
        return resulClientesAs


    def validaAsigbacionSegmentoUsers( self ):
        db = self.db
        resulSegUsr   = db(  ( db.asesores_empresas.id_segmento == self.idSegmento ) & ( db.asesores_empresas.id_asesor == self.idUsuario ) ).select( db.asesores_empresas.ALL ).last()
        return resulSegUsr


    def infoSegmentosAsigUsers( self ):
        db = self.db
        resulSegmentosAsgUser   = db( db.asesores_empresas.id_asesor == self.idUsuario  ).select( db.asesores_empresas.id_segmento )
        return resulSegmentosAsgUser


    def infoUserAsigSegmento( self ):
        varGl        = DataGlobal()
        db = self.db
        resulUsuarioAsgSeg   = db( ( db.asesores_empresas.id_segmento == self.idSegmento ) & ( db.asesores_empresas.tipo_usuario == varGl.tipoUsuAsesor )  ).select( db.asesores_empresas.id_asesor )
        # print('resulUsuarioAsgSeg', resulUsuarioAsgSeg)
        return resulUsuarioAsgSeg


    def listAsesorOneline( self ):
        try:
            varGl          = DataGlobal()
            idAsesorDisp   = varGl.estadoFalsNum
            db = self.db
            adv_dbStaPlaf  = db.estados_plataforma
            asesoresSeg    = self.infoUserAsigSegmento()
            adv_dbStAdv    = db.estado_asesor
            if len(asesoresSeg) > varGl.estadoFalsNum:
                for itemAse in asesoresSeg:
                    estadoAsesorActual =  db( adv_dbStAdv.estado_asesor_asesor == itemAse.id_asesor ).select( adv_dbStaPlaf.estado_plataforma_nombre, left = ( adv_dbStaPlaf.on( adv_dbStaPlaf.id == adv_dbStAdv.estado_asesor_estado_plataforma) ), groupby = adv_dbStAdv.estado_asesor_asesor ).last()
                    if  estadoAsesorActual:
                        if estadoAsesorActual.estado_plataforma_nombre == varGl.estadoInicial:
                            idAsesorDisp = idAsesorDisp + 1
                            pass
                        pass
                    pass
                pass
        except Exception as e:
            idAsesorDisp  = 0
            logs = InfoLogs( 'error', 'Error en: listAsesorOneline => '+str(e)+'' )
            logs.logFile()
            pass
        return idAsesorDisp

    def listAsesorDisponible( self ):
        try:
            varGl        = DataGlobal()
            idAsesorDisp = varGl.estadoFalsNum
            db = self.db
            adv_dbStaPlaf     = db.estados_plataforma
            asesoresSeg       = self.infoUserAsigSegmento()
            adv_dbStAdv      = db.estado_asesor
            if len(asesoresSeg) > varGl.estadoFalsNum:
                tmpAseBol = db( ( db.asesores_bolsa.id_segmento ==  self.idSegmento ) & ( db.asesores_bolsa.fecha_asignacion == varGl.estadoIniNum  ) ).select( db.asesores_bolsa.id, db.asesores_bolsa.id_asesor ).first()
                # print('tmpAseBol Valida 215 =>', tmpAseBol)
                if tmpAseBol:
                    idAsesorDisp = self.selectAsesor()
                else:
                    # print('Para insertar asesores Valida 219 =>', tmpAseBol)
                    db( db.asesores_bolsa.id_segmento == self.idSegmento ).delete()

                    for itemAse in asesoresSeg:
                        # print('itemAse.id_asesor Valida 223 =>', itemAse.id_asesor)
                        estadoAsesorActual =  db( adv_dbStAdv.estado_asesor_asesor == itemAse.id_asesor ).select( adv_dbStaPlaf.estado_plataforma_nombre, left = ( adv_dbStaPlaf.on( adv_dbStaPlaf.id == adv_dbStAdv.estado_asesor_estado_plataforma) ), groupby = adv_dbStAdv.estado_asesor_asesor ).last()
                        # print('estadoAsesorActual Valida 225 =>', estadoAsesorActual)
                        if  estadoAsesorActual:
                            if estadoAsesorActual.estado_plataforma_nombre == varGl.estadoInicial:
                                # print('Insertar  Valida 228 =>', estadoAsesorActual.estado_plataforma_nombre)
                                tmp = db.asesores_bolsa.insert(id_segmento = self.idSegmento,id_asesor = itemAse.id_asesor)
                                # print('Insertar  Valida 231 =>', tmp)
                                tmpHist = db.asesores_bolsa_historica.insert(id_segmento = self.idSegmento,id_asesor = itemAse.id_asesor)
                                # print('Insertar Histo Valida 233 =>', tmpHist)
                            else:
                                # print('No valido el estado En-Linea estadoAsesorActual Valida 232 =>', estadoAsesorActual)
                                pass
                            pass
                        pass
                    idAsesorDisp = self.selectAsesor()
                    pass
            else:
                logs = InfoLogs( 'info', 'asesoresSegs no hay' )
                logs.logFile()
                pass
            # print('idAsesorDisp listAsesorDisponible 245 =>', idAsesorDisp)
            return idAsesorDisp
        except Exception as e:
            idAsesorDisp  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarClienteSegAs => '+str(e)+'' )
            logs.logFile()
            return idAsesorDisp
            pass

    def selectAsesor( self ):
        try:
            varGl    = DataGlobal()
            asesorId = varGl.estadoFalsNum
            db = self.db
            tmpAseBol = db( ( db.asesores_bolsa.id_segmento ==  self.idSegmento ) & ( db.asesores_bolsa.fecha_asignacion == varGl.estadoIniNum  ) ).select( db.asesores_bolsa.id, db.asesores_bolsa.id_asesor ).first()
            # print('tmpAseBol => selectAsesor 253 =>', tmpAseBol)
            if tmpAseBol:
                # print('tmpAseBol => selectAsesor 255 =>', tmpAseBol)
                # print('tmpAseBol.id => selectAsesor 256 =>', tmpAseBol.id)
                # print('tmpAseBol.id_asesor => selectAsesor 257 =>', tmpAseBol.id_asesor)
                db( db.asesores_bolsa.id == tmpAseBol.id ).update( fecha_asignacion = varGl.fechaIntModels, hora_creacion = varGl.horaIntModels)
                db( ( db.asesores_bolsa_historica.id_asesor == tmpAseBol.id_asesor ) & ( db.asesores_bolsa_historica.fecha_asignacion == varGl.estadoIniNum ) ).update( fecha_asignacion = varGl.fechaIntModels, hora_creacion = varGl.horaIntModels)
                # print('tmpAseBol.id_asesor => selectAsesor 260 =>', tmpAseBol.id_asesor)
                asesorId = tmpAseBol.id_asesor
                # print('asesorId => selectAsesor 262 =>', asesorId)
                pass
            return asesorId
        except Exception as e:
            asesorId  = 0
            logs = InfoLogs( 'error', 'Error en: getEliminarClienteSegAs => '+str(e)+'' )
            logs.logFile()
            pass