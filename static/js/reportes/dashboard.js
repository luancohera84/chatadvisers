var reps = {
    empresaLiColor: null,
	idEmpresa: null,
	nomEmpresa: null,
	fechaInicial: null,
	fechaFinal: null,
	fecInicial: null,
	fecFinal: null,
	pantallaGlb: null,
    stars: function() {
        this.carga();
		
    },
    carga: function(){
		reps.fechaInicial = $('#fechaInicial').pickadate().pickadate('picker');
		reps.fechaFinal   = $('#fechaFinal').pickadate().pickadate('picker');
		var date     = new Date();
		var anio     = date.getFullYear();
		var mes_name = date.getMonth();
		var mes_name = date.getMonth();
		$('#fechaInicial').pickadate({
			clear: false,
			weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
			showMonthsShort: false,
			max: new Date(anio,mes_name,date.getDate()),
			onClose: function() {
				reps.fecInicial = reps.fechaInicial.get('select','yyyy-mm-dd');
			},

		});
		$('#fechaFinal').pickadate({
			clear: false,
			weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
			showMonthsShort: false,
			min: new Date(anio,mes_name,1),
			max: new Date(anio,mes_name,date.getDate()),
			clear: false,
			onClose: function() {
				reps.fecFinal = reps.fechaFinal.get('select','yyyy-mm-dd');
					
			},

		});
		$('.picker__nav--next').hide();
	},
    verInfoEmpresa: function( idEmpresa, nomEmpresa ){
		reps.idEmpresa = idEmpresa;
		reps.nomEmpresa = nomEmpresa;
        $('#middle-empresas').load('cuerpoReportEmpresa',{idEmpresa,nomEmpresa},function(){
            if ( parseInt(reps.empresaLiColor) != parseInt(idEmpresa) ){
                $('#empresaLi_'+reps.empresaLiColor+'').css('background-color','');
                $('#empresaLi_'+idEmpresa+'').css('background-color','#e8f9f8');
                reps.empresaLiColor = idEmpresa;
            }
            // $('#tableAsesoresAsig').DataTable({
            //     "responsive": true,
	        //     "autoWidth": true,
	        //     "ordering": true,
	        //     "order": [
	        //         [1, "des"]
	        //     ],
	        //     info: true,
	        //     paging: true,
	        //     "scrollY": "380px",
	        //     "scrollCollapse": true,
	        //     language: {
	        //         "decimal": "",
	        //         "emptyTable": "No hay información",
	        //         "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
	        //         "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
	        //         "infoFiltered": "(Filtrado de _MAX_ total entradas)",
	        //         "infoPostFix": "",
	        //         "thousands": ",",
	        //         "lengthMenu": "Mostrar _MENU_ Entradas",
	        //         "loadingRecords": "Cargando...",
	        //         "processing": "Procesando...",
	        //         "search": "Buscar:",
	        //         "zeroRecords": "Sin resultados encontrados",
	        //         "paginate": {
	        //             "first": "Primero",
	        //             "last": "Ultimo",
	        //             "next": "Siguiente",
	        //             "previous": "Anterior"
	        //         }
	        //     },
            // });            
            template.empresaSelCard   = $('#empresaSelCard').val();
            template.empresaSelNombre = $('#empresaSelNombre').val();
			reps.cargaInfoDashReporte();
        });
    },
	cargaInfoDashReporte: function(){
		reps.chatsAtendidos();
		reps.chatsCola();
		reps.chatsPromAtencion();
		reps.chatsAcuerdos();
		reps.chatsListAsesores();
	},
	chatsAtendidos: function(){
		$.ajax({
			url: 'cargaChatAsignacion',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa},
		})
		.done(function( data ) {
			$('#idSpinerChatAtencion').hide();
			$('#idSpanValoresChatAtencion').html('<b>'+data.cantidadCerrados+'/'+data.cantidadAsig+'</b>');
		});
	},
	chatsCola: function(){
		$.ajax({
			url: 'cargaChatCola',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa},
		})
		.done(function( data ) {
			// console.log("success", data);
			$('#idSpinerChatCola').hide();
			$('#idSpanValoresChatCola').html('<b>'+data.cantidadCola+'/'+data.cantidadAsig+'</b>');
		});
	},
	chatsPromAtencion: function(){
		$.ajax({
			url: 'cargaPromedioAtencion',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa}
		})
		.done(function( data ) {
			var promedio = (parseFloat(data)*60)/60;
			if (promedio < 0) {
				promedio = promedio * -1;
			} else {
				promedio = promedio;
			}
			$('#idSpinerChatPromAtencion').hide();
			$('#idSpanValoresChatPromAtencion').html('<b>'+promedio+' Minutos</b>');
		});
	},
	chatsAcuerdos: function(){
		$.ajax({
			url: 'cargaAcuerdos',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa}
		})
		.done(function( data ) {
			// console.log("success", data);
			$('#idSpinerChatAcPago').hide();
			$('#idSpanValoresChatAcPago').html('<b>'+data+'</b>');
		});
	},
	chatsListAsesores: function(){
		// console.log('idEmpresa => chatsListAsesores', reps.idEmpresa);
		// console.log('nomEmpresa => chatsListAsesores', reps.nomEmpresa);
		$.ajax({
			url: 'cargaListaAsesorAtencion',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa}
		})
		.done(function( data ) {
			// console.log("success", data);
			$('#idSpinerChatListAsesores').hide();
			$('#idDivTableListAsesores').show();
			var dataHtml = [];
			$.each(data, function(index, val) {
				var varTmp = `
					<tr>
						<td>`+val.asesor+`</td>
						<td class="text-center">`+val.cerrados+`</td>
						<td class="text-center">`+val.inCola+`</td>
						<!--td class="text-center">`+val.acuerdos+`</td-->
						<td class="text-center">`+val.fHOldGes+`</td>
					</tr>
				`;
				dataHtml.push(varTmp);
			});
			$('#idTbodyListAsesores').html(dataHtml);
			$('#tableAsesoresAsig').DataTable({
                "responsive": true,
                "autoWidth": true,
                "ordering": true,
                "order": [
                    [0, "asc"]
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
			// $('#tableAsesoresAsig').DataTable();`
		});
	},
	cambioPantalla:function( pantalla, hide, show ){
		$('#'+hide+'').hide(function(){
			$('#'+show+'').show(function(){
				if ( reps.pantallaGlb === 'gestiones' ) {
					$('#btnFechas').removeClass('btnBuscar');
					$('#btnAsignacion').addClass('btnBuscar');
				} else if (reps.pantallaGlb === 'asignacion'){
					$('#btnAsignacion').removeClass('btnBuscar');
					$('#btnFechas').addClass('btnBuscar');
					reps.carga();
				}else{
					if (pantalla === 'gestiones') {
						$('#btnAsignacion').removeClass('btnBuscar');
						$('#btnFechas').addClass('btnBuscar');
						reps.cargaGestionAsig();
					}
				}
				reps.pantallaGlb = pantalla;
			})
		});

	},
	cargaGestionAsig: function() {
		$('#idDivBodyGestionesAsig').html('');
		$('#idDivBodyGestionesAsig').show();
		$('#idDivBodyGestionesAsig').load('gestionesAsig',{idEmpresa:reps.idEmpresa,nomEmpresa:reps.nomEmpresa},function(){
			$('#idSpinerGestionesListAsesores').hide();
			$('#tableGestionesAsig').DataTable({
		        "responsive": true,
		        "autoWidth": true,
		        "ordering": true,
		        "order": [
		            [4, "des"]
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
		        // dom: 'Bfrtip',
		        // buttons: [
		        //     'copyHtml5',
		        //     'excelHtml5',
		        //     'csvHtml5',
		        //     'pdfHtml5'
		        // ]

		    });
		});
	},
	verChats: function( idCliente,nombreCliente, idEmpresa, phone ){
		template.showPreloader('Cargando chat '+nombreCliente+'');
        window.location.href = "../reportes/chatClienteGestion?nCustomer="+nombreCliente+"&nPhone="+phone+"&numberCustomer="+idCliente+"&numberCompany="+idEmpresa+"";
	},
	buscarReporte:function(){
		reps.fecInicial = reps.fechaInicial.get('select','yyyy-mm-dd');
		reps.fecFinal   = reps.fechaFinal.get('select','yyyy-mm-dd');
		if ( reps.fecInicial === '' ) {
			Swal.fire({
				title: 'Campo Fecha inicial vacío',
				text: 'Debe selecionar una fecha de inicio',
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
			});
		} else if ( reps.fecFinal === '' ){
			Swal.fire({
				title: 'Campo Fecha final vacío',
				text: 'Debe selecionar una fecha de final',
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
			});
		}else{
			$('#fechaInicial,#fechaFinal').attr('disabled',true);
			$('.btnBuscar').addClass('disabled');
			const Toast = Swal.mixin({
				toast: true,
				position: 'top-end',
				showConfirmButton: false,
				timer: 7000,
				timerProgressBar: true,
				didOpen: (toast) => {
					toast.addEventListener('mouseenter', Swal.stopTimer)
					toast.addEventListener('mouseleave', Swal.resumeTimer)
				}
			});
			Toast.fire({
				icon: 'success',
				title: 'Información',
				text: 'Iniciaremos con la creación de tu reporte. Por favor no recargues la pagina hasta que terminemos.'
			})
			setTimeout(function() {
				$.ajax({
					url: 'buscarReporte',
					type: 'POST',
					dataType: 'json',
					data: {fecInicial: reps.fecInicial,fecFinal: reps.fecFinal,idEmpresa: reps.idEmpresa, nomEmpresa: reps.nomEmpresa},
				});
				setTimeout(function() {
					var datosHtml = `
						<p align="center" style="font-size:13px;text-align:center;overflow: hidden;">
							<b>Un momento por favor <br>Estamos construyendo tu reporte.</b>
							<br><br>
							<i class="fa fa-spinner fa-spin"  style="font-size:25px;color:#5A078B;text-align:center;"></i>
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
				},100);
			}, 7001);
		}
		
	},
	limpiarReporte: function(){
		$('#fechaInicial,#fechaFinal').val('');
	},
	degargarGestgion: function(){
		template.showPreloader('Descargando gestión');
		$.ajax({
			url: 'buscarReporte',
			type: 'POST',
			dataType: 'json',
			data: {idEmpresa:reps.idEmpresa,nomEmpresa:reps.nomEmpresa},
		}).done(function(data) {
			template.hidePreloader();
			if (data.file != '') {
				window.location.href='../static/multimedia/'+data.file+'';
				setTimeout(function() {reps.limpiarRep(data.file)}, 10000);
			}else{
				Swal.fire({
		            title: 'Información',
		            text: 'No eres tu somos nostros, tenemos problemas para descargar tu gestión.',
		            icon: 'warning',
		            confirmButtonText: 'Entiendo',
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
	},
	limpiarRep: function( file ) {
		$.ajax({
			url: 'limpiarReporte',
			type: 'POST',
			dataType: 'json',
			data: {file},
		});
	}, 
};
reps.stars();
