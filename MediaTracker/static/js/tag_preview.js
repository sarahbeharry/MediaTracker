function updateTagPreview() {
    $("#tag-name-preview").text($("#name").val());
    $("#tag-preview").prop("title", $("#description").val());
    $("#tag-style-preview").css("color", $("#colour").val());
    $("#tag-style-preview").removeClass();
    
    var style = $("input[name='style']:checked").val();
    
    $("#tag-style-preview").addClass("tagColourElement glyphicon glyphicon-" + style);
}

$(document).ready(function() {
    updateTagPreview();
    
    $(".update-tag-preview").change(updateTagPreview);
    $(".update-tag-preview").on('input', updateTagPreview);
});


