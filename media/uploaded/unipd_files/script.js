var UNIPD;
(function($) {

	UNIPD = {
		current_link : '',
		tablist_padding : '',
		tablist_graphic_padding : '',
		tabopen_margin : '',
		tabopen_object : '',

		init_tablist : function() {
			$('#tablist li a').each(function(){
				UNIPD.tablist_padding = Math.floor(($(this).parent().height() - $(this).height()) / 2);
				$(this).css({
					'padding-top' : UNIPD.tablist_padding,
					'padding-bottom' : UNIPD.tablist_padding
				});
			});

			$('#tablistgraphic li span').each(function(){
				UNIPD.tablist_graphic_padding = Math.ceil(($(this).closest('li').height() - $(this).height()) / 2);
				$(this).css({
					'padding-top' : UNIPD.tablist_graphic_padding,
					'padding-bottom' : UNIPD.tablist_graphic_padding
				});
			});

			$('.list-box .box .tophead h2').each(function(){
				UNIPD.tablist_graphic_padding = Math.ceil(($(this).closest('.tophead').height() - $(this).height()) / 2);
				$(this).css({
					'padding-top' : UNIPD.tablist_graphic_padding,
					'padding-bottom' : UNIPD.tablist_graphic_padding
				});
			});
			$('.text-image .height-claim').each(function(){
				UNIPD.tablist_graphic_padding = Math.ceil(($(this).closest('.text-image').height() - $(this).height()) / 2);
				$(this).css({
					'padding-top' : UNIPD.tablist_graphic_padding,
					'padding-bottom' : UNIPD.tablist_graphic_padding
				});
			});

			$('#tablistgraphic li').click(function(){
				$('#'+$(this).attr('class')+' a').click();
			});

			$('#tablist li a').click(function(){
				
				if ($(this).parent().hasClass('active')) {
					$(this).parent().removeClass('active');
					$('.tablistopen').hide();
					$('#tablistgraphic').show();
				} else {
					$(this).parent().siblings().removeClass('active');
					$(this).parent().addClass('active');
					$('.tablistopen').hide();
					UNIPD.tabopen_object = $('[aria-labelledby=' + $(this).parent().attr('id') + ']');
					$(UNIPD.tabopen_object).show();
					if ($(UNIPD.tabopen_object).hasClass('init')) {
						$(UNIPD.tabopen_object).find('li a').each(function(){
							UNIPD.tabopen_margin = Math.floor(($(this).parent().height() - $(this).innerHeight()) / 2);
							$(this).css('margin-top', UNIPD.tabopen_margin);
						});
						$(UNIPD.tabopen_object).removeClass('init');
					}
				}
				return false;
			});



			$('.tablistopen .closelayer').click(function(){
				//$('#tablist li#' + $(this).parent().attr('aria-labelledby') + ' a').click();
				$('.tablistopen').hide();
				$('#tablistgraphic').show();
				$('#tablist li#' + $(this).parent().attr('aria-labelledby')).removeClass('active');
			});

			$('.tablistopen .closelayer').blur(function(){
				//$('#tablist li#' + $(this).parent().attr('aria-labelledby') + ' a').click();
				$('.tablistopen').hide();
				$('#tablistgraphic').show();
				$('#tablist li#' + $(this).parent().attr('aria-labelledby')).removeClass('active');

			});

			$('#tablist li a').focus(function(){
			     if ($(this).parent().hasClass('active')) {
				 	$(this).parent().addClass('focused');
				 //} else {
				   // $(this).parent().addClass('focused');
				 }
			});
			$('#tablist li a').blur(function(){
				 $(this).parent().removeClass('focused');
			});

		},

		manage_hp_links : function() {
			$('.rightHL ul li, .mixedlinks .box, .tablistopen .rightboxes .box, #footer .upstore').click(function(){
				this.current_link = $(this).find('h3 a').eq(0).attr('href')
				if (this.current_link != undefined) {
					window.location.href = this.current_link;
				}
			});
		},

		manage_empty_links : function() {
			$('a[href=#]').click(function(evt){
				evt.preventDefault();
			});
		},

		extend_centercolumn : function() {
			if ($('#centercolumn').height() < $('#maincontent').height()) {
				var last_block_height = $('#centercolumn .centerblock:last').height();
				//$('#centercolumn .centerblock:last').css('min-height', last_block_height + $('#maincontent').height() - $('#centercolumn').height());
				$('#centercolumn .centerblock:last').addClass('minimal-height');
			}
		},

		manage_left_sidebar : function() {
			$('.leftmenu li.active, .leftmenu li.active-trail').each(function(){
				$(this).addClass('expanded');
			});

			$('.leftmenu .acc_control').click(function(){
				var that = $(this);
				if ($(this).parent().hasClass('expanded')) {
					$.Deferred(function($df) {$df
						.pipe(function() {return that.siblings('ul').slideUp();})  /* prima questo */
						.pipe(function() {return that.parent().removeClass('expanded').addClass('collapsed')})  /* poi questo */
					}).resolve();
				} else {
					$(this).parent().siblings('.expanded').children('.acc_control').click();
					$.Deferred(function($df) {$df
						.pipe(function() {return that.siblings('ul').slideDown();})  /* prima questo */
						.pipe(function() {return that.parent().removeClass('collapsed').addClass('expanded')})  /* poi questo */
					}).resolve();
				}
			});
		}
	}

	$(document).ready(function(){
		UNIPD.manage_empty_links();
		UNIPD.manage_hp_links();
		UNIPD.init_tablist();
		UNIPD.extend_centercolumn();
		UNIPD.manage_left_sidebar();

		/* accessibilità focus menu principale */
		var _mli = $("#mainmenu > ul > li"),
			_ma = $("#mainmenu > ul > li > a");


		if ($("#mainmenu").length) {
			_ma.on('focus', function() {
				//_mli.trigger('mouseenter')
				_mli.removeClass('focus');
				$(this).parent().addClass('focus')
				
			});
			_mli.on('mouseenter', function() {
				_mli.removeClass('focus');

				/* calcolo dinamico offset negativo */
				var sublist = $(this).find('ul'),
				    offset  = 0,
					firstli = sublist.find('li').slice(1, 7);

				sublist.find('li:nth-child(n + 8)').hide();
				setTimeout(function() {
					$(firstli).each(function() {offset -= $(this).height();});
					sublist.find('li:nth-child(n + 8)').css('top', offset + 'px').show();
				}, 60);


			})
			_mli.on('mouseleave', function() {
				$(document).off('keydown.menu');
			});


			/* skip link */
			$('#mainmenu').find('.skiplink').on('click', function(evt) {
				evt.preventDefault();
				_mli.removeClass('focus');
				var link = $(this).attr('href');
				$(link).children('a').focus();
			})

		}




		/* Slideshow UNIPD home */
		$('.slideshow').slideshowUNIPD();
                
        setTimeout(function(){ 			
        simple_tooltip(".tp","tooltip");

                // initialize scrollable
                jQuery(".gallery-mask").parent().addClass('js-active');
                jQuery(".gallery-mask").scrollable();

        jQuery(".items img").click(function() {
                // see if same thumb is being clicked
                if (jQuery(this).hasClass("active")) {return;}
                if (jQuery(this).hasClass("active")) {return;}
                // calclulate large image's URL based on the thumbnail URL (flickr specific)

                var url = jQuery(this).attr("src").replace("gallery_small", "gallery_big");

                // get handle to element that wraps the image and make it semi-transparent
                var wrap = jQuery("#image_wrap").fadeTo("medium", 0.5);

                // the large image from www.flickr.com
                var img = new Image();


                // call this function after it's loaded
                img.onload = function() {

                        // make wrapper fully visible
                        wrap.fadeTo("fast", 1);

                        // change the image
                        wrap.find("img").attr("src", url);

                };

                // begin loading the image from www.flickr.com
                img.src = url;

                // activate item
                jQuery(".items img").removeClass("active");
                jQuery(this).addClass("active");
        return false;
        //when page loads simulate a "click" on the first image
        }).filter(":first").click();
        },100);


        
        
        
        
        
        
        if (jQuery('#rubrica-sort').length > 0) {
        jQuery('#rubrica-sort').live("change", function(event) {
            //var url = Drupal.settings.base_url;
            var filtro = jQuery("#rubrica-sort option:selected").attr('value');
            location.href = filtro;
        });
        }
        
        
        if (jQuery('#lista_griglia_rubrica').length > 0) {
        jQuery('#lista_griglia_rubrica_div a').live("click", function(event) {
            event.preventDefault();
            var classe = jQuery(this).attr('id');
            classe = classe.replace('rubrica_', ''); 
            if (jQuery('#lista_griglia_rubrica').hasClass('lista')) {
                jQuery('#lista_griglia_rubrica').removeClass('lista').addClass(classe);
            }
            else {
                jQuery('#lista_griglia_rubrica').removeClass('griglia').addClass(classe);
            }
            
        });
        }
        
        
        


	});





	UNIPD.oldIE	= (jQuery.browser.msie && jQuery.browser.version < 9);
	/**
	 * Asynchronous loader with deferred objects
	 */
	UNIPD.imageLoader = function(src, t) {

		var	image		= $('<img />'),
			imageDFD 	= $.Deferred(),
			timeout 	= setTimeout(function() {
				image.trigger('error.imgloader')
			}, (t * 1000) || 5000),
			timeRequest;


		image
			.one('load.imgloader', function() {
				clearInterval(timeout);
				//console.log("loaded in %d seconds", ((new Date()).getTime() - timeRequest)/1000);
				imageDFD.resolve();
			})
			.bind('error.imgloader', function() {
				clearInterval(timeout);
				imageDFD.reject();
			})
			.bind('readystatechange.imgloader', function() {
				if ('complete' === this.readyState) {
					image.trigger('load.imgloader');
				}
			})
			.attr('src', src);

		//timeRequest	= (new Date()).getTime();

		if (image.get(0).complete) {
			setTimeout(function() {
				image.trigger('load.imgloader');
			}, 16);
		}

		return imageDFD.promise();
	};



	/* photo slideshow */
	(function() {
		var Slideshow = function(s) {

			var _s = {
				url		: null,
				index	: 0,
				timeout	: 8,

				figure  		: s,
				cnt				: s.find('div.contents'),
				image			: s.find('div.contents img.slide-img'),
				caption 		: s.find('div.contents h3 a'),
				linkscnt		: s.find('> ul'),
				links   		: null,
				loader			: $('<div class="loadergallery"><span>Loading</span></div>')
			};

			var busy		= false,
				hovered		= false;
				initCall	= false;
				loadercall  = null,
				loop		= null;

			var doLoop 		= function() {


				loop = setTimeout(function() {
					var next = (_s.index + 1 < _s.JSONlength)? _s.index + 1 : 0;
					requestImage(next);
					doLoop();
				}, 5000)

			};

			var initTriggers 	= function() {
				var cont = 0;
				for (var i=0; i< _s.JSONlength; i++) {
					
					_s.linkscnt.append('<li><a href="#" data-slideshow-index="'+ i +'" tabindex="12'+ cont +'">Notizia ' + (i + 1) + '</a></li>')
					cont+=2;
				}

				_s.links = _s.linkscnt.find('a');

				_s.cnt.off('click').on('click', function() {
					if (_s.JSON['images'][0]['link']) {
						location.href = _s.JSON['images'][0]['link']
					}
				});

				_s.linkscnt.on('click', function(evt) {
					evt.stopPropagation();
					evt.preventDefault();
				});

				_s.links.on('click', function(evt) {
					evt.stopPropagation();
					evt.preventDefault();
					if (loop) {
						clearInterval(loop);
					}
					_s.links.removeClass('current');
					$(this).addClass('current')
					requestImage($(this).data('slideshow-index') | 0);
				})

				requestImage(0, doLoop);

			};

			var requestImage		= function(i, callback) {

				var imageData, imageNode;
				imageData = _s.JSON[i];

				if (_s.image.length) {
					imageNode = $('<img class="loading" />')
						.attr('src', (!!imageData.url)? imageData.url : "/sites/unipd.it/themes/unipd/img/layout/blank.gif")
						.toggleClass('empty', !imageData.url)
						.insertAfter(_s.image);
				}
				else {
					imageNode = $('<img class="slide-img"/>')
						.attr('src', (!!imageData.url)? imageData.url : "/sites/unipd.it/themes/unipd/img/layout/blank.gif")
						.toggleClass('empty', !imageData.url)
						.appendTo(_s.cnt);
				}


				/* waiting for image load, then fadeOut of old image */
				$.when(UNIPD.imageLoader(imageNode.attr('src'), _s.timeout))
				.done(function() {


					imageNode.fadeIn(600, function() { });
					_s.JSON[_s.index]['caption'].fadeOut(300);

					if (_s.image.length) {
						_s.image.fadeOut(600, function() {

							_s.image.remove();
							imageNode.removeClass('loading');

							_s.links.removeClass('current');
							_s.image = imageNode;

							/* successfull load, increment index */
							_s.index = i;
							_s.JSON[_s.index]['caption'].fadeIn(300);

							/* set new image alt */
							_s.image.attr('alt', imageData.alt || "");
							_s.links.eq(i).addClass('current')

							busy = false;
							hideLoader();

							if ('function' === typeof callback) {
								callback();
							}
						});
					}
					else {
						_s.links.removeClass('current');
						_s.image = imageNode;

						/* successfull load, increment index */
						_s.index = i;
						_s.JSON[_s.index]['caption'].fadeIn(300)

						/* set new image alt */
						_s.image.attr('alt', imageData.alt || "");

						_s.links.eq(i).addClass('current')

						busy = false;
						hideLoader();

						if ('function' === typeof callback) {
							callback();
						}
					}
				})
				.fail(function() {
					imageNode.remove();
					busy = false;
					hideLoader();
					if ('function' === typeof callback) {
						callback();
					}
				});

			};


			var showLoader		= function(time) {
				if (time) {
					loadercall = setTimeout(function() {
						clearInterval(loadercall);
						loadercall = null;
						if (UNIPD.oldIE) {_s.loader.appendTo(_s.figure).show();}
						else {_s.loader.appendTo(_s.figure).fadeIn(500);}
					}, time);
				}
				else {
					if (UNIPD.oldIE) {_s.loader.appendTo(_s.figure).show();}
					else {_s.loader.appendTo(_s.figure).fadeIn(500);}
				}
			};

			var hideLoader		= function() {
				if (!loadercall) {
					if (UNIPD.oldIE) {
						_s.loader.hide().remove();
					}
					else {
						_s.loader.fadeOut(500, function() {
							_s.loader.remove();
						});
					}
				}
				else {
					clearInterval(loadercall);
					loadercall = null;
				}

			};



			return {
				init		: function(el, options) {

					_s = $.extend(_s, options);
					_s.JSON = [];
					_s.cnt.find('li').each(function(i) {

						_s.JSON[i] = {
							//'url'		: $(this).data('unipd-slideimage'),
							'url'		: $(this).children('.url-image-placeholder').attr('src'),
							'caption'	: $(this)
						}

					})

					showLoader();
					busy = true;
					_s.JSONlength = _s.JSON.length;
					initTriggers();

				}

			}

		}

		$.fn.slideshowUNIPD = function(options) {
			if (this.length) {
				return this.each(function() {
					var obj = new Slideshow($(this));
					obj.init($(this), options);
					$.data(this, 'slideshow', obj);
				});
			}
			return this;
		};


	}());

}(jQuery));

    
//jQuery(document).ready(function() {


//});

function simple_tooltip(target_items, name){
				jQuery(target_items).each(function(i){
					jQuery("body").append("<div class='"+name+"' id='"+name+i+"'><p>"+jQuery(this).attr('title')+"</p></div>");
					var my_tooltip = jQuery("#"+name+i);
					jQuery(this).removeAttr("title").mouseover(function(){
							my_tooltip.css({opacity:1, display:"none"}).fadeIn(400);
						}).mousemove(function(kmouse){
							my_tooltip.css({left:kmouse.pageX+15, top:kmouse.pageY+15});
						}).mouseout(function(){
							my_tooltip.fadeOut(400);
						});
					});
}
