(function($) {

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
        totalSlides = $('slide').length;
        $('slide').each(paginarSlide);
        $('img').one('load', scaleImage).each(function () {
            if (this.complete) {
                $(this).trigger('load');
            }
        });
    });
})(jQuery);
