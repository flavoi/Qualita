     $(function() {
    if ($('#map_canvas').length > 1) {
    $('#map_canvas').gmap({'center': '45.4294208 , 11.9571571', 'disableDefaultUI':false,  'panControl': true, 'callback': function(map) { 
      var self = this;
      self.set('findLocation', function(location, marker) {
       self.search({'location': location}, function(results, status) {
        if ( status === 'OK' ) {
         $.each(results[0].address_components, function(i,v) {
          if ( v.types[0] == "country") {
           $('#country'+marker.__gm_id).val(v.long_name);
          
                   }
                      });
         indirizzo = results[0].formatted_address; 
         //marker.setTitle(results[0].formatted_address);
         $('#address'+marker.__gm_id).val(results[0].formatted_address);
         
              }
                       });
                    });
      var m = 0;
      var coordinate;
      var dinam;
      
      // se la sede è già localizzata, posiziono il marker
     if( $(".lat").val() != ''){
            m = 1;
            lat = $(".lat").val();
            lon = $(".lon").val();
           
            
      
     }
      
      
     }});
    }
    });

function setCoords(lat,lon){

     $(".lat").val(lat);
     $(".lon").val(lon);

}


;
 /*!
 * jQuery FN Google Map 3.0-beta
 * http://code.google.com/p/jquery-ui-map/
 * Copyright (c) 2010 - 2012 Johan Säll Larsson
 * Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
 */
