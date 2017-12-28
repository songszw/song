/**
 * Created by Emma on 2016/9/21.
 */
$(function(){//搜索框
    $('.seeka li').click(function(){
        var i = $('.seeka li').index(this);//设置下标
        $(this).addClass("show").siblings().removeClass("show");
        if(i==0){
            $('.seekb_a').show();
            $('.seekb_b').hide();
        }
        else{
            $('.seekb_b').show();
            $('.seekb_a').hide();
        }
    });
})