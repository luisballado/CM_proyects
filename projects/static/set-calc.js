function calculateSets(){

    resultados = document.getElementById("set-results");
        
    console.log('Hola Mundo Cruel');

    var resultsContainer = document.getElementById("set-results");
    resultsContainer.style.display = "block";

    //Scroll a los resultados
    resultados.scrollIntoView();

    var conjunto1 = document.getElementById("conjunto1").value;
    var conjunto2 = document.getElementById("conjunto2").value;


    //--- resultados ----
    //unary data
    var d_conjunto_A = document.getElementById("display_conjuntoA")
    var d_conjunto_B = document.getElementById("display_conjuntoB")
    var cardinalidad_A = document.getElementById("cardinalidad_A")
    var cardinalidad_B = document.getElementById("cardinalidad_B")
    var power_A = document.getElementById("power_A")
    var power_B = document.getElementById("power_B")
    var partitions_A = document.getElementById("partitions_A")
    var partitions_B = document.getElementById("partitions_B")

    //binary data
    var comparision_AB = document.getElementById("comparision_AB")
    var subset_AB = document.getElementById("subset_AB")
    var subset_BA = document.getElementById("subset_BA")
    var proper_subset_AB = document.getElementById("proper_subset_AB")
    var proper_subset_BA = document.getElementById("proper_subset_BA")
    var difference_AB = document.getElementById("difference_AB")
    var difference_BA = document.getElementById("difference_BA")
    var symmetric_diff_AB = document.getElementById("symmetric_diff_AB")
    var symmetric_diff_BA = document.getElementById("symmetric_diff_BA")
    var union_AB = document.getElementById("union_AB")
    var interseccion_AB = document.getElementById("interseccion_AB")
    var interseccion_disjoint = document.getElementById("interseccion_disjoint")
    var cartesian_product_AB = document.getElementById("cartesian_product_AB")
    var cartesian_product_BA = document.getElementById("cartesian_product_BA")
    
    //-------------------
    //console.log(conjunto1);
    //console.log(conjunto2);

    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2
    };
    
    $.ajax({
	type: "POST",
	url: "/calc_sets",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    d_conjunto_A.innerHTML = result.unary_op[0]['A'];
	    d_conjunto_B.innerHTML = result.unary_op[0]['B'];
	    cardinalidad_A.innerHTML = result.unary_op[1]['operation']['A'];
	    cardinalidad_B.innerHTML = result.unary_op[1]['operation']['B'];
	    power_A.innerHTML = JSON.stringify(Object.values(result.unary_op[2]['operation']['A']));
	    power_B.innerHTML = JSON.stringify(Object.values(result.unary_op[2]['operation']['B']));
	    
	    partitions_A.innerHTML = result.unary_op[3]['operation']['A'];
	    partitions_B.innerHTML = result.unary_op[3]['operation']['B'];

	    if(result.binary_op[0]['operation'] == 'False'){
		comparision_AB.innerHTML = '<p style="color:Tomato;font-size: 24px">&#10007;</p>'
	    }else{
		comparision_AB.innerHTML = '<p style="color:Green;font-size: 24px">&#10003;</p>'
	    }
	    
	    subset_AB.innerHTML = result.binary_op[1]['operation']['AB'];
	    subset_BA.innerHTML = result.binary_op[1]['operation']['BA'];
	    proper_subset_AB.innerHTML = result.binary_op[2]['operation']['AB'];
	    proper_subset_BA.innerHTML = result.binary_op[2]['operation']['BA'];
	    difference_AB.innerHTML = result.binary_op[3]['operation']['AB'];
	    difference_BA.innerHTML = result.binary_op[3]['operation']['BA'];
	    symmetric_diff_AB.innerHTML = result.binary_op[4]['operation']['AB'];
	    symmetric_diff_BA.innerHTML = result.binary_op[4]['operation']['BA'];
	    union_AB.innerHTML = result.binary_op[5]['operation'];
	    interseccion_AB.innerHTML = result.binary_op[6]['operation'];

	    if(result.binary_op[6]['disjoint'] == 'True'){
		interseccion_disjoint.innerHTML = '<a style="color:Green;font-size: 24px">&#10003;</a>'
	    }else{
		interseccion_disjoint.innerHTML = '<a style="color:Tomato;font-size: 24px">&#10007;</a>'
	    }
	    
	    cartesian_product_AB.innerHTML = result.binary_op[7]['operation']['AB'];
	    cartesian_product_BA.innerHTML = result.binary_op[7]['operation']['BA'];
	} 
    });
}

