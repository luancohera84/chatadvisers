# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos
from usuariosAsignar import UsuariosAsig
from reportes import Reportes

def setListadoEmpresas():
    
    if ( ( userType[0] ==  'Developer' ) | ( userType[0] ==  'Administrador' ) | ( userType[0] ==  'Director') ):
        company            = Empresas( db )
        company.define_table()
        company.idEmpresa  = 0
        listEmpresasOrd    = company.getListarEmpresas()
    elif userType[0] ==  'Gerente':
        asesorSeg            = UsuariosAsig( db )
        asesorSeg.idUsuario  = idUser
        asesorSeg.define_table()
        listEmpresasOrd      = asesorSeg.infoEmpresasAsesor()
    else:
        listEmpresasOrd      = []
        pass
    
    return listEmpresasOrd


def setCargaChatAsignacion( idEmpresa, nombreEmpresa ):
    rept  = Reportes( db )
    rept.idEmpresa = idEmpresa
    dataChatAsig   = rept.setCountGestionesAsigEmpresa()
    coutnAsigChat  = rept.setCountClientAsigEmpresa()
    return dataChatAsig,coutnAsigChat

def setCargaChatCola( idEmpresa, nombreEmpresa ):
    rept  = Reportes( db )
    rept.idEmpresa = idEmpresa
    dataChatCola   = rept.setCountColaAsigEmpresa()
    coutnAsigChat  = rept.setCountSmsAsigEmpresa()
    return dataChatCola,coutnAsigChat



def promedioAtencion( idEmpresa, nombreEmpresa ):
    rept               = Reportes( db )
    rept.idEmpresa     = idEmpresa
    resulPromAntencion = rept.setPromedioAtencion()
    return resulPromAntencion


def acuerdosPago( idEmpresa, nombreEmpresa ):
    rept               = Reportes( db )
    rept.idEmpresa     = idEmpresa
    acuerdosDePgoResul = rept.setAcuerdosDePago()
    return acuerdosDePgoResul


def setAsesoresAtencion( idEmpresa, nombreEmpresa ):
    rept                 = Reportes( db )
    rept.idEmpresa       = idEmpresa
    dataAsesoresAtencion = rept.setAtencionAsesor()
    return dataAsesoresAtencion


def setGestionesAsig( idEmpresa ):
    rept                 = Reportes( db )
    rept.idEmpresa       = idEmpresa
    logsMostrar( 'info', 'setGestionesAsig  rept.idEmpresa=> '+str(rept.idEmpresa)+' ' )
    infoGestiones        = ''  
    infoGestiones        = rept.gestionesAsignacion()
    logsMostrar( 'info', 'setGestionesAsig  infoGestiones=> '+str(infoGestiones)+' ' )
    return infoGestiones


def setlimpiarReporte( file ):
    import os, sys
    import subprocess
    try:
        if os.path.exists("""/var/www/web2py/applications/init/static/multimedia/"""):
            subprocess.call(
                """
                    rm -r /var/www/web2py/applications/init/static/multimedia/"""+str(file)+"""
                """,
                shell=True
            )
            pass
    except Exception as e:
        logsMostrar( 'info', 'setlimpiarReporte  Error=> '+str(e)+' ' )
        pass
    pass

def setDescargaGestion( idEmpresa, nombreEmpresa ):
    import pandas as pd
    import numpy as np
    from datetime import datetime, time, date, timedelta
    from pandas.io import sql
    import os, sys
    import subprocess
    from _clasFunt import DataGlobal
    try:
        engineConexion = conexionBDS( 'chatbot_asesor', 'localhost', 'root', 'j7t05fLcn0' )
        archivoAlaHora   = "gestiones_"+str(nombreEmpresa).replace(' ','_')+".xlsx"
        df_info      = pd.DataFrame()
        varGlb       = DataGlobal()
        sqlGestion = """
            SELECT
                empresa,
                cliente,
                segmento,
                nombre_cliente,
                identificacion_cliente,
                telefono_cliente,
                descripcion_resultado,
                CONCAT(anio_creacion,'-',mes_creacion,'-',dia_creacion) as fecha_interaccion,
                hora_interaccion,
                valor_acuerdo_venta,
                cuotas_acuerdo_venta,
                fecha_pago_acuerdo_venta,
                punto_pago_acuerdo_venta,
                mensajes_conversacion
            FROM
                interacciones_asesor ia
            WHERE 
                ia.id_empresa  = """+str(idEmpresa)+"""
            ORDER BY
                ia.id
        """
        df_info = df_info.append(pd.read_sql_query(sqlGestion,engineConexion))
        if len(df_info) > varGlb.estadoFalsNum:
            df_info.to_excel("/tmp/"+str(archivoAlaHora)+"",index=False)
            # logsMostrar( 'info', 'File en TMP' )
            if os.path.exists("/tmp/"+str(archivoAlaHora)+""):
                subprocess.call(
                    """
                        chmod 777 /tmp/"""+str(archivoAlaHora)+"""
                    """,
                    shell=True
                )
                if os.path.exists("""/var/www/web2py/applications/init/static/multimedia"""):
                    subprocess.call(
                        """
                            mv /tmp/"""+str(archivoAlaHora)+"""  /var/www/web2py/applications/init/static/multimedia/
                        """,
                        shell=True
                    )
                else:
                    subprocess.call(
                        """
                            mkdir /var/www/web2py/applications/init/static/multimedia
                        """,
                        shell=True
                    )
                    subprocess.call(
                        """
                            chmod -R 777 /var/www/web2py/applications/init/static/multimedia
                        """,
                        shell=True
                    )
                    subprocess.call(
                        """
                            mv /tmp/"""+str(archivoAlaHora)+"""  /var/www/web2py/applications/init/static/multimedia/
                        """,
                        shell=True
                    )
                    pass
            else:
                logsMostrar( 'error', 'A la hora no se encontro el archivo creado de nombre: '+str(archivoAlaHora)+'' )
                archivoAlaHora   = ''
                pass
        else:
            logsMostrar( 'error', 'No se encontraron registros para la descarga' )
            archivoAlaHora   = ''
            pass
    except Exception as e:
        logsMostrar( 'info', 'setDescargaGestion  Error=> '+str(e)+' ' )
        archivoAlaHora   = ''
        pass
    return archivoAlaHora
