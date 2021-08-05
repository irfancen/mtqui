$(document).ready(function(){
    $(".square").click(function(){
        var imgurl = $(this).css('background-image')
        imgurl = imgurl.replace('url(','').replace(')','').replace(/\"/gi, "");
        $("#show-img").attr('src', imgurl);
        $("#imgmodal").modal('show');
    });
});