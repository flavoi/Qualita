function close_accordion(acc,io,prima){
	for(var i=0; i<acc.length; i++){
		if (i>=0){
			if (prima){
				io.siblings().eq(i).hide();
			}else {
				io.siblings().eq(i).slideUp('normal');
			}
		}
	}
}

function close_accordion_1(acc,io,prima){
	for(var i=0; i<acc.length; i++){
		if (i>=1){
			if (prima){
				io.siblings().eq(i).hide();
			}else {
				io.siblings().eq(i).slideUp('normal');
			}
		}
	}
}


function set_accordion(){
	$('.accordion-head .acc_control').each(function(){
		
		var fratelli = $(this).siblings();
		var first= 1;
		if($(this).parent().hasClass('closed')){
			if ($(this).hasClass('ta')){
				close_accordion_1(fratelli,$(this),first);
				$(this).parent().toggleClass('closed');
			} else {
			    fratelli = $(this).parent().siblings();
				close_accordion(fratelli,$(this),first);
				$(this).parent().siblings().slideUp('slow');
				$(this).parent().parent().toggleClass('closed');
			}
		}	
		
		//$('#centercolumn .accordion-head .acc_control h2').css('display','block');
	});
	

}

$('.accordion-head .acc_control').live('click', function(){
	
	
	//$(this).siblings().each(function(){
		if($(this).parent().hasClass('opened')){
			var first = 0;
			var fratelli = $(this).siblings();
			if ($(this).hasClass('ta')){
				close_accordion_1(fratelli,$(this),first);
			} else {
			    fratelli = $(this).parent().siblings();
				close_accordion(fratelli,$(this),first);
				$(this).parent().siblings().slideUp('slow');

			}	
		}else{
				if ($(this).hasClass('ta')){
					$(this).siblings().each(function(){
						$(this).slideDown('normal');
					});
				} else {
					$(this).parent().siblings().each(function(){
						$(this).slideDown('normal');
					});
				}	
			
		}
	//});
		$(this).parent().toggleClass('opened');
	
	if ($(this).hasClass('ta')){
		$(this).parent().siblings().slideUp('slow');
	}
});


function setCalendar(){
	
	var dataOdierna = new Date(); 

	var mm;
	mm = dataOdierna.getMonth();

jQuery('#calendarcarousel').jcarousel({
	scroll : 1,
	start : mm+1
});

var id_mese_corrente = jQuery('#calendarcontent').children().eq(mm).attr('id');

if (jQuery('#calendarcarousel a.selected').length == 0) {
	jQuery('.calendarlist#'+id_mese_corrente+', #calendarcarousel li a[rel="'+id_mese_corrente+'"]').addClass('selected');
}

jQuery('#calendarcarousel a').click(function(evt){
	evt.preventDefault();
	if (!jQuery(this).hasClass('selected')) {
		jQuery(this).closest('ul').find('a').removeClass('selected');
		jQuery(this).addClass().addClass('selected');
		jQuery('.calendarlist').removeClass('selected');
		jQuery('#'+jQuery(this).attr('rel')).addClass('selected')
	}
});

}


var geocoder;
var map; 

$(document).ready(function() {

if($("#map_canvas").html() != null){

  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(41.8905198 , 12.4942486);
  var myOptions = {
   
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  
  //if($("#edit-distanza").val())
  var address = $("#edit-distanza").val();   
  var input = document.getElementById('edit-distanza');
  if(input)
    input.setAttribute('placeholder','');
  var autocomplete = new google.maps.places.Autocomplete(input);

 // autocomplete.bindTo('bounds', map);     
 
   google.maps.event.addListener(autocomplete, 'place_changed', function() {
       
        var place = autocomplete.getPlace();
        if (place.geometry.viewport) {
          map.fitBounds(place.geometry.viewport);
        } 

     

        var address = '';
        if (place.address_components) {
          address = [(place.address_components[0] &&
                      place.address_components[0].short_name || ''),
                     (place.address_components[1] &&
                      place.address_components[1].short_name || ''),
                     (place.address_components[2] &&
                      place.address_components[2].short_name || '')
                    ].join(' ');
        }


  
   
  return false;
  
});
}   
});



function get_coords(){
   
   indirizzo = $('#edit-distanza').val();
   
      geocoder.geocode( {'address': indirizzo}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
           coordinate_trovate = results[0].geometry.location;
           $('#edit-localita').val(indirizzo);
           $('#edit-coordinate').val(coordinate_trovate);
            return false;

        } else {
            $('#edit-coordinate').val("");
           return false;

        }

      });
   
}



