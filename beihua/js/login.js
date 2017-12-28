/**
 * Created by Admin on 2017/3/2.
 */
$(function(){

    var onoff = true;
    $('.click').on('click',function(){
        if (onoff){
            $(this).addClass('clickBg');
            onoff = false;
        }else {
            $(this).removeClass('clickBg');
            onoff = true;
        }
//            $(this).toggleClass('clickBg')
    })

    $('.userName input').on('focus',function(){
        $(this).addClass('ipt-Border');
    });
    $('.userName input').on('blur',function(){
        $(this).removeClass('ipt-Border');
    })


    $('.password input').on('focus',function(){
        $(this).addClass('ipt-Border');
    });
    $('.password input').on('blur',function(){
        $(this).removeClass('ipt-Border');
    })

    $('.button').on('click',function(){
        if($('.userName input').val() && $('.password input').val()!=''){
            alert('登录成功')
            $('.hint').css('visibility','hidden');
        }else {
            $('.hint').css('visibility','visibility');
//                alert("登录名或者密码不能为空")
        }
    })
})