( function($) {
	
	/**
	 * This is how you write unmaintainable code :) - the size is small though.
	 * @param namespace:string
	 * @param name:string
	 * @param base:object
	 */
	$.a = function(a, b, c) {
		$[a] = $[a] || {};
		$[a][b] = function(a, b) {
			if ( arguments.length ) {
				this._s(a, b);
			}
		};
		$[a][b].prototype = c;
		$.fn[b] = function(d) {
			var e = this, f = Array.prototype.slice.call(arguments, 1), g = typeof d === 'string';
			if ( g && d.substring(0, 1) === '_' ) { return e; }
			this.each(function() {
				var h = $.data(this, b);
				if ( !h ) {
					h = $.data(this, b, new $[a][b](d, this));
				}
				if ( g ) {
					var i = h[d].apply(h, f);
					if (i != null) {
						e = i;
					}
				}
			});
			return e;  
		};
	};
	
	$.a("ui", "gmap", {
		
		/**
		 * Map options
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#MapOptions
		 */
		options: {
			mapTypeId: 'roadmap',
			zoom: 5	
		},
		
		/**
		 * Get or set options
		 * @param key:string
		 * @param options:object
		 * @return object
		 */
		option: function(a, b) {
			if (b) {
				this.options[a] = b;
				this.get('map').setOptions(this.options);
			}
			return this.options[a];
		},
		
		/**
		 * Setup plugin basics, 
		 * @el is the jQuery element
		 * @options is the 
		 */
		_s: function(a, b) {
			this.el = $(b);
			jQuery.extend(this.options, a);
			this.options.center = this._latLng(this.options.center);
			this._create();
			if ( this._init ) { this._init(); }
		},
		
		/**
		 * Instanciate the Google Maps object
		 */
		_create: function() {
			var a = this; 
			a._a = { 'map': new google.maps.Map(a.el[0], a.options), 'markers': [], 'overlays': [], 'services': [], 'iw': new google.maps.InfoWindow };
			google.maps.event.addListenerOnce(a._a.map, 'bounds_changed', function() { a.el.trigger('init', a._a.map); });
			a._call(a.options.callback, a._a.map);
		},
		
		/**
		 * Adds a latitude longitude pair to the bounds.
		 * @param position:google.maps.LatLng/string
		 */
		addBounds: function(a) {
			this.get('bounds', new google.maps.LatLngBounds()).extend(this._latLng(a));
			this.get('map').fitBounds(this.get('bounds'));
		},
		
		/**
		 * Helper function to check if a LatLng is within the viewport
		 * @param marker:google.maps.Marker
		 */
		inViewport: function(a) {
			var b = this.get('map').getBounds();
			return (b) ? b.contains(a.getPosition()) : false;
		},
		
		/**
		 * Adds a custom control to the map
		 * @param panel:jquery/node/string	
		 * @param position:google.maps.ControlPosition	 
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#ControlPosition
		 */
		addControl: function(a, b) {
			this.get('map').controls[b].push(this._unwrap(a));
		},
		
		/**
		 * Adds a Marker to the map
		 * @param markerOptions:google.maps.MarkerOptions
		 * @param callback:function(map:google.maps.Map, marker:google.maps.Marker) (optional)
		 * @param marker:function (optional)
		 * @return $(google.maps.Marker)
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#MarkerOptions
		 */
		addMarker: function(a, b, c) {
			a.map = this.get('map');
			a.position = this._latLng(a.position);
			var d = new (c || google.maps.Marker)(a);
			var f = this.get('markers');
			if ( d.id ) {
				f[d.id] = d;
			} else {
				f.push(d);
			}
			if ( d.bounds ) {
				this.addBounds(d.getPosition());
			}
			this._call(b, a.map, d);
			return $(d);
		},
		
		/**
		 * Clears by type
		 * @param type:string i.e. 'markers', 'overlays', 'services'
		 */
		clear: function(a) {
			this._c(this.get(a));
			this.set(a, []);
		},
		
		_c: function(a) {
			for ( b in a ) {
				if ( a.hasOwnProperty(b) ) {
					if ( a[b] instanceof google.maps.MVCObject ) {
						google.maps.event.clearInstanceListeners(a[b]);
						a[b].setMap(null);
					} else if ( a[b] instanceof Array ) {
						this._c(a[b]);
					}
					a[b] = null;
				}
			}
		},
		
		/**
		 * Returns the objects with a specific property and value, e.g. 'category', 'tags'
		 * @param context:string	in what context, e.g. 'markers' 
		 * @param options:object	property:string	the property to search within, value:string, delimiter:string (optional)
		 * @param callback:function(marker:google.maps.Marker, isFound:boolean)
		 */
		find: function(a, b, c) {
			var d = this.get(a);
			for ( e in d ) {
				if ( d.hasOwnProperty(e) ) {
					c(d[e], (( b.delimiter && d[e][b.property] ) ? ( d[e][b.property].split(b.delimiter).indexOf(b.value) > -1 ) : ( d[e][b.property] === b.value )));
				}
			};
		},

		/**
		 * Returns an instance property by key. Has the ability to set an object if the property does not exist
		 * @param key:string
		 * @param value:object(optional)
		 */
		get: function(a, b) {
			var c = this._a;
			if (!c[a]) {
				if ( a.indexOf('>') > -1 ) {
					var e = a.replace(/ /g, '').split('>');
					for ( var i = 0; i < e.length; i++ ) {
						if ( !c[e[i]] ) {
							if (b) {
								c[e[i]] = ( (i + 1) < e.length ) ? [] : b;
							} else {
								return null;
							}
						}
						c = c[e[i]];
					}
					return c;
				} else if ( b && !c[a] ) {
					this.set(a, b);
				}
			}
			return c[a];
		},
		
		/**
		 * Triggers an InfoWindow to open
		 * @param infoWindowOptions:google.maps.InfoWindowOptions
		 * @param marker:google.maps.Marker (optional)
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#InfoWindowOptions
		 */
		openInfoWindow: function(a, b) {
			this.get('iw').setOptions(a);
			this.get('iw').open(this.get('map'), this._unwrap(b)); 
		},
				
		/**
		 * Sets an instance property
		 * @param key:string
		 * @param value:object
		 */
		set: function(a, b) {
			this._a[a] = b;
		},
		
		/**
		 * Refreshes the map
		 */
		refresh: function(a) {
			var b = this.get('map');
			var c = b.getCenter();
			$(b).triggerEvent('resize');
			b.setCenter(c);
		},
		
		/**
		 * Destroys the plugin.
		 */
		destroy: function() {
			this.clear('markers');
			this.clear('services');
			this.clear('overlays');
			for ( b in this._a ) {
				this._a[b] = null;
			}
		},
		
		/**
		 * Helper method for calling a function
		 * @param callback
		 */
		_call: function(a) {
			if ( a && $.isFunction(a) ) {
				a.apply(this, Array.prototype.slice.call(arguments, 1));
			}
		},
		
		/**
		 * Helper method for google.maps.Latlng
		 * @param callback
		 */
		_latLng: function(a) {
			if (!a) {
				return new google.maps.LatLng(0.0,0.0);
			}
			if ( a instanceof google.maps.LatLng ) {
				return a;
			} else {
				var b = a.replace(/ /g,'').split(',');
				return new google.maps.LatLng(b[0],b[1]);
			}
		},
		
		/**
		 * Helper method for unwrapping jQuery/DOM/string elements
		 * @param callback
		 */
		_unwrap: function(a) {
			if ( !a ) {
				return null;
			} else if ( a instanceof jQuery ) {
				return a[0];
			} else if ( a instanceof Object ) {
				return a;
			}
			return $('#'+a)[0];
		}
		
	});
	
	jQuery.fn.extend( {
		
		click: function(a, b) { 
			return this.addEventListener('click', a, b);
		},
		
		rightclick: function(a) {
			return this.addEventListener('rightclick', a);
		},
		
		dblclick: function(a, b) {
			return this.addEventListener('dblclick', a, b);
		},
		
		mouseover: function(a, b) {
			return this.addEventListener('mouseover', a, b);
		},
		
		mouseout: function(a, b) {
			return this.addEventListener('mouseout', a, b);
		},
		
		drag: function(a) {
			return this.addEventListener('drag', a );
		},
		
		dragend: function(a) {
			return this.addEventListener('dragend', a );
		},
		
		triggerEvent: function(a) {
			google.maps.event.trigger(this[0], a);		
		},
		
		addEventListener: function(a, b, c) {
			if ( google.maps && this[0] instanceof google.maps.MVCObject ) {
				google.maps.event.addListener(this[0], a, b );
			} else {
				if (c) {
					this.bind(a, b, c);
				} else {
					this.bind(a, b);
				}	
			}
			return this;
		}
		
	});
	
} (jQuery) );;
 /*!
 * jQuery UI Google Map 3.0-beta
 * http://code.google.com/p/jquery-ui-map/
 * Copyright (c) 2010 - 2012 Johan Säll Larsson
 * Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
 *
 * Depends:
 *		jquery.ui.map.js
 */
