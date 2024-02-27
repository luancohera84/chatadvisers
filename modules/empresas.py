from gluon import *
from _clasFunt import InfoLogs
from _clasFunt import DataGlobal


class Empresas:

    def __init__( self, db ):
        self.db             = db
        self.idEmpresa      = 0
        self.nomEmpresa     = ''
        self.punto_pago     = ''
        self.estadoEmpresa  = 0
        self.userCreate     = 0

    def define_table( self ):
        try:
            db = self.db
            varGl     = DataGlobal()
            db.define_table('empresas',
                Field('nombre_empresa','string'),
                Field('estado_empresa',default=True),
                Field('empresas_logo','upload'),
                Field('empresas_color'),
                Field('empresas_dominio'),
                Field('empresas_puerto_conexion',default=varGl.portIntelibpo),
                Field('empresas_usuario_conexion',default=varGl.userIntelibpo),
                Field('empresas_key_dominio',default=varGl.keyIntelibpo),
                Field('empresas_base'),
                Field('empresas_base_dominio'),
                Field('empresas_base_usuario',default=varGl.userBaseInte),
                Field('empresas_base_key',default=varGl.keyBaseIntelibpo),
                Field('empresas_base_puerto',default=varGl.portBaseIntelibpo),
                Field('fecha_creacion_empresa','integer'),
                Field('hora_creacion_empresa','integer')
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table empresas => '+str(e)+'' )
            #logs.logFile()
            return False
            pass

    def getCreateEmpresa( self ):
        db = self.db
        try:
            varGl     = DataGlobal()
            idEmprs = db.empresas.insert(
                nombre_empresa          = self.nomEmpresa,
                fecha_creacion_empresa  = varGl.fechaIntModels,
                hora_creacion_empresa   = varGl.horaIntModels,
                empresas_color          = varGl.colorRgb,
                empresas_dominio        = str(self.nomEmpresa).lower()+str(varGl.urlSubInteli),
                empresas_base           = varGl.baseDatIntelibpo+str(str(self.nomEmpresa).lower()),
                empresas_base_dominio   = str(self.nomEmpresa).lower()+str(varGl.urlSubInteli)
            )
            logs = InfoLogs( 'info', 'Se crear la empresa: '+str(self.nomEmpresa).lower()+'  con id: '+str(idEmprs)+' ' )
            logs.logFile()
        except Exception as e:
            idEmprs  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateEmpresa => '+str(e)+'' )
            # logs.logFile()
            pass
        return idEmprs



    def setCambioEstado( self ):
        db = self.db
        if self.estadoEmpresa == 0:
            self.estadoEmpresa = True
        else:
            self.estadoEmpresa = False
            pass
        idEmpresaUp = db( db.empresas.id == self.idEmpresa ).update( estado_empresa = self.estadoEmpresa )
        return idEmpresaUp


    def setCambioNombre( self ):
        db = self.db
        idEmpresaUp = db( db.empresas.id == self.idEmpresa ).update( nombre_empresa = self.nomEmpresa )
        return idEmpresaUp


    def getListarNomEmpresa( self ):
        db = self.db
        listadoEmpresas = db( ( db.empresas.nombre_empresa == self.nomEmpresa ) & (  db.empresas.estado_empresa == True ) ).select( db.empresas.ALL ).last()
        return listadoEmpresas


    def getListarIdEmpresa( self ):
        db = self.db
        empresaList = db( ( db.empresas.id == self.idEmpresa ) & (  db.empresas.estado_empresa == True ) ).select( db.empresas.ALL ).last()
        return empresaList

    def getListarEmpresas( self ):
        db = self.db
        empresasLista = db( db.empresas.id > self.idEmpresa  ).select( db.empresas.ALL, orderby=db.empresas.nombre_empresa )
        return empresasLista


class Clientes:

    def __init__( self, db ):
        self.db            = db
        self.idEmpresa     = 0
        self.idCliente     = 0
        self.nomCliente    = ''
        self.idCliStrauss  = 0
        self.estadoCliente = 0


    def define_table( self ):
        try:
            db = self.db
            db.define_table('clientes',
                Field('empresa_cliente','reference empresas'),
                Field('nombre_cliente','string'),
                Field('id_cliente_strauss','integer'),
                Field('estado_cliente',default=True),
                Field('fecha_creacion_cliente','integer'),
                Field('hora_creacion_cliente','integer')
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table segmentos => '+str(e)+'' )
            # logs.logFile()
            return False
            pass

    def getCreateCliente( self ):
        db = self.db
        try:
            varGl     = DataGlobal()
            idCliet   = db.clientes.insert(
                empresa_cliente         = self.idEmpresa,
                nombre_cliente          = self.nomCliente,
                id_cliente_strauss      = self.idCliStrauss,
                fecha_creacion_cliente  = varGl.fechaIntModels,
                hora_creacion_cliente   = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se crear el cliente: '+str(self.nomCliente).lower()+'  con id: '+str(idCliet)+' ' )
            logs.logFile()
        except Exception as e:
            idCliet  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateCliente => '+str(e)+'' )
            logs.logFile()
            pass
        return idCliet


    def setCambioEstadoClientesEmpresa( self ):
        db = self.db
        if self.estadoCliente == 0:
            self.estadoCliente = True
        else:
            self.estadoCliente = False
            pass
        idClienteUp = db( db.clientes.empresa_cliente == self.idEmpresa ).update( estado_cliente = self.estadoCliente )
        return idClienteUp


    def setCambioEstadoClientes( self ):
        db = self.db
        if self.estadoCliente == 0:
            self.estadoCliente = True
        else:
            self.estadoCliente = False
            pass
        idClienteUp = db( db.clientes.id == self.idCliente ).update( estado_cliente = self.estadoCliente )
        return idClienteUp


    def setCambioNombreClientes( self ):
        db = self.db
        idClienteUp = db( db.clientes.id == self.idCliente ).update( nombre_cliente = self.nomCliente )
        return idClienteUp
    
    def getListarIdEmpresaClientes( self ):
        db = self.db
        listadoClientesEmpresaId = db( db.clientes.empresa_cliente == self.idEmpresa  ).select( db.clientes.ALL )
        return listadoClientesEmpresaId


    def getListarIdEmpresaCliente( self ):
        db = self.db
        listadoClienteEmpresaId = db( ( db.clientes.empresa_cliente == self.idEmpresa ) & ( db.clientes.nombre_cliente == self.nomCliente ) & (  db.clientes.estado_cliente == True ) ).select( db.clientes.ALL ).last()
        return listadoClienteEmpresaId


    
    def getListarNomClientes( self ):
        db = self.db
        listadoClientes = db( ( db.clientes.nombre_cliente == self.nomCliente ) & (  db.clientes.estado_cliente == True ) ).select( db.clientes.ALL ).last()
        return listadoClientes


    def getListarIdCliente( self ):
        db = self.db
        clienteList = db( ( db.clientes.id == self.idCliente ) & (  db.clientes.estado_cliente == True ) ).select( db.clientes.ALL ).last()
        return clienteList


    def getListarClientes( self ):
        db = self.db
        clientesLista = db( ( db.clientes.id > self.idCliente ) & (  db.clientes.estado_cliente == True ) ).select( db.clientes.ALL )
        return clientesLista


    
class Segmentos:

    def __init__( self, db ):
        self.db                     = db
        self.idCliente              = 0
        self.idEmpresa              = 0
        self.nomSegmento            = ''
        self.idSegStrauss           = 0
        self.idSegmento             = 0
        self.estadoSegmento         = 0
        self.nomCampoReal           = ''
        self.nomCampoRepr           = ''
        self.nomContxto             = ''
        self.userCreate             = 0
        self.nomHorario             = ''
        self.diaIniHr               = ''
        self.diaFinHr               = ''
        self.horaIniHr              = ''
        self.horaFinHr              = ''
        self.diaFest                = ''
        self.punto_pago             = ''
        self.diaLabora              = 0
        self.idHorario              = 0
        self.estadoHorario          = 0
        self.estadoSmsPret          = 0
        self.diaBuscarSem           = ''
        self.idSmsPret              = 0
        self.nomSms                 = ''
        self.tipoSmsPr              = ''
        self.smsPr                  = ''
        self.idConChat              = 0
        self.nomContBot             = ''
        self.bodyContextBot         = ''
        self.cantNodosCont          = 0
        self.nodo_nombre            = ''
        self.nomContBotJson         = ''
        self.nodo_mensaje_error     = ''
        self.nodo_tipo              = ''
        self.nodo_directo           = ''
        self.nodo_num_opciones      = 0
        self.nodo_id_resultado      = 0
        self.nomFormulario          = ''
        self.canCampoFormulario     = 0
        self.tipo_campo             = ''
        self.tipo_dato              = ''
        self.nombre_label           = ''
        self.obligatorio            = True
        self.descripcion_campo      = ''
        self.tamano_texto           = 0
        self.typeFormulario         = 1
        self.idFormulario           = 0
        self.idResultadoF           = 0
        self.resultadoFor           = ''
        self.nodo_opciones          = ''
        self.nodo_mensaje           = ''    
        self.status                 = True
        self.nameNew                = ''


    def define_table( self ):
        try:
            db = self.db
            db.define_table('segmentos',
                Field('cliente_segmento','reference clientes'),
                Field('empresa_segmento','integer'),
                Field('nombre_segmento','string'),
                Field('id_segmento_strauss','integer'),
                Field('estado_segmento',default=True),
                Field('fecha_creacion_segmento','integer'),
                Field('hora_creacion_segmento','integer')
            )

            db.define_table('campo_segmentos',
                Field('segmento','reference segmentos'),
                Field('campo_base'),
                Field('campo_representa'),
                Field('tipo_campo_mostrar'),
                Field('posicion_campo'),
                Field('estado',default=True),
                Field('usuario_creador','integer'),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer')
            )

            db.define_table('sms_prestab_segmentos',
                Field('segmento','reference segmentos'),
                Field('nombre_sms'),
                Field('tipo_sms'),
                Field('sms'),
                Field('estado',default=True),
                Field('usuario_creador','integer'),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer')
            )

            db.define_table('contexto_segmentos',
                Field('segmento','reference segmentos'),
                Field('nombre_contexto'),
                Field('cuerpo_contexto'),
                Field('estado',default=True),
                Field('usuario_creador','integer'),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer')
            )

            db.define_table('horarios_segmentos',
                Field('segmento','reference segmentos'),
                Field('nombre_horario'),
                Field('dia_inicio'),
                Field('hora_inicio'),
                Field('hora_fin'),
                Field('dia_laborable','integer'),
                Field('dias_festivos'),
                Field('estado',default=True),
                Field('usuario_creador','integer'),
                Field('fecha_creacion','integer'),
                Field('hora_creacion','integer')
            )

            db.define_table('contexto_chatbot_segmentos',
                Field('contexto_segmento','reference segmentos'),
                Field('contexto_nombre_contexto'),
                Field('contexto_nombre_json'),
                Field('contexto_cantidad_nodos'),
                Field('contexto_estado',default=False),
                Field('contexto_usuario_creador','integer'),
                Field('contexto_fecha_creacion','integer'),
                Field('contexto_hora_creacion','integer'),
                Field('contexto_fecha_modificacion','integer'),
                Field('contexto_hora_modificacion','integer'),
                Field('contexto_usuario_modificacion','integer'),
            )

            db.define_table('variables_data_prueba_contexto_chatbot',
                Field('segmento','integer'),
                Field('id_contexto'),
                Field('cantidad_campos','integer'),
                Field('valores_variables','text'),
                Field('creador','integer'),
                Field('estado',default=True),
                Field('fecha_creacion'),
                Field('hora_creacion'),
            )

            db.define_table('nodo_contexto_chatbot_segmentos',
                Field('nodo_contexto','reference contexto_chatbot_segmentos'),
                Field('nodo_nombre'),
                Field('nodo_mensaje'),
                Field('nodo_mensaje_error'),
                Field('nodo_tipo'),
                Field('nodo_directo'),
                Field('nodo_num_opciones'),
                Field('nodo_opciones'),
                Field('nodo_id_resultado'),
                Field('nodo_usuario_creador','integer'),
                Field('nodo_fecha_creacion','integer'),
                Field('nodo_hora_creacion','integer'),
                Field('nodo_fecha_modificacion','integer'),
                Field('nodo_hora_modificacion','integer'),
                Field('nodo_usuario_modificacion','integer'),
            )


            db.define_table('configuracion_formularios_segmento',
                Field('segmento','reference segmentos'),
                Field('nombre_formulario'),
                Field('cantidad_campos','integer'),
                Field('creador','integer'),
                Field('estado',default=True),
                Field('fecha_creacion'),
                Field('hora_creacion'),
            )

            db.define_table('configuracion_campos_formulario',
                Field('formulario','reference configuracion_formularios_segmento'),
                Field('tipo_campo'),
                Field('tipo_dato'),
                Field('nombre_label'),
                Field('obligatorio'),
                Field('descripcion_campo'),
                Field('tamano_texto'),
                Field('estado',default=True),
                Field('creador','integer'),
                Field('fecha_creacion' , 'integer'),
                Field('hora_creacion' , 'integer'),
            )

            db.define_table('formulario_resultado',
                Field('formulario','reference configuracion_formularios_segmento'),
                Field('resultado'),
                Field('id_resultado', 'integer'),
                Field('fecha_creacion'),
                Field('hora_creacion'),
            )

            db.define_table('configuracion_resultados_segmento',
                Field('segmento','reference segmentos'),
                Field('resultado'),
                Field('id_resultado'),
                Field('estado',defautl=True),
                Field('creador','integer'),
                Field('fecha_creacion' , 'integer'),
                Field('hora_creacion' , 'integer')
            )

            db.define_table('segmento_puntos_de_pago',
                Field('segmento','reference segmentos'),
                Field('empresa','integer'),
                Field('cliente','integer'),
                Field('punto_pago'),
                Field('estado',defautl=True),
                Field('creador','integer'),
                Field('fecha_creacion' , 'integer'),
                Field('hora_creacion' , 'integer')
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table segmentos, campo_segmentos, contexto_segmentos, sms_prestab_segmentos, horarios_segmentos, contexto_chatbot_segmentos, nodo_contexto_chatbot_segmentos, configuracion_formularios_segmento configuracion_campos_formulario, formulario_resultado => '+str(e)+'' )
            # logs.logFile()
            return False
            pass

    def getCreateSegmento( self ):
        db = self.db
        try:
            varGl     = DataGlobal()
            idSegmt   = db.segmentos.insert(
                cliente_segmento         = self.idCliente,
                empresa_segmento         = self.idEmpresa,
                nombre_segmento          = self.nomSegmento,
                id_segmento_strauss      = self.idSegStrauss,
                fecha_creacion_segmento  = varGl.fechaIntModels,
                hora_creacion_segmento   = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se crear el segmento: '+str(self.nomSegmento).lower()+'  con id: '+str(idSegmt)+' ' )
            logs.logFile()
        except Exception as e:
            idSegmt  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSegmt
    
  
    def setCambioEstadoSegEmpresa( self ):
        db = self.db
        if self.estadoSegmento == 0:
            self.estadoSegmento = True
        else:
            self.estadoSegmento = False
            pass
        idSegmentoUp = db( db.segmentos.empresa_segmento == self.idEmpresa ).update( estado_segmento = self.estadoSegmento )
        return idSegmentoUp
    

    def setCambioEstadoSegCliente( self ):
        db = self.db
        if self.estadoSegmento == 0:
            self.estadoSegmento = True
        else:
            self.estadoSegmento = False
            pass
        idSegmentoUp = db( db.segmentos.cliente_segmento == self.idCliente ).update( estado_segmento = self.estadoSegmento )
        return idSegmentoUp


    def setCambioEstadoSegmentos( self ):
        db = self.db
        if self.estadoSegmento == 0:
            self.estadoSegmento = True
        else:
            self.estadoSegmento = False
            pass
        idSegmentoUp = db( db.segmentos.id == self.idSegmento ).update( estado_segmento = self.estadoSegmento )
        return idSegmentoUp


    def setCambioNombreSegmentos( self ):
        db = self.db
        idSegmnentoUp = db( db.segmentos.id == self.idSegmento ).update( nombre_segmento = self.nomSegmento )
        return idSegmnentoUp

    def getListarIdClienteSegmentos( self ):
        db = self.db
        listadoSegmentosClienteId = db( db.segmentos.cliente_segmento == self.idCliente  ).select( db.segmentos.ALL )
        return listadoSegmentosClienteId


    def getListarIdClienteSegmento( self ):
        db = self.db
        listadoClienteSegmentoId = db( ( db.segmentos.cliente_segmento == self.idCliente ) & ( db.segmentos.nombre_segmento == self.nomSegmento ) & (  db.segmentos.estado_segmento == True ) ).select( db.segmentos.ALL ).last()
        return listadoClienteSegmentoId

    def getListarNomSegmentos( self ):
        db = self.db
        listadoSegmentos = db( ( db.segmentos.nombre_segmento == self.nomSegmento ) & (  db.segmentos.estado_segmento == True ) ).select( db.segmentos.ALL ).last()
        return listadoSegmentos


    def getListarIdSegmento( self ):
        db = self.db
        segmentoList = db( ( db.segmentos.id == self.idSegmento ) & (  db.segmentos.estado_segmento == True ) ).select( db.segmentos.ALL ).last()
        return segmentoList


    def getListarSegmentos( self ):
        db = self.db
        segmentosLista = db( ( db.segmentos.id > self.idSegmento ) & (  db.segmentos.estado_segmento == True ) ).select( db.segmentos.ALL )
        return segmentosLista

    # Puntos de pago
    def getCreatePuntoSegmento( self ):
        db = self.db
        try:
            varGl      = DataGlobal()
            if db( ( db.segmento_puntos_de_pago.segmento== self.idSegmento ) & ( db.segmento_puntos_de_pago.punto_pago == self.punto_pago  ) ).count() == varGl.estadoFalsNum:
                idSegPunto = db.segmento_puntos_de_pago.insert(
                    segmento                = self.idSegmento,
                    cliente                 = self.idCliente,
                    empresa                 = self.idEmpresa,
                    punto_pago              = self.punto_pago,
                    usuario_creador         = self.userCreate,
                    fecha_creacion          = varGl.fechaIntModels,
                    hora_creacion           = varGl.horaIntModels
                )
                logs = InfoLogs( 'info', 'Se crear para el segmento: '+str(self.punto_pago).lower()+'  con id: '+str(idSegPunto)+' ' )
                logs.logFile()
            else:
                idSegPunto  = varGl.estadoFalsNum
                pass
        except Exception as e:
            idSegPunto  = varGl.estadoNoIniNum
            logs = InfoLogs( 'error', 'Error en: getCreatePuntoSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSegPunto


    def getListPuntoSeg( self ):
        db = self.db
        try:
            varGl         = DataGlobal()
            dbEmP         = db.segmento_puntos_de_pago
            listSegPunto  = db( dbEmP.segmento == self.idSegmento ).select( dbEmP.punto_pago, dbEmP.id, orderby = dbEmP.punto_pago )
        except Exception as e: 
            listSegPunto  = varGl.estadoNoIniNum
            logs = InfoLogs( 'error', 'Error en: getListPuntoSeg => '+str(e)+'' )
            logs.logFile()
            pass
        return listSegPunto
    

    def getDeletePuntoSeg( self ):
        db = self.db
        try:
            varGl       = DataGlobal()
            dbEmP       = db.segmento_puntos_de_pago
            idSegPunto  = db( ( dbEmP.segmento == self.idSegmento ) & (dbEmP.punto_pago == self.punto_pago ) ).delete()
        except Exception as e:
            idSegPunto  = varGl.estadoNoIniNum
            logs = InfoLogs( 'error', 'Error en: getDeletePuntoSeg => '+str(e)+'' )
            logs.logFile()
            pass
        return idSegPunto
    # Fin puntos de pago
    # Resultados segmentos
    def getCreateResultadosSegmento( self ):
        try:
            db                       = self.db
            varGl                    = DataGlobal()
            dbResSeg                 = db.configuracion_resultados_segmento
            if db( ( dbResSeg.segmento == self.idSegmento ) & ( dbResSeg.id_resultado == self.idResultadoF ) ).count() > varGl.estadoFalsNum:
                db( ( dbResSeg.segmento == self.idSegmento ) & ( dbResSeg.id_resultado == self.idResultadoF ) ).delete()
                idSegmtResul         = varGl.estadoFalsNum
            else:
                idSegmtResul         = db.configuracion_resultados_segmento.insert(
                    segmento         = self.idSegmento,  
                    resultado        = self.resultadoFor,
                    id_resultado     = self.idResultadoF,
                    usuario_creador  = self.userCreate,
                    fecha_creacion   = varGl.fechaIntModels,
                    hora_creacion    = varGl.horaIntModels
                )
                logs = InfoLogs( 'info', 'Se crear el getCreateResultadosSegmento: con id: '+str(idSegmtResul)+' ' )
                logs.logFile()
                pass
        except Exception as e:
            idSegmtResul  = varGl.estadoNoIniNum
            logs = InfoLogs( 'error', 'Error en: getCreateResultadosSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSegmtResul
    

    def setCountResultadosSegmento( self ):
        try:
            db               = self.db
            varGl            = DataGlobal()
            dbResSeg         = db.configuracion_resultados_segmento
            countSegmtResul  = db( ( dbResSeg.segmento == self.idSegmento ) & ( dbResSeg.id_resultado == self.idResultadoF ) ).count()
        except Exception as e:
            countSegmtResul  = varGl.estadoNoIniNum
            logs = InfoLogs( 'error', 'Error en: setCountResultadosSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return countSegmtResul
    

    def setResultadosSegmento( self ):
        try:
            db               = self.db
            varGl            = DataGlobal()
            dbResSeg         = db.configuracion_resultados_segmento
            listSegmtResul   = db( dbResSeg.segmento == self.idSegmento ).select( dbResSeg.id_resultado, dbResSeg.resultado, orderby = dbResSeg.resultado )
        except Exception as e:
            listSegmtResul   = [] 
            logs = InfoLogs( 'error', 'Error en: setResultadosSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return listSegmtResul

    # Fin resultados segmentos


    def getValidateCampoAsig( self ):
        db = self.db
        fieldRepresenta     = 0
        idFieldSeg          = 0
        fieldRepresentaTmp  = db( ( db.campo_segmentos.segmento == self.idSegmento ) & ( db.campo_segmentos.campo_base == self.nomCampoReal ) ).select( db.campo_segmentos.campo_representa, db.campo_segmentos.id ).last()
        if fieldRepresentaTmp:
            fieldRepresenta = fieldRepresentaTmp.campo_representa
            idFieldSeg      = fieldRepresentaTmp.id
            pass
        return fieldRepresenta,idFieldSeg

    def deleteAsigFieldSeg( self ):
        try:
            db = self.db
            idDeleteField = db( ( db.campo_segmentos.segmento == self.idSegmento ) & ( db.campo_segmentos.campo_base == self.nomCampoReal ) & ( db.campo_segmentos.campo_representa == self.nomCampoRepr ) ).delete()
        except Exception as e:
            idDeleteField = 0
            logs = InfoLogs( 'error', 'Error en: deleteAsigFieldSeg => '+str(e)+'' )
            logs.logFile()
            pass
        return idDeleteField 
    
    def getCreateCampoSegmento( self ):
        try:
            db                       = self.db
            varGl                    = DataGlobal()
            fieldRep,idFieldRet      = self.getValidateCampoAsig()
            if fieldRep              == 0:
                idSegmtField         = db.campo_segmentos.insert(
                    segmento         = self.idSegmento,  
                    campo_base       = self.nomCampoReal,
                    campo_representa = self.nomCampoRepr,
                    usuario_creador  = self.userCreate,
                    fecha_creacion   = varGl.fechaIntModels,
                    hora_creacion    = varGl.horaIntModels
                )
                logs = InfoLogs( 'info', 'Se crear el getCreateCampoSegmento: con id: '+str(idSegmtField)+' ' )
                logs.logFile()
            else:
                idSegmtField =  db( db.campo_segmentos.id == idFieldRet ).delete()
                pass
        except Exception as e:
            idSegmtField  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateCampoSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSegmtField

    def getCamposAsigSeg( self ):
        db = self.db
        fieldsSegmento  = db( db.campo_segmentos.segmento == self.idSegmento ).select( db.campo_segmentos.campo_base, db.campo_segmentos.campo_representa )
        return fieldsSegmento


    def getCreateHorarioSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegH               = db.horarios_segmentos
            if db( dbSegH.segmento == self.idSegmento ).count() < varGl.cantHorarioSeg:
            
                idHoraSeg            = dbSegH.insert(
                    segmento         = self.idSegmento,  
                    nombre_horario   = self.nomHorario,
                    dia_inicio       = self.diaIniHr,
                    hora_inicio      = self.horaIniHr,
                    dia_laborable    = self.diaLabora,
                    hora_fin         = self.horaFinHr,
                    usuario_creador  = self.userCreate,
                    dias_festivos    = self.diaFest,
                    fecha_creacion   = varGl.fechaIntModels,
                    hora_creacion    = varGl.horaIntModels
                )

                logs = InfoLogs( 'info', 'Se crear el getCreateHorarioSegmento: con id: '+str(idHoraSeg)+' ' )
                logs.logFile()
            else:
                idHoraSeg = -1
                pass
        except Exception as e:
            idHoraSeg  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateHorarioSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idHoraSeg

    def getUpdateHorarioSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegH               = db.horarios_segmentos
            idHorarioUp          = db( dbSegH.id == self.idHorario ).update(
                nombre_horario   = self.nomHorario,
                dia_inicio       = self.diaIniHr,
                hora_inicio      = self.horaIniHr,
                dia_laborable    = self.diaLabora,
                hora_fin         = self.horaFinHr,
                usuario_creador  = self.userCreate,
                dias_festivos    = self.diaFest,
                fecha_creacion   = varGl.fechaIntModels,
                hora_creacion    = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se Actualiza el getUpdateHorarioSegmento: con id: '+str(idHorarioUp)+' ' )
            logs.logFile()
        except Exception as e:
            idHorarioUp  = 0
            logs = InfoLogs( 'error', 'Error en: getUpdateHorarioSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idHorarioUp


    def setListHorariosSeg( self ):
        db = self.db
        listHorSeg  = db( ( db.horarios_segmentos.segmento == self.idSegmento ) & ( db.horarios_segmentos.estado == True )  ).select( db.horarios_segmentos.ALL, orderby =~db.horarios_segmentos.estado )
        return listHorSeg

    def setHorariosSegId( self ):
        db = self.db
        listHorSegId  = db( ( db.horarios_segmentos.segmento == self.idSegmento ) & ( db.horarios_segmentos.estado == True ) & ( db.horarios_segmentos.dia_inicio == self.diaBuscarSem )  ).select( db.horarios_segmentos.dia_laborable,db.horarios_segmentos.hora_inicio,db.horarios_segmentos.hora_fin,db.horarios_segmentos.dias_festivos ).last()
        return listHorSegId


    def setCambioEstadoHorario( self ):
        db = self.db
        if self.estadoHorario == 0:
            self.estadoHorario = True
        else:
            self.estadoHorario = False
            pass
        idHorarioUp = db( db.horarios_segmentos.id == self.idHorario ).update( estado = self.estadoHorario )
        return idHorarioUp



    # Formularios

    def setListFormularioSegmento( self ):
        db = self.db
        listFormulariosSeg  = db( ( db.configuracion_formularios_segmento.segmento == self.idSegmento ) & ( db.configuracion_formularios_segmento.estado == True )  ).select( db.configuracion_formularios_segmento.ALL, orderby =~db.configuracion_formularios_segmento.estado )
        return listFormulariosSeg


    def setCantResulInFormulario( self ):
        db = self.db
        cantResForm  = db( db.formulario_resultado.formulario == self.idFormulario ).count()
        return cantResForm

    def getCreateFormularioSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegForm            = db.configuracion_formularios_segmento
            if db( ( ( dbSegForm.segmento == self.idSegmento ) & ( dbSegForm.nombre_formulario == self.nomFormulario ) ) ).count() == varGl.estadoFalsNum:
                
                idFormularioSeg       = dbSegForm.insert(
                    segmento          = self.idSegmento,
                    nombre_formulario = self.nomFormulario, 
                    cantidad_campos   = self.canCampoFormulario,
                    creador           = self.userCreate,
                    fecha_creacion    = varGl.fechaIntModels,
                    hora_creacion     = varGl.horaIntModels
                )
                logs = InfoLogs( 'info', 'Se crear el getCreateFormularioSegmento: con id: '+str(idFormularioSeg)+' ' )
                logs.logFile()
            else:
                idFormularioSegTmp = db( ( ( dbSegForm.segmento == self.idSegmento ) & ( dbSegForm.nombre_formulario == self.nomFormulario ) ) ).select( dbSegForm.id ).last()
                if idFormularioSegTmp:
                    idFormularioSeg = idFormularioSegTmp.id    
                else:
                    idFormularioSeg = 0
                    pass
                pass
        except Exception as e:
            idFormularioSeg  = -1
            logs = InfoLogs( 'error', 'Error en: getCreateFormularioSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idFormularioSeg


    def getCreateCampoForm( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegForm            = db.configuracion_formularios_segmento
            if db(  dbSegForm.id == self.idFormulario  ).count() == varGl.estadoIniNum:
                
                if db(  ( db.configuracion_campos_formulario.formulario == self.idFormulario ) & ( db.configuracion_campos_formulario.nombre_label == self.nombre_label )  ).count() == varGl.estadoFalsNum:

                    idCampoForm = db.configuracion_campos_formulario.insert(
                        formulario        = self.idFormulario,
                        tipo_campo        = self.tipo_campo,
                        tipo_dato         = self.tipo_dato,
                        nombre_label      = self.nombre_label,
                        obligatorio       = self.obligatorio,
                        descripcion_campo = self.descripcion_campo,
                        tamano_texto      = self.tamano_texto,
                        creador           = self.userCreate,
                        fecha_creacion    = varGl.fechaIntModels,
                        hora_creacion     = varGl.horaIntModels
                    )
                    logs = InfoLogs( 'info', 'Se crear el getCreateCampoForm: con id: '+str(idCampoForm)+' ' )
                    logs.logFile()
                else:
                    idCampoForm = 0
                    pass
            else:
                idCampoForm = -2
                pass
        except Exception as e:
            idCampoForm  = -1
            logs = InfoLogs( 'error', 'Error en: getCreateCampoForm => '+str(e)+'' )
            logs.logFile()
            pass
        return idCampoForm


    def getUpdateFormularioSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegH               = db.horarios_segmentos
            idHorarioUp          = db( dbSegH.id == self.idHorario ).update(
                nombre_horario   = self.nomHorario,
                dia_inicio       = self.diaIniHr,
                hora_inicio      = self.horaIniHr,
                dia_laborable    = self.diaLabora,
                hora_fin         = self.horaFinHr,
                usuario_creador  = self.userCreate,
                dias_festivos    = self.diaFest,
                fecha_creacion   = varGl.fechaIntModels,
                hora_creacion    = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se Actualiza el getUpdateFormularioSegmento: con id: '+str(idHorarioUp)+' ' )
            logs.logFile()
        except Exception as e:
            idHorarioUp  = 0
            logs = InfoLogs( 'error', 'Error en: getUpdateFormularioSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idHorarioUp


    def setInfoFormulario( self ):
        db = self.db
        dbConfigForm  = db.configuracion_formularios_segmento
        listFormSeg   = db( ( dbConfigForm.id == self.idFormulario ) & ( dbConfigForm.estado == True )  ).select( dbConfigForm.ALL ).last()
        return listFormSeg

    def setFormulariosSegId( self ):
        db = self.db
        dbConfigForm    = db.configuracion_formularios_segmento
        listsFormSegId  = db( ( dbConfigForm.segmento == self.idSegmento ) & ( dbConfigForm.estado == True )  ).select( dbConfigForm.id )
        return listsFormSegId


    def setCambioEstadoFormulario( self ):
        db = self.db
        if self.estadoHorario == 0:
            self.estadoHorario = True
        else:
            self.estadoHorario = False
            pass
        idHorarioUp = db( db.horarios_segmentos.id == self.idHorario ).update( estado = self.estadoHorario )
        return idHorarioUp


    def setCountFormularioResul( self ):
        db             = self.db
        dbFRes         = db.formulario_resultado
        cantResulForm  = db( ( dbFRes.formulario == self.idFormulario ) & ( dbFRes.resultado == self.resultadoFor ) & ( dbFRes.id_resultado == self.idResultadoF ) ).count()
        return cantResulForm


    def setAgregarQuitarResultado( self ):
        db             = self.db
        varGl          = DataGlobal()
        dbFRes         = db.formulario_resultado
        if db( ( dbFRes.formulario == self.idFormulario ) & ( dbFRes.resultado == self.resultadoFor ) & ( dbFRes.id_resultado == self.idResultadoF ) ).count() > 0:
            db( ( dbFRes.formulario == self.idFormulario ) & ( dbFRes.resultado == self.resultadoFor ) & ( dbFRes.id_resultado == self.idResultadoF ) ).delete()
            resulOpResForm  = varGl.estadoFalsNum
        else:
            resulOpResForm = dbFRes.insert(
                formulario        = self.idFormulario,
                resultado         = self.resultadoFor,
                id_resultado      = self.idResultadoF,
                fecha_creacion    = varGl.fechaIntModels,
                hora_creacion     = varGl.horaIntModels
            )
            pass
        return resulOpResForm


    def setCamposFormulario( self ):
        db             = self.db
        dbConfigForm   = db.configuracion_formularios_segmento
        dbCampFor      = db.configuracion_campos_formulario
        campos         = db( dbConfigForm.id ==  self.idFormulario  ).select( dbCampFor.nombre_label,dbCampFor.id,dbCampFor.obligatorio, dbCampFor.tipo_dato,dbCampFor.tipo_campo,\
            dbCampFor.descripcion_campo,dbCampFor.tamano_texto,dbCampFor.formulario,left=(dbConfigForm.on(dbConfigForm.id == dbCampFor.formulario)),orderby=dbCampFor.id)
        return campos

    # Fin formulario


    def getCreateSmsPrestbSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegSms             = db.sms_prestab_segmentos
            idSmsPreSeg          = dbSegSms.insert(
                segmento         = self.idSegmento,  
                nombre_sms       = self.nomSms,  
                tipo_sms         = self.tipoSmsPr,
                sms              = self.smsPr,
                usuario_creador  = self.userCreate,
                fecha_creacion   = varGl.fechaIntModels,
                hora_creacion    = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se crear el getCreateSmsPrestbSegmento: con id: '+str(idSmsPreSeg)+' ' )
            logs.logFile()
        except Exception as e:
            idSmsPreSeg  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateSmsPrestbSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSmsPreSeg


    def getUpdateSmsPrestbSegmento( self ):
        try:
            db                   = self.db
            varGl                = DataGlobal()
            dbSegSms             = db.sms_prestab_segmentos
            idSmsPreSegUp        = db( dbSegSms.id == self.idSmsPret ).update(
                nombre_sms       = self.nomSms,  
                tipo_sms         = self.tipoSmsPr,
                sms              = self.smsPr,
                usuario_creador  = self.userCreate,
                fecha_creacion   = varGl.fechaIntModels,
                hora_creacion    = varGl.horaIntModels
            )
            logs = InfoLogs( 'info', 'Se Actualiza el getUpdateSmsPrestbSegmento: con id: '+str(idSmsPreSegUp)+' ' )
            logs.logFile()
        except Exception as e:
            idSmsPreSegUp  = 0
            logs = InfoLogs( 'error', 'Error en: getUpdateSmsPrestbSegmento => '+str(e)+'' )
            logs.logFile()
            pass
        return idSmsPreSegUp


    def setListSmsPrebSeg( self ):
        db = self.db
        listSmsPrSeg  = db( ( db.sms_prestab_segmentos.segmento == self.idSegmento ) & ( db.sms_prestab_segmentos.estado == True )  ).select( db.sms_prestab_segmentos.ALL, orderby =~db.sms_prestab_segmentos.estado )
        return listSmsPrSeg


    def setSmsPrebSegId( self ):
        db = self.db
        listSmPrSegId  = db( ( db.sms_prestab_segmentos.segmento == self.idSegmento ) & ( db.sms_prestab_segmentos.estado == True ) & ( db.sms_prestab_segmentos.tipo_sms == self.tipoSmsPr )  ).select( db.sms_prestab_segmentos.sms ).last()
        return listSmPrSegId


    def setSmssPrebSegId( self ):
        db = self.db
        listSmsPrSegId  = db( ( db.sms_prestab_segmentos.segmento == self.idSegmento ) & ( db.sms_prestab_segmentos.estado == True ) & ( db.sms_prestab_segmentos.tipo_sms == self.tipoSmsPr )  ).select( db.sms_prestab_segmentos.sms )
        return listSmsPrSegId


    def setCambioEstadoSmsPrest( self ):
        db = self.db
        if self.estadoSmsPret == 0:
            self.estadoSmsPret = True
        else:
            self.estadoSmsPret = False
            pass
        idSmsPretUp = db( db.sms_prestab_segmentos.id == self.idSmsPret ).update( estado = self.estadoSmsPret )
        # print('idSmsPretUp', idSmsPretUp)
        return idSmsPretUp


    # Inicio contextos chatbot 

    def getCreateContChatBot( self ):
        try:
            db       = self.db
            varGl    = DataGlobal()
            dbConCh  = db.contexto_chatbot_segmentos
            if db( ( dbConCh.contexto_segmento == self.idSegmento ) & ( dbConCh.contexto_nombre_contexto == str(self.nomContBot).lower() )   ).count() == varGl.estadoFalsNum:
            
                idContCahtBot                      = dbConCh.insert(
                    contexto_segmento              = self.idSegmento,
                    contexto_nombre_contexto       = str(self.nomContBot).lower(),
                    contexto_nombre_json           = self.nomContBotJson,
                    contexto_cantidad_nodos        = self.cantNodosCont,
                    contexto_usuario_creador       = self.userCreate,
                    contexto_fecha_creacion        = varGl.fechaIntModels,
                    contexto_hora_creacion         = varGl.horaIntModels,
                    contexto_fecha_modificacion    = varGl.fechaIntModels,
                    contexto_hora_modificacion     = varGl.horaIntModels,
                    contexto_usuario_modificacion  = self.userCreate
                )
                db( dbConCh.id == idContCahtBot  ).update(
                    contexto_nombre_json  = str(idContCahtBot)+'.json'
                )
                logs = InfoLogs( 'info', 'Se Crea el contextoBot getCreateContChatBot: con id: '+str(idContCahtBot)+' ' )
                logs.logFile()
            else:
                idContCahtBotTmp = db( ( dbConCh.contexto_segmento == self.idSegmento ) & ( dbConCh.contexto_nombre_contexto == str(self.nomContBot).lower() )   ).select( dbConCh.id ).last()
                if idContCahtBotTmp:
                    idContCahtBot = idContCahtBotTmp.id 
                    pass
                pass
        except Exception as e:
            idContCahtBot  = 0
            logs           = InfoLogs( 'error', 'Error en: getCreateContChatBot => '+str(e)+'' )
            logs.logFile()
            pass
        return idContCahtBot



    def getCreateNodoIdContexto( self ):
        try:
            db            = self.db
            varGl         = DataGlobal()
            dbNodC        = db.nodo_contexto_chatbot_segmentos

            if db( ( dbNodC.nodo_contexto == self.idConChat ) & ( dbNodC.nodo_nombre == str(self.nodo_nombre).lower() )   ).count() == varGl.estadoFalsNum:

                idNodoReturn                  = dbNodC.insert(
                    nodo_contexto             = self.idConChat,
                    nodo_nombre               = self.nodo_nombre,
                    nodo_mensaje              = self.nodo_mensaje,
                    nodo_mensaje_error        = self.nodo_mensaje_error,
                    nodo_tipo                 = self.nodo_tipo,
                    nodo_directo              = self.nodo_directo,
                    nodo_num_opciones         = self.nodo_num_opciones,
                    nodo_opciones             = self.nodo_opciones,
                    nodo_id_resultado         = self.nodo_id_resultado,
                    nodo_usuario_creador      = self.userCreate,
                    nodo_fecha_creacion       = varGl.fechaIntModels,
                    nodo_hora_creacion        = varGl.horaIntModels,
                    nodo_fecha_modificacion   = varGl.fechaIntModels,
                    nodo_hora_modificacion    = varGl.horaIntModels,
                    nodo_usuario_modificacion = self.userCreate,
                )
                logs = InfoLogs( 'info', 'Se Crea el nodo el getCreateNodoIdContexto: con id: '+str(idNodoReturn)+' ' )
                logs.logFile()
            else:
                idNodoReturnTmp = db( ( dbNodC.nodo_contexto == self.idConChat ) & ( dbNodC.nodo_nombre == str(self.nodo_nombre).lower() )   ).select( dbNodC.id ).last()
                if idNodoReturnTmp:
                    idNodoReturn = idNodoReturnTmp.id 
                    pass
                pass
        except Exception as e:
            idNodoReturn  = 0
            logs           = InfoLogs( 'error', 'Error en: getCreateNodoIdContexto => '+str(e)+'' )
            logs.logFile()
            pass
        return idNodoReturn



    def setContextChatbotSegId( self ):
        db                    = self.db
        dbConCh               = db.contexto_chatbot_segmentos
        listsContChatbotegId  = db( dbConCh.contexto_segmento == self.idSegmento  ).select( dbConCh.ALL)
        return listsContChatbotegId

    def setContextChatbotSegStatus( self ):
        db          = self.db
        dbConCh     = db.contexto_chatbot_segmentos
        countContx  = db( ( dbConCh.contexto_segmento == self.idSegmento ) & ( dbConCh.contexto_estado == True )  ).count()
        return countContx

    def setContextChatbotId( self ):
        try:
            db                    = self.db
            dbConCh               = db.contexto_chatbot_segmentos
            listsContChatbotegId  = db( dbConCh.id == self.idConChat  ).select( dbConCh.contexto_nombre_json ).last()
        except Exception as e:
            listsContChatbotegId  = False
            logs           = InfoLogs( 'error', 'Error en: setContextChatbotId => '+str(e)+'' )
            logs.logFile()
            pass
        return listsContChatbotegId


    def getchangeStatus( self ):
        try:
            varGl          = DataGlobal()
            db             = self.db
            dbConCh        = db.contexto_chatbot_segmentos
            db( dbConCh.contexto_segmento == self.idSegmento  ).update( contexto_estado = False )
            print('self.idConChat =>', self.idConChat)
            idChangercont  = db( dbConCh.id == self.idConChat  ).update( 
                contexto_nombre_json           = self.nameNew, 
                contexto_estado                = self.status,
                contexto_fecha_modificacion    = varGl.fechaIntModels,
                contexto_hora_modificacion     = varGl.horaIntModels,
                contexto_usuario_modificacion  = self.userCreate
            )
        except Exception as e:
            idChangercont  = 0
            logs           = InfoLogs( 'error', 'Error en: getchangeStatus => '+str(e)+'' )
            logs.logFile()
            pass
        return idChangercont


    def setContextChatbotConteId( self ):
        db                = self.db
        dbNodC            = db.nodo_contexto_chatbot_segmentos
        infoNodosContext  = db( dbNodC.nodo_contexto == self.idConChat ).select( dbNodC.ALL )
        return infoNodosContext


    def getCamposPruebaContex( self ):
        try:
            varGl          = DataGlobal()
            db             = self.db
            dbConCh        = db.variables_data_prueba_contexto_chatbot
            dataCamps      = db( dbConCh.id_contexto == self.idConChat ).select( dbConCh.ALL )
        except Exception as e:
            dataCamps      = False
            logs           = InfoLogs( 'error', 'Error en: getCamposPruebaContex => '+str(e)+'' )
            logs.logFile()
            pass
        return dataCamps

    # Fin contextos chatbot