$(function(){
    var numbers = /^1(3|4|5|7|8)\d{9}$/;//验证手机号
    var NAME = /^([\u4e00-\u9fa5]){2,7}$/;//验证姓名
    var passW = /^[\w]{6,20}$/;//验证密码
    $('.name_a').focus(function(){
        //----------------------获取焦点改变输入框的颜色
        $('.name_a').addClass('tel_a').removeClass('tel_c');
    })
    $('.name_a').blur(function(){
        if(NAME.test(this.value)){
            $('.name_a').addClass('tel_a').removeClass('tel_c');
        }else{
            $('.name_a').addClass('tel_c').removeClass('tel_a');
        }
    })
    $('.tel').focus(function(){
        $('.tel').addClass('tel_a').removeClass('tel_c');
    })
    $('.tel').blur(function(){//---------验证手机号码
        if(numbers.test(this.value)){
            $('.tel').addClass('tel_a').removeClass('tel_c');
        }else{
            $('.tel').addClass('tel_c').removeClass('tel_a');
        }
    })
    $('.authCode_one').focus(function(){
        //-------------获取焦点的时候改变输入框的颜色
        $('.authCode_one').addClass('authCode_ok').removeClass('authCode_wrong');
    })
    $('.authCode_one').blur(function(){//失去焦点
        var code = /^\d{4}$/;//验证码格式
        if(code.test(this.value)){//验证输入框的内容
            $('.authCode_one').addClass('authCode_ok').removeClass('authCode_wrong');
        }
        else{
            $('.authCode_one').addClass('authCode_wrong').removeClass('authCode_ok');
        }
    })
        //debugger;打断点
    //--------------------------------获取验证码 函数
    $(function(){
        var onoff = true;
        function Cli(){
            var time = null;
            var i = 30;
            onoff = false;
            time=setInterval(function(){
                i--;
                $('.click').html(i+"s后再次发送").css({"background":"#ccc","color":"#fff"});
                if(i<20){
                    $('.hint').html('<span class="hint_a">✔</span>&nbsp;验证码发送成功请注意查收');
                }
                if(i==0){
                    clearInterval(time);
                    onoff = true;
                    $('.click').html("获取验证码").css({"background":"#fff","color":"#ff7f20"});
                }
            },1000)
        };
        //-----------------------绑定点击事件    调取上面函数
        $('.click').click(function(){
            if(onoff){
                Cli();
            }
        })
    })
    $('.pass_a').focus(function(){
        $('.pass_a').addClass('tel_a').removeClass('tel_c').css('border','1px solid #fff');
    })
    $('.pass_a').blur(function(){
        if(passW.test(this.value)){
            $('.pass_a').addClass('tel_a').removeClass('tel_c').css('border','1px solid #fff');
        }else {
            $('.pass_a').addClass('tel_c').removeClass('tel_a');
        }
    })
    })
