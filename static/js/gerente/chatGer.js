var chatGer = {
    URL: 'https://chatadvisers.intelibpo.com/init/static/contextosChatbot/',
    stars: function() {
        this.carga();
    },
    carga: function(){},
    changeStatus: function( idContxChatbot, nombreContexto, idSegmento, status ){

    },
    verNodosContexto: function( idContxChatbot, nombreContexto, idSegmento, nomJson ) {
        $('#divRegistrosContextos').hide('slow/400/fast', function() {
            $('#divBodyNodosContextos').show('slow/400/fast', function() {
                var a = document.getElementById('aHrefLessJson'); //or grab it by tagname etc
                a.href = chatGer.URL+nomJson;
                $('#nombreContexChatBot').html(nombreContexto);
                $('#bodyNodos').html('');
                $('#bodyPreloadsCuerpoContextoChatBot').show();
                $.ajax({
                    url: 'verNodosContexto',
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
                                    <div class="col col-lg-3">
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
                                    <div class="col col-lg-3">
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
                                url: 'resultadoHomologa',
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
    showPasoToPasoAeditarContexto: function() {
        
    },
};
chatGer.stars();