( function($) {
	
	$.extend($.ui.gmap.prototype, {
		
		/**
		 * Computes directions between two or more places.
		 * @param directionsRequest:google.maps.DirectionsRequest
		 * @param directionsRendererOptions:google.maps.DirectionsRendererOptions (optional)
		 * @param callback:function(result:google.maps.DirectionsResult, status:google.maps.DirectionsStatus)
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#DirectionsRequest
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#DirectionsRendererOptions
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#DirectionsResult
		 */
		displayDirections: function(a, b, c) {
			var d = this;		
			var e = this.get('services > DirectionsService', new google.maps.DirectionsService());
			var f = this.get('services > DirectionsRenderer', new google.maps.DirectionsRenderer());
			if ( b ) {
				f.setOptions(b);
			}
			e.route(a, function(g, h) {
				if ( h === 'OK' ) {
					f.setDirections(g);
					f.setMap(d.get('map'));
				} else {
					f.setMap(null);
				}
				d._call(c, g, h);
			});
		},
		
		/**
		 * Displays the panorama for a given LatLng or panorama ID.
		 * @param panel:jQuery/String/Node
		 * @param streetViewPanoramaOptions:google.maps.StreetViewPanoramaOptions (optional) 
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#StreetViewPanoramaOptions
		 */
		displayStreetView: function(a, b) {
			this.get('map').setStreetView(this.get('services > StreetViewPanorama', new google.maps.StreetViewPanorama(this._unwrap(a), b)));
		},
		
		/**
		 * A service for converting between an address and a LatLng.
		 * @param geocoderRequest:google.maps.GeocoderRequest
		 * @param callback:function(result:google.maps.GeocoderResult, status:google.maps.GeocoderStatus), 
		 * @see http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#GeocoderResult
		 */
		search: function(a, b) {
			this.get('services > Geocoder', new google.maps.Geocoder()).geocode(a, b);
		}
	
	});
	
} (jQuery) );;
 /*!
 * jQuery UI Google Map 3.0-alpha
 * http://code.google.com/p/jquery-ui-map/
 * Copyright (c) 2010 - 2011 Johan Säll Larsson
 * Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
 *
 * Depends:
 *      jquery.ui.map.js
 */
