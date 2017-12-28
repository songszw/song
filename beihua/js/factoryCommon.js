$(function(){
    var onoff = true;
    $('.stateTitle').height($('.classify').height())
    $('.classify ul li').on('click',function(){
        if(onoff){//开关判断多选单选
            //console.log(1)
            var i = $(this).index();
            $('.classify ul li span').removeClass('show').eq(i).addClass('show');
            $(this).addClass('active').siblings().removeClass('active');
        }else{
            //console.log(2)
            var i = $(this).index();
            $('.classify ul li span').eq(i).toggleClass('show');
            $(this).toggleClass('active');
        }
    })
    $('.more').on('click',function(){
        onoff=false
        $('.classify p').animate({'height':50});
        $('.stateTitle').animate({'height':117});
    })
    $('.confirm').on('click',function(){
        onoff = true
        $('.classify p').animate({'height':0});
        $('.stateTitle').animate({'height':67});
        //test();
    })
})