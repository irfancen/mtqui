$(document).ready(function(){
    $(".rafi-img-modal").click(function(){
        var imgurl = $(this).attr('src')
        $("#show-img").attr('src', imgurl);
        $("#imgmodal").modal('show');
    });
});