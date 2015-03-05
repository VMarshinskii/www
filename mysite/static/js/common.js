$(document).ready(function(){

    jQuery.each($("#basccc .sliderkit-panels img"), function(){
        $("#basccc .sliderkit-panels img").css({"width":"auto", "height":"290px"})
    });
    jQuery.each($("#basccc .sliderkit-nav img"), function(){
        $("#basccc .sliderkit-nav img").css({"width":"auto", "height":"82px"})
    });
    var winWidth = $(window).width();
    if (winWidth >= 1250) {
        $(".inside-block").css({"width": "1210px"});
        $("#categories figure").css({"margin":"0 95px 0 0"});
        $("#categories figure:last-child").css({"margin":"0"});
        $(".shop-item:nth-child(2n)").css({"margin-right":"21px"});
        $(".shop-item:nth-child(3n)").css({"margin-right":"0"});
        $("#categories2 figure").css({"margin":"0 130px 0 0"});
        $("#categories2 figure:last-child").css({"margin":"0"});

        //cart
        if ($("#center-page-content").hasClass("isCart")) {
            $("#center-page-content").removeClass("cart-page");
            $("#right-page-content").removeClass("null-width");
            $("#cart-small").html(" ");    
        };
    }
    else {
        $(".inside-block").css({"width": "960px"});
        $("#categories figure").css({"margin":"0 8px 0 0"});
        $("#categories figure:last-child").css({"margin":"0"});
        $(".shop-item:nth-child(3n)").css({"margin-right":"21px"});
        $(".shop-item:nth-child(2n)").css({"margin-right":"0"});
        $("#categories2 figure").css({"margin":"0 47px 0 0"});
        $("#categories2 figure:last-child").css({"margin":"0"});

        //cart
        if ($("#center-page-content").hasClass("isCart")) {
            $("#center-page-content").addClass("cart-page");
            $("#right-page-content").addClass("null-width");
            $cont = $("#right-page-content").html();
            $("#cart-small").html($cont);
        };
    }


    $('header #header-menu nav ul li ul').mouseover(function(){
        $(this).parent().addClass("tcurrent");
    });
    $('header #header-menu nav ul li ul').mouseleave(function(){
        $(this).parent().removeClass("tcurrent");
    });


    var carousel = $("#carousel").featureCarousel({
        containerWidth: 220,
        containerHeight: 125,
        largeFeatureWidth: 139,
        largeFeatureHeight: 103,
        smallFeatureWidth:    96,
        smallFeatureHeight:   89,
        sidePadding: 10,
        topPadding: 0,
        smallFeatureOffset: 15,
        autoPlay: false
    });

    $("#window-wrap").click(function(e) {
        if($(e.target).closest("#window").length==0) {
            $('#window-wrap').hide();
            $('#window').hide();
        }
    });


    $("#categories .inside-block figure").hover(
        function(){
            $img = $(this).children('a').children('img');
            $img.css({"transform":"scale(1.0)"});
        }, 
        function(){
            $img = $(this).children('a').children('img');
            $img.css({"transform":"scale(0.95)"});
        }
    );

    $("div#basiccc").slideViewerPro({
        thumbs: 3,
        thumbsActiveBorderColor: "#24aa98",
        buttonsWidth: 1,
        thumbsRightMargin: 8,
        thumbsPercentReduction: 30,
    });
    $(".cart-full-img").removeAttr("style");
    $(".cart-right > div").removeAttr("style");

    $("select").change(function(){
        $.get("/catalog/ajax/filter/", {
            type: $("#ajax_form_type").val(),
            year: $("#ajax_form_year").val(),
            model: $("#ajax_form_model").val()
        }, function(data) {
            $('article').html(data);
        });
    });

    $(".slick-slide img").live('click', function(){
        var img = $(this).attr("src");
        $(".galeryBoxImg img").attr("src", img);
        $(".slick-slide-active").removeClass("slick-slide-active");
        $(this).addClass("slick-slide-active");
    });

});

$(window).resize(function(){
    var winWidth = $(window).width();
    if (winWidth >= 1250) {
        $(".inside-block").css({"width": "1210px"});
        $("#categories figure").css({"margin":"0 95px 0 0"});
        $("#categories figure:last-child").css({"margin":"0"});
        $(".shop-item:nth-child(2n)").css({"margin-right":"21px"});
        $(".shop-item:nth-child(3n)").css({"margin-right":"0"});
        $("#categories2 figure").css({"margin":"0 130px 0 0"});
        $("#categories2 figure:last-child").css({"margin":"0"});

        //cart
        if ($("#center-page-content").hasClass("isCart")) {
            $("#center-page-content").removeClass("cart-page");
            $("#right-page-content").removeClass("null-width");
            $("#cart-small").html(" ");    
        };
    }
    else {
        $(".inside-block").css({"width": "960px"});
        $("#categories figure").css({"margin":"0 8px 0 0"});
        $("#categories figure:last-child").css({"margin":"0"});
        $(".shop-item:nth-child(3n)").css({"margin-right":"21px"});
        $(".shop-item:nth-child(2n)").css({"margin-right":"0"});
        $("#categories2 figure").css({"margin":"0 47px 0 0"});
        $("#categories2 figure:last-child").css({"margin":"0"});

        //cart
        if ($("#center-page-content").hasClass("isCart")) {
            $("#center-page-content").addClass("cart-page");
            $("#right-page-content").addClass("null-width");
            $cont = $("#right-page-content").html();
            $("#cart-small").html($cont);
        };
    }
});




(function($) {
    $(function() {

        $('select').selectbox();

        $('#add').click(function(e) {
            $(this).parents('div.section').append('<br /><br /><select><option>-- Выберите --</option><option>Пункт 1</option><option>Пункт 2</option><option>Пункт 3</option><option>Пункт 4</option><option>Пункт 5</option></select>');
            $('select').selectbox();
            e.preventDefault();
        })

        $('#add2').click(function(e) {
            var options = '';
            for (i = 1; i <= 5; i++) {
                options += '<option>Option ' + i + '</option>';
            }
            $(this).parents('div.section').find('select').each(function() {
                $(this).append(options);
            })
            $('select').trigger('refresh');
                e.preventDefault();
        })

        $('#che').click(function(e) {
            $(this).parents('div.section').find('option:nth-child(5)').attr('selected', true);
            $('select').trigger('refresh');
            e.preventDefault();
        })

        $('input.styled').checkbox();

            $('#add').click(function() {
                var inputs = '';
                for (i = 1; i <= 5; i++) {
                    inputs += '<br /><label><input type="checkbox" name="checkbox" class="styled" /> checkbox ' + i + '</label>';
                }
                $('form').append(inputs);
                $('input.styled').checkbox();
                return false;
            })

            $('#disabled').click(function() {
                (function($) {
                    $.fn.toggleDisabled = function() {
                        return this.each(function() {
                            this.disabled = !this.disabled;
                        });
                    };
                })(jQuery);
                $('input.styled').toggleDisabled().trigger('refresh');
                return false;
            })

            $('#checked').click(function() {
                (function($) {
                    $.fn.toggleChecked = function() {
                        return this.each(function() {
                            this.checked = !this.checked;
                        });
                    };
                })(jQuery);
                $('input.styled').toggleChecked().trigger('refresh');
                return false;
            })
    })
})(jQuery)

