# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos


def createCompany( empresaNombreApi ):
    company            =  Empresas( db )
    company.nomEmpresa =  empresaNombreApi
    company.define_table()
    infoCompany        = company.getListarNomEmpresa()
    if not infoCompany: 
        idCompany      = company.getCreateEmpresa()
    else:
        idCompany      = infoCompany.id
        pass
    return idCompany



def createCustomers( idCompany, clienteNombreApi, idClienteStraussApi ):
    customers              = Clientes( db )
    customers.idEmpresa    = idCompany
    customers.nomCliente   = clienteNombreApi
    customers.idCliStrauss = idClienteStraussApi if idClienteStraussApi else 0
    customers.define_table()
    infoCustomers          = customers.getListarIdEmpresaCliente()
    if not infoCustomers:
        idCustomers        = customers.getCreateCliente()
    else:
        idCustomers        = infoCustomers.id
        pass
    return idCustomers


def createSegment( idCustomers, segmentoNombreApi, idSegmentoStaruss, idCompany ): 
    segment              = Segmentos( db )
    segment.idCliente    = idCustomers
    segment.nomSegmento  = segmentoNombreApi
    segment.idEmpresa    = idCompany
    segment.idSegStrauss = idSegmentoStaruss if idSegmentoStaruss else 0
    segment.define_table()
    infosegment          = segment.getListarIdClienteSegmento()
    if not infosegment:
        idSegment        = segment.getCreateSegmento()
    else:
        idSegment        = infosegment.id
        pass

    segment.idSegmento         = idSegment
    segment.nomFormulario      = 'Compromiso pago'
    segment.canCampoFormulario = 7
    segment.userCreate         = 0
    idFormulario  = segment.getCreateFormularioSegmento()
    if idFormulario > 0:
        label = [
            {'label':'telefono','tipo_dato':'text','tipo_campo':'input','obligatorio': '','tamano_texto':100,'descripcion_campo':''},
            {'label':'valor_acordado','tipo_dato':'number','tipo_campo':'input','obligatorio': 'required','tamano_texto':100,'descripcion_campo':''},
            {'label':'cuotas_acordadas','tipo_dato':'number','tipo_campo':'input','obligatorio': 'required','tamano_texto':100,'descripcion_campo':''},
            {'label':'interes_acordados','tipo_dato':'text','tipo_campo':'input','obligatorio': '','tamano_texto':100,'descripcion_campo':''},
            {'label':'fecha_pago','tipo_dato':'date','tipo_campo':'input','obligatorio': 'required','tamano_texto':100,'descripcion_campo':''},
            {'label':'punto_pago','tipo_dato':'text','tipo_campo':'input','obligatorio': '','tamano_texto':12,'descripcion_campo':''},
            {'label':'numero_producto','tipo_dato':'text','tipo_campo':'input','obligatorio': 'required','tamano_texto':100,'descripcion_campo':''}
        ]
        # Formulario default
        for item in label:
            segment.idFormulario       = idFormulario
            segment.tipo_campo         = item['tipo_campo']
            segment.tipo_dato          = item['tipo_dato']             
            segment.nombre_label       = item['label']
            segment.obligatorio        = item['obligatorio']
            segment.descripcion_campo  = item['descripcion_campo']
            segment.tamano_texto       = item['tamano_texto']
            idCamFormulario            = segment.getCreateCampoForm()
            pass
        # Fin formulario default
        pass

    return idSegment

