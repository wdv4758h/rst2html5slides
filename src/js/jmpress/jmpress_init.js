(function($) {

    var jmpress_init = function() {
        $('deck').jmpress({
            stepSelector: 'slide'
        });
    }

    $(jmpress_init);


    // ref: http://tjvantoll.com/2012/06/15/detecting-print-requests-with-javascript/

    var beforePrint = function() {
        // clean up inline styles
        $('html').removeAttr('style');
        $('body').removeAttr('style');
        $('deck').removeAttr('style');
        $('slide').removeAttr('style');
        var slides = $('deck > div').html();
        $('deck > div').remove()
        $('deck').append(slides);
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