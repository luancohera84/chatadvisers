var currentTime = new Date();
var template = {
    idEmpresaTemplate: $('#idEmpresaTemplate').val() || 0,
    idUsersTemplate: $('#idUsersTemplate').val() || 0,
    chatServicio: $('#chatServicio').val() || 0,
    imagenAsesor: $('#imagenAsesor').val() || '',
    nombreAsesor: $('#nombreAsesor').val() || 'Asesor sin nombre',
    horaActual:  currentTime.getHours()+':'+currentTime.getMinutes()+':'+currentTime.getSeconds(),
    fechaActual: currentTime.getFullYear()+'-'+(currentTime.getMonth() + 1)+'-'+currentTime.getDay(),
    estadoFin: 'Fuera-linea',
    idParamGlb: null,
    empresaSelCard :null,
    empresaSelNombre:null,
    clienteSelCard :null,
    clienteSelNombre:null,
    usuarioSelCard :null,
    usuarioSelNombre:null,
    textChatAsesor:null,
    // 1445
    stars: function() {
        this.carga();
    },
    carga() { 
        if ( parseInt(template.chatServicio) > 0 ) {
            template.showPreloader('Tines una conversacion en proceso.');
            $.ajax({
                url: '../template/chatServicio',
                type: 'GET',
                dataType: 'json',
                data: {idClientePlaf: template.chatServicio}
            })
            .done(function(data) {
                console.log('data =>', data);
                window.location.href = "../asesor/listaChatEmpresa?prem="+data[0].idEmpresa+"&atrg="+data[0].idUser+"&mena="+data[0].empresa+"";
            });
        }

        // var DELAY = 700,
        // clicks = 0,
        // timer = null;
        // $("textarea").bind("click", function(e){
        //     console.log('Cliccccckkkk');
        //     clicks++;  //count clicks

        //     if(clicks === 1) {

        //         timer = setTimeout(function() {

        //             alert('Single Click'); //perform single-click action

        //             clicks = 0;  //after action performed, reset counter

        //         }, DELAY);

        //     } else {

        //         clearTimeout(timer);  //prevent single-click action

        //         alert('Double Click');  //perform double-click action

        //         clicks = 0;  //after action performed, reset counter
        //     }

        // })
        // .bind("dblclick", function(e){
        //     e.preventDefault();  //cancel system double-click event
        // });
    },
    avisoDeLogaut: function() {
        Swal.fire({
            title: 'Aviso.!',
            text: '¿Desea cerrar la sesión?',
            icon: 'info',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si',
            cancelButtonText: 'No',
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
        }).then((result) => {
            if (result.value) {
                template.cambioEstado(template.estadoFin, template.idUsersTemplate, template.idEmpresaTemplate);
            }
        });
    },
    // 6015878009
    cambioEstado: function(estado, idUser, idEmpresa) {
        template.showPreloader('Cerrando session...');
        $.ajax({
            url: '../template/cambioEstado',
            type: 'GET',
            dataType: 'json',
            data: {
                estado,
                idUserClt: idUser,
                empresaClt: idEmpresa
            }
        })
        .done(function(data) {
            if (parseInt(data) > 0) {
                window.location.href = "../default/user/logout";
            } else {
                Swal.fire({
                    title: 'Información', 
                    text:'No se pudo cerrar la session. Intentalo nuevamente', 
                    icon: 'warning',
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
        });
    },
    showPreloader: function(txt) {
        var datosHtml = `
            <p align="center" style="font-size:13px;text-align:center;overflow: hidden;">
                <b>Un momento por favor <br>` + txt + `</b>
                <br><br>
                <i class="fa fa-spinner fa-spin"  style="font-size:35px;color:#5A078B;text-align:center;"></i>
            </p>
        `;
        Swal.fire({
            html: datosHtml,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
            showDenyButton: false,
            showCancelButton: false,
            showConfirmButton: false,
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutRight'
            }
        });
    },
    hidePreloader: function() {
        Swal.close();
    },
    updateEstado: function( opc, idParm, estadoActual ) {
        Swal.fire({
            title: "El estado se modificara!",
            text: "Esta seguro de continuar el proceso?",
            icon: "info",
            showCancelButton: true,
            cancelButtonText: "Cancelar",
            confirmButtonColor: "#007bff",
            confirmButtonText: "Si, continuar",
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
        }).then((result) => {
            if (result.value) {
                template.showPreloader('Modificando su estado');
                $.ajax({
                    url: '../template/updateEstado',
                    type: 'GET',
                    dataType: 'json',
                    data: {
                        opc,
                        idParm,
                        estadoActual,
                        empresaSelCard:template.empresaSelCard
                    }
                })
                .done(function(data) {

                    if ( ( opc === 'empresa' ) & ( parseInt(data) > 0 ) ){
                        template.hidePreloader();
                        template.showSmsUpdate('Estado Empresa');
                    } else if( ( opc === 'cliente' ) & ( parseInt(data) > 0 ) ){ 
                        template.hidePreloader();
                        emp.verInfoEmpresa( template.empresaSelCard, template.empresaSelNombre);
                    } else if( ( opc === 'segmento' ) & ( parseInt(data) > 0 ) ){ 
                        template.hidePreloader();
                        emp.verInfoCliente( template.clienteSelCard, template.clienteSelNombre);
                    } else if( ( opc === 'usuario' ) & ( parseInt(data) > 0 ) ){ 
                        template.hidePreloader();
                        template.showSmsUpdate('Estado Usuario');
                    } else if( ( opc === 'horario' ) & ( parseInt(data) > 0 ) ){ 
                        template.hidePreloader();
                        let htmlLet = `
                            <i class="fas fa-thumbs-up fa-2x text-success"></i>
                            <p align='center' style='padding-top:-20px;'>
                            <b> Hirario eliminado con exito.</b>
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
                    } else if( ( opc === 'smsPrest' ) & ( parseInt(data) > 0 ) ){ 
                        template.hidePreloader();
                        let htmlLet = `
                            <i class="fas fa-thumbs-up fa-2x text-success"></i>
                            <p align='center' style='padding-top:-20px;'>
                            <b> Sms eliminado con exito.</b>
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
                        Swal.fire('Información', 'No se pudo modificar el estado. Intentalo nuevamente', 'warning');
                    }
                });
            }
        });
    },
    showSmsUpdate: function( text ){
        let htmlLet = `
            <i class="fas fa-thumbs-up fa-2x text-success"></i>
            <p align='center' style='padding-top:-20px;'>
               <b> `+text+`, modificado con exito</b>
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
            window.location.href = "";
        }, 2000);
    },
    showSmsNew: function( text ){
        Swal.fire({
            title:'Información', 
            text:''+text+' creado con exito', 
            icon:'info',
            showCancelButton: false,
            showConfirmButton:false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,

        });
        setTimeout(function(){
            window.location.href = "";
        }, 4000);
    },
    showModal: function( modalId, title, idPar ){
        template.idParamGlb = idPar;
        $('#headerEditEmpresa').html('<span><i class="far fa-edit"></i></span> '+title+' ');
        $('#headerEditCliente').html('<span><i class="far fa-edit"></i></span> '+title+' ');
        $('#headerEditSegmento').html('<span><i class="far fa-edit"></i></span> '+title+' ');
        $('#headerEditUsuario').html('<span><i class="far fa-edit"></i></span> '+title+' ');
        const myModal = new bootstrap.Modal('#'+modalId+'', {
            keyboard: false,
            // backdrop: false,
        });
        myModal.show(function(){
            $('#nombreEmpresaUp,#nombreClienteUp,nombreSegmentoUp').focus();
        });

    },
    validaCampo(selector, campo) {
        Swal.fire({
            title: 'Advertencia',
            text: 'Campo ' + selector + ' vacío',
            icon: 'warning',
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
                $('#' + campo + '').trigger('focus');
            }
        });
    },
    updateNombre: function( opc, nombreCambioParm ){
        let nombreCambioPaVal = $('#'+nombreCambioParm+'').val();
        if ( nombreCambioPaVal === '' ){
            template.validaCampo('Nombre',''+nombreCambioParm+'');
            return false;
        }else{
            template.showPreloader('Modificando su nombre');
            $.ajax({
                url: '../template/updateNombre',
                type: 'GET',
                dataType: 'json',
                data: {
                    opc,
                    idParm:template.idParamGlb,
                    nombreCambioPaVal
                }
            })
            .done(function(data) {
                $('#'+nombreCambioParm+'').val('');
                if ( ( opc === 'empresa' ) & ( parseInt(data) > 0 ) ){
                    template.hidePreloader();
                    template.showSmsUpdate('Nombre Empresa');
                } else if( ( opc === 'cliente' ) & ( parseInt(data) > 0 ) ){ 
                    template.hidePreloader();
                    $('.modal').modal('hide');
                    emp.verInfoEmpresa( template.empresaSelCard, template.empresaSelNombre);
                } else if( ( opc === 'segmento' ) & ( parseInt(data) > 0 ) ){ 
                    template.hidePreloader();
                    $('.modal').modal('hide');
                    emp.verInfoCliente( template.clienteSelCard, template.clienteSelNombre);
                } else if( ( opc === 'usuario' ) & ( parseInt(data) > 0 ) ){ 
                    template.hidePreloader();
                    template.showSmsUpdate('Nombre/Email Usuario');
                }else{
                    Swal.fire({
                        title: 'Información', 
                        text:'No se pudo modificar el estado. Intentalo nuevamente', 
                        icon: 'warning',
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
                }
            });
        }
    },
    updateUsers: function(){
        let emailUsuarioUp = $('#emailUsuarioUp').val();
        let passwordUsuarioUp = $('#passwordUsuarioUp').val();
        if ( ( emailUsuarioUp === '' ) && ( passwordUsuarioUp === '' ) ){
            template.validaCampo('Email/Password','emailUsuarioUp');
            return false;
        }else{
            template.showPreloader('Modificando email/password');
            $.ajax({
                url: '../template/updateNombre',
                type: 'GET',
                dataType: 'json',
                data: {
                    opc:'usuario',
                    idParm:template.idParamGlb,
                    emailUsuarioUp,
                    passwordUsuarioUp
                }
            })
            .done(function(data) {
                $('#emailUsuarioUp,#passwordUsuarioUp').val('');
                if( parseInt(data) > 0  ){ 
                    template.hidePreloader();
                    template.showSmsUpdate('Email/Password Usuario');
                } else if( parseInt(data) === 0  ){
                    Swal.fire({
                        title: 'Error', 
                        text:'Email ingresado ya esta registrado', 
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
                }else{
                    Swal.fire({
                        title: 'Información', 
                        text:'No se pudo modificar el estado. Intentalo nuevamente', 
                        icon: 'warning',
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
            });
        }
    },
    monedaNumber: function( numberVal, cod_pais, cog_moneda ){
        numerResul = 0;
        if( numberVal ){
            numerResul = new Intl.NumberFormat(cod_pais, { style: 'currency', currency: cog_moneda,maximumSignificantDigits: 20  }).format(numberVal);
        }
        return numerResul
    },
    searchClientesList: function() {
        var input, filter, section, div, h1, i;
        input = document.getElementById("searchClienteListado");
        filter = input.value.toUpperCase();
        section = document.getElementById("chatsidebar");
        div = section.getElementsByTagName("li");
      
      
      
        for (i = 0; i < div.length; i++) {
          h1 = div[i].getElementsByTagName("h5")[0];
          if (h1) {
            var palabrasEnFiltro = filter.split(' ');
            var hallado = 0;
            for (var filtro of palabrasEnFiltro) {
              if (h1.innerHTML.toUpperCase().indexOf(filtro) > -1) {
                hallado++;
              }
            }
      
            if (hallado === palabrasEnFiltro.length) {
              div[i].style.display = "";
            } else {
              div[i].style.display = "none";
            }
      
          }
        }
      
    },
    getMessages: function() {
        const el = document.getElementsByClassName('slimscroll');
        $.each(el, function(index, val) {
            el[index].scrollTop = el[index].scrollHeight;
        });
    },
    hideModal: function( idModal ){
        ger.myModal.hide();
        $('#'+idModal+'').hide();
    },
};
template.stars();