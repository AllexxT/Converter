$(function(){
    $("#aj").click(function(event){
        dic = $("#numer").val()
        data = JSON.stringify(dic)
        var csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value')
        console.log(csrf_token)
        $.ajax({
            url: location.href + "ajax/",
            method: "POST",
            data: {"pack": data},
            dataType:"json",
            success: function(data){
                
                $("#ajx").text(data)
            }
        })
        event.preventDefault();
    })
    
})