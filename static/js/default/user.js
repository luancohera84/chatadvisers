var emailIngreso = '';
var img;
var ing = {
    stars: function() {
        this.carga();
    },
    carga() {
        var local = false;
        if (local) {
            $('#emailIngreso').val('');
            $('#emailIngreso').val(local.usuario);
            $('#passIngreso').focus()
        } else {
            $('#btnIngreso').click(function(event) {

                var emailIngreso = $('#emailIngreso').val();
                var passIngreso = $('#passIngreso').val();
                if (emailIngreso == '') {
                    swal.fire({
                        title: "Campo email vacío",
                        text: "Debe ingresar un email",
                        icon: "error",
                        showClass: {
                            popup: 'animate__animated animate__fadeInDown'
                          },
                          hideClass: {
                            popup: 'animate__animated animate__fadeOutUp'
                        },
                        customClass: 'swalTextTmna',
                        buttonsStyling: true,
                        confirmButtonText: "Revisar",
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        onDestroy:  $('#emailIngreso').focus()
                    }).then(( result ) => {
                        if (result) {}
                    });


                    return false;
                } else if (passIngreso == '') {
                    swal.fire({
                        title: "Campo password vacío",
                        text: "Debe ingresar un password",
                        icon: "error",
                        showClass: {
                            popup: 'animate__animated animate__fadeInDown'
                          },
                          hideClass: {
                            popup: 'animate__animated animate__fadeOutUp'
                        },
                        customClass: 'swalTextTmna',
                        buttonsStyling: true,
                        confirmButtonText: "Revisar",
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        onDestroy:  $('#passIngreso').focus()
                    }).then(( result ) => {
                        if (result) {}
                    });
                    return false;
                } else {
                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", true);
                    $('#btns_ingreso,#olvidePss').hide();
                    $('#validando').show();
                    $.post('../ingresoUsuario', { emailIngreso: emailIngreso, passIngreso: passIngreso }, function(data, textStatus, xhr) {

                        var dat = JSON.parse(data);
                        if (dat.vars_valores == 'usuario') {
                            swal.fire({
                                title: "Error",
                                text: "Email no encontrtado",
                                icon: "error",
                                showClass: {
                                    popup: 'animate__animated animate__fadeInLeft'
                                },
                                hideClass: {
                                    popup: 'animate__animated animate__fadeOutRight'
                                },
                                customClass: 'swalTextTmna',
                                buttonsStyling: true,
                                confirmButtonText: "Revisar",
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                onDestroy:  $('#passIngreso').focus()
                            }).then(( result ) => {
                                if (result) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso').show();
                                    $('#emailIngreso').focus();
                                }
                            });
                            return false;
                        } else if (dat.vars_valores == 'invalido') {
                            swal.fire({
                                title: "Error",
                                text: "Password Invalido",
                                icon: "error",
                                showClass: {
                                    popup: 'animate__animated animate__fadeInLeft'
                                },
                                hideClass: {
                                    popup: 'animate__animated animate__fadeOutRight'
                                },
                                customClass: 'swalTextTmna',
                                buttonsStyling: true,
                                confirmButtonText: "Revisar",
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                onDestroy:  $('#passIngreso').focus()
                            }).then(( result ) => {
                                if (result) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso').show();
                                    $('#passIngreso').focus();
                                }
                            });
                        } else if (dat.vars_valores == 'estado') {
                            swal.fire({
                                title: "Usuario Bloquedo",
                                text: "Comuniquese con su asesor",
                                icon: "error",
                                showClass: {
                                    popup: 'animate__animated animate__fadeInLeft'
                                },
                                hideClass: {
                                    popup: 'animate__animated animate__fadeOutRight'
                                },
                                customClass: 'swalTextTmna',
                                buttonsStyling: true,
                                confirmButtonText: "Revisar",
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                onDestroy:  $('#passIngreso').focus()
                            }).then(( result ) => {
                                if (result) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso').show();
                                    $('#passIngreso').focus();
                                }
                            });
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
                                title: 'Bienvenido(a) '+dat.vars_valores+'.'
                            });
                            setTimeout(function() {
                                window.location.href = '../../default/index';
                            }, 3001);
                        }
                    });
                }
            });
        }
    },
    limpiarSession: function() {
        localStorage.clear();
        location.reload();
    },

    ingresoSession: function() {
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        emailIngreso = local.usuario;
        var passIngreso = $('#passwordSession').val();
        if (passIngreso == '') {
            toastr.error('Campo password vacío', 'Debe ingresar un password', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#passIngreso').focus(); });
            return false;
        } else {
            $('#FormIngresoSession,#ingOtroUsuario').hide();
            $('#validandoSession').show();
            $.post('../ingresoUsuario', { emailIngreso: emailIngreso, passIngreso: passIngreso }, function(data, textStatus, xhr) {

                var dat = JSON.parse(data);
                if (dat.multi_valores == 'usuario') {
                    toastr.error('Error', 'Email no encontrtado', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#emailIngreso').focus(); });
                } else if (dat.multi_valores == 'invalido') {
                    toastr.error('Error', 'Password Invalido', { timeOut: 2000 }, toastr.options.onHidden = function() {

                        $('#validandoSession').hide();
                        $('#FormIngresoSession,#ingOtroUsuario').show();
                        $('#passwordSession').focus();
                    });
                }else if (dat.multi_valores == 'estado') {
                    toastr.error('Usuario Bloquedo. Comuniquese con su asesor.', 'Error', { timeOut: 10000 }, toastr.options.onHidden = function() {
                        $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                        $('#validando').hide();
                        $('#btns_ingreso').show();
                        $('#passIngreso').focus();
                    });
                } else {

                    if (typeof(Storage) !== "undefined") {
                        if ($('#inputCheckbox').is(':checked')) {
                            mi_objeto = {
                                usuario: emailIngreso,
                                nombres: dat.multi_valores,
                                img: dat.img
                            }
                            localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                            var local = JSON.parse(localStorage.getItem("datosUsuario"));
                            toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                        } else {
                            localStorage.clear();
                            toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                        }
                    } else {
                        toastr.info('Advertencia.', 'El navegador que está utilizando no soporta el recordar datos', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });

                    }
                }
            });
        }
    },

    mostrarPassword: function(){
        var cambio = document.getElementById("passIngreso");
        
        if(cambio.type == "password"){
            cambio.type = "text";
            $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
        }else{
            cambio.type = "password";
            $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
        }
    },

    mostrarPasswordAfter: function(){
        var cambio = document.getElementById("passwordSession");
        
        if(cambio.type == "password"){
            cambio.type = "text";
            $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
        }else{
            cambio.type = "password";
            $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
        }
    },
};
ing.stars();