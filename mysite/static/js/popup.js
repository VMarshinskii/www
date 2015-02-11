$(document).ready(function() {
 
    $('body').append('<div id="blackout"></div>');
     
    var boxWidth = 400;

    function centerBox() {

        /* определяем нужные данные */
        var winWidth = $(window).width();
        var winHeight = $(document).height();
        var scrollPos = $(window).scrollTop();

        /* Вычисляем позицию */

        var disWidth = (winWidth - boxWidth) / 2
        var disHeight = scrollPos + 150;

        /* Добавляем стили к блокам */
        $('.popup-box').css({'width' : boxWidth+'px', 'left' : disWidth+'px', 'top' : disHeight+'px'});
        $('#blackout').css({'width' : winWidth+'px', 'height' : winHeight+'px'});

        return false;
    }


    $(window).resize(centerBox);
    $(window).scroll(centerBox);
    centerBox();


    $('[class*=popup-link]').click(function(e) {

        /* Предотвращаем действия по умолчанию */
        e.preventDefault();
        e.stopPropagation();

        /* Получаем id (последний номер в имени класса ссылки) */
        var name = $(this).attr('class');
        var id = name[name.length - 1];
        var scrollPos = $(window).scrollTop();

        /* Корректный вывод popup окна, накрытие тенью, предотвращение скроллинга */
        $('#popup-box-'+id).show();
        $('#blackout').show();
        $('html,body').css('overflow', 'hidden');

        /* Убираем баг в Firefox */
        $('html').scrollTop(scrollPos);
    });

    $('[class*=popup-box]').click(function(e) {
        /* Предотвращаем работу ссылки, если она являеться нашим popup окном */
        e.stopPropagation();
    });
    $('html').click(function() {
        var scrollPos = $(window).scrollTop();
        /* Скрыть окно, когда кликаем вне его области */
        $('[id^=popup-box-]').hide();
        $('#blackout').hide();
        $("html,body").css("overflow","auto");
        $('html').scrollTop(scrollPos);
    });
    $('.close').click(function() {
        var scrollPos = $(window).scrollTop();
        /* Скрываем тень и окно, когда пользователь кликнул по X */
        $('[id^=popup-box-]').hide();
        $('#blackout').hide();
        $("html,body").css("overflow","auto");
        $('html').scrollTop(scrollPos);
    });

    $('.popup_error').hide();

    $('.bottom_popup').click(function(){
        $name = $('#popup_form_name').val();
        $phone = $('#popup_form_phone').val();
        $email = $('#popup_form_email').val();
        $id = $('.bottom_popup').attr('data-id');

        $error = false;

        if($name == "")
        {
            $('#popup_form_name').css({'border':'1px solid #BB0000', 'box-shadow': '0 0 6px #ff0000'});
            $('.popup_error').show(500);
            $('.popup_error').attr('data-name', '1');
            $error = true;
        }

        if($phone == "")
        {
            $('#popup_form_phone').css({'border':'1px solid #BB0000', 'box-shadow': '0 0 6px #ff0000'});
            $('.popup_error').show(500);
            $('.popup_error').attr('data-phone', '1');
            $error = true;
        }

        if(!$error)
        {
            $.get("/orders/place/", {
                name: $name,
                phone: $phone,
                email: $email,
                id: $id
            }, function(data) {
                $('.ajax_popup').html(data);
                $('.request_3').click(function(){
                    var scrollPos = $(window).scrollTop();
                    /* Скрываем тень и окно, когда пользователь кликнул по X */
                    $('[id^=popup-box-]').hide();
                    $('#blackout').hide();
                    $("html,body").css("overflow","auto");
                    $('html').scrollTop(scrollPos);
                });
            });
        }
    });

    $('#popup_form_name').keypress(function(){
        $(this).css({'border':'1px solid #CFCFCF', 'box-shadow': 'none'});
        $('.popup_error').attr('data-name', '0');
        if($('.popup_error').attr('data-phone') == '0'){
            $('.popup_error').hide(500);
        }
    });
    $('#popup_form_phone').keypress(function(){
        $(this).css({'border':'1px solid #CFCFCF', 'box-shadow': 'none'});
        $('.popup_error').attr('data-phone', '0');
        if($('.popup_error').attr('data-name') == '0'){
            $('.popup_error').hide(500);
        }
    });
});