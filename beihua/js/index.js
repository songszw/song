/**
 * Created by songs on 2016/11/30.
 */
$(function () {
    /*
     * banner图
     */

    var bannerNum = 0;
    var bannerUl = $('.banner01 ul li').eq(0).width()*$('.banner01 ul li').length;
    $('.banner01 ul').css('width',bannerUl+'px')
    $('.bannerBtn li').each(function () {
        $(this).on('click',function () {
            bannerNum = $(this).index();
            $('.banner01 ul').animate({'left':-$('.banner01 ul li').eq(0).width()*bannerNum});
            addActive();
        })
    });
    var timer;
    timer = setInterval(function () {
        banner();
    },3000);
    $('.banner01').on('mouseover',function () {
        clearInterval(timer);
    });
    $('.bannerBtn ul').on('mouseover',function () {
        clearInterval(timer);
    });
    $('.banner01').on('mouseout',function () {
        timer = setInterval(function () {
            banner();
        },3000);
    });
    $('.bannerBtn ul').on('mouseout',function () {
        timer = setInterval(function () {
            banner();
        },3000);
    });
    function banner() {
        bannerNum++;
        addActive();
        $('.banner01 ul').animate({'left':-$('.banner01 ul li').eq(0).width()*bannerNum-1});
        if(bannerNum>=$('.banner01 ul li').length-1){
            $('.banner01 ul').animate({'left':0},0);
            bannerNum=0;
            addActive();
        }
    };
    function addActive() {
        $('.bannerBtn li').each(function () {
            $(this).removeClass('active');
        });
        $('.bannerBtn li').eq(bannerNum).addClass('active');
    };

    //-----------------导航二级菜单
    $('.navTitle>li').hover(function(){
        //alert(1);
        var i = $(this).index();
        $(this).addClass('title-active');
        $('.navTitle>li>div').eq(i).stop().animate({
            width: '430px'
        },1000)

    },function(e){
        var i = $(this).index();
        var o = e.relatedTarget || e.toElement;//判断下移动到的对象，移动到option上ie下是null，firefox等为undefined。。
        if (!o) return;//为option
        $(this).removeClass('title-active');
        $('.navTitle>li>div').eq(i).stop().animate({
            width: '0px'
        },0);
        $('#province').eq(i).css('display','none');
    });



$('.seekTitle li').on('click',function(){
    var i = $(this).index();
    $(this).addClass('seek-show').siblings().removeClass('seek-show');
    $('.int-seek p').eq(i).addClass('intSeek-show').siblings().removeClass('intSeek-show');
})
    // window.onload = function () {
    //     $("#select>option").click(function(){
    //         $("#select").removeAttr("size");
    //         $("#select").blur();
    //         // this.attr("selected","");
    //     });
    //
    //     $("#select").focus(function(){
    //         $("#select").attr("size","5");
    //     })
    // }

    /*
     交易动态上滚效果
     */
    function roll(con,scroll){
        var factoryScrollW = $(con).height();
        var i = 0,time = null;
        $(con).clone(true).insertBefore(con);
        time = setInterval(function(){
            i--;
            if(i <= -factoryScrollW){
                i=0;
            }
            $(scroll).css('top',i+'px');
        },40)
    }

    roll($('#factoryScrollCon1'),$('#factoryScrollCon'));
    roll($('#factoryScrollCo'),$('#factoryScrollCon2'));
    /*
     工厂直采点击切换
     */
    function tab(list,con){
        $(list).each(function(){
            $(this).click(function(){
                var i = $(this).index();
                $(this).addClass('active').siblings().removeClass('active');
                $(con).eq(i).addClass('show').siblings().removeClass('show');
            })
        })
        }
    tab($('.gas li'),$('.gasListCon ul'));
    tab($('.liquid li'),$('.liquidListCon ul'));
    tab($('.solid li'),$('.solidListCon ul'));
    /*
     * 点击变色
     */
         // $('body').on('click',function (e) {
         //     var _this = e.target;
         //     $(_this).parent().siblings().removeClass('active');
         //     $(_this).parent().addClass('active');
         //     console.log( $(_this).parent()siblings())
         // })
    /*
     * 物流/货主点击切换
     */
    $('.logisticsRightTop').find('li').each(function () {
        $(this).on('click',function () {
            $(this).addClass('active').siblings().removeClass('active');
        })
    });
    /*
     * 城市筛选
     */
    // function city(val,con,conList){
    //     $(val).click(function(ev){
    //         var ev = ev||event;
    //         ev.stopPropagation();
    //         $(con).css('display','block');
    //     });
    //     $(conList).click(function(){
    //         $(val).html($(this).html());
    //         $(this).addClass('cityShow').siblings().removeClass('cityShow');
    //         $(con).css('display','none');
    //     });
    //     $(conList).mouseover(function(){
    //         $(this).addClass('cityShow').siblings().removeClass('cityShow');
    //     });
    //     $(conList).mouseout(function(){
    //         $(this).addClass('cityShow').siblings().removeClass('cityShow');
    //     });
    //     $('body').on('click',function(){
    //         $(con).css('display','none');
    //     });
    // };
    // city($('.province p'),$('.province ul'),$('.province ul li'));
    // city($('.city p'),$('.city ul'),$('.city ul li'));
    // city($('.county p'),$('.county ul'),$('.county ul li'));

    //----------首页二级导航菜单
    // city($('.ccTable-province p'),$('.province'),$('.province li'));
    // city($('.ccTable-city p'),$('.cityCon'),$('.cityCon li'));
    // city($('.ccTable-county p'),$('.County'),$('.County li'));


isPlaceholer();
    //$('.ccTable-county>p').on('click',function(){
    //    $('.district').css('display','block');
    //})
    //$('.district>li').on('mouseover',function(){
    //
    //})
    /*
     * 设置cookie
     */
    /*
    function createCookie(name,value,days) {
        if (days) {
            var date = new Date();
            date.setTime(date.getTime()+(days*24*60*60*1000));
            var expires = "; expires="+date.toGMTString();
        }
        else var expires = "";
        document.cookie = name+"="+value+expires+"; path=/";
    }

    //读取cookie值
    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++)
        {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
    }
    var marsk = readCookie('marsk');
    if(marsk){
        $('.marsk').css('display','none');
        $('body').css('overflow','auto');
    }else {
        createCookie('marsk','true',1)
        $('.marsk').css('display','block');
    }

    //清空cookie
    function eraseCookie(name) {
        createCookie(name,"",-1);
    }
    // if(marsk=='true'){
    //     $('.marsk').css('display','block')
    // }else{
    //     $('.marsk').css('display','none')
    // }

    //弹出层

    $('.close').on('click',function () {
        $('.marsk').css('display','none');
        $('body').css('overflow','auto');
    });
    setTimeout(function () {
        $('.marsk').css('display','none');
        $('body').css('overflow','auto');
    },5000)
    */
});

//-----------回到顶部
$(function () {
    $('#top').click(function () {
        $('html,body').animate({
            scrollTop: 0
        },200);

    })
})

//---------------------------------------------注册Vip弹出层
// $(function(){
//     $('.order').on('click', function(){
//         $(".PopUp").css('display','block');
//         var html=document.documentElement;
//         $("html").css({overflow:"hidden"}); //禁用滚动条
//     });
//
//     $('.popupTitleabolish').on('click',function(){
//         $(".PopUp").css('display','none');
//         $("html,body").css({overflow:"visible"});
//     })
//     $('.sumBtn').on('click',function(){
//         $(".PopUp").css('display','none');
//         $("html,body").css({overflow:"visible"});
//     })
//     var x = 0;
//     $('.popupCon li').each(function(){
//         $(this).attr('onoff','true');
//         $(this).on('click', function () {
//             if($(this).attr('onoff')=='true'){
//                 $(this).addClass('active');
//                 x+=1;
//                 $(this).attr('onoff','false')
//             }else{
//                 $(this).removeClass('active');
//                 x-=1;
//                 $(this).attr('onoff','true')
//             }
//             $('.number').text(x*350);
//         })
//     })
//
// })