( function($) {

	$.extend($.ui.gmap.prototype, {
		 
		/**
		 * Gets the current position
		 * @param callback:function(position, status)
		 * @param geoPositionOptions:object, see https://developer.mozilla.org/en/XPCOM_Interface_Reference/nsIDOMGeoPositionOptions
		 */
		getCurrentPosition: function(a, b) {
			var c = this;
			if ( navigator.geolocation ) {
				navigator.geolocation.getCurrentPosition ( 
					function(d) {
						c._call(a, d, "OK");
					}, 
					function(error) {
						c._call(a, null, error);
					}, 
					b 
				);	
			} else {
				c._call(a, null, "NOT_SUPPORTED");
			}
		},
		
		/**
		 * Watches current position
		 * To clear watch, call navigator.geolocation.clearWatch(this.get('watch'));
		 * @param callback:function(position, status)
		 * @param geoPositionOptions:object, see https://developer.mozilla.org/en/XPCOM_Interface_Reference/nsIDOMGeoPositionOptions
		 */
		watchPosition: function(a, b) {
			var c = this;
			if ( navigator.geolocation ) {
				this.set('watch', navigator.geolocation.watchPosition ( 
					function(d) {
						c._call(a, d, "OK");
					}, 
					function(error) {
						c._call(a, null, error);
					}, 
					b 
				));	
			} else {
				c._call(a, null, "NOT_SUPPORTED");
			}
		},

		/**
		 * Clears any watches
		 */
		clearWatch: function() {
			if ( navigator.geolocation ) {
				navigator.geolocation.clearWatch(this.get('watch'));
			}
		},
		
		/**
		 * Autocomplete using Google Geocoder
		 * @param panel:string/node/jquery
		 * @param callback:function(results, status)
		 */
		autocomplete: function(a, b) {
			var self = this;
			$(this._unwrap(a)).autocomplete({
				source: function( request, response ) {
					self.search({'address':request.term}, function(results, status) {
						if ( status === 'OK' ) {
							response( $.map( results, function(item) {
								return { label: item.formatted_address, value: item.formatted_address, position: item.geometry.location }
							}));
						} else if ( status === 'OVER_QUERY_LIMIT' ) {
							alert('Google said it\'s too much!');
						}
					});
				},
				minLength: 3,
				select: function(event, ui) { 
					self._call(b, ui);
				},
				open: function() { $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" ); },
				close: function() { $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" ); }
			});
		},
		
		/**
		 * Retrieves a list of Places in a given area. The PlaceResultss passed to the callback are stripped-down versions of a full PlaceResult. A more detailed PlaceResult for each Place can be obtained by sending a Place Details request with the desired Place's reference value.
		 * @param a:google.maps.places.PlaceSearchRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceSearchRequest
		 * @param b:function(result:google.maps.places.PlaceResult, status:google.maps.places.PlacesServiceStatus), http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceResult
		 */
		placesSearch: function(a, b) {
			this.get('services > PlacesService', new google.maps.places.PlacesService(this.get('map'))).search(a, b);
		},
		
		/**
		 * Clears any directions
		 */
		clearDirections: function() {
			var a = this.get('services > DirectionsRenderer');
			if (a) {
				a.setMap(null);
				a.setPanel(null);
			}
		}
		
		/**
		 * A layer that displays data from Panoramio.
		 * @param panoramioLayerOptions:google.maps.panoramio.PanoramioLayerOptions, http://code.google.com/apis/maps/documentation/javascript/reference.html#PanoramioLayerOptions
		 */
		/*loadPanoramio: function(a) {
			if ( !this.get('overlays').PanoramioLayer ) {
				this.get('overlays').PanoramioLayer = new google.maps.panoramio.PanoramioLayer();
			}
			this.get('overlays').PanoramioLayer.setOptions(jQuery.extend({'map': this.get('map') }, a));
		},*/
		
		/**
		 * Makes an elevation request along a path, where the elevation data are returned as distance-based samples along that path.
		 * @param a:google.maps.PathElevationRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#PathElevationRequest
		 * @param b:function(result:google.maps.ElevationResult, status:google.maps.ElevationStatus), http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#ElevationResult
		 */
		/*elevationPath: function(a, b) {
			this.get('services > ElevationService', new google.maps.ElevationService()).getElevationAlongPath(a, b);
		},*/
		
		/**
		 * Makes an elevation request for a list of discrete locations.
		 * @param a:google.maps.PathElevationRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#PathElevationRequest
		 * @param b:function(result:google.maps.ElevationResult, status:google.maps.ElevationStatus), http://code.google.com/intl/sv-SE/apis/maps/documentation/javascript/reference.html#ElevationResult
		 */
		/*elevationLocations: function(a, b) {
			this.get('services > ElevationService', new google.maps.ElevationService()).getElevationForLocations(a, b);
		},*/
		
		/* PLACES SERVICE */		
		
		/**
		 * Retrieves a list of Places in a given area. The PlaceResultss passed to the callback are stripped-down versions of a full PlaceResult. A more detailed PlaceResult for each Place can be obtained by sending a Place Details request with the desired Place's reference value.
		 * @param a:google.maps.places.PlaceSearchRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceSearchRequest
		 * @param b:function(result:google.maps.places.PlaceResult, status:google.maps.places.PlacesServiceStatus), http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceResult
		 */
		/*placesSearch: function(a, b) {
			this.get('services > PlacesService', new google.maps.places.PlacesService(this.get('map'))).search(a, b);
		},*/
		
		/**
		 * Retrieves details about the Place identified by the given reference.
		 * @param a:google.maps.places.PlaceDetailsRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceDetailsRequest
		 * @param b:function(result:google.maps.places.PlaceResult, status:google.maps.places.PlacesServiceStatus), http://code.google.com/apis/maps/documentation/javascript/reference.html#PlaceResult
		 */
		/*placesDetails: function(a, b) {
			this.get('services > PlacesService', new google.maps.places.PlacesService(this.get('map'))).getDetails(a, b);
		},*/
		
		/**
		 * A service to predict the desired Place based on user input. The service is attached to an <input> field in the form of a drop-down list. The list of predictions is updated dynamically as text is typed into the input field. 
		 * @param a:jquery/node/string
		 * @param b:google.maps.places.AutocompleteOptions, http://code.google.com/apis/maps/documentation/javascript/reference.html#AutocompleteOptions
		 */		
		/*placesAutocomplete: function(a, b) {
			this.get('services > Autocomplete', new google.maps.places.Autocomplete(this._unwrap(a)));
		},*/
		
		/* DISTANCE MATRIX SERVICE */
		
		/**
		 * Issues a distance matrix request.
		 * @param a:google.maps.DistanceMatrixRequest, http://code.google.com/apis/maps/documentation/javascript/reference.html#DistanceMatrixRequest 
		 * @param b:function(result:google.maps.DistanceMatrixResponse, status: google.maps.DistanceMatrixStatus), http://code.google.com/apis/maps/documentation/javascript/reference.html#DistanceMatrixResponse
		 */
		/*displayDistanceMatrix: function(a, b) {
			this.get('services > DistanceMatrixService', new google.maps.DistanceMatrixService()).getDistanceMatrix(a, b);
		}*/
	
	});
	
} (jQuery) );;
