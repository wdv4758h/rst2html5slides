(function($) {

    // var deck = 'div#impress'; // should be defined at ?mpress_init.js
    var slide = 'div.step';
    var totalSlides = 0;

    var paginarSlide = function(index, elem) {
        $(elem).append('<div class="pagination"><span class="pagenum">' + (index + 1) +
                       '</span> / <span class="pagetotal">' + totalSlides+ '</span></div>');
    };

    var scaleImage = function () {
        if ($(this).hasClass('no-resize')) {
            return;
        }

        var parent = $(this).parents('section')[0];
        var elem_height = this.naturalHeight;
        var elem_width = this.naturalWidth;
        var height_ratio = $(parent).height() / elem_height;
        var width_ratio = $(parent).width() / elem_width;
        var ratio = Math.min(height_ratio, width_ratio);
        var height = Math.round(elem_height * ratio).toString() + 'px';
        var width = Math.round(elem_width * ratio).toString() + 'px';
        $(this).attr('height', height).attr('width', width);
        console.log(this);
   };


    $(function() {
        totalSlides = $(slide).length;
        $(slide).each(paginarSlide);
        // .one('load') is not working on Firefox
        $('img').on('load', scaleImage).each(function () {
            if (this.complete) {
                $(this).trigger('load');
            }
        });
    });


    // ref: http://tjvantoll.com/2012/06/15/detecting-print-requests-with-javascript/

    var beforePrint = function() {
        // clean up inline styles
        $('html').removeAttr('style');
        $('body').removeAttr('style');
        $(deck).removeAttr('style');
        $(slide).removeAttr('style');
        var slides = $(deck + ' > div').html();
        $(deck + ' > div').remove()
        $(deck).append(slides);
    };

    var afterPrint = function() {
    // firing just after beforePrint!
    // It's not sure if this can be changed at all:
    // http://stackoverflow.com/questions/9920397/window-onbeforeprint-and-window-onafterprint-get-fired-at-the-same-time/9920784#9920784
    //    jmpress_init();
    };

    // if (window.matchMedia) {
    //     var mediaQueryList = window.matchMedia('print');
    //     mediaQueryList.addListener(function(mql) {
    //         if (mql.matches) {
    //             beforePrint();
    //         } else {
    //             afterPrint();
    //         }
    //     });
    // }

    window.onbeforeprint = beforePrint;
    window.onafterprint = afterPrint;

})(jQuery);
