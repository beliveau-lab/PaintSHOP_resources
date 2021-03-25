// execute when the DOM is fully loaded
$(function() {

    // configure website footer
    var d = new Date();
    $("#footer_wrapper").append(
        "<div class='footer'><center><i>Copyright &copy; "
        + d.getFullYear()
        + "</i></center></div>"
    );

});