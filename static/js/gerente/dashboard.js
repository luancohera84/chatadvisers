var ger = {
    empresaLiColor: null,
    clienteLiColor: null,
    segmentoLiColor: null,
    nomSegmentoGlb: null,
    idSegmentoGlb: null,
    ubicacionFocus: null,
    tabIdentificador: null,
    myModal:      new bootstrap.Modal('#configSegmento'),
    stars: function() {
        this.carga();
    },
    carga: function(){},
    clickFocusTab: function( tab, identificador ) {
        if (tab === 'contextosBot') {
            $('#newNodos').hide();
            $('#divRegistrosContextos').show();
        }
        $('.nav-tabs a[href="'+ger.ubicacionFocus+'"]').tab('hide');
        $('#'+ger.tabIdentificador+'').removeClass('active');
        $('#'+ger.ubicacionFocus+'').removeClass('show');
        $('#'+ger.ubicacionFocus+'').removeClass('active');
        ger.ubicacionFocus = tab;
        ger.tabIdentificador = identificador;

        // if (tab == 'smsPrestNab') {
        //     $('#idTbodyListSmsPrest').DataTable();
        // }
        
    },
    verInfoEmpresa: function( idEmpresa, nomEmpresa ){
        $('#middle-empresas').load('infoEmpresa',{idEmpresa,nomEmpresa},function(){
            if ( parseInt(ger.empresaLiColor) != parseInt(idEmpresa) ){
                $('#empresaLi_'+ger.empresaLiColor+'').css('background-color','');
                $('#empresaLi_'+idEmpresa+'').css('background-color','#e8f9f8');
                ger.empresaLiColor = idEmpresa;
            }
            template.empresaSelCard   = $('#empresaSelCard').val();
            template.empresaSelNombre = $('#empresaSelNombre').val();
        });
    },
    verInfoCliente: function( idCliente, nomCliente ){
        $('#listClientesDiv').load('infoClientes',{idCliente,nomCliente},function(){
            if ( parseInt(ger.clienteLiColor) != parseInt(idCliente) ){
                $('#clienteLi_'+ger.clienteLiColor+'').css('background-color','');
                $('#clienteLi_'+idCliente+'').css('background-color','#e8f9f8');
                ger.clienteLiColor = idCliente;
            }else{
                console.log('Dice que es igual');
            }
            template.clienteSelCard   = $('#clienteSelCard').val();
            template.clienteSelNombre = $('#clienteSelNombre').val();
        });
    },
    verInfoSegmento: function( idSegmento, nombreSegmentoUp ){
        
        ger.nomSegmentoGlb = nombreSegmentoUp;
        ger.idSegmentoGlb  = idSegmento;
        // $('#configSegmento').modal('hide');
        $('#headerTextconfigSegmento').html(`
            <i class="fas fa-cog"></i>Configuracion del segmento: `+nombreSegmentoUp+`
        `);
        ger.myModal.show();
        // myModal: new bootstrap.Modal('#'),
        
        $('#bodyConfigSegmentos').load('../gerente/infoSegmento',{idSegmento,nombreSegmentoUp},function(){
            
            $('[data-bs-toggle="tooltip"]').tooltip();

            if ( ger.ubicacionFocus ) {
                $('.nav-tabs a[href="'+ger.ubicacionFocus+'"]').tab('show');
                $('#'+ger.tabIdentificador+'').addClass('active');
                $('#'+ger.ubicacionFocus+'').addClass('show');
                $('#'+ger.ubicacionFocus+'').addClass('active');
            }else{
                $('.nav-tabs a[href="# "]').tab('show');
                $('#nav-campos-tab').addClass('active');
                $('#campos').addClass('show');
                $('#campos').addClass('active');
                ger.clickFocusTab('campos','nav-campos-tab');
            }
            // $('#jstree_demo_div').jstree();
            $('#jstree').jstree();
        });
    },
    nuevoHorario: function(){
        $('#divIdTableRegHor').hide();
        $('#divIdRegitroHorSeg').show();
        $('.timepicker').pickatime({
            format: 'HH:i',
            formatSubmit: 'HH:i'
        });
    },
    regresarNuevoHorario: function(){
        $('#divIdRegitroHorSeg').hide();
        $('#divIdTableRegHor').show();
    },
    guardarHorario: function(){
        var nomHorario     = $('#nomHorario').val();
        var diaIniHr       = $('#diaInicio').val();
        var diaLaborable   = $('#diaLaborable').val();
        // var diaFinHr    = $('#diaFin').val();
        var horaIniHr      = $('#horaIncio').val();
        var horaFinHr      = $('#horaFin').val();
        var diaFestivos    = $('#diaFestivos').val();
        if (nomHorario === '' ) {
            template.validaCampo('Nombre horario','nomHorario');
            return false;
        }else if ( diaIniHr === '' ){
            template.validaCampo('Dia inicial','diaInicio');
            return false;
         }else if ( diaLaborable === '' ){
            template.validaCampo('Dia laboral','diaLaborable');
            return false;
        // } else if ( diaFinHr === '' ){
        //     template.validaCampo('Dia final','diaFin');
        //     return false;
        } else if ( horaIniHr === '' ){
            template.validaCampo('Hora inicial','horaIncio');
            return false;
        } else if ( horaFinHr === '' ){
            template.validaCampo('Hora final','horaFin');
            return false;
        } else if ( diaFestivos === '' ){
            template.validaCampo('Festivos','diaFestivos');
            return false;
        }else{
            const dat = {
                nomHorario,
                diaIniHr,
                // diaFinHr,
                diaFestivos,
                horaIniHr,
                horaFinHr,
                diaLaborable,
                idSegment: ger.idSegmentoGlb
            }
            ger.myModal.hide();
            $('#btnAgregarHorario').hide();
            $('#nomHorario,#diaInicio,#diaFin,#diaFestivos,#horaIncio,#horaFin,#diaLaborable').prop('disabled', true);
            $.ajax({
                url: 'agregarHorarioSeg',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                if ( parseInt(data) > 0 ){
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Horario creado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Felicidades',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000);
                }else{
                    if (parseInt(data) === 0) {
                        
                        Swal.fire({
                            title: 'Error', 
                            text:'No se pudo crear el horario. Intentalo nuevamente', 
                            icon: 'error',
                            customClass: 'swalTextTmna',
                            showClass: {
                                popup: 'animate__animated animate__fadeInLeft'
                            },
                            hideClass: {
                                popup: 'animate__animated animate__fadeOutRight'
                            }

                        });
                        ger.myModal.show();
                        $('#btnAgregarHorario').show();
                        $('#nomHorario,#diaInicio,#diaFin,#diaFestivos,#horaIncio,#horaFin,#diaLaborable').prop('disabled', false);
                    } else {
                        Swal.fire({
                            title: 'Resultado', 
                            text:'No se pudo crear el horario. El segmento ya cuenta con  7 horarios creados.', 
                            icon: 'warning',
                            customClass: 'swalTextTmna',
                            showClass: {
                                popup: 'animate__animated animate__fadeInLeft'
                            },
                            hideClass: {
                                popup: 'animate__animated animate__fadeOutRight'
                            }

                        });
                        ger.myModal.show();
                        $('#btnAgregarHorario').show();
                        $('#nomHorario,#diaInicio,#diaFin,#diaFestivos,#horaIncio,#horaFin,#diaLaborable').prop('disabled', false);
                    }
                }
            });
        }
    },
    nuevoPuntoPago: function(){
        $('#divIdTableRegPuntoPago').hide();
        $('#divIdRegitroPuntoPSeg').show();
    },
    guardarPuntoPago: function(){
        var nomPuntoPago     = $('#nomPuntoPago').val();
        if (nomPuntoPago === '' ) {
            template.validaCampo('Punto de pago','nomPuntoPago');
            return false;
        }else{
            const dat = {
                nomPuntoPago,
                idSegment: ger.idSegmentoGlb
            }
            ger.myModal.hide();
            $('#nomPuntoPago').prop('disabled', true);
            $.ajax({
                url: 'agregarPuntoPagoSeg',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                if ( parseInt(data) > 0 ){
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Punto de pago creado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Felicidades',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000);
                }else{
                    if (parseInt(data) < 0) {
                        Swal.fire({
                            title: 'Error', 
                            text:'No se pudo crear el punto de pago. Intentalo nuevamente', 
                            icon: 'error',
                            customClass: 'swalTextTmna',
                            showClass: {
                                popup: 'animate__animated animate__fadeInLeft'
                            },
                            hideClass: {
                                popup: 'animate__animated animate__fadeOutRight'
                            }

                        });
                        ger.myModal.show();
                        $('#nomPuntoPago').prop('disabled', false);
                    } else {
                        Swal.fire({
                            title: 'Resultado', 
                            text:'No se pudo crear el punto de pago. El segmento ya cuenta con este punto de pago', 
                            icon: 'warning',
                            customClass: 'swalTextTmna',
                            showClass: {
                                popup: 'animate__animated animate__fadeInLeft'
                            },
                            hideClass: {
                                popup: 'animate__animated animate__fadeOutRight'
                            }

                        });
                        ger.myModal.show();
                        $('#nomPuntoPago').prop('disabled', false);
                    }
                }
            });
        }
    },
    asignarCampoSegmento: function( idSegmento, nomCampoRep, nomCampoReal, opc ){
        if ( parseInt(opc) === 1 ) {
            template.showPreloader('Quitando campo a mostrar.');
            $.post('quitarCamposSegmentos', {campoRespresenta: nomCampoRep,nomCampoReal,idSegmento}, function(data, textStatus, xhr) {
                if (parseInt(data) > 0) {
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Campo eliminado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Felicidades',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000); 
                }else{
                    Swal.fire('Información', 'No se pudo quitar el campo a mostrar. Intentalo nuevamente', 'warning');
                }
            });
        }else{
            ger.myModal.hide();
            Swal.fire({
                title: 'Confirmacion',
                html: '<p align="justify" style="font-size:14px !important;">Con que nombre se representara a <b>'+nomCampoReal+'</b>,  en las ofertas para el asesor.?<br><b>Nota: Recuerde que el no debe ingresar numeros ni caracteres especiales,solo esta permitido el caracter especial _ , el tamano maximo es de 20 carecteres.</b></p>',
                input: 'text',
                inputAttributes: {
                    autocapitalize: 'off',
                },
                inputValue:nomCampoReal,
                showCancelButton: true,
                confirmButtonText: 'Confirmar',
                showLoaderOnConfirm: true,
                allowOutsideClick: false,
                allowEscapeKey: false,
                showCloseButton: false,
                allowEnterKey:false,
                customClass: 'swalTextTmna',
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                },
                inputValidator: (value) => {
                    return new Promise((resolve) => {
                        // Inicializacion de la variable de validacion
                        let isValid = false;
                        // El valor ingresado
                        let m = value;
                        // El tamaño maximo para nuestro input
                        const maximo = 20;
                        // El pattern que vamos a comprobar
                        const pattern = new RegExp('^[A-ZÁÉÍÓÚÑa-z_]+$', 'i');
                        // Priemra validacion, si input es mayor que 20 caracteres
                        if(value.length > maximo) {
                            isValid = false;
                        } else {
                            if(!pattern.test(value)){ 
                                // Si queremos agregar letras acentuadas y/o letra ñ debemos usar
                                // codigos de Unicode (ejemplo: Ñ: \u00D1  ñ: \u00F1)
                                isValid = false;
                            }else{
                                // Si pasamos todas la validaciones anteriores, entonces el input es valido
                                isValid = true;
                            }
                        }

                        if(!isValid) {
                            resolve('El dato ingresado es incorrecto o su tamano es superior a 20 caracteres')
                        }else{
                            resolve()
                        }
                    })
                },
                preConfirm: (value) => {
                    if (!value) {
                        return Swal.showValidationMessage(`Campo nombre respresentacion vacio`)
                    }
                },
            }).then((result) => {
                if (result.isConfirmed) {
                    if (result.value) {
                        template.showPreloader('Configurando campo a mostrar.');
                        $.post('asignarCamposSegmentos', {campoRespresenta: result.value,nomCampoReal,idSegmento}, function(data, textStatus, xhr) {
                            if (parseInt(data) > 0) {
                                let htmlLet = `
                                    <i class="fas fa-thumbs-up fa-2x text-success"></i>
                                    <p align='center' style='padding-top:-20px;'>
                                    <b> Campo configurado con exito.</b>
                                    </p>
                                `;
                                Swal.fire({
                                    title: 'Felicidades',
                                    html: htmlLet,
                                    showCancelButton: false,
                                    showConfirmButton:false,
                                    allowOutsideClick: false,
                                    allowEscapeKey: false,
                                    allowEnterKey: false,
                
                                });
                                setTimeout(function(){
                                    Swal.close();
                                    ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                                }, 1000);
                            } else {
                                Swal.fire('Información', 'No se pudo configurar en campo. Intentalo nuevamente', 'warning');
                            }
                        });
                    }
                }else{
                    ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                }
            });
        }
    },
    asignarContextoSegmento: function( idSegmento, cuerpoTexto, opc ){},
    nuevoSmsPrest: function(){
        $('#divIdTableRegSmsPres').hide();
        $('#divIdRegitroSmsPresSeg').show();
    },
    regresarNuevoSmsPrest: function(){
        $('#divIdRegitroSmsPresSeg').hide();
        $('#divIdTableRegSmsPres').show();
    },
    guardarSmsPrest: function(){
        var nomSmsPrest   = $('#nomSmsPrest').val();
        var tipoSmsPrest  = $('#tipoSmsPrest').val();
        var smsPrest      = $('#smsPrest').val();
        if (nomSmsPrest === '' ) {
            template.validaCampo('Nombre sms','nomSmsPrest');
            return false;
        }else if ( tipoSmsPrest === '' ){
            template.validaCampo('Tipo sms','tipoSmsPrest');
            return false;
        } else if ( smsPrest === '' ){
            template.validaCampo('Sms','smsPrest');
            return false;
        }else{
            const dat = {
                nomSmsPrest,
                tipoSmsPrest,
                smsPrest,
                idSegment: ger.idSegmentoGlb
            }
            ger.myModal.hide();
            template.showPreloader('Creando sms');
            $('#nomSmsPrest,#tipoSmsPrest,#smsPrest').prop('disabled', true);
            $.ajax({
                url: 'agregarSmsPrestSeg',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                console.log('data =>', data);
                template.hidePreloader();
                if ( parseInt(data) > 0 ){
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Sms creado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Felicidades',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000);
                }else{
                    Swal.fire({
                        title: 'Error', 
                        text:'No se pudo crear el sms. Intentalo nuevamente', 
                        icon: 'error',
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }

                    });
                    ger.myModal.show();
                    $('#nomSmsPrest,#tipoSmsPrest,#smsPrest').prop('disabled', false);
                }
            });
        }
    },
    editarInfoSms: function( idSms, nomSms, tipSms, sms ) {
        $('#divIdTableRegSmsPres').hide();
        $('#divEitarSmsPresSeg').show(); 
        $('#nomSmsPrestEdit').val(nomSms);
        $('#tipoSmsPrestEdit').val(tipSms);
        $('#smsPrestEdit').val(sms);
        $('#idSmsEdit').val(idSms);
    },
    actualizarSmsPrest: function(){
        var nomSmsPrestEdit   = $('#nomSmsPrestEdit').val();
        var tipoSmsPrestEdit  = $('#tipoSmsPrestEdit').val();
        var smsPrestEdit      = $('#smsPrestEdit').val();
        var idSms             = $('#idSmsEdit').val();
        if (nomSmsPrestEdit === '' ) {
            template.validaCampo('Nombre sms','nomSmsPrestEdit');
            return false;
        }else if ( tipoSmsPrestEdit === '' ){
            template.validaCampo('Tipo sms','tipoSmsPrestEdit');
            return false;
        } else if ( smsPrestEdit === '' ){
            template.validaCampo('Sms','smsPrestEdit');
            return false;
        }else{
            const dat = {
                nomSmsPrestEdit,
                tipoSmsPrestEdit,
                smsPrestEdit,
                idSms
            }
            ger.myModal.hide();
            template.showPreloader('Actualizando sms');
            $('#nomSmsPrestEdit,#tipoSmsPrestEdit,#smsPrestEdit').prop('disabled', true);
            $.ajax({
                url: 'actualizarSmsPrest',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                console.log('data =>', data);
                template.hidePreloader();
                if ( parseInt(data) > 0 ){
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Sms actualizado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Información',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000);
                }else{
                    Swal.fire({
                        title: 'Error', 
                        text:'No se pudo actualizar el sms. Intentalo nuevamente', 
                        icon: 'error',
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }

                    });
                    ger.myModal.show();
                    $('#nomSmsPrestEdit,#tipoSmsPrestEdit,#smsPrestEdit').prop('disabled', false);
                }
            });
        }
    },
    editarInfoHorario: function( idHorario, nomHorarioEditar, diaInicioEditar, diaFestivosEditar,horaIncioEditar,horaFinHrEditar,diaLaboraEditar ) {
        $('#divIdTableRegHor').hide();
        $('#divEitarHorSeg').show(); 
        $('#nomHorarioEditar').val(nomHorarioEditar);
        $('#diaInicioEditar').val(diaInicioEditar);
        $('#diaFestivosEditar').val(diaFestivosEditar);
        $('#horaIncioEditar').val(horaIncioEditar);
        $('#horaFinHrEditar').val(horaFinHrEditar);
        $('#diaLaboraEditar').val(diaLaboraEditar);
        $('#idHorarioEdit').val(idHorario);
    },
    
    actualizarHorario: function(){
        var nomHorarioEditar  = $('#nomHorarioEditar').val();
        var diaIniHrEditar    = $('#diaInicioEditar').val();
        var diaFestivosEditar = $('#diaFestivosEditar').val();
        var horaIniHrEditar   = $('#horaIncioEditar').val();
        var horaFinHrEditar   = $('#horaFinHrEditar').val();
        var idHorario         = $('#idHorarioEdit').val();
        var diaLaboraEditar   = $('#diaLaboraEditar').val();
        if (nomHorarioEditar === '' ) {
            template.validaCampo('Nombre horario','nomHorarioEditar');
            return false;
        }else if ( diaIniHrEditar === '' ){
            template.validaCampo('Dia inicial','diaInicioEditar');
            return false;
        }else if ( diaLaboraEditar === '' ){
            template.validaCampo('Dia laboral','diaLaboraEditar');
            return false;
        } else if ( horaIniHrEditar === '' ){
            template.validaCampo('Hora inicial','horaIncioEditar');
            return false;
        } else if ( horaFinHrEditar === '' ){
            template.validaCampo('Hora final','horaFinHrEditar');
            return false;
        } else if ( diaFestivosEditar === '' ){
            template.validaCampo('Festivos','diaFestivosEditar');
            return false;
        }else{
            const dat = {
                nomHorarioEditar,
                diaIniHrEditar,
                diaFestivosEditar,
                horaIniHrEditar,
                horaFinHrEditar,
                diaLaboraEditar,
                idHorario
            }
            ger.myModal.hide();
            $('#btnAgregarHorario').hide();
            $('#nomHorarioEditar,#diaInicioEditar,#diaFestivosEditar,#horaIncioEditar,#horaFinEditar,#diaLaboraEditar').prop('disabled', true);
            $.ajax({
                url: 'actualizarHorario',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                if ( parseInt(data) > 0 ){
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Horario actualizado con exito.</b>
                        </p>
                    `;
                    Swal.fire({
                        title: 'Información',
                        html: htmlLet,
                        showCancelButton: false,
                        showConfirmButton:false,
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,

                    });
                    setTimeout(function(){
                        Swal.close();
                        ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                    }, 1000);
                }else{
                    Swal.fire({
                        title: 'Error', 
                        text:'No se pudo actualizar el horario. Intentalo nuevamente', 
                        icon: 'error',
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }

                    });
                    ger.myModal.show();
                    $('#nomHorarioEditar,#diaInicioEditar,#diaFestivosEditar,#horaIncioEditar,#horaFinEditar,#diaLaboraEditar').prop('disabled', false);
                }
                
            });
        }
    },
    diaLaborable: function( thsValue ) {
        // console.log('thsValue', thsValue.val());
        if (parseInt(thsValue.val()) === 0) {
            $('#divRowHorariosFestivos').hide();
            $('#horaIncio').val('00:00');
            $('#horaFin').val('00:00');
            $('#diaFestivos').val('No');
        } else {
            $('#divRowHorariosFestivos').show();
            $('#horaIncio').val('');
            $('#horaFin').val('');
            $('#diaFestivos').val('');
        }
    },
};
ger.stars();
