jQuery(document).ready(function($) {
	   
     'use strict';
     
  	//*** Function Banner
  	jQuery('.careerfy-testimonial-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-arrows4'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-arrows4'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Services Slider
    jQuery('.careerfy-service-slider').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        centerMode: true,
        centerPadding: '0px',
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-arrows4'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-arrows4'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Partner Slider
    jQuery('.careerfy-partner-slider').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        centerMode: true,
        centerPadding: '0px',
        arrows: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Partner Slider
    jQuery('.careerfy-partnertwo-slider').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-arrow-pointing-to-left'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-arrow-pointing-to-right'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Partner Slider
    jQuery('.careerfy-testimonial-styletwo').slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: true,
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-arrows22'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-arrows22'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Partner Slider
    jQuery('.careerfy-testimonial-slider-style3').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: true,
        fade: true,
        prevArrow: $('.careerfy-prev'),
        nextArrow: $('.careerfy-next'),
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Partner Slider
    jQuery('.careerfy-partner-style3').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        arrows: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //*** Function Banner Six
    jQuery('.jobsearch-banner-six').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: false,
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-right-arrow'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-right-arrow'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });
    //*** Function Employer Slider
    jQuery('.careerfy-employer-slider').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: true,
        prevArrow: "<span class='slick-arrow-left'><i class='careerfy-icon careerfy-right-arrow'></i></span>",
        nextArrow: "<span class='slick-arrow-right'><i class='careerfy-icon careerfy-right-arrow'></i></span>",
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });
    //*** Function Testimonial Slider
    jQuery('.careerfy-testimonial-style4').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        dots: true,
        arrows: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
            }
          },
          {
            breakpoint: 800,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 400,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });

    //***************************
    // Parent AddClass Function
    //***************************
    jQuery(".navbar-nav .sub-menu").parent("li").addClass("submenu-addicon");

    $('#circle-pie-1').pieChart({
        barColor: '#1873da',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });
    $('#circle-pie-2').pieChart({
        barColor: '#53cffc',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });
    $('#circle-pie-3').pieChart({
        barColor: '#8bc34a',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });
    $('#circle-pie-4').pieChart({
        barColor: '#ffa34d',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });
    $('#circle-pie-5').pieChart({
        barColor: '#f54518',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });
    $('#circle-pie-6').pieChart({
        barColor: '#007eb3',
        trackColor: '#e4e8e9',
        lineCap: 'butt',
        lineWidth: 19,
        onStep: function (from, to, percent) {
            $(this.element).find('.pie-value').text(Math.round(percent) + '%');
        }
    });

});


if (jQuery('#widget-application-countdown').length > 0) {
  var austDay = new Date(2019, 03 - 1, 31, 00, 00, 00);
  jQuery('#widget-application-countdown').countdown({
      until: austDay
  });
}



if (jQuery('#map').length > 0) {
  // When the window has finished loading create our google map below
  google.maps.event.addDomListener(window, 'load', init);

  function init() {
      // Basic options for a simple Google Map
      // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
      var mapOptions = {
          // How zoomed in you want the map to start at (always required)
          zoom: 11,

          // The latitude and longitude to center the map (always required)
          center: new google.maps.LatLng(40.6700, -73.9400), // New York

          // How you would like to style the map. 
          // This is where you would paste any style found on Snazzy Maps.
          styles: [{"featureType":"administrative","elementType":"labels.text.fill","stylers":[{"color":"#444444"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#46bcec"},{"visibility":"on"}]}]
      };

      // Get the HTML DOM element that will contain your map 
      // We are using a div with id="map" seen below in the <body>
      var mapElement = document.getElementById('map');

      // Create the Google Map using our element and options defined above
      var map = new google.maps.Map(mapElement, mapOptions);

      // Let's also add a marker while we're at it
      var marker = new google.maps.Marker({
          position: new google.maps.LatLng(40.6700, -73.9400),
          map: map,
          title: 'Snazzy!'
      });
  }
}


//********************************
// Mediaelementplayer Function
//********************************
if (jQuery('video').length > 0) {
  jQuery('video').mediaelementplayer({
    success: function(player, node) {
      jQuery('#' + node.id + '-mode').html('mode: ' + player.pluginType);
    }
  });

  jQuery(function() {
    jQuery(".nav-list-mode").click(function()
     {                     
      jQuery(".careerfy-header-four .careerfy-navigation").slideToggle();
      });
   });
}