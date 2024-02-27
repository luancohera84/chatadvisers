from gluon import *
from _clasFunt import InfoLogs, DataGlobal
from conversaCliAdv import ConversClientAdv
from clientesUsers import ClientesUsers

class InteraccionesAsesor:

    def __init__( self, db ):

        self.db                          = db
        self.idCliPlaf                   = 0
        self.idCliPlafHist               = 0
        self.idAdvisers                  = 0
        self.idInsertCov                 = 0
        self.idInsertCovHist             = 0
        self.id_resultado                = 0
        self.descripcion_resultado       = ''
        self.valor_acuerdo_venta         = 0
        self.cuotas_acuerdo_venta        = 1
        self.fecha_pago_acuerdo_venta    = 0
        self.punto_pago_acuerdo_venta    = ''
        self.fechaInicial                = 0
        self.fechaFinal                  = 0
        self.comentarios                 = ''
        self.formulario                  = ''
        self.formulario_id               = 0
        self.formulario_nombre           = ''
        self.id_interacion               = 0
        self.id_interacionHis            = 0
        self.telefono                    = ''
        self.numero_producto             = ''
        self.valor_acordado              = 0
        self.cuotas_acordadas            = 0
        self.interes_acordados           = 0
        self.fecha_pago                  = ''
        self.punto_pago                  = ''

    def define_table( self ):
        try:
            cliOfertas = ConversClientAdv( self.db )
            cliOfertas.define_table()
            varGl     = DataGlobal()
            db = self.db

            db.define_table('interacciones_asesor',
                Field('id_conversacion'),
                Field('id_asesor'),
                Field('id_info_cliente'),
                Field('id_resultado'),
                Field('descripcion_resultado'),
                Field('nombre_cliente'),
                Field('identificacion_cliente'),
                Field('telefono_cliente'),
                # Field('valor_acuerdo_venta'),
                # Field('cuotas_acuerdo_venta','integer'),
                # Field('fecha_pago_acuerdo_venta'),
                # Field('punto_pago_acuerdo_venta'),
                Field('id_empresa'),
                Field('id_cliente'),
                Field('id_segmento'),
                Field('empresa'),
                Field('cliente'),
                Field('segmento'),
                Field('id_asignacion','integer'),
                Field('informacion_inicial_cliente','text'),
                Field('mensajes_conversacion','text'),
                Field('anio_creacion',default = varGl.anioGlb),
                Field('mes_creacion',default = varGl.mesGlb),
                Field('dia_creacion',default = varGl.dayGlb),
                Field('fecha_interaccion',default = varGl.fechaIntModels),
                Field('hora_interaccion',default  = varGl.horaIntModels),
                Field('comentarios','text'),
                Field('formulario','text', default=''),
                Field('formulario_id','text', default=''),
                Field('formulario_nombre','text', default='')
            )

            db.define_table('interacciones_asesor_historica',
                Field('id_conversacion_historica','reference conversaciones_historica'),
                Field('id_asesor'),
                Field('id_info_cliente'),
                Field('id_resultado'),
                Field('descripcion_resultado'),
                Field('nombre_cliente'),
                Field('identificacion_cliente'),
                Field('telefono_cliente'),
                # Field('valor_acuerdo_venta'),
                # Field('cuotas_acuerdo_venta','integer'),
                # Field('fecha_pago_acuerdo_venta'),
                # Field('punto_pago_acuerdo_venta'),
                Field('id_empresa'),
                Field('id_cliente'),
                Field('id_segmento'),
                Field('empresa'),
                Field('cliente'),
                Field('segmento'),
                Field('id_asignacion','integer'),
                Field('informacion_inicial_cliente','text'),
                Field('mensajes_conversacion','text'),
                Field('anio_creacion',default = varGl.anioGlb),
                Field('mes_creacion',default = varGl.mesGlb),
                Field('dia_creacion',default = varGl.dayGlb),
                Field('fecha_interaccion',default = varGl.fechaIntModels),
                Field('hora_interaccion',default  = varGl.horaIntModels),
                Field('comentarios','text'),
                Field('formulario','text', default=''),
                Field('formulario_id','text', default=''),
                Field('formulario_nombre','text', default='')
            )

            db.define_table('acuerdos',
                Field('id_interacion','reference interacciones_asesor'),
                Field('telefono'),
                Field('numero_producto'),
                Field('valor_acordado','double', default=0),
                Field('cuotas_acordadas','integer', default=0),
                Field('interes_acordados', default=0),
                Field('fecha_pago'),
                Field('punto_pago'),
                Field('fecha_creacion','integer' ,default= varGl.fechaIntModels),
                Field('hora_creacion','integer',default=varGl.horaIntModels),
                Field('dia','integer',default=varGl.dayGlb),
                Field('mes','integer',default=varGl.mesGlb),
                Field('anio','integer',default=varGl.anioGlb)
            )

            db.define_table('acuerdos_historica',
                Field('id_interacion','reference interacciones_asesor_historica'),
                Field('telefono'),
                Field('numero_producto'),
                Field('valor_acordado','double', default=0),
                Field('cuotas_acordadas','integer', default=0),
                Field('interes_acordados', default=0),
                Field('fecha_pago'),
                Field('punto_pago'),
                Field('fecha_creacion','integer' ,default= varGl.fechaIntModels),
                Field('hora_creacion','integer',default=varGl.horaIntModels),
                Field('dia','integer',default=varGl.dayGlb),
                Field('mes','integer',default=varGl.mesGlb),
                Field('anio','integer',default=varGl.anioGlb)
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table interacciones_asesor interacciones_asesor_historica => '+str(e)+'' )
            #logs.logFile()
            return False
            pass

    def insertInteraccion( self ):
        db                                   = self.db
        idInteraccion                        = 0
        varGl                                = DataGlobal()
        cliOfertas                           = ClientesUsers( db )
        conSms                               = ConversClientAdv( db )
        cliOfertas.idCliPlaf                 = self.idCliPlaf
        cliOfertas.idCliPlafHist             = self.idCliPlafHist
        conSms.idInsertCov                   = self.idInsertCov
        infoCliente                          = cliOfertas.consultingClieDictRet()
        infoClienteHist                      = cliOfertas.consultingClieDictHistRet()
        infoConverSms                        = conSms.infoSmsConversaciones()
        if len(infoCliente)                  > varGl.estadoFalsNum:
            idInteraccion                    = db.interacciones_asesor.insert(
                id_conversacion              = self.idInsertCov,
                id_asesor                    = self.idAdvisers,
                id_info_cliente              = infoCliente['id'],
                id_resultado                 = self.id_resultado,
                descripcion_resultado        = self.descripcion_resultado,
                nombre_cliente               = infoCliente['Nombre'], 
                identificacion_cliente       = infoCliente['identificacion'],
                telefono_cliente             = infoCliente['telefono'],
                # valor_acuerdo_venta          = self.valor_acuerdo_venta,
                # cuotas_acuerdo_venta         = self.cuotas_acuerdo_venta,
                # fecha_pago_acuerdo_venta     = self.fecha_pago_acuerdo_venta,
                # punto_pago_acuerdo_venta     = self.punto_pago_acuerdo_venta,
                empresa                      = infoCliente['empresa_strauss'],
                cliente                      = infoCliente['cliente_strauss'],
                segmento                     = infoCliente['segmento_strauss'],
                id_empresa                   = infoCliente['empresa'],
                id_cliente                   = infoCliente['cliente'],
                id_segmento                  = infoCliente['segmento'],
                id_asignacion                = infoCliente['id_asignacion'],
                informacion_inicial_cliente  = str(infoCliente).replace("'",'"'),
                mensajes_conversacion        = str(infoConverSms).replace("'",'"'),
                comentarios                  = self.comentarios,
                formulario                   = self.formulario,
                formulario_id                = self.formulario_id,
                formulario_nombre            = self.formulario_nombre
            )
            pass
        if len(infoClienteHist)             > varGl.estadoFalsNum:
            db.interacciones_asesor_historica.insert(
                id_conversacion_historica   = self.idInsertCovHist,
                id_asesor                   = self.idAdvisers,
                id_info_cliente             = infoClienteHist['id'],
                id_resultado                = self.id_resultado,
                descripcion_resultado       = self.descripcion_resultado,
                nombre_cliente              = infoCliente['Nombre'], 
                identificacion_cliente      = infoClienteHist['identificacion'],
                telefono_cliente            = infoClienteHist['telefono'],
                # valor_acuerdo_venta         = self.valor_acuerdo_venta,
                # cuotas_acuerdo_venta        = self.cuotas_acuerdo_venta,
                # fecha_pago_acuerdo_venta    = self.fecha_pago_acuerdo_venta,
                # punto_pago_acuerdo_venta    = self.punto_pago_acuerdo_venta,
                id_empresa                  = infoClienteHist['empresa'],
                id_cliente                  = infoClienteHist['cliente'],
                id_segmento                 = infoClienteHist['segmento'],
                empresa                     = infoClienteHist['empresa_strauss'],
                cliente                     = infoClienteHist['cliente_strauss'],
                segmento                    = infoClienteHist['segmento_strauss'],
                id_asignacion               = infoClienteHist['id_asignacion'],
                informacion_inicial_cliente = str(infoClienteHist).replace("'",'"'),
                mensajes_conversacion       = str(infoConverSms).replace("'",'"'),
                comentarios                 = self.comentarios,
                formulario                  = self.formulario,
                formulario_id               = self.formulario_id,
                formulario_nombre           = self.formulario_nombre
            )
            pass
        print('idInteraccion =>', idInteraccion)
        return idInteraccion


    def saveAcuerdosInteraccion( self ):
        varGl         = DataGlobal()
        idAcuerdoInt  = varGl.estadoIniNum
        try:
            db            = self.db
            idAcuerdoInt  = db.acuerdos.insert(
                id_interacion     = self.id_interacion,
                telefono          = self.telefono,
                numero_producto   = self.numero_producto,
                valor_acordado    = self.valor_acordado,
                cuotas_acordadas  = self.cuotas_acordadas,
                interes_acordados = self.interes_acordados,
                fecha_pago        = self.fecha_pago,
                punto_pago        = self.punto_pago
            )
            db.acuerdos_historica.insert(
                id_interacion     = self.id_interacionHis,
                telefono          = self.telefono,
                numero_producto   = self.numero_producto,
                valor_acordado    = self.valor_acordado,
                cuotas_acordadas  = self.cuotas_acordadas,
                interes_acordados = self.interes_acordados,
                fecha_pago        = self.fecha_pago,
                punto_pago        = self.punto_pago
            )
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: saveAcuerdosInteraccion => '+str(e)+'' )
            logs.logFile()
            pass
        return idAcuerdoInt

    def deleteClinInfo( self ):
        db = self.db
        varGl              = DataGlobal()
        cliOfertas         = ClientesUsers( db )
        infoConver         = ConversClientAdv( db )
        cliOfertas.define_table()
        infoConver.define_table()
        dbConv             = db.conversaciones
        dbMsm              = db.mensajes_conversacion
        dbAc               = db.asesor_cliente
        dbAtCli            = db.asesor_atencion_cliente
        dbConvHist         = db.conversaciones_historica
        dbMsmHist          = db.mensajes_conversacion_historica
        dbAcHist           = db.asesor_cliente_historica

        idClientInfo       = db( db.info_cliente.id == self.idCliPlaf  ).update( estado = False )
        
        db( dbAtCli.id_cliente == self.idCliPlaf ).delete()
        db( dbConv.id_cliente == self.idCliPlaf  ).update( estado_conversacion = False )
        db( dbAc.id_cliente == self.idCliPlaf  ).update( estado_asesor_cliente = False )
        listConver = db( dbConv.id_cliente == self.idCliPlaf  ).select( dbConv.id ).last()
        db( dbMsm.id_conversacion == listConver.id  ).update( estado_lectura = varGl.msmLeido )
        
        db( db.info_cliente_historica.id == self.idCliPlafHist  ).update( estado = False )
        # db( dbConvHist.id_cliente == self.idCliPlafHist  ).update( estado_conversacion = False )
        # db( dbAcHist.id_cliente == self.idCliPlafHist  ).update( estado_asesor_cliente = False )
        # listConverHist = db( dbConvHist.id_cliente == self.idCliPlafHist  ).select( dbConvHist.id ).last()
        # db( dbMsmHist.id_conversacion == listConverHist.id  ).update( estado_lectura = varGl.msmLeido )
        return idClientInfo


    
    def gestionesAsesor( self ):
        infoGestiones = []
        varGl     = DataGlobal()
        try:
            db = self.db
            sqlGestion = """
                SELECT
                    empresa,
                    cliente,
                    segmento,
                    nombre_cliente,
                    identificacion_cliente,
                    telefono_cliente,
                    descripcion_resultado,
                    fecha_interaccion,
                    hora_interaccion,
                    id_conversacion,
                    id_info_cliente,
                    id_empresa,
                    id,
                    comentarios,
                    formulario,
                    formulario_id,
                    formulario_nombre
                FROM
                    interacciones_asesor ia
                WHERE 
                    ia.id_asesor  = """+str(self.idAdvisers)+"""
                ORDER BY
                    ia.id
            """
            infoGestionesTmp    = db.executesql(sqlGestion)
            if infoGestionesTmp:
                for items in infoGestionesTmp:
                    infoGestiones.append(
                        dict(
                            empresa                = items[0],
                            cliente                = items[1],
                            segmento               = items[2],
                            nombre_cliente         = items[3],
                            identificacion_cliente = items[4],
                            telefono_cliente       = items[5],
                            descripcion_resultado  = items[6],
                            fecha_interaccion      = str(self.fechaFormato(items[7],'fecha')),
                            hora_interaccion       = str(self.fechaFormato(items[8],'hora')),
                            id_conversacion        = items[9],
                            id_info_cliente        = items[10],
                            id_empresa             = items[11],
                            id                     = items[12],
                            comentarios            = items[13],
                            formulario             = items[14],
                            formulario_id          = items[15],
                            formulario_nombre      = items[16]
                        )
                    )
                    pass
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: gestionesAsesor => '+str(e)+'' )
            logs.logFile()
            pass
        return infoGestiones


    def gestionesAsesorFechas( self ):
        infoGestionesFechas = []
        varGl     = DataGlobal()
        try:
            db = self.db
            if int(varGl.mesGlb) == int(varGl.estadoIniNum):
                mesAntes = 12
                anioQuery = int(varGl.anioGlb) - int(varGl.estadoIniNum)
            else:
                anioQuery = varGl.anioGlb
                mesAntes = int(varGl.mesGlb) - int(varGl.estadoIniNum)
                pass
            sqlGestion = """
                SELECT
                    empresa,
                    cliente,
                    segmento,
                    nombre_cliente,
                    identificacion_cliente,
                    telefono_cliente,
                    descripcion_resultado,
                    fecha_interaccion,
                    hora_interaccion,
                    id_conversacion_historica,
                    id_info_cliente,
                    id_empresa,
                    id,
                    comentarios,
                    formulario,
                    formulario_id,
                    formulario_nombre
                FROM
                    interacciones_asesor_historica ia
                WHERE 
                    ia.id_asesor  = """+str(self.idAdvisers)+"""
                AND
                    ia.anio_creacion >= """+str(anioQuery)+"""
                AND
                    ia.mes_creacion <= """+str(mesAntes)+"""
                ORDER BY
                    ia.id
            """
            # print('sqlGestion', sqlGestion)
            infoGestionesTmp    = db.executesql(sqlGestion)
            if infoGestionesTmp:
                for items in infoGestionesTmp:
                    infoGestionesFechas.append(
                        dict(
                            empresa                = items[0],
                            cliente                = items[1],
                            segmento               = items[2],
                            nombre_cliente         = items[3],
                            identificacion_cliente = items[4],
                            telefono_cliente       = items[5],
                            descripcion_resultado  = items[6],
                            fecha_interaccion      = str(self.fechaFormato(items[7],'fecha')),
                            hora_interaccion       = str(self.fechaFormato(items[8],'hora')),
                            id_conversacion        = items[9],
                            id_info_cliente        = items[10],
                            id_empresa             = items[11],
                            id                     = items[12],
                            comentarios            = items[13],
                            formulario             = items[14],
                            formulario_id          = items[15],
                            formulario_nombre      = items[16]
                        )
                    )
                    pass
                pass
            # print('infoGestionesFechas', infoGestionesFechas)
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: gestionesAsesorFechas => '+str(e)+'' )
            logs.logFile()
            pass
        return infoGestionesFechas


    def fechaFormato(self, valor, opc):
        formato  = ''
        try:
            hora  = '00'
            minu  = '00'
            segun = '00'
            if opc == 'fecha':
                anio = str(valor)[:4]
                mes  = str(valor)[4:-2]
                dia  = str(valor)[6:]
                formato = anio+'-'+str(mes)+'-'+str(dia)
            else:
                if len(str(valor)) == 5:
                    hora  = str(valor)[:1]
                    minu  = str(valor)[1:3]
                    segun = str(valor)[3:]
                elif len(str(valor)) == 6:
                    hora  = str(valor)[:2]
                    minu  = str(valor)[2:4]
                    segun = str(valor)[4:]
                    pass
                if hora == '24':
                    hora = hora.replace('24','00')
                    pass
                formato = hora+':'+str(minu)+':'+str(segun)
                pass
            return formato
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: fechaFormato => '+str(e)+'' )
            logs.logFile()
            pass