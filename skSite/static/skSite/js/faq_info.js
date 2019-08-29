function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }

  (function() {
    if (document.location.hash) {
        setTimeout(function() {
            window.scrollTo(window.scrollX, window.scrollY - 100);
        }, 10);
    }
})();