var rTime = {
    start: function() {
        this.carga()
    },
    carga() {
        // rTime.notifyMe('Buenas esta es my notificacion');
        // rTime.newCompanyInfo(6,'Fundamujer','20220811','231011');
    },
    conRt: function(url) {
        console.log('url =>', url);
        try {
            rTime.websocket(url, function(e) { eval(e.data) });
        } catch (error) {
            console.error(error);
            // expected output: ReferenceError: nonExistentFunction is not defined
            // Note - error messages will vary depending on browser
        }
    },
    websocket: function(url, onmessage, onopen, onclose) {
        // console.log('url =>', url);
        if ("WebSocket" in window) {
            var ws = new WebSocket(url);
            ws.onopen = onopen ? onopen : (function() {});
            ws.onmessage = onmessage;
            ws.onclose = onclose ? onclose : (function() {});
            return true; /* supported */
        } else return false; /* not supported */
    },
    notifyMe: function( title, text )  {
        if  (!("Notification"  in  window))  {   
            alert("Este navegador no soporta notificaciones de escritorio");  
        }else  if  (Notification.permission  ===  "granted")  {
            // console.log('Permiso consedido');
            const  options  =   {
                body:   text,
                icon:   "https://chatadvisers.intelibpo.com/init/static/images/cropped-favicon2-32x32.png",
                dir :   "ltr"
            };
            // console.log('permission', permission);
            // console.log('options', options);
            const  notification  =  new  Notification(title, options);
            // notification.onclick = function() {
            //     window.open("https://chatadvisers.intelibpo.com/");
            // };
            // console.log('notification', notification);
            // notificatio
            // notification.onclick = function () {
            //     window.location.href = 'https://chatadvisers.intelibpo.com';
            // }
        } else  if  (Notification.permission  !==  'denied')  {
            console.log('Permiso denegado');
            Notification.requestPermission(function (permission)  {
                if  (!('permission'  in  Notification))  {
                    Notification.permission  =  permission;
                }
                console.log('permission', permission);
                if  (permission  ===  "granted")  {
                    const  options  =   {
                        body:   "Descripción o cuerpo de la notificación",
                        icon:   "https://chatadvisers.intelibpo.com/init/static/images/cropped-favicon2-32x32.png",
                        dir :   "ltr"
                    };     
                    const  notification  =  new  Notification("Hola :)", options);
                    notification.onclick = function() {
                        window.open("https://chatadvisers.intelibpo.com/");
                    };
                }   
            });  
        }else{
            console.log('Ninguna de las anteriores');
        }
    },
    newCompanyInfo: function( idEmpresa, nombreEmpresa, fechaCreacion, horaCreacion ){
        rTime.notifyMe('Empresa '+nombreEmpresa+' creada...');
        const htmlEmpresa = `
            <li class="user-list-item" id="empresaLi_`+idEmpresa+`">
                <div>
                    <div class="avatar avatar-online">
                        <div class="letter-avatar" onclick="emp.verInfoEmpresa( '`+idEmpresa+`','`+nombreEmpresa+`' )">
                            `+nombreEmpresa.charAt(0)+`
                        </div>
                    </div>
                </div>
                <div class="users-list-body">
                    <div>
                        <h5>`+nombreEmpresa+`</h5>
                        <p><span class="material-icons">check_circle</span>  `+fechaCreacion+` | `+horaCreacion+`</p>
                    </div>
                    <div class="chat-action-btns me-2">
                        <div class="chat-action-col">
                            <a class="#" href="#" data-bs-toggle="dropdown">
                                <i class="fas fa-ellipsis-h"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-end">
                                <a href="javascript:template.showModal('edicionEmpresa','`+nombreEmpresa+`','`+idEmpresa+`');" class="dropdown-item dream_profile_menu">Editar <span><i class="far fa-edit"></i></span></a>
                                <a href="javascript:template.updateEstado('empresa','`+idEmpresa+`',1)" class="dropdown-item">Inactivar <span><i class="far fa-thumbs-down"></i></span></a>
                            </div>
                        </div>
                    </div>
                </div>
            </li>
        `;
        $('#listaEmpresas').append(htmlEmpresa);
    },
    newSmsAsesor: function( cliAdvOnLine,idClientePlf, idAdviser, sms, idEmpresa, tipoSms, nombreCliente, cantSms, tiempoSms ){
        if (parseInt( cliAdvOnLine ) > 0 ) {
            // let tmpHtml = `
            //     <div class="chats">
            //         <div class="chat-avatar">
            //             <img src="../static/template/base/assets/img/logo.png" class="rounded-circle dreams_chat" alt="image">
            //         </div>
            //         <div class="chat-content">
            //             <div class="message-content">
            //                 `+sms.toString()+`
            //                 <div class="chat-time">
            //                     <div>
            //                         <div class="time"><i class="fas fa-clock"></i> `+template.horaActual+`</div>
            //                     </div>
            //                 </div>
            //             </div>
            //             <div class="chat-profile-name">
            //                 <h6>`+nombreCliente+`</h6>
            //             </div>
            //         </div>
            //     </div>
            //     <br><br>
            // `;
            // $('#idBodySmsConversacion').append(tmpHtml);
            if (ases.formulario) {
                var formulario = ases.formulario;
            } else {
                var formulario = 'formularioEncvioSms';
            }
            console.log('FORMULARIO =>', formulario);
            ases.verInfoChatCliente( ases.idClienteGlb, ases.idClientHstGlb, ases.idEmpresaGlb, template.idUsersTemplate, ases.nombreClienteGlb, formulario );
            const music = new Audio('../static/sonido/sonido_sms.mp3');
            music.play();
        } else {
            rTime.notifyMe('Nuevo mensaje','Tienes un nuevo mensaje, valida tu bandeja de chats');
        }
        $('#indicadorSmsCantidadTiempo_'+idClientePlf+'').html(`
            <small class="text-muted">`+tiempoSms+`</small>
            <div class="new-message-count">`+cantSms+`</div>
        `);
        template.getMessages();
    },
    newAsignacionClienteAsesor: function( idClientePlf, idAdviser ){
        rTime.notifyMe('Nueva asignacion','Tienes un nuevo cliente para atender, valida tu bandeja de chats');
        $('#idDivUlEmpresasChatAsesor_'+idAdviser+'').load('../asesor/listaEmpresasAsesor',{idUser: idAdviser});
    },
    
};
rTime.start();