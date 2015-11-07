$(document).ready(function() {
    var link = "";
    
    $( "#dialog-delete-confirm" ).dialog({
        autoOpen: false,
        width: 450,
        modal: true,
        //position: { my: "left top", at: "left top", of: ".confirm-delete"},
        buttons: {
            "Yes, let's do it!": function() {
                window.location = link.href;
            },
            "Actually, nah...": function() {
                $(this).dialog("close");
            }
        }
    });
    
    $(".confirm-delete").click(function(event) {
        link = this;
        event.preventDefault();
        
        $("#dialog-delete-confirm").dialog("open");
    
    });
});
