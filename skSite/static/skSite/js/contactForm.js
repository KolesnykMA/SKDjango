console.log('Примати без фільтра')

$(document).ready(function() {
    $('.button_form_contact').click(function (event){

        var name = $('.name').val()
        var email = $('.email').val()
        var tg = $('.tg').val()
        var message = $('.message').val()

        var statusElm = $('.status')
        statusElm.empty()

        if(email.length > 5 && email.includes('@') && email.includes('.')){

        }else{
            event.preventDefault();
            statusElm.append('<div>Недійсна пошта</div>')
        }

        if(name.length < 6){
            event.preventDefault();
            statusElm.append("<div>Ім'я має містити мінімум 6 символів</div>")
        }


        if(message.length < 20){
            event.preventDefault();
            statusElm.append('<div>Повідомлення має містити мінімум 20 символів</div>')
        }

    })
})