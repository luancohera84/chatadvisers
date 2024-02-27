var usus = {
    usuLiColor: null,
    empresaLiColor: null,
    clienteLiColor: null,
    segmentoLiColor: null,
    nomUsuario: null,
    idUser: null,
    asigEmpresaAll: 1,
    asigEmpresaClSeg: 2,
    desAsigEmpresaAll: 0,
    nombreEmpresa: null,
    stars: function() {
        this.carga();
    },
    carga: function(){

    },
    verInfoUsuario: function( idUsers, nombreUsers, emailUsers ){
        $('#middle-usuarios').load('infoEmpresaUsuario',{idUsers,nombreUsers,emailUsers},function(){
            if ( parseInt(usus.usuLiColor) != parseInt(idUsers) ){
                $('#usuarioLi_'+usus.usuLiColor+'').css('background-color','');
                $('#usuarioLi_'+idUsers+'').css('background-color','#e8f9f8');
                usus.usuLiColor = idUsers;
            }
            template.usuarioSelCard   = $('#empresaSelCard').val();
            template.usuarioSelNombre = $('#empresaSelNombre').val();
            usus.nomUsuario = nombreUsers;
            usus.idUser = idUsers;
        });
    },
    questionAsigEmpresa( idEmpresa, idUser, tipo, iniEmpresa,nomEmpresa ){
        if ( parseInt(tipo) === usus.asigEmpresaAll ) {
            
            Swal.fire({
                title: 'Pregunta', 
                text:'Desea eliminar la empresa a este usuario', 
                icon: 'question',
                customClass: 'swalTextTmna',
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                },
                showCancelButton: true,
                confirmButtonText: 'Si',
                cancelButtonText: 'No',
    
            }).then((result) => {
                if (result.isConfirmed) {
                    usus.agregarUsuEmpresa( idEmpresa, idUser, usus.desAsigEmpresaAll, tipo, iniEmpresa,nomEmpresa );
                }else{
                    Swal.close();
                }
            });
        } else {
        
            Swal.fire({
                title: 'Confirmacion', 
                text:'Desea asignar todos los clientes y segmentos de esta empresa', 
                icon: 'question',
                customClass: 'swalTextTmna',
                confirmButtonText: 'Validar',
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                showClass: {
                    popup: 'animate__animated animate__fadeInLeft'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutRight'
                },
                showCancelButton: true,
                confirmButtonText: 'Si, todos',
                cancelButtonText: 'No, validar',
    
            }).then((result) => {
                if (result.isConfirmed) {
                    usus.agregarUsuEmpresa( idEmpresa, idUser, usus.asigEmpresaAll, tipo, iniEmpresa,nomEmpresa );
                }else{
                  //usus.agregarUsuEmpresa( idEmpresa, idUser, usus.asigEmpresaClSeg, tipo, iniEmpresa,nomEmpresa );
                  Swal.close();
                }
            });
        }
    },
    agregarUsuEmpresa: function( idEmpresa, idUser, opc,tipo, iniEmpresa, nomEmpresa ){
        template.showPreloader('Asignado empresa a usuario');
        // console.log('La opcion que recibo es: '+opc+' ', idEmpresa, idUser,+'tipo:'+' '+tipo);
        $.ajax({
            url: 'agregarUsuEmpresa',
            type: 'POST',
            dataType: 'json',
            data: {
                opc,
                idEmpresa,
                idUser,
                tipo
            }
        })
        .done(function(data) {
            // console.log('Dta', data);
            template.hidePreloader();
            if ( ( parseInt(tipo) === usus.asigEmpresaAll ) && ( parseInt(data) > usus.desAsigEmpresaAll ) ) {
                $('#empresUsuarioaDiv_'+idEmpresa+'_'+idUser+'').html('');
                const htmlLi = `
                    <li class="user-list-item" id="empresUsuarioaLi_`+idEmpresa+`_`+idUser+`" onclick="usus.questionAsigEmpresa( `+idEmpresa+`,`+idUser+`, `+usus.desAsigEmpresaAll+`,'`+iniEmpresa+`','`+nomEmpresa+`');">
                        <div>
                            <div class="avatar avatar-online">
                                <div class="letter-avatar">
                                    `+iniEmpresa+`
                                </div>
                            </div>
                        </div>
                        <div class="users-list-body">
                            <div>
                                <h5>`+nomEmpresa+`</h5>
                            </div>
                        </div>
                    </li>
                `;
                $('#empresUsuarioaDiv_'+idEmpresa+'_'+idUser+'').html(htmlLi);
                
            }else if ( ( parseInt(tipo) === usus.desAsigEmpresaAll ) && ( parseInt(data) > usus.desAsigEmpresaAll ) ) {
                $('#empresUsuarioaDiv_'+idEmpresa+'_'+idUser+'').html('');
                const htmlLi = `
                    <li class="user-list-item" id="empresUsuarioaLi_`+idEmpresa+`_`+idUser+`" onclick="usus.questionAsigEmpresa( `+idEmpresa+`,`+idUser+`, `+usus.asigEmpresaAll+`,'`+iniEmpresa+`','`+nomEmpresa+`');"  style='background-color:#e8f9f8;'>
                        <div>
                            <div class="avatar avatar-online">
                                <div class="letter-avatar">
                                    `+iniEmpresa+`
                                </div>
                            </div>
                        </div>
                        <div class="users-list-body">
                            <div>
                                <h5>`+nomEmpresa+`</h5>
                            </div>
                        </div>
                    </li>
                `;
                $('#empresUsuarioaDiv_'+idEmpresa+'_'+idUser+'').html(htmlLi);
            }else{
                Swal.fire({
                    title: 'Error', 
                    text:'No se pudo asignar la empresa a el usuario', 
                    icon: 'error',
                    customClass: 'swalTextTmna',
                    allowOutsideClick: false,
                    allowEscapeKey: false,
                    allowEnterKey: false,
                    showClass: {
                        popup: 'animate__animated animate__fadeInLeft'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOutRight'
                    }

                });
            }
            usus.verInfoUsuario( usus.idUser, usus.nomUsuario );
        });

    },
    verListadoEmpresas: function( idUser ){

        $('#bodyModalEmpresasUsuarios').load('getlistaEmpresas',{idUser}, function() {
            const myModal = new bootstrap.Modal('#listabodyModalEmpresasUsuarios', {
                keyboard: false,
                // backdrop: false,
            });
            myModal.show();
        });
    },
    verInfoClientes: function( idEmpresa, nomEmpresa, idUser ){
        $('#listClientesDiv').load('getlistaClientes',{idEmpresa,nomEmpresa,idUser},function(){
            if ( parseInt(usus.empresaLiColor) != parseInt(idEmpresa) ){
                $('#empresaAsigAsesor_'+usus.empresaLiColor+'').css('background-color','');
                $('#empresaAsigAsesor_'+idEmpresa+'').css('background-color','#e8f9f8');
                usus.empresaLiColor = idEmpresa;
            }else{
                console.log('Dice que es igual');
            }
            template.clienteSelCard   = $('#clienteSelCard').val();
            template.clienteSelNombre = $('#clienteSelNombre').val();
            usus.nombreEmpresa = nomEmpresa;
        });
    },
    asigSegmentoCliente: function( idEmpresa, idCliente, idSegmento, idUser, parmOpc ) {
        // console.log('asigSegmentoCliente idEmpresa =>>>', idEmpresa);
        // console.log('asigSegmentoCliente idCliente =>>>', idCliente);
        // console.log('asigSegmentoCliente idSegmento =>>>', idSegmento);
        // console.log('asigSegmentoCliente idUser =>>>', idUser);
        // console.log('asigSegmentoCliente parmOpc =>>>', parmOpc);
        const dat = {
            idEmpresa,
            idCliente,
            idSegmento,
            idUser,
            parmOpc
        }
        template.showPreloader('Asignado empresa a usuario');
        $.ajax({
            url: 'asigSegmentoClienteUsuario',
            type: 'POST',
            dataType: 'json',
            data: dat
        })
        .done(function(data) {
            template.hidePreloader();
            if ( parseInt(data) > 0 ){
                // console.log('dsataaa', data);
                usus.verInfoClientes( idEmpresa, usus.nombreEmpresa, idUser);
            }else{
                let textoSwal = 'Asignar';
                if ( parseInt(parmOpc)  === 1 ) {
                    textoSwal = 'Desasignar';
                }
                Swal.fire({
                    title: 'Error', 
                    text:'No se pudo '+textoSwal+' el cliente/segmento a el usuario. Intentalo nuevamente', 
                    icon: 'error',
                    customClass: 'swalTextTmna',
                    showClass: {
                        popup: 'animate__animated animate__fadeInLeft'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOutRight'
                    }

                });
            }
        });
    },
    cambioEstado: function( opc, idParm, estadoActual ){
        
    },
    agrergarUsuario: function(){
        if ( $('#nombreUusario').val() === '' ){
            template.validaCampo('Nombres usuario','nombreUusario');
            return false;
        } else if ( $('#apellidosUusario').val() === '' ){
            template.validaCampo('Apellidos usuario','apellidosUusario');
            return false;
        } else if ( $('#tipoUsuario').val() === '' ){
            template.validaCampo('Tipo usuario','tipoUsuario');
            return false;
        } else if ( $('#genero').val() === '' ){
            template.validaCampo('Genero','genero');
            return false;
        } else if ( $('#emailUsuario').val() === '' ){
            template.validaCampo('Email usuario','emailUsuario');
            return false;
        } else if ( $('#passwordUsuario').val() === '' ){
            template.validaCampo('Password usuario','passwordUsuario');
            return false;
        }else{
            const dat = {
                nombreUusario : $('#nombreUusario').val(),
                apellidosUusario : $('#apellidosUusario').val(),
                tipoUsuario : $('#tipoUsuario').val(),
                emailUsuario : $('#emailUsuario').val(),
                passwordUsuario : $('#passwordUsuario').val(),
                genero : $('#genero').val(),
            }
            template.showPreloader('Creando usuario');
            $('#btnAgregarUsuario').hide();
            $('#nombreUusario,#apellidosUusario,#tipoUsuario,#emailUsuario,#passwordUsuario,#genero').prop('disabled', true);
            $.ajax({
                url: 'agrergarUsuario',
                type: 'POST',
                dataType: 'json',
                data: dat
            })
            .done(function(data) {
                template.hidePreloader();
                if ( parseInt(data) > 0 ){
                    template.showSmsNew('Usuario');
                }else{
                    Swal.fire({
                        title: 'Error', 
                        text:'No se pudo crear el usuario. Intentalo nuevamente', 
                        icon: 'error',
                        customClass: 'swalTextTmna',
                        showClass: {
                            popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                            popup: 'animate__animated animate__fadeOutRight'
                        }

                    });
                    $('#btnAgregarUsuario').show();
                    $('#nombreUusario,#apellidosUusario,#tipoUsuario,#emailUsuario,#passwordUsuario,#genero').prop('disabled', false);
                }
                
            });
        }
    },

    
};
usus.stars();
