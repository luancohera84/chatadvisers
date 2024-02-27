var ases = {
    nombreEmpresaGlb: null,
    idEmpresaGlb: $('#idEmpresaChatCli').val() || null,
    idClienteGlb: $('#id_info_cliente').val() || null,
    idClientHstGlb: null,
    nombreClienteGlb: null,
    clienteSegGlb: null,
    identificacionClienteGlb: null,
    idLiAserClienteColor: null,
    valorIngresadoCampoSms: null,
    valorIngresadoCampoSmsHistory: null,
    identificaHora: null,
    formulario: null,
    vAcuerdo: 0,
    cCuotas: 1,
    fPago: template.fechaActual,
    pPago: '',
    fechaInicial: null,
	fechaFinal: null,
	fecInicial: null,
	fecFinal: null,
	pantallaGlb: null,
    descripResul: null,
    idFormExtra: null,
    idResul:null,
    dataRequeridos: new Array(),
    idFormResul: 0,
    dataFormExtra: [],
    idInteraccionGlb: null,
    stars: function(){
        this.carga();
    },
    //???Soporte*2017***
    carga: function(){
        
        // Capturar el evento de cierre del modal
        $("#emojisRes").on("hidden.bs.modal", function() {
            ases.moveCursorToEnd('mensajeEscribiendoAsesor');
            ases.moveCursorToEnd('mensajeEscribiendoAsesorHistory');
            // $('#mensajeEscribiendoAsesor').focus();
            // $('#mensajeEscribiendoAsesorHistory').focus();
        });

        if (ases.idClienteGlb) {
            ases.cargaHistorial();
        }

        $('#idDivUlEmpresasChatAsesor_'+template.idUsersTemplate+'').load('listaEmpresasAsesor',{idUser: template.idUsersTemplate},function(){
            $('[data-bs-toggle="tooltip"]').tooltip();
        });
        $("#formularioEncvioSms").on("submit" ,function(){
            ases.valorIngresadoCampoSms = $("#mensajeEscribiendoAsesor").val();
            if( ( ases.valorIngresadoCampoSms != '' ) || ( ases.valorIngresadoCampoSms != 'undefined' ) || ( ases.valorIngresadoCampoSms != undefined ) || ( ases.valorIngresadoCampoSms != null ) ){
                ases.envioSmsPrest( $("#mensajeEscribiendoAsesor").val() );
                // ases.validateEmojis( $("#mensajeEscribiendoAsesor").val() );
            }
        });
        $("#formularioEncvioSmsHistory").on("submit" ,function(){
            ases.valorIngresadoCampoSmsHistory = $("#mensajeEscribiendoAsesorHistory").val();
            if( ( ases.valorIngresadoCampoSmsHistory != '' ) || ( ases.valorIngresadoCampoSmsHistory != 'undefined' ) || ( ases.valorIngresadoCampoSmsHistory != undefined ) || ( ases.valorIngresadoCampoSmsHistory != null ) ){
                ases.envioSmsPrestHistory( $("#mensajeEscribiendoAsesorHistory").val() );
            }
        });
        
        if ( ( parseInt($('#chatServicioListChats').val()) > 0 ) && ( parseInt($('#pageChats').val()) === 1) ) {
            template.showPreloader('Tines una conversacion en proceso.');
            let idCliente = $('#chatServicioListChats').val();
            let nombreCliente = $('#chatServicionombreCliente').val();
            let chatServicioIdentificacion = $('#chatServicioIdentificacion').val();
            let chatServicioSegmento = $('#chatServicioSegmento').val();
            let idEmpresa = $('#chatServicioIdEmpresa').val();
            let idAsesor = $('#chatServicioIdAsesor').val();
            ases.verInfoChatCliente(idCliente,idCliente,idEmpresa,idAsesor,nombreCliente,'formularioEncvioSms', chatServicioIdentificacion,chatServicioSegmento);
        }
        const myModal = document.getElementById('tipificarModal');

        const myModalAct = document.getElementById('actDatosModal');

        myModal.addEventListener('shown.bs.modal', () => {
            ases.tipificaGestion();
        });

        myModalAct.addEventListener('shown.bs.modal', () => {
            ases.actuDatos();
        });

        myModal.addEventListener('hide.bs.modal', () => {
            $('#bodyCargaResultados, #bodyCargaActDatos').html('');
            $('#bodyPreloads, #bodyPreloadsActDatos').show();
        });
        $('#tableAsesoresAsig').DataTable({
            "responsive": true,
            "autoWidth": true,
            "ordering": true,
            "order": [
                [7, "des"]
            ],
            info: true,
            paging: true,
            "scrollY": "380px",
            "scrollCollapse": true,
            language: {
                "decimal": "",
                "emptyTable": "No hay información",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": "Mostrar _MENU_ Entradas",
                "loadingRecords": "Cargando...",
                "processing": "Procesando...",
                "search": "Buscar:",
                "zeroRecords": "Sin resultados encontrados",
                "paginate": {
                    "first": "Primero",
                    "last": "Ultimo",
                    "next": "Siguiente",
                    "previous": "Anterior"
                }
            },
        });
        // ases.tipificaGestion();
    },
    moveCursorToEnd: function(id) {
        var el = document.getElementById(id) 
        el.focus()
        if (typeof el.selectionStart == "number") {
            el.selectionStart = el.selectionEnd = el.value.length;
        } else if (typeof el.createTextRange != "undefined") {           
            var range = el.createTextRange();
            range.collapse(false);
            range.select();
        }
    },
    validateEmojis: function( data ){
        console.log('Dta =>', data.toString().split(' '));
        var tmp = data.toString().split(' ');
        console.log('Tamano =>', tmp.length);
        if (tmp.length > 1){
            $.each(tmp, function (indexInArray, valueOfElement) { 
                var codigoUnicode = valueOfElement.codePointAt(0).toString(16).toUpperCase();
                if (codigoUnicode) {
                    console.log('codigoUnicode each =>', codigoUnicode);
                } else {
                    console.log('Texto each =>', codigoUnicode);
                }
            });
        }else{

            for (var i=1; i < data.length; i++) {
                console.log('Texto =>', data[i]);
                var codigoUnicode = data[i].codePointAt(0).toString(16).toUpperCase();
                var codigoEscapeUnicode = "\\u" + "0000".substring(0, 4 - codigoUnicode.length) + codigoUnicode;
                if (codigoEscapeUnicode) {
                    console.log('codigoUnicode for =>', codigoEscapeUnicode);
                } else {
                    console.log('Texto for =>', codigoEscapeUnicode);
                }
                //document.write(arrayDeCadenas[i] + " / ");
            }
        }
    },
    verInfoClientesChat: function( idEmpresa, idUser, nombreEmpresa ){
        ases.nombreEmpresaGlb = nombreEmpresa;
        ases.idEmpresaGlb     = idEmpresa;
        $('#bodyChat').hide();
        $('#listaChatEmpresa').show();
        $('#listaChatEmpresa').load('listaChatEmpresa',{idEmpresa,idUser,nombreEmpresa});
    },
    verInfoChatCliente: function( idCliente, idClientHst, idEmpresa, idUser, nombreCliente, formulario, identificacion, clienteSeg ){
        ases.formulario = formulario;
        template.hidePreloader();
        $('#middle1').removeClass('right-sidebar right_sidebar_profile hide show-right-sidebar');
        $('#middle1').addClass('right-sidebar right_sidebar_profile hide-right-sidebar hide');
        ases.idClienteGlb             = idCliente;
        ases.idClientHstGlb           = idClientHst;
        ases.nombreClienteGlb         = nombreCliente;
        ases.idEmpresaGlb             = idEmpresa;
        ases.identificacionClienteGlb = identificacion;
        ases.clienteSegGlb            = clienteSeg;
        $('#chatServicioSegmento').val(clienteSeg);
        $('#middle,#middle1').show();
        $('#nombreBodyChatCliente').html(nombreCliente);
        $('#identificacionBodyChatCliente').html(identificacion+' - '+clienteSeg);
        if ( parseInt(ases.idLiAserClienteColor) != parseInt(idCliente) ){
            $('#idLiAserCliente_'+ases.idLiAserClienteColor+'').css('background-color','');
            $('#idLiAserCliente_'+idCliente+'').css('background-color','#5A078B');
            $('.idTextAserClienteColor_'+ases.idLiAserClienteColor+'').css('color','#000000');
            $('.idTextAserClienteColor_'+idCliente+'').css('color','#FFFFFF');
            ases.idLiAserClienteColor = idCliente;
        }
        // console.log('ases.formulario', ases.formulario)
        if (ases.formulario === 'formularioEncvioSms') {

            $.ajax({
                url: 'verInfoChatCliente',
                type: 'POST',
                dataType: 'json',
                data: {
                    idCliente,
                    idClientHst,
                    idEmpresa,
                    idUser
                }
            })
            .done(function(data) {
                ases.rederBodySms( data );
            });
        }else{
            ases.cargaHistorial();
        }
    },
    rederBodySms: function( data ) {
        // console.log('data => rederBodySms', data);
        let dataHtml = [];
        let contadorFechas = 0;
        let fechaLinea = 0;
        $.each(data, function(index, val) {
            let lineaFecha = `
                <div class="chat-line">
                    <span class="chat-date">`+val.textFecSms+`</span>
                </div>
            `
            if ( contadorFechas === 0 ) {
                dataHtml.push(lineaFecha);
            }else{
                if (fechaLinea != val.fechaSms ) {
                    dataHtml.push(lineaFecha);
                }
            }
            if ( val.tipoUsuario === 'cliente' ) {
                if ( val.tipoSms === 'image' ) {
                    var tmpHtml = `
                        <div class="chats">
                            <div class="chat-avatar">
                                <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                            </div>
                            <div class="chat-content">
                                <div class="message-content">
                                    <div class="download-col">
                                        <ul>
                                            <li>
                                                <div class="image-download-col">
                                                    <a href="../static/multimedia/image/`+val.sms+`" data-fancybox="gallery" class="fancybox">
                                                        <img src="../static/multimedia/image/`+val.sms+`" height="50px" width="50px" alt="image">
                                                    </a>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="chat-time">
                                        <div>
                                            <div class="time"><i class="fas fa-clock"></i> `+val.horaSms+`</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="chat-profile-name">
                                    <h6>`+val.cliente+`</h6>
                                </div>
                            </div>
                        </div>
                        <br><br>
                    `;
                } else if ( val.tipoSms === 'audio' ){ 
                    var tmpHtml = `
                        <div class="chats">
                            <div class="chat-avatar">
                                <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                            </div>
                            <div class="chat-content">
                                <div class="message-content">
                                    <audio controls>
                                        <source src="../static/multimedia/audio/`+val.sms+`" type="audio/mpeg">
                                        Your browser does not support the audio element.
                                    </audio>
                                    <div class="chat-time">
                                        <div>
                                            <div class="time"><i class="fas fa-clock"></i> `+val.horaSms+`</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="chat-profile-name">
                                    <h6>`+val.cliente+`</h6>
                                </div>
                            </div>
                        </div>
                        <br><br>
                    `;
                } else {
                    var tmpHtml = `
                        <div class="chats">
                            <div class="chat-avatar">
                                <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                            </div>
                            <div class="chat-content">
                                <div class="message-content">
                                    `+val.sms+`
                                    <div class="chat-time">
                                        <div>
                                            <div class="time"><i class="fas fa-clock"></i> `+val.horaSms+`</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="chat-profile-name">
                                    <h6>`+val.cliente+`</h6>
                                </div>
                            </div>
                        </div>
                        <br><br>
                    `;
                }
                dataHtml.push(tmpHtml);
                
            } else {
                let tmpHtml = `
                    <div class="chats chats-right">
                        <div class="chat-content">
                            <div class="message-content">
                                `+val.sms+`
                                <div class="chat-time">
                                    <div>
                                        <div class="time"><i class="fas fa-clock"></i> `+val.horaSms+`</div>
                                    </div>
                                </div>
                            </div>
                            <div class="chat-profile-name text-end">
                                <h6>`+val.asesor+`</h6>
                            </div>
                        </div>
                        <div class="chat-avatar">
                            <img src="`+template.imagenAsesor+`" class="rounded-circle dreams_chat" alt="image">
                        </div>
                    </div>
                    <br><br>
                `;
                dataHtml.push(tmpHtml);
            }
            contadorFechas = contadorFechas + 1;
            fechaLinea = val.fechaSms;
        });
        $('#idBodySmsConversacion').html(dataHtml);
        $('#idBodySmsConversacion').append(`
            <a class="ir-arriba icon-arrow-up2 btn btn-info rounded-pill">
                <i class="fas fa-search text-white"></i>
            </a>
        `);
        if ( ases.formulario === 'formularioEncvioSms' ) {
            $('#idFooterFomularioEnvioHistory').hide();
            $('#idFooterFomularioEnvioDia').show();
            $("#mensajeEscribiendoAsesor").focus();
        }else{
            $('#idFooterFomularioEnvioDia').hide();
            $('#idFooterFomularioEnvioHistory').show();
            $("#mensajeEscribiendoAsesorHistory").focus();
        }
        
        template.getMessages();
    },
    cargaOfertas: function( ){
        $('body>.tooltip').remove();
        $.ajax({
            url: 'verInfoOfertasCliente',
            type: 'POST',
            dataType: 'json',
            data: {
                idCliente: ases.idClienteGlb
            }
        })
        .done(function(data) {
            // console.log('Data cargaOfertas =>', data);
            $('#nav-tab,#ulNabTabOferta').html('');
            $.each(data, function(index, val) {
                // console.log('val', val.canal);
                if ( val.canal === 'chat') {
                    $('#canal').hide();
                    $('#ofertaUnica').show();
                    // statement
                    let liHtml = `
                        <a class="nav-item nav-link active" id="nav-home-tab" data-bs-toggle="tab" href="#about">`+val.numProducto+`</a>
                    `;
                    if (val.valorCampo === '') {
                        var valorCampo = 'Sin valor'
                    } else {
                        var valorCampo = val.valorCampo
                    }
                    let listaValuesOferta = `
                        <li>
                            <h6 class="textOfertaViews">`+val.campoRespresenta.replace('_',' ').toUpperCase()+`</h6>
                            <span  class="textOfertaViews">`+valorCampo+`</span>
                        </li>
                    `;
                    $('#nav-tab').html(liHtml);
                    $('#ulNabTabOferta').append(listaValuesOferta);
                    $('#linkIdTuacuerdo').html('<a href="https://'+val.url+'" target="_blank" title="Tuacuerdo.com"><i class="fab fa-html5"></i></a>');
                } else {
                    ases.renderTuacuerdo( data );
                }
            });
        });
    },
    renderTuacuerdo: function( data ) {
        // console.log('Data renderTuacuerdo =>', data);
        
        // const htmlTmp = `
        //     <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        //       <ol class="carousel-indicators">
        //         <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        //         <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        //         <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        //         <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
        //       </ol>
              
        //       <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        //         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        //         <span class="sr-only">Previous</span>
        //       </a>
        //       <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        //         <span class="carousel-control-next-icon" aria-hidden="true"></span>
        //         <span class="sr-only">Next</span>
        //       </a>
        //     </div>
        // `;
        $('#ofertaUnica').hide();
        $('#canal').show();
        $('#canal').html('');
        $('#canal').append('<div class="row m-2" id="dicSliderJava"><p class="textOfertaViews" align="justify">Asesor recuerde que la infomacion aca mostrada corresponde a la ultima cargada a el cliente.</p><hr></div>');
        // $('#carouselExampleIndicators').carousel({
        //     interval: 2000
        // });
        // $('#carouselExampleIndicators').on('slide.bs.carousel', function () {
        //   // do something…
        // });
        let htmlRecor  = [];
        let contador   = 1;
        $.each(data, function(index, val) {
            const htmlInterno = `
                <div class="table-responsive">    
                    <table class="table table-inverse">
                        <thead>
                            <!--tr>
                                <th>Segmento</th>
                                <td>`+val.segmento+`</td>
                            </tr-->
                            <tr>
                                <th>Identificacion</th>
                                <td>`+val.identiPersona+`</td>
                            </tr>
                            <tr>
                                <th>Tipo_cliente</th>
                                <td>`+val.tipo_cliente+`</td>
                            </tr>
                            <tr>
                                <th>Condonacion</th>
                                <td>`+val.condonac+`</td>
                            </tr>
                            <tr>
                                <th>Produto</th>
                                <td>`+val.producto+`</td>
                            </tr>
                            <tr>
                                <th>Cuotas</th>
                                <td>`+val.ncuotas+`</td>
                            </tr>
                            <tr>
                                <th>Valor obligacion</th>
                                <td>`+template.monedaNumber(val.vTotalDeuda, 'es-CO', 'COP')+`</td>
                            </tr>
                            <tr>
                                <th>Valor oferta</th>
                                <td>`+template.monedaNumber(val.Voferta, 'es-CO', 'COP')+`</td>
                            </tr>
                            <tr>
                                <th>Tuacuerdo.com</th>
                                <td><a href='https://`+val.urlTu+`' target="_blank">Ver link</a></td>
                            </tr>
                            <tr>
                                <th>DMora</th>
                                <td>`+val.dMora+`</td>
                            </tr>
                        </thead>
                    </table>
                </div>
                <hr style='background-color:#000000;'>
            `;
            // htmlRecor.append(htmlInterno);
            $('#dicSliderJava').append(htmlInterno);
            contador  = contador + 1;
        });

    },
    tipificaGestion: function(){
        $('body>.tooltip').remove();
        // $('#tipificarModal').show();
        // $('#tipificarModal').removeClass('right-sidebar right_sidebar_profile hide-right-sidebar hide');
        // $('#tipificarModal').addClass('right-sidebar right_sidebar_profile hide show-right-sidebar');
        // console.log('ases.idClienteGlb', ases.idClienteGlb);
        // console.log('ases.idEmpresaGlb', ases.idEmpresaGlb);
        $('#bodyCargaResultados').load('tipificacion',{idClienteGlb:ases.idClienteGlb,idEmpresa: ases.idEmpresaGlb},function(){
            $('#bodyPreloads').hide();
        });
    },
    cambioEstado: (statusIngr, idAsesor) => {
        template.showPreloader('Cambiando estado');
        $.post('cambioEstado', {statusIngr,idUserClt: idAsesor}, function(data, textStatus, xhr) {
            console.log('data', data);
            template.hidePreloader();
            if (parseInt(data) > 0) {
                template.showSmsUpdate('Estado');
            } else {
                Swal.fire('Información', 'No se pudo modificar el estado. Intentalo nuevamente', 'warning');
            }
        });
    },
    capitalize: function( texto ) {
        if (texto === '') {
            return texto;
        } else {
            return texto[0].toUpperCase() + texto.slice(1); 
        }
    },
    validarFormularioGestion:  async function( descripResul, idResul ){
        ases.descripResul = descripResul; 
        ases.idResul   = idResul;
        $('#listTiificacion,#idHeaderListResultado').hide();
        $('#bodyPreloadsFormularioValidate').show();
        $.ajax({
            url: 'validarFormularioGestion',
            type: 'POST',
            dataType: 'json',
            data: {idCliente: ases.idClienteGlb,idClientHist: ases.idClientHstGlb,descripResul,idResul},
        })
        .done(function( data ) {
            // console.log('data', data.pPagos);
            $('#idHeaderListResumen,#divResumenTipificacion,#moduleComentarios').show();
            $('#resultadoTitle').html(ases.capitalize(descripResul));
            $('#comentariosGestion').val('');
            $('#divCuerpoFormulario').html('');
            if ( data.listadoCampos.length > 0 ) {
                var tmpHtml = [];
                $('#bodyPreloadsFormularioValidate').hide();
                $('#divFormularisTipificado').show();
                
                $.each(data.listadoCampos, async function(index, val) {
                    ases.idFormResul = val.formulario;
                    if (val.obligatorio === 'required') {
                        var dataTmp = {
                            'nombreCampo': val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario
                        }
                        ases.dataRequeridos.push(dataTmp);
                        var fileReq = '(*)';
                    }else {
                        var fileReq = '';
                    }

                    if ( val.tipo_dato === 'texarea' ) {  
                        var style = 12;
                        var campo = `
                            <textarea cols="10" rows="10" type="`+val.tipo_dato+`" class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" placeholder="`+ases.capitalize(val.nombre_label)+` `+fileReq+`"></textarea>
                        `;
                    }else{
                        if ( data.length === 1 ) {
                            var style = 12;
                        }else if ( data.length === 2 ) {
                            var style = 6;
                        }else{
                            var style = 4;
                        }
                        if ( val.tipo_dato === 'punto_pago' ) {
                            if ( data.pPagos.length > 0 ) {
                                var campoTmp = [`<select class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" `+fileReq+`"><option val="">Seleccione un punto de pago</option>`];
                                var campoFinal = 1;
                                $.each(data.pPagos, function (indexInArray, valueOfElement) { 
                                    if (campoFinal === data.pPagos.length){
                                        campoTmp.push('<option val="'+valueOfElement.punto_pago+'">'+ases.capitalize(valueOfElement.punto_pago)+'</option>');
                                        campoTmp.push('</select>');
                                    }else{
                                        campoTmp.push('<option val="'+valueOfElement.punto_pago+'">'+ases.capitalize(valueOfElement.punto_pago)+'</option>');
                                    }
                                    campoFinal += campoFinal;
                                });
                                var campo = campoTmp;
                                
                            } else {
                                var campo = `
                                    <input type="text" class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" placeholder="`+ases.capitalize(val.nombre_label)+` `+fileReq+`">
                                `;
                            }
                        } else {
                            var campo = `
                                <input type="`+val.tipo_dato+`" class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" placeholder="`+ases.capitalize(val.nombre_label)+` `+fileReq+`">
                            `;
                        }

                    }
                    var tmp  = `
                        <div class="col-lg-`+style+`">
                            <div class="form-group">
                              <label>`+ases.capitalize(val.nombre_label)+` `+fileReq+`</label>
                              `+campo+`
                              <span class="form-text text-muted">Ingrese `+ases.capitalize(val.nombre_label)+`.</span>
                            </div>
                        </div>
                    `;
                    // console.log('tmp => ', tmp);
                    
                    $('#divCuerpoFormulario').append(tmp);
                    $('#botoneraFormulario,#moduleComentarios').show();
                });
                // console.dirxml('Tamano =>', ases.dataRequeridos.length);
                // console.dirxml('ases.dataRequeridos =>', ases.dataRequeridos);
            }else{
                $('#bodyPreloadsFormularioValidate').hide();
                // $('#idHeaderListResumen,#divResumenTipificacion,#moduleComentarios').show();
            }
        });
        // divResumenTipificacion
        // divFormularisTipificado
        // 
        // idClienteGlb
    },
    cerrarGestion: function() {
        let comentarios = $('#comentariosGestion').val();
        if (ases.dataRequeridos.length > 0) {    
            var elements = document.getElementById("formularisTipificadocampos").elements;
            var data = [];
            for (var i = 0, element; element = elements[i++];) {
                var tmp = element.name;
                var tmpVal = element.value;
                const fileReq = ases.dataRequeridos.find(element => element.nombreCampo === tmp );
                
                if (fileReq) {
                    if (tmpVal === '') {
                        template.validaCampo(ases.capitalize(tmp.replace('_'+ases.idFormResul,'')),tmp);
                        return false
                    }else{
                       data.push({ 'nombreCampo': tmp.replace('_'+ases.idFormResul,''), 'valorCampo': tmpVal }); 
                    }
                }else{
                    data.push({ 'nombreCampo': tmp.replace('_'+ases.idFormResul,''), 'valorCampo': tmpVal });
                }
            }
            ases.dataFormExtra = data;
            // template.showPreloader('Guardando gestion');
            ases.cerrarGestionTer( comentarios );
        }else {
            
            // template.showPreloader('Guardando gestion');
            ases.cerrarGestionTer( comentarios );
        }
    },
    cerrarGestionTer: function( comentarios ) {
        template.showPreloader('Estamos guardando su gestión');
        var dat = {
            idCliente: ases.idClienteGlb,
            idClientHist: ases.idClientHstGlb,
            descripResul:ases.descripResul,
            idResul:ases.idResul,
            comentarios,
            idFormResul: ases.idFormResul,
            dataFormExtra: JSON.stringify(ases.dataFormExtra)
        }
        // console.log('dat', dat);
        $.post('cerrarGestion', dat, function(data, textStatus, xhr) {
            // console.log('dataaaa Resul', data);
            // template.hidePreloader();
            if (parseInt(data) > 0) {
                const Toast = Swal.mixin({
                    customClass: 'swalTextTmna',
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                });

                Toast.fire({
                    icon: 'success',
                    title: 'Gestion guardada con exito.'
                });
                setTimeout(function() {
                    window.location.href = "";
                }, 3001);
            }else {
                Swal.fire('Error','Lo sentimos no pudimos procesar tu solicitud.\nIntenta nuevamente, si el problema continua consulta con tu administrador.','error');
            }
        });
    },
    renderTuacuerdoResultado: function( data ) {
        $('#ofertaUnicaResultado').hide();
        $('#canalResultado').show();
        $('#canalResultado').html('');
        $('#canalResultado').append('<div class="row m-2" id="dicSliderJavaResultado"><p class="textOfertaViews" align="justify">Asesor recuerde que la infomacion aca mostrada corresponde a la ultima cargada a el cliente.</p><hr></div>');
        // $('#carouselExampleIndicators').carousel({
        //     interval: 2000
        // });
        // $('#carouselExampleIndicators').on('slide.bs.carousel', function () {
        //   // do something…
        // });
        let htmlRecor  = [];
        let contador   = 1;
        $.each(data, function(index, val) {
            // if (contador === 1) {
            //     var active = 'active'
            // }else{
            //     var active     = ''
            // }
            // console.log('active', active);
            const htmlInterno = `
                <div class="table-responsive">    
                    <table class="table table-inverse">
                        <thead>
                            <tr>
                                <th>Tipo_cliente</th>
                                <td>`+val.tipo_cliente+`</td>
                            </tr>
                            <tr>
                                <th>Condonacion</th>
                                <td>`+val.condonac+`</td>
                            </tr>
                            <tr>
                                <th>Produto</th>
                                <td>`+val.producto+`</td>
                            </tr>
                            <tr>
                                <th>Cuotas</th>
                                <td>`+val.ncuotas+`</td>
                            </tr>
                            <tr>
                                <th>Valor obligacion</th>
                                <td>`+template.monedaNumber(val.vTotalDeuda, 'es-CO', 'COP')+`</td>
                            </tr>
                            <tr>
                                <th>Valor oferta</th>
                                <td>`+template.monedaNumber(val.Voferta, 'es-CO', 'COP')+`</td>
                            </tr>
                            <tr>
                                <th>Tuacuerdo.com</th>
                                <td><a href='https://`+val.urlTu+`' target="_blank">Ver link</a></td>
                            </tr>
                            <tr>
                                <th>DMora</th>
                                <td>`+val.dMora+`</td>
                            </tr>
                        </thead>
                    </table>
                </div>
                <hr style='background-color:#000000;'>
            `;
            // htmlRecor.append(htmlInterno);
            $('#dicSliderJavaResultado').append(htmlInterno);
            contador  = contador + 1;
        });

    },
    actuDatos: function( ){
        $('body>.tooltip').remove();
        $('#bodyCargaActDatos').load('actualizaDatos',{idClienteGlb:ases.idClienteGlb,idEmpresa: ases.idEmpresaGlb},function(){
            $('#bodyPreloadsActDatos').hide();
        });
    },
    cargaOfertasResultado: function( ){
        $('#divInfoFormularioComet').removeClass('col-lg-12');
        $('#divInfoFormularioComet').addClass('col-lg-8');
        $('#btnOfertaResultado').hide();
        $('#divListOfertas,#cerrarBtnOfertas').show();
        $.ajax({
            url: 'verInfoOfertasCliente',
            type: 'POST',
            dataType: 'json',
            data: {
                idCliente: ases.idClienteGlb
            }
        })
        .done(function(data) {
            $('#nav-tabResult,#ulNabTabOfertaResultado').html('');
            $.each(data, function(index, val) {
                if ( val.canal === 'chat') {
                    $('#canal').hide();
                    $('#ofertaUnica').show();
                    
                    let liHtml = `
                        <a class="nav-item nav-link active" id="nav-home-tab" data-bs-toggle="tab" href="#about">`+val.numProducto+`</a>
                    `;
                    if (val.valorCampo === '') {
                        var valorCampo = 'Sin valor'
                    } else {
                        var valorCampo = val.valorCampo
                    }
                    let listaValuesOferta = `
                        <li>
                            <h6 class="textOfertaViewsResultados">`+val.campoRespresenta.replace('_',' ').toUpperCase()+`</h6>
                            <span  class="textOfertaViewsResultados">`+valorCampo+`</span>
                        </li>
                    `;
                    $('#nav-tabResult').html(liHtml);
                    $('#ulNabTabOfertaResultado').append(listaValuesOferta);
                    $('#linkIdTuacuerdo').html('<a href="https://'+val.url+'" target="_blank" title="Tuacuerdo.com"><i class="fab fa-html5"></i></a>');
                } else {
                    ases.renderTuacuerdoResultado( data );
                }
            });
        });
    },
    cerrarOfertas: function() {
        $('#divListOfertas,#cerrarBtnOfertas').hide();
        $('#btnOfertaResultado').show();
        $('#divInfoFormularioComet').removeClass('col-lg-8');
        $('#divInfoFormularioComet').addClass('col-lg-12');
    },
    emojisRes: function(){
        $('#bodyModalSmsPrestNA').hide();
        $('#bodyModalSmsPrest').html('');
        $('#bodyPreloadsSmsPrest').show();
        $('body>.tooltip').remove();
        $('#emojisRes').modal('show');
        
        // $.ajax({
        //     url: 'smsPrestablecidos',
        //     type: 'POST',
        //     dataType: 'json',
        //     data: {idCliente: ases.idClienteGlb},
        // })
        // .done(function( data ) {
        //     console.log("success", data);
        //     $('#bodyPreloadsSmsPrest').hide();
        //     if (data.length > 0) {
        //         $('#bodyModalSmsPrest').show();
        //         let tmpHtml = '';
        //         $.each(data, function(index, val) {
        //             tmpHtml = `
        //                 <div class="col-12">
        //                     <li class="cardTipi" onclick="ases.envioSmsPrest('`+val.sms+`');">
        //                         <div class="users-list-body">
        //                             <div>
        //                                 <h6 class="textOfertaViews">`+val.sms+`</h6>
        //                             </div>
        //                         </div>
        //                     </li>
        //                 </div>
        //             `;
        //             $('#bodyModalSmsPrest').append(tmpHtml);
        //         });
        //     } else {
        //         $('#bodyModalSmsPrestNA').show();
        //     }
        // });
    },
    smsPrestablecidos: function(){
        $('#bodyModalSmsPrestNA').hide();
        $('#bodyModalSmsPrest').html('');
        $('#bodyPreloadsSmsPrest').show();
        $('body>.tooltip').remove();
        $('#smsPrestablecidos').modal('show');
        $.ajax({
            url: 'smsPrestablecidos',
            type: 'POST',
            dataType: 'json',
            data: {idCliente: ases.idClienteGlb},
        })
        .done(function( data ) {
            console.log("success", data);
            $('#bodyPreloadsSmsPrest').hide();
            if (data.length > 0) {
                $('#bodyModalSmsPrest').show();
                let tmpHtml = '';
                $.each(data, function(index, val) {
                    tmpHtml = `
                        <div class="col-12">
                            <li class="cardTipi" onclick="ases.envioSmsPrest('`+val.sms+`');">
                                <div class="users-list-body">
                                    <div>
                                        <h6 class="textOfertaViews">`+val.sms+`</h6>
                                    </div>
                                </div>
                            </li>
                        </div>
                    `;
                    $('#bodyModalSmsPrest').append(tmpHtml);
                });
            } else {
                $('#bodyModalSmsPrestNA').show();
            }
        });
    },
    envioSmsPrest: function( sms ){
        ases.valorIngresadoCampoSms = sms;
        $("#mensajeEscribiendoAsesor").val('');
        $("#mensajeEscribiendoAsesor").focus();
        $('#smsPrestablecidos').modal('hide');
        const smsAsesor = `
            <div class="chats chats-right">
                <div class="chat-content">
                    <div class="message-content">
                        `+ases.valorIngresadoCampoSms+`
                        <div class="chat-time">
                            <div>
                                <div class="time"><span class="material-icons">send</span> Enviando ....</div>
                            </div>
                        </div>
                    </div>
                    <div class="chat-profile-name text-end">
                        <h6>`+template.nombreAsesor+`</h6>
                    </div>
                </div>
                <div class="chat-avatar">
                    <img src="`+template.imagenAsesor+`" class="rounded-circle dreams_chat" alt="image">
                </div>
            </div>
        `;
        $('#idBodySmsConversacion').append(smsAsesor);
        
        $.ajax({
            url: 'envioSmsCliente',
            type: 'POST',
            dataType: 'json',
            data: {
                idEmpresaGlb:ases.idEmpresaGlb,
                idClienteGlb:ases.idClienteGlb,
                idClientHstGlb:ases.idClientHstGlb,
                sms
                
            }
        })
        .done(function(data) {
            if (parseInt(data) > 0) {
                $('#indicadorSmsCantidadTiempo_'+ases.idClienteGlb+'').html(`
                    <small class="text-muted">0</small>
                    <div class="new-message-count">0</div>
                `);
                ases.verInfoChatCliente( ases.idClienteGlb, ases.idClientHstGlb, ases.idEmpresaGlb, template.idUsersTemplate, ases.nombreClienteGlb, 'formularioEncvioSms', ases.identificacionClienteGlb );
            } else {
                Swal.fire('Error','No se pudo entregar el sms a el cliente','error');
            }
        });
    },
    envioSmsPrestHistory: function( sms ){
        ases.valorIngresadoCampoSmsHistory = sms;
        $("#mensajeEscribiendoAsesorHistory").val('');
        $("#mensajeEscribiendoAsesorHistory").focus();
        $('#smsPrestablecidos').modal('hide');
        const smsAsesor = `
            <div class="chats chats-right">
                <div class="chat-content">
                    <div class="message-content">
                        `+ases.valorIngresadoCampoSmsHistory+`
                        <div class="chat-time">
                            <div>
                                <div class="time"><span class="material-icons">send</span> Enviando ....</div>
                            </div>
                        </div>
                    </div>
                    <div class="chat-profile-name text-end">
                        <h6>`+template.nombreAsesor+`</h6>
                    </div>
                </div>
                <div class="chat-avatar">
                    <img src="`+template.imagenAsesor+`" class="rounded-circle dreams_chat" alt="image">
                </div>
            </div>
        `;
        $('#idBodySmsConversacion').append(smsAsesor);
        $.ajax({
            url: 'envioSmsCliente',
            type: 'POST',
            dataType: 'json',
            data: {
                idEmpresaGlb:ases.idEmpresaGlb,
                idClienteGlb:ases.idClienteGlb,
                idClientHstGlb:ases.idClientHstGlb,
                sms
            }
        })
        .done(function(data) {
            if (parseInt(data) > 0) {
                $('#indicadorSmsCantidadTiempo_'+ases.idClienteGlb+'').html(`
                    <small class="text-muted">0</small>
                    <div class="new-message-count">0</div>
                `);
                ases.formulario = 'formularioEncvioSmsHistory';
                ases.verInfoChatCliente( ases.idClienteGlb, ases.idClientHstGlb, ases.idEmpresaGlb, template.idUsersTemplate, ases.nombreClienteGlb, ases.formulario, ases.identificacionClienteGlb );
            } else {
                Swal.fire('Error','No se pudo entregar el sms a el cliente','error');
            }
        });
    },
    cargaHistorial: function() {
        if (ases.formulario === 'formularioEncvioSms') {
            template.showPreloader('Cargando historial');
        }
        $.ajax({
            url: 'cargaHistorial',
            type: 'POST',
            dataType: 'json',
            data: {idCliente: ases.idClienteGlb},
        })
        .done(function( data ) {
            // console.log("success", data);
            if (ases.formulario === 'formularioEncvioSms') {
                template.hidePreloader();
            }
            ases.formulario = 'formularioEncvioSmsHistory';;
            ases.rederBodySms( data );
        });
        
    },
    cambioPantalla:function( show, titulo ){
        ases.cerrarMasInfo();
        $('#tituloMostrar').html('<b>Mostrando gestiones '+titulo+'</b>');
        $('#idDivBodyAsignacion,#idDivBodyMesAntes').hide();
        $('#idSpinerChatListAsesores').show();
        $('#textoSpinner').html('Listando gestiones '+titulo+'');
        if (show === 'mesActual') {
            $('#idSpinerChatListAsesores').hide();
            $('#idDivBodyAsignacion').show();
        } else {
            $('#idDivBodyMesAntes').show();
            $('#idDivBodyMesAntes').load('misGestionesMesAntes', function(){
                $('#idSpinerChatListAsesores').hide();
            });
        }
	},
	verChats: function( idCliente,nombreCliente, idEmpresa, phone ){
		template.showPreloader('Cargando chat '+nombreCliente+'');
        window.location.href = "../asesor/chatClienteGestion?nCustomer="+nombreCliente+"&nPhone="+phone+"&numberCustomer="+idCliente+"&numberCompany="+idEmpresa+"";
	},
    masInfoGestion: function ( idInteraccion, nomCliente, comentarios, formulario, idFormulario ) {
        $('#contenidoChatMasInfoGestion').html('');
        $('#idSpinerChatMasInfoGestion').show();
        $('#idTrGestionInfo_'+ases.idInteraccionGlb+'').removeClass('table-success');
        ases.idInteraccionGlb = idInteraccion;
        $('#divResumenGestiones').removeClass('col-lg-12');
        $('#divResumenGestiones').addClass('col-lg-8');
        $('#divMasInfoGestion').show();
        $('#idTrGestionInfo_'+ases.idInteraccionGlb+'').addClass('table-success');
        $('#infoClienteMasInfo').html('<b>Más información ( '+nomCliente+' )</b>');
        if (parseInt(idFormulario) > 0 ) {
            var formulario = JSON.parse(formulario);
            var tmpHtml    = [];
            $.each(formulario, function(index, val) {
                // console.log('val =>', val)
                tmpHtml.push(`
                    <div class="col col-12">
                        <div class="form-group">
                            <label class="col-form-label">`+ases.capitalize(val.nombreCampo)+`</label>
                            <input 
                                type="text" 
                                class="form-control inputLower" 
                                autocomplete="false"
                                readonly=""
                                value='`+ases.capitalize(val.valorCampo)+`'>
                        </div>
                    </div>
                `);
            });
            tmpHtml.push(`
                <div class="col col-12">
                    <div class="form-group">
                        <label><b>Comentarios de la gestión</b></label>
                        <textarea class="form-control" id="comentariosGestion" name="comentariosGestion" maxlength="200000000" minlength="1" rows="5" readonly="">`+ases.capitalize(comentarios)+`</textarea>
                    </div>    
                </div>
            `);
            $('#contenidoChatMasInfoGestion').html(tmpHtml);
            $('#idSpinerChatMasInfoGestion').hide();
        }else{
            var tmpHtml = `
                <div class="col col-12">
                    <div class="form-group">
                        <label><b>Comentarios de la gestión</b></label>
                        <textarea class="form-control" id="comentariosGestion" name="comentariosGestion" maxlength="200000000" minlength="1" rows="5" readonly="">`+ases.capitalize(comentarios)+`</textarea>
                    </div>    
                </div>
            `;
            $('#contenidoChatMasInfoGestion').html(tmpHtml);
            $('#idSpinerChatMasInfoGestion').hide();
        }
    },
    cerrarMasInfo: function() {
        $('#divMasInfoGestion').hide();
        $('#divResumenGestiones').removeClass('col-lg-8');
        $('#divResumenGestiones').addClass('col-lg-12');
        $('#idTrGestionInfo_'+ases.idInteraccionGlb+'').removeClass('table-success');
    },
    smsTemplates: function(){

    },

};
ases.stars();