function calc_relations(){

    resultados2 = document.getElementById("set-results2");
    
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    console.log(conjunto1);
    console.log(conjunto2);
    //console.log("Relaciones");

    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2,
	"calculation":"relations"
    };
    var caption_txt = document.getElementById("type")
    caption_txt.innerHTML = "Lista de Relaciones";
    $.ajax({
	type: "POST",
	url: "/calc_functions",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    $('#table1').html('');
	    console.log(result);
	    var row_data = '';
	    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
	    let count = 1;
	    for (var arr in result){
		var obj = result[arr];
		
		row_data += '<tr>';
		
		row_data += '<th scope="row">' + count + '</th>';
		row_data += '<td>' + obj['relation'] + '</td>';
		if (obj['is_relation'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_function'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_inyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_suprayective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_biyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		
		row_data += '</tr>'
		count = count + 1;
	    };
	    $('#table1').append(row_data);
	    
	    var resultsContainer2 = document.getElementById("set-results2");
	    resultsContainer2.style.display = "block";
	    
	    //Scroll a los resultados
	    resultados2.scrollIntoView();
	}
    });
    
    var resultsContainer2 = document.getElementById("set-results2");
    resultsContainer2.style.display = "block";

    //Scroll a los resultados
    resultados2.scrollIntoView();
    
    
}

function calc_funciones(){
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    console.log(conjunto1);
    console.log(conjunto2);
    //console.log("Funciones");

    resultados2 = document.getElementById("set-results2");
    
    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2,
	"calculation":"functions"
	
    };

    var caption_txt = document.getElementById("type")
    caption_txt.innerHTML = "Lista de Funciones";
    
    $.ajax({
	type: "POST",
	url: "/calc_functions",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    $('#table1').html('');
	    console.log(result);
	    var row_data = '';
	    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
	    let count = 1;
	    for (var arr in result){
		var obj = result[arr];
		
		row_data += '<tr>';
		
		row_data += '<th scope="row">' + count + '</th>';
		row_data += '<td>' + obj['relation'] + '</td>';
		if (obj['is_relation'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_function'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_inyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_suprayective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_biyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		
		row_data += '</tr>'
		count = count + 1;
	    };
	    $('#table1').append(row_data);
	    
	    var resultsContainer2 = document.getElementById("set-results2");
	    resultsContainer2.style.display = "block";
	    
	    //Scroll a los resultados
	    resultados2.scrollIntoView();
	} 
    });
    
}

function calc_inyectivas(){
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    console.log(conjunto1);
    console.log(conjunto2);
    //console.log("Funciones Inyectivas");

    resultados2 = document.getElementById("set-results2");
    
    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2,
	"calculation":"inyective"
	
    };

    var caption_txt = document.getElementById("type")
    caption_txt.innerHTML = "Lista de Funciones Inyectivas";
    
    $.ajax({
	type: "POST",
	url: "/calc_functions",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    $('#table1').html('');
	    console.log('INYECTIVE');
	    console.log(result);
	    var row_data = '';
	    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
	    let count = 1;
	    for (var arr in result){
		var obj = result[arr];
		
		row_data += '<tr>';
		
		row_data += '<th scope="row">' + count + '</th>';
		row_data += '<td>' + obj['relation'] + '</td>';
		if (obj['is_relation'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_function'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_inyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_suprayective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_biyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		
		row_data += '</tr>'
		count = count + 1;
	    };
	    $('#table1').append(row_data);
	    
	    var resultsContainer2 = document.getElementById("set-results2");
	    resultsContainer2.style.display = "block";
	    
	    //Scroll a los resultados
	    resultados2.scrollIntoView();
	} 
    });
    
}

function calc_sobreyectivas(){
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    console.log(conjunto1);
    console.log(conjunto2);
    //console.log("Funciones Sobreyectivas");

    resultados2 = document.getElementById("set-results2");
    
    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2,
	"calculation":"sobreyective"
	
    };

    var caption_txt = document.getElementById("type")
    caption_txt.innerHTML = "Lista de Funciones Sobreyectivas";
    
    $.ajax({
	type: "POST",
	url: "/calc_functions",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    $('#table1').html('');
	    console.log(result);
	    var row_data = '';
	    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
	    let count = 1;
	    for (var arr in result){
		var obj = result[arr];
		
		row_data += '<tr>';
		
		row_data += '<th scope="row">' + count + '</th>';
		row_data += '<td>' + obj['relation'] + '</td>';
		if (obj['is_relation'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_function'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_inyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_suprayective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_biyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		
		row_data += '</tr>'
		count = count + 1;
	    };
	    $('#table1').append(row_data);
	    
	    var resultsContainer2 = document.getElementById("set-results2");
	    resultsContainer2.style.display = "block";
	    
	    //Scroll a los resultados
	    resultados2.scrollIntoView();
	    
	} 
    });
    
}

