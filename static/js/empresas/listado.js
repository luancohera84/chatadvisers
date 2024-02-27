var emp = {
    empresaLiColor: null,
    clienteLiColor: null,
    segmentoLiColor: null,
    nomSegmentoGlb: null,
    idSegmentoGlb: null,
    myModal: new bootstrap.Modal('#configSegmento'),
    stars: function() {
        this.carga();
    },
    carga: function(){

    },
    verInfoEmpresa: function( idEmpresa, nomEmpresa ){
        $('#middle-empresas').load('infoEmpresa',{idEmpresa,nomEmpresa},function(){
            if ( parseInt(emp.empresaLiColor) != parseInt(idEmpresa) ){
                $('#empresaLi_'+emp.empresaLiColor+'').css('background-color','');
                $('#empresaLi_'+idEmpresa+'').css('background-color','#e8f9f8');
                emp.empresaLiColor = idEmpresa;
            }
            template.empresaSelCard   = $('#empresaSelCard').val();
            template.empresaSelNombre = $('#empresaSelNombre').val();
        });
    },
    verInfoCliente: function( idCliente, nomCliente ){
        console.log('verInfoCliente =>>>', idCliente);
        console.log('verInfoCliente =>>>', nomCliente);
        $('#listClientesDiv').load('infoClientes',{idCliente,nomCliente},function(){
            if ( parseInt(emp.clienteLiColor) != parseInt(idCliente) ){
                $('#clienteLi_'+emp.clienteLiColor+'').css('background-color','');
                $('#clienteLi_'+idCliente+'').css('background-color','#e8f9f8');
                emp.clienteLiColor = idCliente;
            }else{
                console.log('Dice que es igual');
            }
            template.clienteSelCard   = $('#clienteSelCard').val();
            template.clienteSelNombre = $('#clienteSelNombre').val();
        });
    },
    verInfoSegmento: function( idSegmento, nombreSegmentoUp ){
        emp.nomSegmentoGlb = nombreSegmentoUp;
        emp.idSegmentoGlb  = idSegmento;
        $('#headerTextconfigSegmento').html(`
            <i class="fas fa-cog"></i>Configuracion del segmento: `+nombreSegmentoUp+`
        `);
        
        emp.myModal.show();
        $('#bodyConfigSegmentos').load('infoSegmento',{idSegmento,nombreSegmentoUp},function(){
            $('[data-bs-toggle="tooltip"]').tooltip();
        });
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
                        emp.verInfoSegmento( emp.idSegmentoGlb, emp.nomSegmentoGlb );
                    }, 1000); 
                }else{
                    Swal.fire('Información', 'No se pudo quitar el campo a mostrar. Intentalo nuevamente', 'warning');
                }
            });
        }else{
            emp.myModal.hide();
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
                                    emp.verInfoSegmento( emp.idSegmentoGlb, emp.nomSegmentoGlb );
                                }, 1000);
                            } else {
                                Swal.fire('Información', 'No se pudo configurar en campo. Intentalo nuevamente', 'warning');
                            }
                        });
                    }
                }else{
                    emp.verInfoSegmento( emp.idSegmentoGlb, emp.nomSegmentoGlb );
                }
            });
        }
    },
    asignarContextoSegmento: function( idSegmento, cuerpoTexto, opc ){

    }
    
};
emp.stars();
