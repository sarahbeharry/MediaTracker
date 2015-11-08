$(document).ready(function() {
    var link = "";

    $(".confirm-delete").click(function(event) {
        link = this;
        event.preventDefault();
        
        $("#dialog-delete-confirm").show();
    });

    $("#cancel-delete-button").click(function() {
        $("#dialog-delete-confirm").hide();
    });

    $("#confirm-delete-button").click(function() {
        $("#dialog-delete-confirm").hide();
        window.location = link.href;
    });
});

