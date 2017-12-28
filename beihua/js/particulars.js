/**
 * Created by dong on 2016/9/30.
 */
$(function(){
    $(".subnavCon_img").click(function(){
        var x=$(".subnavCon_img").index(this);
        var m=$(".subnavCon_img img").eq(x).attr("src");
        $('.subnavCon_img').eq(x).addClass('show_a').siblings().removeClass('show_a');
        $(".conO_a_img img").attr("src",m);
    });
    var subnavCon_imgW = $('.subnavCon_img').width()+4;
    var i = 0;
    $(".subnav_l").click(function(){
        if(i>0){
            i--;
            $(".stubnav_r").removeAttr("disable");
            $(".subnav_con").animate({"scrollLeft":subnavCon_imgW*i})
        }else{
            $(".stubnav_l").attr("disable","true");
        };
    });

    $(".subnav_r").click(function(){
        if (i>=$('.subnavCon_img').length-4){
            $(".stubnav_r").attr("disable","true");
        }else{
            i++;
            $(".stubnav_l").removeAttr("disable");
        };
        $(".subnav_con").animate({"scrollLeft":subnavCon_imgW*i})
    });
});
$(function(){
   $('#submenuTypeAb').click(function(){
       $('#submenuTypeAb').addClass('showb').siblings().removeClass('showb');
       $('#submenuTypeBb').hide();
       $('#submenuTypeBa').show();
   })
    $('#submenuTypeA_a').click(function(){
        $('#submenuTypeA_a').addClass('showb').siblings().removeClass('showb');
        $('#submenuTypeBb').show();
        $('#submenuTypeBa').hide();
    })
    $('.submenuTypeBa_1').click(function(){
        $('.submenuTypeBa_1').addClass('showc');
        $('.submenuTypeBa_2').removeClass('showc');
    })
    $('.submenuTypeBa_2').click(function(){
        $('.submenuTypeBa_2').addClass('showc');
        $('.submenuTypeBa_1').removeClass('showc');
    })
});
$(function(){
    //String.prototype.trim=function(){
    //    return this.replace(/(^\s*)|(\s*$)/g,"");
    //};
    $('#con_ton').click(function(){
        // $('#con').slideToggle(500);
        $('#ton_list').show();
        $('.icn_ton_a').hide();
        $('.icn_ton_b').show();
    });
    $('#ton_list li').click(function(){
        $("#con_ton").html($(this).html());
        $('#ton_list').hide();
        $('.icn_ton_a').show();
        $('.icn_ton_b').hide();
        $('#ipt').val('1');
       })
})