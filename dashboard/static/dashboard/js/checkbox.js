$(document).ready( () => {
    $(".checkbox").change( function() {
        $(".checkbox").prop('checked', false);
        $(this).prop('checked', true);
    });
});
