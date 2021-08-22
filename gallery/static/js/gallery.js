$(document).ready(function(){
    $(".rafi-img-modal").click(function(){
        var imgurl = $(this).attr('src')
        var imgalt = $(this).attr('alt')

        if(imgalt !== ""){
            $(".modal-content").append("<div class=\"alt-text-div\"> <p id=\"alt-text\">"+ imgalt +"</p> </div>")
        }

        $("#show-img").attr('src', imgurl);
        $("#imgmodal").modal('show');
    });

    $("#imgmodal").on('hidden.bs.modal', function (){
        $(".alt-text-div").remove();
    })
});