function calc_biyectivas(){
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    console.log(conjunto1);
    console.log(conjunto2);
    //console.log("Funciones Biyectivas");

    resultados2 = document.getElementById("set-results2");
    
    var data_sets = {
	"conjunto1":conjunto1,
	"conjunto2":conjunto2,
	"calculation":"biyective"
	
    };

    var caption_txt = document.getElementById("type")
    caption_txt.innerHTML = "Lista de Funciones Biyectivas";
    
    $.ajax({
	type: "POST",
	url: "/calc_functions",
	data: JSON.stringify(data_sets),
	contentType: "application/json",
	dataType: 'json',
	success: function(result) {
	    $('#table1').html('');
	    console.log(result);
	    var row_data = '';
	    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
	    let count = 1;
	    for (var arr in result){
		var obj = result[arr];
		
		row_data += '<tr>';
		
		row_data += '<th scope="row">' + count + '</th>';
		row_data += '<td>' + obj['relation'] + '</td>';
		if (obj['is_relation'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_function'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_inyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_suprayective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		if (obj['is_biyective'] == true){
		    row_data += '<td style="color:Green;">&#10003;</td>';
		}else{
		    row_data += '<td style="color:Tomato;">&#10007;</td>';
		}
		
		
		row_data += '</tr>'
		count = count + 1;
	    };
	    $('#table1').append(row_data);
	    
	    var resultsContainer2 = document.getElementById("set-results2");
	    resultsContainer2.style.display = "block";
	    
	    //Scroll a los resultados
	    resultados2.scrollIntoView();
	} 
    });
    
}

function calc_especifica(val){
    var conjunto1 = document.getElementById("p2_conjunto1").value;
    var conjunto2 = document.getElementById("p2_conjunto2").value;
    //levantar modal
    if(val!=1){
	//console.log("Especifica");
	$("#espModal").modal('show');
    }else{

	resultados2 = document.getElementById("set-results2");
	
	//enviar peticion con los datos especificos
	var c_esp = document.getElementById("esp-value").value;
	
	//dummy validar que no sea nulo
	if(c_esp != ""){
	    //tengo un valor
	    //hacer llamada ajax aqui
	    //quitar modal en el success
	    console.log(conjunto1);
	    console.log(conjunto2);
	    console.log(c_esp);
	    
	    var data_sets = {
		"conjunto1":conjunto1,
		"conjunto2":conjunto2,
		"conjuntoe":c_esp,
		"calculation":"especial"
		
	    };

	    var caption_txt = document.getElementById("type")
	    caption_txt.innerHTML = "Lista Especial";
	    
	    $.ajax({
		type: "POST",
		url: "/calc_functions",
		data: JSON.stringify(data_sets),
		contentType: "application/json",
		dataType: 'json',
		success: function(result) {
		    //Quitar si todo esta bien
		    $("#espModal").modal('hide');
		    
		    $('#table1').html('');
		    console.log(result);
		    var row_data = '';
		    row_data += '<thead><tr><th scope="col">#</th><th scope="col">Pares Ordenados</th><th scope="col">Relaci??n</th><th scope="col">Funci??n</th><th scope="col">Fn Inyectiva</th><th scope="col">Fn Suprayectiva</th><th scope="col">Fn Biyectiva</th></tr></thead>';
		    let count = 1;
		    for (var arr in result){
			var obj = result[arr];
			
			row_data += '<tr>';
			
			row_data += '<th scope="row">' + count + '</th>';
			row_data += '<td>' + obj['relation'] + '</td>';
			if (obj['is_relation'] == true){
			    row_data += '<td style="color:Green;">&#10003;</td>';
			}else{
			    row_data += '<td style="color:Tomato;">&#10007;</td>';
			}

			if (obj['is_function'] == true){
			    row_data += '<td style="color:Green;">&#10003;</td>';
			}else{
			    row_data += '<td style="color:Tomato;">&#10007;</td>';
			}

			if (obj['is_inyective'] == true){
			    row_data += '<td style="color:Green;">&#10003;</td>';
			}else{
			    row_data += '<td style="color:Tomato;">&#10007;</td>';
			}

			if (obj['is_suprayective'] == true){
			    row_data += '<td style="color:Green;">&#10003;</td>';
			}else{
			    row_data += '<td style="color:Tomato;">&#10007;</td>';
			}

			if (obj['is_biyective'] == true){
			    row_data += '<td style="color:Green;">&#10003;</td>';
			}else{
			    row_data += '<td style="color:Tomato;">&#10007;</td>';
			}
			
			
			row_data += '</tr>'
			count = count + 1;
		    };
		    $('#table1').append(row_data);

		    var resultsContainer2 = document.getElementById("set-results2");
		    resultsContainer2.style.display = "block";
		    
		    //Scroll a los resultados
		    resultados2.scrollIntoView();
		    
		},
		error(request,status,error){
		    alert(request.responseText);
		}
	    });
	    
	    //si existe un err en la llamada
	    //usar show_err("error en ajax");
	    
	}else{
	    $("#espModal").modal('hide');
	    setTimeout(show_err(), 300);
	}
    }
}

//dummy mostrar un error
function show_err(val){
    alert('No puede ser nulo');
}
