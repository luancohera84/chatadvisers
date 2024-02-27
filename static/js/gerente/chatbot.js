var URL = 'https://chatadvisers.intelibpo.com/init/static/contextosChatbot/';
var chatBot = {
    resultadoHomologa:null,
    nodoInicio: 'inicio',
    nodoDespedida: 'despedida',
    nomContexto: '',
    cantNBodos: '',
    cantNBodosGlb: -1,
    arraNombreNodos: new Array(),
    arraOpcionesNodos: new Array(),
    arraCompoNodos: new Array(),
    arraCamposFormNew: new Array(),
    nodoOrigen: null,
    nomNodoGuardar: null,
    idSegmGlb: null,
    myModalEl: document.getElementById('listNodos'),
    bdyCreateForm: 'idBodyCreateFormulario',
    nombreFormulario: null,
    canCampos: null,
    resulatdos: [],
    idContxChatbot: null,
    nameJson: null,
    nodoAnterior: 'nodo_inicio',
    dataNodoAnterior: {},
    valorIngresadoCampoSms: null,
    arraCamposForPrWhas: new Array(),
    stars: function() {
        this.carga();
    },
    carga: function(){
        $("#cantNodos").blur(function(){
            chatBot.arraNombreNodos = [];
            chatBot.arraOpcionesNodos = [];
            chatBot.cantNBodos  = $('#cantNodos').val();
            if (parseInt(chatBot.cantNBodos) > 0) {
                $('#divNombreNodos').html('');
                $('#idHTextoNodos').show();
                for (var i = 1; i <= parseInt(chatBot.cantNBodos); i++) {
                    var tmpHtml = `
                        <div class="col col-lg-3">
                            <label class="col-form-label">Nombre nodo `+i+` </label>
                            <input 
                                id="nombreNodo`+i+`"
                                name="nombreNodo`+i+`"
                                type="text" 
                                _value='Nombre nodo `+i+`'
                                class="form-control inputLower" 
                                placeholder="Nombre nodo `+i+`" 
                                autocomplete="false" o_nchange='chatBot.valueInput("nombreNodo`+i+`")'>
                        </div>
                    `;
                    $('#divNombreNodos').append(tmpHtml);
                }
            }else{
                $('#divNombreNodos').html('');
                $('#idHTextoNodos').hide();
            }
        });
        chatBot.myModalEl.addEventListener('hidden.bs.modal', event => {
          chatBot.validaPrintOpcNodos();
        });
        $("#formularioEncvioSms").on("submit" ,function(){
            chatBot.valorIngresadoCampoSms = $("#mensajeEscribiendoGerente").val();
            if( ( chatBot.valorIngresadoCampoSms != '' ) || ( chatBot.valorIngresadoCampoSms != 'undefined' ) || ( chatBot.valorIngresadoCampoSms != undefined ) || ( chatBot.valorIngresadoCampoSms != null ) ){
                chatBot.buscarJsonAndpintar( $("#mensajeEscribiendoGerente").val() );
                $("#mensajeEscribiendoGerente").val('');
                $("#mensajeEscribiendoGerente").focus();
            }
        });
    },
    buscarJsonAndpintar( dato ){
        const fechaActual = new Date();
        const horaActual = fechaActual.getHours();
        const minutosActuales = fechaActual.getMinutes();
        const segundosActuales = fechaActual.getSeconds();

        // Formatear la hora y los minutos para que tengan 2 dígitos
        const horaFormateada = horaActual.toString().padStart(2, '0');
        const minutosFormateados = minutosActuales.toString().padStart(2, '0');
        const segundosFormateados = segundosActuales.toString().padStart(2, '0');

        // Mostrar la hora actual en la consola
        var hora = horaFormateada + ':' + minutosFormateados + ':' + segundosFormateados;
        $("#mensajeEscribiendoAsesor").val('');
        $("#mensajeEscribiendoAsesor").focus();
        const smsAsesor = `
            <div class="chats chats-right">
                <div class="chat-content">
                    <div class="message-content">
                        `+dato+`
                        <div class="chat-time">
                            <div>
                                <div class="time"><i class="fas fa-clock"></i> `+hora+`</div>
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
        $('#divMsms').append(smsAsesor);
        if (parseInt(dato) <= parseInt(chatBot.dataNodoAnterior.num_opciones)) {
            var newNodoTmp = 'opcion'+parseInt(dato)+'';
            var newNodo    = chatBot.dataNodoAnterior[newNodoTmp];
            fetch(URL+chatBot.nameJson)
            .then(response => response.json())
            .then(respuestas => {
                var tmpHtml = `
                    <div class="chats">
                        <div class="chat-avatar">
                            <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                        </div>
                        <div class="chat-content">
                            <div class="message-content">
                                `+respuestas[newNodo].mensaje.replaceAll('\nn','<br>').replaceAll('\n','<br>').replaceAll('.n','')+`
                                <div class="chat-time">
                                    <div>
                                        <div class="time"><i class="fas fa-clock"></i> `+hora+`</div>
                                    </div>
                                </div>
                            </div>
                            <div class="chat-profile-name">
                                <h6>ChatBot</h6>
                            </div>
                        </div>
                    </div>
                    <br><br>
                `;
                $('#divMsms').append(tmpHtml);
                $("#mensajeEscribiendoGerente").val('');
                $("#mensajeEscribiendoGerente").focus();
                chatBot.nodoAnterior  = newNodo;
                chatBot.dataNodoAnterior = respuestas[newNodo];
            });
        } else {
            var tmpHtml = `
                <div class="chats">
                    <div class="chat-avatar">
                        <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                    </div>
                    <div class="chat-content">
                        <div class="message-content">
                            `+chatBot.dataNodoAnterior.mensaje_error.replaceAll('\n','<br>').replaceAll('.n','')+`
                            <div class="chat-time">
                                <div>
                                    <div class="time"><i class="fas fa-clock"></i> `+hora+`</div>
                                </div>
                            </div>
                        </div>
                        <div class="chat-profile-name">
                            <h6>ChatBot</h6>
                        </div>
                    </div>
                </div>
                <br><br>
            `;
            $('#divMsms').append(tmpHtml);
            $("#mensajeEscribiendoGerente").val('');
            $("#mensajeEscribiendoGerente").focus();
        }
        chatBot.getMessages();
    },
    valueInput: function( thsValue ) {
        // console.log('thsValue', $('#'+thsValue+'').val());
        var tmpValor = $('#'+thsValue+'').val();
        var valTmp = {
            'identificaCampo': thsValue,
            'valorCampo': tmpValor
        };
        // console.log('valTmp', valTmp);
        chatBot.arraNombreNodos.push(valTmp);
        // console.log('chatBot.arraNombreNodos', chatBot.arraNombreNodos);
    },
    newContBot: function( idSegmento ){
        $('#divRegistrosContextos').hide('slow/400/fast', function() {
            console.log('idSegmento =>', idSegmento);
            $('#newNodos,#bodyPreloadsCreateContextoChatBot').show('slow/400/fast', function() {
                console.log('newNodos => paso');
                $('#newNodos').load('../gerente/newNodos',{idSegmento} ,function(){
                    console.log('Retorno server => paso');
                    $('#bodyPreloadsCreateContextoChatBot').hide()
                });
            });
        });
    },
    showPasoToPaso: function() {
        let html = `
            <ul class="list-group" style='font-size:13px !important;'>
              <li class="list-group-item active" aria-current="true"><b>Para realizar un contexto debes tener claro varios puntos.</b></li>
              <li class="list-group-item" style='text-align:left !important;'>1. Los contextos deben tener como minimo dos <b>NODOS</b> (nodo_inicio, nodo_despedida)</li>
              <li class="list-group-item" style='text-align:left !important;'>2. Los <b>NODOS</b> creados deben terner por lo menos 2 opciones.</li>
              <li class="list-group-item" style='text-align:left !important;'>3. El nombre de los <b>NODOS</b> deben ser en letras minusculas.</li>
            </ul>
        `;
        Swal.fire({
            title: '<strong>Tener presente.</strong>',
            icon: 'info',
            html,
            showCloseButton: true,
            showConfirmButton:false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
            confirmButtonText:
                '<i class="fa fa-thumbs-up"></i> Great!',
            confirmButtonAriaLabel: 'Thumbs up, great!',
            cancelButtonText:
                '<i class="fa fa-thumbs-down"></i>',
            cancelButtonAriaLabel: 'Thumbs down',
            customClass: 'swalTextTmna',
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutRight'
            }
        });
        $('#nomContexto').val('');
        $('#cantNodos').val('');
        chatBot.nomContexto  = '';
        chatBot.cantNBodos  = '';
        $('#cantNodos').focus();
    },
    showPasoToPasoFormulario: function() {
        let html = `
            <ul class="list-group" style='font-size:13px !important;'>
              <li class="list-group-item active" aria-current="true"><b>Para realizar un contexto debes tener claro varios puntos.</b></li>
              <li class="list-group-item" style='text-align:left !important;'>1. Los contextos deben tener como minimo dos <b>NODOS</b> (nodo_inicio, nodo_despedida)</li>
              <li class="list-group-item" style='text-align:left !important;'>2. Los <b>NODOS</b> creados deben terner por lo menos 2 opciones.</li>
              <li class="list-group-item" style='text-align:left !important;'>3. El nombre de los <b>NODOS</b> deben ser en letras minusculas.</li>
            </ul>
        `;
        Swal.fire({
            title: '<strong>Tener presente.</strong>',
            icon: 'info',
            html,
            showCloseButton: true,
            showConfirmButton:false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
            confirmButtonText:
                '<i class="fa fa-thumbs-up"></i> Great!',
            confirmButtonAriaLabel: 'Thumbs up, great!',
            cancelButtonText:
                '<i class="fa fa-thumbs-down"></i>',
            cancelButtonAriaLabel: 'Thumbs down',
            customClass: 'swalTextTmna',
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutRight'
            }
        });
        $('#nomContexto').val('');
        $('#cantNodos').val('');
        chatBot.nomContexto  = '';
        chatBot.cantNBodos  = '';
        $('#cantNodos').focus();
    },
    regresarNewContBot: function(){
        $('#newNodos').hide('slow/400/fast', function() {
            $('#divRegistrosContextos').show('slow/400/fast', function() {});
        });
    },
    darPasoSiguiente: function( actual, proximo ) {
        $('.'+actual+'').hide('slow/400/fast', function() {$('.'+proximo+'').show('slow/400/fast', function() {})});
    },
    configNodosInicioDes: function() {
        chatBot.darPasoSiguiente('modeleCreateOne','modeleConfigNodoIniciodespedida');
    },
    nodosAdicionales: function() {
        chatBot.nomContexto = $('#nomContexto').val();
        if (nomContexto != '') {
            $.ajax({
                url: '../gerente/resultadoHomologa',
                type: 'POST',
                dataType: 'json',
                data: {idSegmento: ger.idSegmentoGlb},
            })
            .done(function( dat ) {
                $.each(dat, function(indexResul, valResul) {
                    chatBot.resulatdos.push('<option value="'+valResul.idResultado+'">'+valResul.idResultado+' - '+valResul.descripcion+'</option>');
                });
                $('#pasoTresNodosAdcionales').html('');
                $.each(chatBot.arraNombreNodos, function(index, val) {
                    var valorCampo = val.valorCampo.replace(/\s+/g, '_');
                    var tmpHtml = `
                        <div class="col col-lg-3">
                            <div class="card h-100">
                                <div class="card-body">
                                    <h5 class="card-title">Nodo `+chatBot.capitalizarPrimeraLetra(val.valorCampo)+`</h5>
                                    <textarea id="mensaje`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3" cols="30" placeholder="Mensaje" rows="4" value='Mensje `+chatBot.capitalizarPrimeraLetra(valorCampo)+`'></textarea>
                                    <textarea id="mensajeError`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3" placeholder="Mensaje error" value='Mensje Error `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' cols="30" rows="2"></textarea>
                                    <div class="form-check form-switch">
                                      <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheck`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                      <label class="form-check-label" for="flexSwitchCheck`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">Directo</label>
                                    </div>
                                    <div>
                                        <p  class="mb-3">Opciones  
                                            <i class="fa fa-plus cursor" onclick="chatBot.opcionesNodos('`+valorCampo+`');" id="iIdOpciones`+chatBot.capitalizarPrimeraLetra(valorCampo)+`"></i>
                                            <p id="divIdOpcionesNodos`+chatBot.capitalizarPrimeraLetra(valorCampo)+`"></p>
                                        </p>
                                    </div>
                                    <select name="tipoChatNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" id="tipoChatNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3">
                                        <option value="">Seleccione un tipo</option>
                                        <option value="chat">Texto</option>
                                        <option value="imagen">Imagen</option>
                                    </select>
                                    
                                    <select name="resultadoNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" id="resultadoNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3">
                                        <option value="">Seleccione un resultado</option>
                                        `+chatBot.resulatdos+`
                                    </select>
                                </div>
                                <div class="card-footer">
                                    <div class="derechaFloat">
                                        <a href="javascript:chatBot.guardarNodo('`+valorCampo+`');" class="btn btn-icon btn-success" title='Guardar nodo `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' id="btnIdGuardarNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                            <i class="fa fa-save"></i>
                                        </a>
                                        <a href="javascript:chatBot.editarNodo('`+valorCampo+`');" class="btn btn-icon btn-primary hide" title='Editar nodo `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' id="btnIdEditaNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                            <i class="far fa-edit"></i>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    $('#pasoTresNodosAdcionales').append(tmpHtml);
                });
            });
        }else{
            template.validaCampo('Nombre contexto','nomContexto');
            return false;    
        }
    },
    siguienteNodosAdicionales: function() {
        // console.log('chatBot.arraCompoNodos', chatBot.arraCompoNodos);
        // console.log('chatBot.arraCompoNodos', chatBot.arraCompoNodos.length);
        if (chatBot.arraCompoNodos.length >= 2) {
            chatBot.darPasoSiguiente('modeleConfigNodoIniciodespedida','modeleConfigNodos');
            chatBot.nodosAdicionales();
        }else{
            Swal.fire({
                title: 'Error',
                text: 'Verifique la información suministrada para los nodos Inicio/Despedida faltan algunos parametros.',
                icon: 'error',
                confirmButtonText: 'Validar',
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                customClass: 'swalTextTmna',
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                }
            }).then((result) => {
                if (result.value) {
                    Swal.close();
                }
            });
            return false;
        }
    },
    siguienteNodoCreateJson: function() {
        const validaNodosTotales = (chatBot.arraNombreNodos.length + 2);
        console.log('validaNodosTotales =>', validaNodosTotales);
        console.log('chatBot.arraCompoNodos.length =>', chatBot.arraCompoNodos.length);
        if (parseInt(validaNodosTotales) > chatBot.arraCompoNodos.length) {
            Swal.fire({
                title: 'Error',
                text: 'Verifique la información suministrada para los nodos adicionales faltan algunos parametros.',
                icon: 'error',
                confirmButtonText: 'Validar',
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                customClass: 'swalTextTmna',
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                }
            }).then((result) => {
                if (result.value) {
                    Swal.close();
                }
            });
            return false;
        }else{
            // chatBot.darPasoSiguiente('modeleConfigNodos','modeleterminaNodos');
            const data = {
                'arraNombreNodos_cantidad':    chatBot.arraNombreNodos.length,
                'ger.idSegmentoGlb':    ger.idSegmentoGlb,
                'nomContexto':    chatBot.nomContexto,
                'arraNombreNodos':    chatBot.arraNombreNodos, 
                'arraOpcionesNodos':    chatBot.arraOpcionesNodos, 
                'arraCompoNodos':   chatBot.arraCompoNodos
            }
            console.log('Data =>', data);
            $.ajax({
                url: '../gerente/procesarJson',
                type: 'POST',
                dataType: 'json',
                data: {canNodos:chatBot.arraNombreNodos.length,idSegemnto: ger.idSegmentoGlb,nomContexto: chatBot.nomContexto,nodos: JSON.stringify(chatBot.arraNombreNodos), opcionesNodos: JSON.stringify(chatBot.arraOpcionesNodos), compoNodos: JSON.stringify(chatBot.arraCompoNodos)},
            })
            .done(function( dat ) {
                console.log("success", dat);
                if ( dat.resul === 'success' ) {
                    // window.location.href=URL+dat.json;
                    let a= document.createElement('a');
                    a.target= '_blank';
                    a.href= URL+dat.json;
                    a.click();
                    chatBot.darPasoSiguiente('modeleConfigNodos','modeleterminaNodos');
                }else{
                     Swal.fire({
                        title: 'Informacióon',
                        text: 'No se puede crear el formulario. Por que no se ha configurado la cantidad de campos ingresado anteriormente.',
                        icon: 'error',
                        confirmButtonText: 'Validar',
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }
                    });
                    return false;    
                }
            });
        } 
    },
    cleanArray: function( actual ){
        var newArray = new Array();
        for( var i = 0, j = actual.length; i < j; i++ ){
          if ( actual[ i ] ){
            newArray.push( actual[ i ] );
          }
        }
        return newArray;
    },
    selNombresNodos: function( idSegmento, nomNodo, tipNodo, idNomNodo ) {
        chatBot.nomContexto =  $('#nomContexto').val();
        const valTmp      = {
            'id_nodo': parseInt(idNomNodo),
            'identificaCampo': nomNodo,
            'valorCampo': nomNodo,
            tipNodo
        };
        if (chatBot.arraNombreNodos.length > 0) {
            const resultadoInicial = chatBot.arraNombreNodos.find( idNodo =>  idNodo.id_nodo === parseInt(idNomNodo) );
            if ( resultadoInicial ) {
                chatBot.arraNombreNodos.find((value, index) => {
                    if ( value.id_nodo === parseInt(idNomNodo) ) {
                        delete chatBot.arraNombreNodos[index];
                        $('#nomNodoLi_'+idNomNodo+'').css('background-color','');
                    }
                });
                chatBot.arraNombreNodos = chatBot.cleanArray( chatBot.arraNombreNodos );
                if ( ( chatBot.arraNombreNodos.length === 0 ) && ( chatBot.nomContexto != '' ) ) {
                    $("#btnSiguieNombreNodo").addClass('disabled');
                }
            }else{
                chatBot.arraNombreNodos.push(valTmp);
                $('#nomNodoLi_'+idNomNodo+'').css('background-color','#e8f9f8');
            }
        }else {
            chatBot.arraNombreNodos.push(valTmp);
            if (  chatBot.nomContexto != ''  ) {
                $("#btnSiguieNombreNodo").removeClass('disabled');
            }
            $('#nomNodoLi_'+idNomNodo+'').css('background-color','#e8f9f8');
        }
    },
    siguienteNodos: function( hide, show, hideHeader, showHeader, origen ) {
        if (origen === 'pasoOne') {
            // console.log('El HP paso 1');
            // chatBot.arraNombreNodos = [];
            chatBot.nomContexto = $('#nomContexto').val();
            // 
            if( chatBot.cantNBodos === '' ){
                template.validaCampo('Cantidad nodos','cantNodos');
                return false;
            }else if( chatBot.cantNBodos < 0 ){
                template.validaCampo('Cantidad nodos debe ser 0 o mayor a 0','cantNodos');
                return false;
            }else if ( chatBot.nomContexto === '' ) {
                template.validaCampo('Nombre contexto','nomContexto');
                return false;
            }else if( parseInt(chatBot.cantNBodos) > 0 ){
                
                var elements = document.getElementById("formNombresNodosId").elements;
                // console.log('elements =>', elements);
                // for (var i = 1; i <= parseInt(chatBot.cantNBodos); i++) {
                for (var i = 0, element; element = elements[i++];) {
                    // console.log('element =>', element);
                    // console.log('element.name =>', element.name);
                    // console.log('chatBot.arraNombreNodos.length 168 =>', chatBot.arraNombreNodos.length);
                    // console.log('chatBot.cantNBodos 169 =>', chatBot.cantNBodos);
                    if ( element.name === 'nombreNodo'+i+'' ) {
                        var valorCampo = element.value;
                        if ( valorCampo === '' ) {
                            template.validaCampo('Nombre nodo '+i+' ',''+element.name+'');
                            return false;
                        }else{
                            // console.log('chatBot.cantNBodos 176 =>', chatBot.cantNBodos);
                            // console.log('chatBot.arraNombreNodos.length 177 =>', chatBot.arraNombreNodos.length);
                            if (chatBot.arraNombreNodos.length < parseInt(chatBot.cantNBodos)) {
                                var valTmp = {
                                    'id_nodo': i,
                                    'identificaCampo': element.name,
                                    'valorCampo': valorCampo
                                };
                                var valiNodoArray = chatBot.arraNombreNodos.indexOf( valTmp );
                                // console.log('valiNodoArray', valiNodoArray);
                                if (valiNodoArray < 0) {
                                    chatBot.arraNombreNodos.push(valTmp);
                                }
                                // console.log('chatBot.arraNombreNodos 185 =>', chatBot.arraNombreNodos);
                            } else {
                                // chatBot.arraOpcionesNodos = [];
                                if (chatBot.cantNBodosGlb === parseInt(chatBot.cantNBodos) ) {
                                    $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
                                        $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {
                                            chatBot.cantNBodosGlb = parseInt(chatBot.cantNBodos)
                                        });
                                    });
                                } else {
                                    chatBot.cantNBodosGlb = parseInt(chatBot.cantNBodos);
                                    $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
                                        $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {
                                            chatBot.limpiarCeroNodos();
                                        });
                                    });
                                }
                            }
                        }
                    }else{
                        console.log('element.name no es igualllll =>', element.name);
                    }
                }
            }else{
                $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
                    $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {chatBot.limpiarCeroNodos();});
                });
            }
        } else if (origen === 'pasoTwo') {
            // Validamos los nodos inicio & despedida

            if ( parseInt(chatBot.cantNBodos) > 0 ) {
                $('#pasoTresNodosAdcionalesSinNodos').hide();
                $('#pasoTresNodosAdcionales').show();
                // Hay nodos adicionales
                // chatBot.resultadoHomologa =  JSON.parse($('#resultadoHomologa').val());
                var resulatdos = [];
                // console.log('ger.idSegmentoGlb', ger.idSegmentoGlb);
                $.ajax({
                    url: '../gerente/resultadoHomologa',
                    type: 'POST',
                    dataType: 'json',
                    data: {idSegmento: ger.idSegmentoGlb},
                })
                .done(function( dat ) {
                    $.each(dat, function(indexResul, valResul) {
                        // console.log('valResul.idResultado', valResul.idResultado);
                        // console.log('valResul.descripcion', valResul.descripcion);
                        resulatdos.push('<option value="'+valResul.idResultado+'">'+valResul.idResultado+' - '+valResul.descripcion+'</option>');
                    });
                    // console.dirxml('resulatdos', resulatdos);
                    $('#pasoTresNodosAdcionales').html('');
                    $.each(chatBot.arraNombreNodos, function(index, val) {
                        var valorCampo = val.valorCampo.replace(/\s+/g, '_');
                        var tmpHtml = `
                            <div class="col col-lg-4 recuadro">
                                <div class="card h-100">
                                    <div class="card-body">
                                        <h5 class="card-title">Nodo `+chatBot.capitalizarPrimeraLetra(val.valorCampo)+`</h5>
                                        <textarea id="mensaje`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3" cols="30" placeholder="Mensaje" rows="4" value='Mensje `+chatBot.capitalizarPrimeraLetra(valorCampo)+`'></textarea>
                                        <textarea id="mensajeError`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3" placeholder="Mensaje error" value='Mensje Error `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' cols="30" rows="2"></textarea>
                                        <div class="form-check form-switch">
                                          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheck`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                          <label class="form-check-label" for="flexSwitchCheck`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">Directo</label>
                                        </div>
                                        <div>
                                            <p  class="mb-3">Opciones  
                                                <i class="fa fa-plus cursor" onclick="chatBot.opcionesNodos('`+valorCampo+`');" id="iIdOpciones`+chatBot.capitalizarPrimeraLetra(valorCampo)+`"></i>
                                                <p id="divIdOpcionesNodos`+chatBot.capitalizarPrimeraLetra(valorCampo)+`"></p>
                                            </p>
                                        </div>
                                        <select name="tipoChatNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" id="tipoChatNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3">
                                            <option value="">Seleccione un tipo</option>
                                            <option value="chat">Texto</option>
                                            <option value="imagen">Imagen</option>
                                        </select>
                                        
                                        <select name="resultadoNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" id="resultadoNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`" class="form-control mb-3">
                                            <option value="">Seleccione un resultado</option>
                                            `+resulatdos+`
                                        </select>
                                    </div>
                                    <div class="card-footer">
                                        <div class="derechaFloat">
                                            <a href="javascript:chatBot.guardarNodo('`+valorCampo+`');" class="btn btn-icon btn-success" title='Guardar nodo `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' id="btnIdGuardarNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                                <i class="fa fa-save"></i>
                                            </a>
                                            <a href="javascript:chatBot.editarNodo('`+valorCampo+`');" class="btn btn-icon btn-primary hide" title='Editar nodo `+chatBot.capitalizarPrimeraLetra(valorCampo)+`' id="btnIdEditaNodo`+chatBot.capitalizarPrimeraLetra(valorCampo)+`">
                                                <i class="far fa-edit"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `;
                        $('#pasoTresNodosAdcionales').append(tmpHtml);
                    });
                });
            }else{
                $('#pasoTresNodosAdcionales').hide();
                $('#pasoTresNodosAdcionalesSinNodos').show();
            }
            $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
                $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {});
            });
        } else {
            // Otra funcionalidad
            // console.log('chatBot.arraNombreNodos =>', chatBot.arraNombreNodos);
            // console.log('chatBot.arraCompoNodos =>', chatBot.arraCompoNodos);
            // console.log('chatBot.arraOpcionesNodos', chatBot.arraOpcionesNodos);
            $.ajax({
                url: '../gerente/procesarJson',
                type: 'POST',
                dataType: 'json',
                data: {canNodos:chatBot.cantNBodos,idSegemnto: ger.idSegmentoGlb,nomContexto: chatBot.nomContexto,nodos: JSON.stringify(chatBot.arraNombreNodos), opcionesNodos: JSON.stringify(chatBot.arraOpcionesNodos), compoNodos: JSON.stringify(chatBot.arraCompoNodos)},
            })
            .done(function( dat ) {
                // console.log("success", JSON.parse(dat));
                $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
                    $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {
                        
                    });
                });
                if ( dat.resul === 'success' ) {
                    // window.location.href=URL+dat.json;
                    let a= document.createElement('a');
                    a.target= '_blank';
                    a.href= URL+dat.json;
                    a.click();
                }else{
                     Swal.fire({
                        title: 'Informacióon',
                        text: 'No se puede crear el formulario. Por que no se ha configurado la cantidad de campos ingresado anteriormente.',
                        icon: 'error',
                        confirmButtonText: 'Validar',
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }
                    });
                    return false;    
                }
            });
            
            // $.each(array/object, function(index, val) {
            //      /* iterate through array or object */
            // });
        }
    },
    limpiarCeroNodos: function () {
        $('#pasoTresNodosAdcionales,#divIdOpcionesNodosInicio,#pasoTresNodosAdcionales').html('');
        $('#mensajeInicio,#mensajeDespedida,#mensajeErrorInicio,#flexSwitchCheckInicio,#tipoChatNodoInicio,#resultadoNodoInicio').prop('disabled', false);
        $('#mensajeInicio,#mensajeDespedida,#mensajeErrorInicio,#flexSwitchCheckInicio,#tipoChatNodoInicio,#resultadoNodoInicio').val('');
        $('#btnIdEditaNodoInicio,#btnIdEditaNodoDespedida').hide();
        $('#btnIdGuardarNodoInicio,#btnIdGuardarNodoDespedida').show();
    },
    regresasNodos: function( hide, show, hideHeader, showHeader, origen ) {
        $('#'+hide+',#'+hideHeader+' ').hide('slow/400/fast', function() {
            $('#'+show+',#'+showHeader+' ').show('slow/400/fast', function() {});
        });
        // chatBot.arraNombreNodos = [];
    },
    opcionesNodos: function( nodoOrigen ) {
        chatBot.nodoOrigen = nodoOrigen;
        $('#listNodos').modal('show');
        $('#headerTextListNodos').html('Listados de opciones para el nodo: '+nodoOrigen+' ');
        $('#bodyListNodos').html('');

        let indiceIncio = chatBot.arraOpcionesNodos.findIndex(opcNodo => ( ( opcNodo.nodo === nodoOrigen ) &&  ( opcNodo.opc === chatBot.nodoInicio ) ));

        if (indiceIncio === -1 ) {
            var checkbox = '';
        }else{
            var checkbox = 'checked';
        }

        if ( nodoOrigen != chatBot.nodoInicio ) {
            var tmpHtml = `
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" `+checkbox+` value="" onclick="chatBot.selecTionNodosOpc('`+chatBot.nodoInicio+`','`+chatBot.nodoInicio+`','`+nodoOrigen+`');" id="flexCheckinicio">
                  <label class="form-check-label" for="flexCheckinicio">
                   Inicio
                  </label>
                </div>
            `;
            $('#bodyListNodos').append(tmpHtml);
        }

        $.each(chatBot.arraNombreNodos, function(index, val) {
            
            let indiceEach = chatBot.arraOpcionesNodos.findIndex(opcNodo => ( ( opcNodo.nodo === nodoOrigen ) &&  ( opcNodo.opc === val.valorCampo ) ));

            if (indiceEach === -1 ) {
                var checkbox = '';
            }else{
                var checkbox = 'checked';
            }

            // console.log('nodoOrigen != val.valorCampo', nodoOrigen , val.valorCampo)
            var nodoOrigenGn = nodoOrigen.replace(/\s+/g, '_');
            var valorCampo = val.valorCampo.replace(/\s+/g, '_');

            if ( nodoOrigen != valorCampo ) {
                var tmpHtml = `
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" `+checkbox+` value="" onclick="chatBot.selecTionNodosOpc('`+val.valorCampo+`','`+val.identificaCampo+`','`+nodoOrigen+`');" id="flexCheck`+val.identificaCampo+`">
                      <label class="form-check-label" for="flexCheck`+val.identificaCampo+`">
                        `+chatBot.capitalizarPrimeraLetra(val.valorCampo)+`
                      </label>
                    </div>
                `;
            }
            $('#bodyListNodos').append(tmpHtml);
        });

        let indiceDesp = chatBot.arraOpcionesNodos.findIndex(opcNodo => ( ( opcNodo.nodo === nodoOrigen ) &&  ( opcNodo.opc === chatBot.nodoDespedida ) ));

        if (indiceDesp === -1 ) {
            var checkbox = '';
        }else{
            var checkbox = 'checked';
        }

        if ( nodoOrigen != chatBot.nodoDespedida ) {
            var tmpHtml = `
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" `+checkbox+` value="" onclick="chatBot.selecTionNodosOpc('`+chatBot.nodoDespedida+`','`+chatBot.nodoDespedida+`','`+nodoOrigen+`');" id="flexCheckdespedida">
                  <label class="form-check-label" for="flexCheckdespedida">
                   Despedida
                  </label>
                </div>
            `;
            $('#bodyListNodos').append(tmpHtml);
        }
        
    },
    selecTionNodosOpc: function( selecCheckOpc, valIdentificaCampo, nodoDestino ) {
        var varTmpOpcNodos = {
            'nodo': nodoDestino,
            'opc': selecCheckOpc
        };
        let indice = chatBot.arraOpcionesNodos.findIndex(opcNodo => ( ( opcNodo.nodo === varTmpOpcNodos.nodo ) &&  ( opcNodo.opc === varTmpOpcNodos.opc ) ));
        if (indice === -1 ) {
            chatBot.arraOpcionesNodos.push(varTmpOpcNodos);
        }else{
            chatBot.arraOpcionesNodos.splice(indice,1);
        }
        // console.log('chatBot.arraOpcionesNodos =>', chatBot.arraOpcionesNodos);
    },
    capitalizarPrimeraLetra: function (str) {
      str.replace(' ','_')
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
    validaPrintOpcNodos: function() {
        // console.log('Inicio cerro modal');
        $('#divIdOpcionesNodos'+chatBot.capitalizarPrimeraLetra(chatBot.nodoOrigen)+'').html('');
        var tmpHtml = [];
        $.each(chatBot.arraOpcionesNodos, function(index, val) {

            $.each(chatBot.arraNombreNodos, function(indexNoNodos, valNonNodos) {
                // console.log('valll =>', val.nodo);
                // console.log('valNonNodos =>', valNonNodos.valorCampo);
                // console.log('chatBot.nodoOrigen =>', chatBot.nodoOrigen);

                if ( (val.opc === valNonNodos.valorCampo) && ( val.nodo === chatBot.nodoOrigen ) ) {

                    if (val.nodo === chatBot.nodoOrigen) {
                        tmpHtml.push('<span class="badge rounded-pill text-bg-success">'+chatBot.capitalizarPrimeraLetra(val.opc)+'</span>');
                    }
                }

                // console.log('tmpHtml =>', tmpHtml);
            });

            if(  (val.opc === chatBot.nodoInicio) && ( val.nodo === chatBot.nodoOrigen ) ){
                tmpHtml.push('<span class="badge rounded-pill text-bg-success">'+chatBot.capitalizarPrimeraLetra(val.opc)+'</span>');
            }else if(  (val.opc === chatBot.nodoDespedida) && ( val.nodo === chatBot.nodoOrigen ) ){
                tmpHtml.push('<span class="badge rounded-pill text-bg-success">'+chatBot.capitalizarPrimeraLetra(val.opc)+'</span>');
            }
        });
        // console.log('chatBot.capitalizarPrimeraLetra(chatBot.nodoOrigen)',chatBot.capitalizarPrimeraLetra(chatBot.nodoOrigen) )
        // console.log('Html edit =>', 'divIdOpcionesNodos'+chatBot.capitalizarPrimeraLetra(chatBot.nodoOrigen));
        $('#divIdOpcionesNodos'+chatBot.capitalizarPrimeraLetra(chatBot.nodoOrigen)+'').html(tmpHtml);
        // $('#divIdOpcionesNodosIncio').html(tmpHtml);
        // console.log('Fin cerro modal');
    },
    guardarNodo: function( nomNodo ) {
        chatBot.nomNodoGuardar = nomNodo;
        // console.log('chatBot.arraOpcionesNodos', chatBot.arraOpcionesNodos);
        var smsNodo           = $('#mensaje'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').val();
        var smsErrorNodo      = $('#mensajeError'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').val();
        var directoNodo       = 'off';
        //$('#flexSwitchCheck'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').val();
        var tipoSmsNodo       = $('#tipoChatNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').val();
        var resultadoSmsNodo  = $('#resultadoNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').val();
        // var opcionesNodos     = {};
        if ( nomNodo != chatBot.nodoDespedida ) {
            if ( smsNodo === '' ) {
                template.validaCampo('Sms nodo: '+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+' vacío','');
                return false;
            }else if ( smsErrorNodo === '' ) {
                template.validaCampo('Sms error nodo: '+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+' vacío','');
                return false;
            }else if ( tipoSmsNodo === '' ) {
                template.validaCampo('Tipo sms nodo: '+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+' no seleccionado','');
                return false;
            }else if ( resultadoSmsNodo === '' ) {
                template.validaCampo('Resultado sms nodo: '+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+' no seleccionado','');
                return false;
            }else{
                $('#mensaje'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#mensajeError'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#flexSwitchCheck'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#tipoChatNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#resultadoNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').prop('disabled', true);
                $('#iIdOpciones'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').hide();
                // console.log('Nodo a guardar =>', chatBot.nomNodoGuardar);
                // console.log('nombre identificador =>', '#btnIdGuardarNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'');
                $('#btnIdGuardarNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').hide('slow/400/fast', function() {
                    $('#btnIdEditaNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').show('slow/400/fast', function() {});    
                });
            }
        }else{
            if ( smsNodo === '' ) {
                template.validaCampo('Sms nodo: '+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+' vacío','');
                return false;
            }else{
                $('#mensaje'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').prop('disabled', true);
                $('#btnIdGuardarNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').hide('slow/400/fast', function() {
                    $('#btnIdEditaNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').show('slow/400/fast', function() {});    
                });
            }
        }
        // console.log('Directo =>', $('#flexSwitchCheck'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').is(":checked"));
        if ($('#flexSwitchCheck'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').is(":checked")) {
            directoNodo  = 'on';
        }else{
            directoNodo  = 'off';
        }
        var opcionesNodos  = {
            'nodo': nomNodo,
            'smsNodo': smsNodo,
            'smsErrorNodo': smsErrorNodo,
            'directoNodo': directoNodo,
            'tipoSmsNodo': tipoSmsNodo,
            'resultadoSmsNodo': resultadoSmsNodo
        };
        const resultadoInicial = chatBot.arraCompoNodos.find( infoNodo =>  infoNodo.nodo === nomNodo );
        if ( resultadoInicial ) {
            chatBot.arraCompoNodos.find((value, index) => {
                if ( value.nodo === nomNodo ) {
                    delete chatBot.arraCompoNodos[index];
                }
            });
            chatBot.arraCompoNodos = chatBot.cleanArray( chatBot.arraCompoNodos );

        }
        chatBot.arraCompoNodos.push(opcionesNodos);
        // console.log('chatBot.arraCompoNodos', chatBot.arraCompoNodos);
    },
    editarNodo: function( nomNodo ) {
        chatBot.nomNodoGuardar = nomNodo;
        $('#mensaje'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#mensajeError'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#flexSwitchCheck'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#tipoChatNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+',#resultadoNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').prop('disabled', false);
        $('#iIdOpciones'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').show();
        $('#btnIdEditaNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').hide('slow/400/fast', function() {
            $('#btnIdGuardarNodo'+chatBot.capitalizarPrimeraLetra(chatBot.nomNodoGuardar)+'').show('slow/400/fast', function() {});    
        });
    },
    newFormularioSeg: function( idSegmento ) {
        $('#divRegistrosFormularios').hide('slow/400/fast', function() {
            $('#divCrecionFormulario').show('slow/400/fast', function() {});
        });
    },
    regresarNewFormularioSeg: function(){
        $('#divCrecionFormulario').hide();
        $('#divRegistrosFormularios').show();
    },
    capitalize: function( texto ) {
      return texto[0].toUpperCase() + texto.slice(1);
    },
    verCamposFormulario: function( idFomulario, idSegmento ) {
        $('#divRegistrosFormularios').hide('slow/400/fast', function() {
            $('#divCuerpoFormularios').show('slow/400/fast', function() {
                $('#divCuerpoFormulario').html('');
                $('#bodyPreloadsCuerpoFormulario').show();
                $.ajax({
                    url: '../gerente/verCamposFormulario',
                    type: 'POST',
                    dataType: 'json',
                    data: {idFomulario},
                })
                .done(function( data ) {
                    // console.log('data', data);
                    if ( data.length > 0 ) {
                        var tmpHtml = [];
                        $('#bodyPreloadsCuerpoFormulario').hide();
                        
                        $.each(data, function(index, val) {
                            if ( val.tipo_dato === 'texarea' ) {  
                                var style = 12;
                                var campo = `
                                    <textarea cols="10" rows="10" type="`+val.tipo_dato+`" class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" placeholder="`+chatBot.capitalize(val.nombre_label)+`" `+val.obligatorio+`></textarea>
                                `;
                            }else{
                                if ( data.length === 1 ) {
                                    var style = 12;
                                }else if ( data.length === 2 ) {
                                    var style = 6;
                                }else{
                                    var style = 4;
                                }
                                var campo = `
                                    <input type="`+val.tipo_dato+`" class="form-control"  name="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" id="`+val.nombre_label.replace(' ','_').toLowerCase()+`_`+val.formulario+`" placeholder="`+chatBot.capitalize(val.nombre_label)+`" `+val.obligatorio+`>
                                `;
                            }
                            var tmp  = `
                                <div class="col-lg-`+style+`">
                                    <div class="form-group">
                                      <label>`+chatBot.capitalize(val.nombre_label)+`:</label>
                                      `+campo+`
                                      <span class="form-text text-muted">Ingrese `+chatBot.capitalize(val.nombre_label)+`.</span>
                                    </div>
                                </div>
                            `;
                            $('#divCuerpoFormulario').append(tmp);
                        });
                    }else{
                        $('#bodyPreloadsCuerpoFormulario').hide();
                        $('#divCuerpoFormulario').html('<p>No se encontro cuerpo de este formulario.</p>');
                    }
                });
            });
        });
    },
    verResultadosFormulario: function( idFomulario,idSegmento ) {
        chatBot.idSegmGlb = idSegmento;
        $('#divRegistrosFormularios').hide('slow/400/fast', function() {
            $('#divResultadosFormularios').show('slow/400/fast', function() {
                $('#bodyCargaResultados').html('');
                $('#bodyPreloadsFortmulario').show();
                $.ajax({
                    url: '../gerente/resultadoHomologa',
                    type: 'POST',
                    dataType: 'json',
                    data: {idSegmento},
                })
                .done(function( data ) {
                    if ( data.length > 0 ) {
                        var tmpHtml = [];
                        $.each(data, function(index, val) {
                            $.ajax({
                                url: '../gerente/resultAgregado',
                                type: 'POST',
                                dataType: 'json',
                                data: {resultadoId: val['idResultado'], idFomulario, resultado: val['descripcion']},
                            })
                            .done(function( datResul ) {
                                // console.log('datResul =>', datResul);
                                if ( parseInt(datResul) > 0 ) {
                                    var smsTol = 'Click para quitar el resultado: '+val['descripcion']+' del formulario';
                                    var style = 'background-color:#e8f9f8;';
                                    var texPreloads = 'Estamos removiendo el resultado';
                                } else {
                                    var smsTol = 'Click para agregar el resultado: '+val['descripcion']+' del formulario';
                                    var style = '';
                                    var texPreloads = 'Estamos agregando el resultado';
                                }
                                var tmp  = `
                                    <div class="col-3" data-bs-toggle="tooltip" data-bs-placement="bottom" title="`+smsTol+`">
                                        <li class="cardTipi" style='`+style+`' onclick="chatBot.agregarQuitarResultado('`+val['idResultado']+`', '`+val['descripcion']+`' ,`+idFomulario+`);">
                                            <div class="users-list-body">
                                                <div id='liResultado_`+val['idResultado']+`'>
                                                    <h6 class="textOfertaViews">`+val['descripcion']+`</h6>
                                                </div>
                                                <div id="bodyPreloads_`+val['idResultado']+`" class='hide'>
                                                    <p align="center" style="font-size:10px;text-align:center;overflow: hidden;">
                                                        <b>Un momento por favor <br>
                                                           `+texPreloads+` 
                                                        </b>
                                                        <br>
                                                        <i class="fa fa-spinner fa-spin"  style="font-size:25px;color:#5A078B;text-align:center;"></i>
                                                    </p>
                                                </div>
                                            </div>
                                        </li>
                                    </div>
                                `;
                                $('#bodyCargaResultados').append(tmp);
                            }); 
                        });
                        $('#bodyPreloadsFortmulario').hide();
                        $('[data-bs-toggle="tooltip"]').tooltip();
                    } else {
                        $('#bodyPreloadsFortmulario').hide();
                        $('#bodyCargaResultados').html('<p>No se encontraron resultados para este segmento.</p>')
                    }
                });
            });
        });
    },
    agregarQuitarResultado: function( idResultado, resultado, idFomulario ) {
        $('#liResultado_'+idResultado+'').hide();
        $('#bodyPreloads_'+idResultado+'').show();
        $.post('agregarQuitarResultado', {idResultado, resultado, idFomulario}, function(data, textStatus, xhr) {
            $('#bodyPreloads_'+idResultado+'').hide();
            chatBot.verResultadosFormulario( idFomulario, chatBot.idSegmGlb );
        });
    },
    agregarQuitarResultadoConf: function( idResultado, resultado, idSegmento ) {
        $('#liResultado_'+idResultado+'').hide();
        $('#bodyPreloads_'+idResultado+'').show();
        $.post('agregarQuitarResultadoConf', {idResultado, resultado, idSegmento}, function(data, textStatus, xhr) {
            $('#bodyPreloads_'+idResultado+'').hide();
            ger.verInfoSegmento( idSegmento, ger.nomSegmentoGlb );
        });
    },
    siguientePasoFormulario: function( hide, show, hideHeader, showHeader ) {
        chatBot.nombreFormulario  = $('#nombreFormulario').val();
        chatBot.canCampos         = $('#canCampos').val();
        if (hide === chatBot.bdyCreateForm) {
            if (nombreFormulario === '') {
                template.validaCampo('Nombre formulario','nombreFormulario');
                return false;
            }else if ( canCampos === '' ) {
                template.validaCampo('Cantidad campos','canCampos');
                return false;
            } else if (parseInt(chatBot.canCampos) === 0 ) {
                template.validaCampo('Cantidad campos debe ser mayor a 0','canCampos');
                return false;
            }else{
                $('#'+hide+'').hide();
                $('#'+show+'').show();
                $('#'+hideHeader+'').hide();
                $('#'+showHeader+'').show();
            }
        }else{
            $('#'+hide+'').hide();
            $('#'+show+'').show();
            $('#'+hideHeader+'').hide();
            $('#'+showHeader+'').show();
        }
    },
    siguienteCampo: function() {
        var tituloCampo   = $('#tituloCampo').val();
        var tipoDatoForm  = $('#tipoDatoForm').val();  
        var obligatorio   = $('#obligatorio').val();
        if ( tituloCampo === '' ){
            template.validaCampo('Titulo campo','tituloCampo');
            return false;
        }else if ( tipoDatoForm === '' ) {
            template.validaCampo('Tipo dato','tipoDatoForm');
            return false;
        }else if ( obligatorio === '' ) {
            template.validaCampo('Obligatorio','obligatorio');
            return false;
        } else if( chatBot.arraCamposFormNew.length >= parseInt(chatBot.canCampos)  ){ 
            template.validaCampo('Superas la cantidad de campos ingresados','obligatorio');
            return false;
        }else{
            if (parseInt(obligatorio) === 1 ) {
                obligatorio = 'required';
            }else{
                obligatorio = '';
            }
            var valTmp = {
                'id'          : Math.random(),
                'nombre_label': tituloCampo,
                'tipo_dato': tipoDatoForm,
                'obligatorio': obligatorio
            };
            chatBot.arraCamposFormNew.push(valTmp);
            chatBot.recorreCamporFormPrevio();
        }
    }, 
    recorreCamporFormPrevio: function() {
        if ( chatBot.arraCamposFormNew.length > 0 ) {
            $('#divVistaPreviaForm').html('');
            $.each(chatBot.arraCamposFormNew, function(index, val) {
                if ( val.tipo_dato === 'texarea' ) {  
                    var campo = `
                        <textarea cols="10" rows="10" type="`+val.tipo_dato+`" class="form-control"  placeholder="`+chatBot.capitalize(val.nombre_label)+`" `+val.obligatorio+`></textarea>
                    `;
                }else{
                    var campo = `
                        <input type="`+val.tipo_dato+`" class="form-control"  placeholder="`+chatBot.capitalize(val.nombre_label)+`" `+val.obligatorio+`>
                    `;
                }
                var tmp  = `
                    <div class='row' id='idDivForm_`+val.id+`'>
                        <div class="col-lg-10">
                            <div class="form-group">
                              <label>`+chatBot.capitalize(val.nombre_label)+`:</label>
                              `+campo+`
                              <span class="form-text text-muted">Ingrese `+chatBot.capitalize(val.nombre_label)+`.</span>
                            </div>
                        </div>
                        <div class="col-lg-2">
                            <div class="form-group">
                                <label>Eliminar</label>
                                <br>
                                <a href="javascript:chatBot.eliminarCampoPrevio( `+val.id+`, `+index+` );" class="btn btn-icon btn-danger">
                                    <i class="fas fa-window-close text-while" style="font-size:17px;"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                `;
                $('#divVistaPreviaForm').append(tmp);
            });
            $('#tituloCampo').val('');
            $('#tipoDatoForm').val('');  
            $('#obligatorio').val('');
        }else{
            $('#divVistaPreviaForm').html('');
        }
    },
    eliminarCampoPrevio: function( id, index ) {
        chatBot.arraCamposFormNew = chatBot.arraCamposFormNew.filter(datos => datos.id !== id);
        chatBot.recorreCamporFormPrevio();
    },
    guardarFormPrevio: function( idSegmento ) {
        // console.log('chatBot.arraCamposFormNew.length === chatBot.canCampos', chatBot.arraCamposFormNew.length, chatBot.canCampos );
        if ( parseInt(chatBot.arraCamposFormNew.length) === parseInt(chatBot.canCampos) ) {
            template.showPreloader('Estamos creando tu formulario');
            $.ajax({
                url: '../gerente/guardarFormPrevio',
                type: 'POST',
                dataType: 'json',
                data: {nomForm: chatBot.nombreFormulario, canCampos: chatBot.canCampos, idSegmento},
            })
            .done(function( data ) {
                template.hidePreloader();
                // console.log("Resul", data);
                if (parseInt(data) > 0) {
                    console.log("Estamos bien =>", data);
                    let htmlLet = `
                        <i class="fas fa-thumbs-up fa-2x text-success"></i>
                        <p align='center' style='padding-top:-20px;'>
                        <b> Formulario creado con exito.</b>
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
                        // ger.verInfoSegmento( ger.idSegmentoGlb, ger.nomSegmentoGlb );
                        chatBot.guardarCamposFormPrevio( data, idSegmento );
                    }, 2000);
                }else{
                    Swal.fire('Error', 'No se pudo crear el formulario. Intentalo nuevamente', 'error');
                }
            });
            
        }else{
            Swal.fire({
                title: 'Informacióon',
                text: 'No se puede crear el formulario. Por que no se ha configurado la cantidad de campos ingresado anteriormente.',
                icon: 'error',
                confirmButtonText: 'Validar',
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                customClass: 'swalTextTmna',
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                }
            });
            return false;
        }
    },
    guardarCamposFormPrevio: function( idFomulario, idSegmento ) {
        // console.log("idFomulario =>", idFomulario);
        // console.log("idSegmento =>", idSegmento);
        var tmpConteo = 0;
        $.each(chatBot.arraCamposFormNew, function(index, val) { 
            template.showPreloader('Estamos configurando el  campo: '+chatBot.capitalize(val.nombre_label)+' de tu formulario');
            $.ajax({
                url: '../gerente/guardarCamposFormPrevio',
                type: 'POST',
                dataType: 'json',
                data: {idFomulario,tipo_campo:val.tipo_dato,label:val.nombre_label,obligatorio:val.obligatorio},
            })
            .done(function( dataResul ) {
                // console.log("success", dataResul);
                tmpConteo = tmpConteo + 1;
                if ( parseInt(tmpConteo) === chatBot.arraCamposFormNew.length  ) {
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
                        title: 'Formulario finalizado.'
                    });
                    setTimeout(function() {
                        template.hidePreloader();
                        ger.verInfoSegmento( idSegmento, ger.nomSegmentoGlb )    
                    }, 3001);
                }
            });
        });

        
    },
    resultadoHomologa: function( idSegmento, resultado ) {
        var resulatdosHomo;
        $.ajax({
            url: '../gerente/resultadoHomologa',
            type: 'POST',
            dataType: 'json',
            data: {idSegmento},
        })
        .done(function( dat ) {
            resulatdosHomo = dat
            // $.each(dat, function(indexResul, valResul) {
            //     if (parseInt(resultado) === valResul.idResultado ) {
            //         var select = 'selected';
            //     }else{
            //         var select = '';
            //     }
            //     // resulatdosHomo.push('<option '+select+' value="'+valResul.idResultado+'">'+valResul.idResultado+' - '+valResul.descripcion+'</option>');
            //     // resulatdosHomo.push('<option '+select+' value="'+valResul.idResultado+'">'+valResul.idResultado+' - '+valResul.descripcion+'</option>');
            // });
        });
        return resulatdosHomo;
    },
    changeStatus: function( idContxChatbot, nombreContexto, idSegmento, status ){
        Swal.fire({
            title: 'Confirmación',
            text: 'Desea cambiar de estado este contexto: '+nombreContexto+'.?',
            icon: 'question',
            confirmButtonText: 'Si',
            cancelButtonText: 'No',
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
            customClass: 'swalTextTmna',
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutRight'
            }
        }).then((result) => {
            if (result.value) {
                template.showPreloader('Cambiando de estado el contexto');
                $.ajax({
                    type: "post",
                    url: "../gerente/changeStatus",
                    data: {idContxChatbot,idSegmento,status,nombreContexto},
                    dataType: "json"
                })
                .done( function( resul ){
                    console.log('resul =>', resul);
                    if (parseInt(resul) === -1) {
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
                            icon: 'error',
                            title: 'No se puede modificar el estado por que tiene un contexto activo, debe inactivar primero el contexto que esta activo'
                        });
                        setTimeout(function() {
                            template.hidePreloader();
                            ger.verInfoSegmento( idSegmento, ger.nomSegmentoGlb )    
                        }, 3001);
                    } else {
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
                            title: 'Contexto modificado con exito.'
                        });
                        setTimeout(function() {
                            template.hidePreloader();
                            ger.verInfoSegmento( idSegmento, ger.nomSegmentoGlb )    
                        }, 3001);
                    }
                });
            }
        });
        return false;
    },
    verNodosContexto: function( idContxChatbot, nombreContexto, idSegmento, nomJson ) {
        $('#divRegistrosContextos').hide('slow/400/fast', function() {
            $('#divBodyNodosContextos').show('slow/400/fast', function() {
                var a = document.getElementById('aHrefLessJson'); //or grab it by tagname etc
                a.href = URL+nomJson;
                $('#nombreContexChatBot').html(nombreContexto);
                $('#bodyNodos').html('');
                $('#bodyPreloadsCuerpoContextoChatBot').show();
                $.ajax({
                    url: '../gerente/verNodosContexto',
                    type: 'POST',
                    dataType: 'json',
                    data: {idContxChatbot},
                })
                .done(function( data ) {
                    // console.log('data', data);
                    if ( data.length > 0 ) {
                        var tmpHtml = [];
                        $.each(data, function(index, val) {
                            // var valorCampo = val.valorCampo.replace(/\s+/g, '_');
                            if (val.nodo_directo === 'SI') {
                                var checked = 'checked';
                            }else{
                                var checked = '';
                            }
                            // var resulTmp = chatBot.resultadoHomologa(idSegmento, val.nodo_id_resultado);
                            // console.log('resulTmp', resulTmp);
                            if (val.nodo_nombre === chatBot.nodoDespedida) {
                                var tmpHtml = `
                                    <div class="col col-lg-4 mb-3 recuadro">
                                        <div class="card h-100">
                                            <div class="card-body">
                                                <h5 class="card-title">Nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`</h5>
                                                <textarea id="mensajeEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" class="form-control mb-3" disabled cols="30" placeholder="Mensaje" rows="4" value='Mensje `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`'>`+val.nodo_mensaje+`</textarea>
                                            </div>
                                            <div class="card-footer">
                                                <div class="derechaFloat">
                                                    <a href="javascript:chatBot.guardarNodoEditar('`+val.nodo_nombre+`');" class="btn btn-icon btn-success hide" title='Actualizar nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`' id="btnIdGuardarNodo`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">
                                                        <i class="fa fa-save"></i>
                                                    </a>
                                                    <a href="javascript:chatBot.editarNodoEditar('`+val.nodo_nombre+`');" class="btn btn-icon btn-primary" title='Editar nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`' id="btnIdEditaNodo`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">
                                                        <i class="far fa-edit"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                `;
                            }else{
                                var tmpHtml = `
                                    <div class="col col-lg-4 mb-3 recuadro">
                                        <div class="card h-100">
                                            <div class="card-body">
                                                <h5 class="card-title">Nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`</h5>
                                                <textarea id="mensajeEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" class="form-control mb-3" disabled cols="30" placeholder="Mensaje" rows="4" value='Mensje `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`'>`+val.nodo_mensaje+`</textarea>
                                                <textarea id="mensajeErrorEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" class="form-control mb-3" disabled placeholder="Mensaje error" cols="30" rows="2">`+val.nodo_mensaje_error+`</textarea>
                                                <div class="form-check form-switch">
                                                  <input class="form-check-input" `+checked+` type="checkbox"  role="switch" id="flexSwitchCheckEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" disabled>
                                                  <label class="form-check-label" for="flexSwitchCheckEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">Directo</label>
                                                </div>
                                                <div>
                                                    <p  class="mb-3">Opciones  
                                                        <i class="fa fa-plus cursor hide" onclick="chatBot.opcionesNodos('`+val.nodo_nombre+`');" id="iIdOpcionesEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`"></i>
                                                        <p id="divIdOpcionesNodosEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">
                                                            `+val.nodo_opciones+`
                                                        </p>
                                                    </p>
                                                </div>
                                                <select name="tipoChatNodoEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" id="tipoChatNodoEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" class="form-control mb-3">
                                                    <option value="">Seleccione un tipo</option>
                                                    <option value="chat">Texto</option>
                                                    <option value="imagen">Imagen</option>
                                                </select>
                                                
                                                <select name="resultadoNodoEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" id="resultadoNodoEditar`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`" class="form-control mb-3"></select>
                                            </div>
                                            <div class="card-footer">
                                                <div class="derechaFloat">
                                                    <a href="javascript:chatBot.guardarNodoEditar('`+val.nodo_nombre+`');" class="btn btn-icon btn-success hide" title='Actualizar nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`' id="btnIdGuardarNodo`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">
                                                        <i class="fa fa-save"></i>
                                                    </a>
                                                    <a href="javascript:chatBot.editarNodoEditar('`+val.nodo_nombre+`');" class="btn btn-icon btn-primary" title='Editar nodo `+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`' id="btnIdEditaNodo`+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+`">
                                                        <i class="far fa-edit"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                `;
                            }
                            $('#bodyNodos').append(tmpHtml);
                            var opcTmp = val.nodo_opciones.split(',');
                            console.dirxml('opcTmp', opcTmp);
                            var tmpHtml = [];
                            $.each(opcTmp, function(indexNodo, valNodo) {
                                tmpHtml.push('<span class="badge rounded-pill text-bg-success">'+chatBot.capitalizarPrimeraLetra(valNodo.replaceAll('[', '').replaceAll(']', '').replaceAll("'","").replaceAll("_"," "))+'</span>');
                            });
                            $('#divIdOpcionesNodosEditar'+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+'').html(tmpHtml);
                            $.ajax({
                                url: '../gerente/resultadoHomologa',
                                type: 'POST',
                                dataType: 'json',
                                data: {idSegmento},
                            })
                            .done(function( dat ) {
                                $.each(dat, function(indexResul, valResul) {
                                    if (parseInt(val.nodo_id_resultado) === valResul.idResultado ) {
                                        var select = 'selected';
                                    }else{
                                        var select = '';
                                    }
                                    $('#resultadoNodoEditar'+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+'').append('<option '+select+' value="'+valResul.idResultado+'">'+valResul.idResultado+' - '+valResul.descripcion+'</option>');
                                });
                                var dataTipo = ['chat','image'];
                                $.each(dataTipo, function(indexTipo, valTipo) {
                                    if (val.nodo_tipo === valTipo ) {
                                        var selectTipo = 'selected';
                                    }else{
                                        var selectTipo = '';
                                    }
                                    $('#tipoChatNodoEditar'+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+'').append('<option '+selectTipo+' value="'+valTipo+'">'+valTipo+'</option>');
                                });
                                $('#resultadoNodoEditar'+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+',#tipoChatNodoEditar'+chatBot.capitalizarPrimeraLetra(val.nodo_nombre)+'').attr('disabled',true);
                            });
                        });
                        $('#bodyPreloadsCuerpoContextoChatBot').hide();
                    }else{
                        $('#bodyPreloadsCuerpoContextoChatBot').hide();
                        $('#bodyNodos').html('<p>No se encontraron nodos para este contexto.</p>');
                    }
                });
            });
        });
    },
    showPasoToPasoAeditarContexto: function() {},
    reiniciarChat: function(){
        chatBot.probarChatCont( chatBot.idContxChatbot, chatBot.nomContexto, chatBot.nameJson, 1 );
    },
    probarChatCont: function( idContxChatbot, nombreContexto, json, limpiar ){
        chatBot.nomContexto     = nombreContexto;  
        chatBot.idContxChatbot  = idContxChatbot;
        chatBot.nameJson        = json; 
        const fechaActual = new Date();
        const horaActual = fechaActual.getHours();
        const minutosActuales = fechaActual.getMinutes();
        const segundosActuales = fechaActual.getSeconds();
        
        // Formatear la hora y los minutos para que tengan 2 dígitos
        const horaFormateada = horaActual.toString().padStart(2, '0');
        const minutosFormateados = minutosActuales.toString().padStart(2, '0');
        const segundosFormateados = segundosActuales.toString().padStart(2, '0');

        // Mostrar la hora actual en la consola
        var hora = horaFormateada + ':' + minutosFormateados + ':' + segundosFormateados;
        
        if (parseInt(limpiar) === 0) {
            $('#divRegistrosContextos').hide('slow/400/fast', function() {
                $('#bodyPruebaContexto').show('slow/400/fast', function() {});
            });
        }
        fetch(URL+json)
        .then(response => response.json())
        .then(respuestas => {
            chatBot.nodoAnterior  = 'nodo_inicio';
            chatBot.dataNodoAnterior = respuestas['nodo_inicio'];
            $('#divMsms').html('');
            var tmpHtml = `
                <div class="chats">
                    <div class="chat-avatar">
                        <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
                    </div>
                    <div class="chat-content">
                        <div class="message-content">
                            `+respuestas['nodo_inicio'].mensaje.replaceAll('\nn','<br>').replaceAll('\n','<br>')+`
                            <div class="chat-time">
                                <div>
                                    <div class="time"><i class="fas fa-clock"></i> `+hora+`</div>
                                </div>
                            </div>
                        </div>
                        <div class="chat-profile-name">
                            <h6>ChatBot</h6>
                        </div>
                    </div>
                </div>
                <br><br>
            `;
            $('#divMsms').html(tmpHtml);
            $("#mensajeEscribiendoGerente").val('');
            $("#mensajeEscribiendoGerente").focus();
        });
        chatBot.getMessages();
    },
    probarChatWhas: function( idContxChatbot, nombreContexto, json ){

        $('#divRegistrosContextos').hide('slow/400/fast', function() {
            $('#bodyPruebaWhast').show('slow/400/fast', function() {
                $.ajax({
                    type: "get",
                    url: "../gerente/probarChatWhas",
                    data: {idContxChatbot},
                    dataType: "json"
                })
                .done( function( data ){
                    if (data.length > 0) {
                        $('#bodyPreloadsCreateConfiCamposChatbot').hide();
                        $('#listConlistConfiguradoCamposfigCampos,#newInteraccionCreate,#btnRegresarPruebWhas').show();
                    } else {
                        $('#bodyPreloadsCreateConfiCamposChatbot').hide();
                        $('#listConfigCampos,#btnRegresarPruebWhas,#btnSigFormulari').show();
                    }
                });
            });
        });
    },
    agregarCampWhasPru: function( data ){
        
        const valTmp      = {
            'nameCampo': data
        };
        if (chatBot.arraCamposForPrWhas.length > 0) {
            const resultadoInicial = chatBot.arraCamposForPrWhas.find( dataArray =>  dataArray.nameCampo === data );
            if ( resultadoInicial ) {
                chatBot.arraCamposForPrWhas.find((value, index) => {
                    if ( value.nameCampo === data ) {
                        delete chatBot.arraCamposForPrWhas[index];
                        $('#nomNodoLiWhas_'+data+'').css('background-color','');
                    }
                });
                chatBot.arraCamposForPrWhas = chatBot.cleanArray( chatBot.arraCamposForPrWhas );
                if ( chatBot.arraCamposForPrWhas.length === 0  ) {
                    $("#btnSigFormulari").addClass('disabled');
                }
            }else{
                chatBot.arraCamposForPrWhas.push(valTmp);
                $('#nomNodoLiWhas_'+data+'').css('background-color','#e8f9f8');
            }
        }else {
            chatBot.arraCamposForPrWhas.push(valTmp);
            $("#btnSigFormulari").removeClass('disabled');
            $('#nomNodoLiWhas_'+data+'').css('background-color','#e8f9f8');
        }
    },
    getMessages: function() {
        $("#divMsms").animate({ scrollTop: $('#divMsms').prop("scrollHeight")}, 1000);
    },
    editarIntance: function( idIntance, nameIntance ){
        $('#divRegistrosInstancias').hide();
        $('#divEditarInstancias').show();
        $('#bodyInfoEditarInstancias').load('../gerente/bodyInfoEditarInstancias',{idIntance},function(){
            $('#titleIntancesEdit').html('');
            $('#titleIntancesEdit').html('Información de la instancia '+nameIntance);
            $('#bodyPreloadsEditarInstancias').hide();
        });
    },
    detalleIntance: function( idIntance, nameIntance ){
        $('#divRegistrosInstancias').hide();
        $('#divDetalleInstancias').show();
    },
    regresarList: function( hide, show ){
        $('#'+hide+'').hide();
        $('#'+show+'').show();
    },
};
chatBot.stars();