jQuery(document).ready(function(){  
                
                 //$("#box-din").html("");
                 
                 
                 $('#box-close').click(function(){
					$("#box-ricerca").addClass("hidden-content");
				 }); 
                
                 $( "#inphead1" ).autocomplete({
                    
                        source: function( request, response ) {
                                $.ajax({
                                    
                                        url:  '/call_solr',
                                        dataType: "json",
                                        data: {
                                                featureClass: "P",
                                                style: "full",
                                                termine: $( "#inphead1" ).val()
                                               
                                        },
                                       
                                    success: function( data ) {
                                        
                                                if(!data){                                                    
                                                    //$("#box-ricerca").hide();  
                                                    $("#box-ricerca").addClass("hidden-content");                                                  
                                                }       
                                                else {
                                                    response( $.map( data, function( item ) {
                                                            var testo;
                                                            var titolo;  
                                                            var tipo;
                                                            var tipo_desc;
                                                            var path_immagine;
                                                            var output;
                                                            var link_nodo;
                                                            var link_mostra_tutti;
                                                            var base_url = location.host;
                                                            
                                                            $("#box-din").html(" ");
                                                            if(item.numFound > 0 || item != 0){
                                                                    for (var key in item.docs) {
                                                                            
                                                                           
                                                                            //$("#box-ricerca").show();
                                                                            $("#box-ricerca").removeClass("hidden-content");
                                                                            testo = item.docs[key].body;

                                                                            titolo = item.docs[key].title;
                                                                            tipo = item.docs[key].type_name;
                                                                            
                                                                            if(tipo == 'Foglia semplice' || tipo == 'Foglia complessa') {
        																		tipo_desc = 'Pagina'; 
        																	}else {
        																		tipo_desc = tipo; 
        																	}	
																			tipo_desc="";
                                                                            
                                                                            testo = item.docs[key].teaser;
                                                                            //testo = testo.truncatable({limit:250});
                                                                            path_immagine = item.docs[key].image_path;
                                                                            link_nodo = item.docs[key].url;
                                                                            link_nodo = link_nodo.replace("http://unipd.it","http://"+base_url);
                                                                            
                                                                            link_mostra_tutti = "/ricerca-avanzata/"+request.term;


                                                                            output = '<h4>'+tipo_desc+'</h4> '
                                                                                + '<div class="list-cerca clearfix">'
                                                                                + '<a class="clearfix" href="' + link_nodo + '">'
                                                                                +  '<div class="thumb">'; {
                                                                                
                                                                            if (path_immagine!=undefined)     
                                                                            output = output     
                                                                                + ' <img src="/' + path_immagine  + '" alt="' +titolo+ '" />';
                                                                            }
                                                                            output = output    
                                                                                +  '</div> <h5>' +titolo+ '</h5>';


                                                                            testo = truncate(250,testo);
                                                                            output+= "<p>"+ testo + "...</p>";
                                                                                output+= '</a></div>';
                                                                                if(output != '')
                                                                                $("#box-din").append(output); 




                                                                        }
                                                                        $("#link-mostra-tutti").attr("href",link_mostra_tutti);
                                                            }
                                                            
                                                    

                                                    }));
                                                            }
                                            }
                                    });
                              
                        },
                        minLength: 3,
                        select: function( event, ui ) {
                            
                                log( ui.item ?
                                        "Selected: " + ui.item.label :
                                        "Nothing selected, input was " + this.value);
                              
                        },
                        open: function() {
                                $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
                        },
                        close: function() {
                                $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
                        }
                });
       

        });(jQuery);

 
function search_order(path){    
    
    var filtro = $("#ordina").val();
    var redirect = '/' + path ;
    if(filtro == 'Titolo')
        redirect = '/' + path + "?solrsort=sort_title asc"; 
    if(filtro == 'Tipo')
        redirect = '/' + path + "?solrsort=type asc"; 
    if(filtro == 'Autore')
        redirect = '/' + path + "?solrsort=sort_name asc"; 
    if(filtro == 'Data')
        redirect = '/' + path + "?solrsort=created desc"; 
    
    
    location.href = redirect;
}

 function truncate(len,stringa) {
 
 var trunc = stringa;
 
    if (trunc.length > len) {

      /* Truncate the content of the P, then go back to the end of the
         previous word to ensure that we don't truncate in the middle of
         a word */
      trunc = trunc.substring(0, len);
      trunc = trunc.replace(/\w+$/, '');

    
    }
  
  
  return trunc;
}

function filter_type(){    
    
    redirect = $("#categoria").val();
    location.href = redirect;
    
    
}