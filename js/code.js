function adjustCodeLanguage() {
    var code_blocks = document.querySelectorAll('code');
    for (var i = 0; i < code_blocks.length; i++) {
        var language = code_blocks[i].className.match(/language-([\w]+)/);
        if (language && language.length == 2) {
            language = language[1];
            code_blocks[i].parentNode.dataset.language = language;
        }
    }
}