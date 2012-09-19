/**
 * @author André Felipe Dias
 * Copyright (C) 2012 Pronus Engenharia de Software http://www.pronus.eng.br
 */

 /**
 * @constructor
 */

 function SlideDeck() {
    this.slideNo = 1;
    this.slides = document.querySelectorAll('slide');

    // Add slide numbers and total slide count metadata to each slide.
    var that = this;
    for (var i = 0, slide; slide = this.slides[i]; i++) {
        slide.dataset.slideNum = i + 1;
        slide.dataset.totalSlides = this.slides.length;
        slide.onclick = function(e) {
            that.goToSlide(this.dataset.slideNum);
            return false;
        }
    }

    document.onkeydown = this.keydown.bind(this);
    window.onhashchange = this.hashchange.bind(this);
    document.body.classList.add('loaded');
    this.showSlide(this.slides[0]);
 }


/**
 * Handler for the document level 'keydown' event.
 *
 * @param {Object} event
 */
SlideDeck.prototype.keydown = function(event) {

    // Disregard the event if the target is editable or a
    // modifier is present
    if (event.target.contentEditable != 'inherit' || event.shiftKey || event.altKey ||
        event.ctrlKey || event.metaKey) return;

    switch(event.keyCode) {

        case 37: // left arrow
        case 8: // Backspace
        case 33: // PgUp
        case 38: // up arrow
            event.preventDefault();
            this.goToSlide(this.slideNo - 1)
            break;

        case 32: // space
        case 39: // right arrow
        case 34: // PgDown
        case 40: // down arrow
            event.preventDefault();
            this.goToSlide(this.slideNo + 1);
            break;

        case 35: // end
            event.preventDefault();
            this.goToSlide(this.slides.length);
            break;

        case 36: // home
            event.preventDefault();
            this.goToSlide(1);
            break;

        case 13: // enter
            event.preventDefault();
            this.toggleOverview();
            break;

        case 27: // esc
            event.preventDefault();
            break;

    }
}


/**
 *
 */
SlideDeck.prototype.goToSlide = function(number) {
    if (number < 1) { number = 1; }
    else if (number > this.slides.length) { number = this.slides.length; }
    if (this.slideNo == number) return;

    this.hideSlide(this.slides[this.slideNo - 1]);
    this.showSlide(this.slides[number - 1]);
    this.slideNo = number;
}


SlideDeck.prototype.showSlide = function(slide) {
    if (!slide) return;
    slide.classList.add('current');
}

SlideDeck.prototype.hideSlide = function(slide) {
    if (!slide) {return;}
    slide.classList.remove('current');
}

SlideDeck.prototype.hashchange = function(event) {
    return;
};
