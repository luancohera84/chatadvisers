from gluon import *
from _clasFunt import InfoLogs,DataGlobal


class ClientesUsers:

    def __init__( self, db ):
        self.db                 = db
        self.dataCliente        = []
        self.idCliPlaf          = 0
        self.idCliPlafHist      = 0
        self.telfonoCliente     = ''
        self.idetficCliente     = ''
        self.idEmpresa          = 0
        self.idCliente          = 0
        self.idSegmento         = 0
        self.empresa_strauss    = ''
        self.cliente_strauss    = ''
        self.segmento_strauss   = 0


    def define_table( self ):
        try:
            db = self.db
            db.define_table('info_cliente',
                Field('empresa'),
                Field('cliente'),
                Field('segmento'),
                Field('identificacion'),
                Field('telefono'),
                Field('producto'),
                Field('Nombre'),
                Field('name'),
                Field('surname'),
                Field('fecha1'),
                Field('fecha2'),
                Field('valor1'),
                Field('valor2'),
                Field('dias_mora'),
                Field('email'),
                Field('token'),
                Field('url'),
                Field('id_asignacion'),
                Field('v1'),
                Field('v2'),
                Field('v3'),
                Field('v4'),
                Field('v5'),
                Field('v6'),
                Field('v7'),
                Field('v8'),
                Field('v9'),
                Field('v10'),
                Field('fecha_fin_asignacion'),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer'),
                Field('id_info_cliente_historica','integer'),
                Field('empresa_strauss'),
                Field('cliente_strauss'),
                Field('segmento_strauss'),
                Field('bolsa_previa'),
                Field('bolsa_actual'),
                Field('nombre_sin_afinar'),
                Field('id_base', 'integer'),
                Field('estado',default=True)
            )
            db.define_table('info_cliente_historica',
                Field('empresa'),
                Field('cliente'),
                Field('segmento'),
                Field('identificacion'),
                Field('telefono'),
                Field('producto'),
                Field('Nombre'),
                Field('name'),
                Field('surname'),
                Field('fecha1'),
                Field('fecha2'),
                Field('valor1'),
                Field('valor2'),
                Field('dias_mora'),
                Field('email'),
                Field('token'),
                Field('url'),
                Field('id_asignacion'),
                Field('v1'),
                Field('v2'),
                Field('v3'),
                Field('v4'),
                Field('v5'),
                Field('v6'),
                Field('v7'),
                Field('v8'),
                Field('v9'),
                Field('v10'),
                Field('fecha_fin_asignacion'),
                Field('fecha_creacion','integer'),
                Field('anio_creacion','integer'),
                Field('mes_creacion','integer'),
                Field('dia_creacion','integer'),
                Field('hora_creacion','integer'),
                Field('empresa_strauss'),
                Field('cliente_strauss'),
                Field('segmento_strauss'),
                Field('bolsa_previa'),
                Field('bolsa_actual'),
                Field('nombre_sin_afinar'),
                Field('id_base', 'integer'),
                Field('estado',default=True)
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table info_cliente info_cliente_historica => '+str(e)+'' )
            #logs.logFile()
            return False
            pass

    def getCreateInfoCliente( self ):
        db = self.db
        try:
            varGl                    = DataGlobal()
            idClUserHistory          = db.info_cliente_historica.insert(
                empresa              = self.idEmpresa,
                cliente              = self.idCliente,
                segmento             = self.idSegmento,
                identificacion       = self.idetficCliente,
                telefono             = self.telfonoCliente,
                producto             = self.dataCliente['producto'][0],
                Nombre               = self.dataCliente['Nombre'][0],
                name                 = self.dataCliente['name'][0],
                surname              = self.dataCliente['surname'][0],
                fecha1               = self.dataCliente['fecha1'][0],
                fecha2               = self.dataCliente['fecha2'][0],
                valor1               = self.dataCliente['valor1'][0],
                valor2               = self.dataCliente['valor2'][0],
                dias_mora            = self.dataCliente['dias_mora'][0],
                email                = self.dataCliente['email'][0],
                token                = self.dataCliente['token'][0],
                url                  = self.dataCliente['url'][0],
                id_asignacion        = self.dataCliente['id_asignacion'][0],
                v1                   = self.dataCliente['v1'][0],
                v2                   = self.dataCliente['v2'][0],
                v3                   = self.dataCliente['v3'][0],
                v4                   = self.dataCliente['v4'][0],
                v5                   = self.dataCliente['v5'][0],
                v6                   = self.dataCliente['v6'][0],
                v7                   = self.dataCliente['v7'][0],
                v8                   = self.dataCliente['v8'][0],
                v9                   = self.dataCliente['v9'][0],
                v10                  = self.dataCliente['v10'][0],  
                fecha_fin_asignacion = self.dataCliente['fecha_fin_asignacion'][0],
                bolsa_previa         = self.dataCliente['bolsa_previa'][0],
                bolsa_actual         = self.dataCliente['bolsa_actual'][0],
                nombre_sin_afinar    = self.dataCliente['nombre_sin_afinar'][0],
                id_base              = self.dataCliente['id_base'][0],
                empresa_strauss      = self.empresa_strauss,
                cliente_strauss      = self.cliente_strauss,
                segmento_strauss     = self.segmento_strauss,
                fecha_creacion       = varGl.fechaIntModels,
                hora_creacion        = varGl.horaIntModels,
                anio_creacion        = varGl.anioGlb,
                mes_creacion         = varGl.mesGlb,
                dia_creacion         = varGl.dayGlb
            )

            idClUser                      = db.info_cliente.insert(
                empresa                   = self.idEmpresa,
                cliente                   = self.idCliente,
                segmento                  = self.idSegmento,
                identificacion            = self.idetficCliente,
                telefono                  = self.telfonoCliente,
                producto                  = self.dataCliente['producto'][0],
                Nombre                    = self.dataCliente['Nombre'][0],
                name                      = self.dataCliente['name'][0],
                surname                   = self.dataCliente['surname'][0],
                fecha1                    = self.dataCliente['fecha1'][0],
                fecha2                    = self.dataCliente['fecha2'][0],
                valor1                    = self.dataCliente['valor1'][0],
                valor2                    = self.dataCliente['valor2'][0],
                dias_mora                 = self.dataCliente['dias_mora'][0],
                email                     = self.dataCliente['email'][0],
                token                     = self.dataCliente['token'][0],
                url                       = self.dataCliente['url'][0],
                id_asignacion             = self.dataCliente['id_asignacion'][0],
                v1                        = self.dataCliente['v1'][0],
                v2                        = self.dataCliente['v2'][0],
                v3                        = self.dataCliente['v3'][0],
                v4                        = self.dataCliente['v4'][0],
                v5                        = self.dataCliente['v5'][0],
                v6                        = self.dataCliente['v6'][0],
                v7                        = self.dataCliente['v7'][0],
                v8                        = self.dataCliente['v8'][0],
                v9                        = self.dataCliente['v9'][0],
                v10                       = self.dataCliente['v10'][0],  
                fecha_fin_asignacion      = self.dataCliente['fecha_fin_asignacion'][0],
                bolsa_previa              = self.dataCliente['bolsa_previa'][0],
                bolsa_actual              = self.dataCliente['bolsa_actual'][0],
                nombre_sin_afinar         = self.dataCliente['nombre_sin_afinar'][0],
                id_base                   = self.dataCliente['id_base'][0],
                empresa_strauss           = self.empresa_strauss,
                cliente_strauss           = self.cliente_strauss,
                segmento_strauss          = self.segmento_strauss,
                fecha_creacion            = varGl.fechaIntModels,
                hora_creacion             = varGl.horaIntModels,
                id_info_cliente_historica = idClUserHistory
            )
            logs = InfoLogs( 'info', 'Se crea el cliente usuario => getCreateInfoCliente: '+str(self.telfonoCliente)+'  con id: '+str(idClUser)+' ' )
            logs.logFile()
        except Exception as e:
            idClUser        = 0
            idClUserHistory = 0
            logs = InfoLogs( 'error', 'Error en: getCreateInfoCliente => '+str(e)+'' )
            logs.logFile()
            pass
        return idClUser,idClUserHistory

    def consultingClieTrueId( self ):
        db = self.db
        # infoCliUsLis = []
        # print('self.idCliPlaf', self.idCliPlaf)
        infoCliUsLis = db( db.info_cliente.id == self.idCliPlaf ).select( db.info_cliente.ALL ).last()
        return infoCliUsLis

    
    def consultingClieDictRet( self ):
        db = self.db
        infoCliDictRet = {}
        infoCliDict    = db( db.info_cliente.id == self.idCliPlaf   ).select( db.info_cliente.ALL ).last()
        if infoCliDict:
            infoCliDictRet                = dict(
                id                        = infoCliDict.id,
                empresa                   = infoCliDict.empresa,
                cliente                   = infoCliDict.cliente,
                segmento                  = infoCliDict.segmento,
                identificacion            = infoCliDict.identificacion,
                telefono                  = infoCliDict.telefono,
                producto                  = infoCliDict.producto,
                Nombre                    = infoCliDict.Nombre,
                name                      = infoCliDict.name,
                surname                   = infoCliDict.surname,
                fecha1                    = infoCliDict.fecha1,
                fecha2                    = infoCliDict.fecha2,
                valor1                    = infoCliDict.valor1,
                valor2                    = infoCliDict.valor2,
                dias_mora                 = infoCliDict.dias_mora,
                email                     = infoCliDict.email,
                token                     = infoCliDict.token,
                url                       = infoCliDict.url,
                id_asignacion             = infoCliDict.id_asignacion,
                v1                        = infoCliDict.v1,
                v2                        = infoCliDict.v2,
                v3                        = infoCliDict.v3,
                v4                        = infoCliDict.v4,
                v5                        = infoCliDict.v5,
                v6                        = infoCliDict.v6,
                v7                        = infoCliDict.v7,
                v8                        = infoCliDict.v8,
                v9                        = infoCliDict.v9,
                v10                       = infoCliDict.v10,
                fecha_fin_asignacion      = infoCliDict.fecha_fin_asignacion,
                bolsa_previa              = infoCliDict.bolsa_previa,
                bolsa_actual              = infoCliDict.bolsa_actual,
                nombre_sin_afinar         = infoCliDict.nombre_sin_afinar,
                id_base                   = infoCliDict.id_base,
                fecha_creacion            = infoCliDict.fecha_creacion,
                hora_creacion             = infoCliDict.hora_creacion,
                id_info_cliente_historica = infoCliDict.id_info_cliente_historica,
                empresa_strauss           = infoCliDict.empresa_strauss,
                cliente_strauss           = infoCliDict.cliente_strauss,
                segmento_strauss          = infoCliDict.segmento_strauss,
                estado                    = infoCliDict.estado,
            )
            pass
        return infoCliDictRet

    def consultingClieDictHistRet( self ):
        db = self.db
        infoCliDictHitRet = {}
        infoCliDictHist    = db( db.info_cliente_historica.id == self.idCliPlaf   ).select( db.info_cliente_historica.ALL ).last()
        if infoCliDictHist:
            infoCliDictHitRet             = dict(
                id                        = infoCliDictHist.id,
                empresa                   = infoCliDictHist.empresa,
                cliente                   = infoCliDictHist.cliente,
                segmento                  = infoCliDictHist.segmento,
                identificacion            = infoCliDictHist.identificacion,
                telefono                  = infoCliDictHist.telefono,
                producto                  = infoCliDictHist.producto,
                Nombre                    = infoCliDictHist.Nombre,
                name                      = infoCliDictHist.name,
                surname                   = infoCliDictHist.surname,
                fecha1                    = infoCliDictHist.fecha1,
                fecha2                    = infoCliDictHist.fecha2,
                valor1                    = infoCliDictHist.valor1,
                valor2                    = infoCliDictHist.valor2,
                dias_mora                 = infoCliDictHist.dias_mora,
                email                     = infoCliDictHist.email,
                token                     = infoCliDictHist.token,
                url                       = infoCliDictHist.url,
                id_asignacion             = infoCliDictHist.id_asignacion,
                v1                        = infoCliDictHist.v1,
                v2                        = infoCliDictHist.v2,
                v3                        = infoCliDictHist.v3,
                v4                        = infoCliDictHist.v4,
                v5                        = infoCliDictHist.v5,
                v6                        = infoCliDictHist.v6,
                v7                        = infoCliDictHist.v7,
                v8                        = infoCliDictHist.v8,
                v9                        = infoCliDictHist.v9,
                v10                       = infoCliDictHist.v10,
                fecha_fin_asignacion      = infoCliDictHist.fecha_fin_asignacion,
                bolsa_previa              = infoCliDictHist.bolsa_previa,
                bolsa_actual              = infoCliDictHist.bolsa_actual,
                nombre_sin_afinar         = infoCliDictHist.nombre_sin_afinar,
                id_base                   = infoCliDictHist.id_base,
                fecha_creacion            = infoCliDictHist.fecha_creacion,
                hora_creacion             = infoCliDictHist.hora_creacion,
                empresa_strauss           = infoCliDictHist.empresa_strauss,
                cliente_strauss           = infoCliDictHist.cliente_strauss,
                segmento_strauss          = infoCliDictHist.segmento_strauss,
                estado                    = infoCliDictHist.estado
            )
            pass
        return infoCliDictHitRet

    def consultingClieTrueIdHist( self ):
        db = self.db
        infoCliUsLisHist = []
        infoCliUsLisHist = db( ( db.info_cliente_historica.id == self.idCliPlafHist ) & ( db.info_cliente_historica.estado == True) ).select( db.info_cliente_historica.ALL ).last()
        return infoCliUsLisHist


    def consultingClieTrueIdentEmClSeg( self ):
        db = self.db
        listInfoClIden = []
        if self.idetficCliente:
            listInfoClIden = db( ( db.info_cliente.telefono == self.telfonoCliente ) & ( db.info_cliente.identificacion == self.idetficCliente ) & ( db.info_cliente.estado == True) & ( db.info_cliente.empresa == self.idEmpresa ) & ( db.info_cliente.cliente == self.idCliente ) & ( db.info_cliente.segmento == self.idSegmento ) ).select( db.info_cliente.ALL ).last()
        else:
            listInfoClIden = db( ( db.info_cliente.telefono == self.telfonoCliente ) & ( db.info_cliente.estado == True) & ( db.info_cliente.empresa == self.idEmpresa ) & ( db.info_cliente.cliente == self.idCliente ) & ( db.info_cliente.segmento == self.idSegmento ) ).select( db.info_cliente.ALL ).last()
            pass
        return listInfoClIden

    
    def consultingClieTrueIdentEmClSinSeg( self ):
        db = self.db
        listInfoClIden = []
        listInfoClIden = db( ( ( db.info_cliente.telefono == self.telfonoCliente ) | ( db.info_cliente.identificacion == self.idetficCliente ) ) & ( db.info_cliente.estado == True) ).select( db.info_cliente.ALL ).last()
        return listInfoClIden


    def consultingClieApiSinSeg( self ):
        db = self.db
        listInfoClIden = []
        listInfoClIden = db( ( ( db.info_cliente.telefono == self.telfonoCliente ) | ( db.info_cliente.identificacion == self.idetficCliente ) )  & ( db.info_cliente.empresa_strauss == self.empresa_strauss ) & ( db.info_cliente.cliente_strauss == self.cliente_strauss )  ).select( db.info_cliente.ALL ).last()
        return listInfoClIden

    def consultingClieTrueIdentEmClSegHist( self ):
        db = self.db
        listInfoClIdenHist = []
        if self.idetficCliente:
            listInfoClIdenHist = db( ( db.info_cliente_historica.telefono == self.telfonoCliente ) & ( db.info_cliente_historica.identificacion == self.idetficCliente )  & ( db.info_cliente_historica.estado == True) & ( db.info_cliente_historica.empresa == self.idEmpresa ) & ( db.info_cliente_historica.cliente == self.idCliente ) & ( db.info_cliente_historica.segmento == self.idSegmento ) ).select( db.info_cliente_historica.ALL ).last()
        else:
            listInfoClIdenHist = db( ( db.info_cliente_historica.telefono == self.telfonoCliente )  & ( db.info_cliente_historica.estado == True) & ( db.info_cliente_historica.empresa == self.idEmpresa ) & ( db.info_cliente_historica.cliente == self.idCliente ) & ( db.info_cliente_historica.segmento == self.idSegmento ) ).select( db.info_cliente_historica.ALL ).last()
            pass
        return listInfoClIdenHist


    def consultingClieHist( self ):
        db = self.db
        listInfoClIdenHist = []
        listInfoClIdenHist = db( ( ( db.info_cliente_historica.telefono == self.telfonoCliente ) | ( db.info_cliente_historica.identificacion == self.idetficCliente ) ) & ( db.info_cliente_historica.empresa == self.idEmpresa ) & ( db.info_cliente_historica.cliente == self.idCliente ) & ( db.info_cliente_historica.segmento == self.idSegmento ) ).select( db.info_cliente_historica.id )
        return listInfoClIdenHist


    def consultingClieTrueTelEmClSeg( self ):
        db = self.db
        listInfoClTel = []
        listInfoClTel = db( ( db.info_cliente.telefono == self.telfonoCliente ) & ( db.info_cliente.estado == True) & ( db.info_cliente.empresa == self.idEmpresa ) & ( db.info_cliente.cliente == self.idCliente ) & ( db.info_cliente.segmento == self.idSegmento )  ).select( db.info_cliente.ALL )
        return listInfoClTel


    def consultingClieTrueTelEmClSegHist( self ):
        db = self.db
        listInfoClTelHist = []
        listInfoClTelHist = db( ( db.info_cliente_historica.telefono == self.telfonoCliente ) & ( db.info_cliente_historica.estado == True) & ( db.info_cliente_historica.empresa == self.idEmpresa ) & ( db.info_cliente_historica.cliente == self.idCliente ) & ( db.info_cliente_historica.segmento == self.idSegmento )  ).select( db.info_cliente_historica.ALL )
        return listInfoClTelHist


    def consultingClieTrueEmClSeg( self ):
        db = self.db
        listInfoEmp = []
        listInfoEmp = db( ( db.info_cliente.empresa == self.idEmpresa ) & ( db.info_cliente.cliente == self.idCliente ) & ( db.info_cliente.segmento == self.idSegmento ) & ( db.info_cliente.estado == True) ).select( db.info_cliente.ALL )
        return listInfoEmp

    def consultingClieTrueEmClSegHist( self ):
        db = self.db
        listInfoEmpHist = []
        listInfoEmpHist = db( ( db.info_cliente_historica.empresa == self.idEmpresa ) & ( db.info_cliente_historica.estado == True) & ( db.info_cliente_historica.cliente == self.idCliente ) & ( db.info_cliente_historica.segmento == self.idSegmento ) ).select( db.info_cliente_historica.ALL )
        return listInfoEmpHist