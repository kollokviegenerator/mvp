$( function() {

    $( "#tag_input" ).keypress( function(event) {
        if ( event.which == 13 || event.which == 44 ) {
            var value = event.target.value;
            $("#tag_set").append(
                "<span class=\"tag\"><span class=\"key\">"
                + value +
                "</span><span class=\"remove\">x</span></span>"
            );

            $(this).val("");
        }
    } );

    $( ".remove" ).live( 'click', function(event) {
        $(this).parent().remove()
    } );

})