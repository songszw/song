/**
 * Created by Admin on 2017/3/24.
 */
$(function(){
    //左侧折叠菜单功能
    function menu(click,con){
        var offon = true;

        $(click).click(function(){
            if (offon){
                $(this).css('background','url("../img/userData/jiantou_up.png") 170px center no-repeat');
                $(con).css('display','none');
                offon = false;
            }else{
                $(this).css('background','url("../img/userData/arrow_two_up.png") 170px center no-repeat');
                $(con).css('display','block');
                offon = true;
            }
        })
    }
    menu($('.userManageA>p'),$('.userManageListA'));
    menu($('.userManageB>p'),$('.userManageListB'));
    menu($('.userManageC>p'),$('.userManageListC'));

    //---------------切换内容显示

    //
    // $('.accountData').height($('.modifyBefore').height());
    // $('.userContainer').height($('.modifyBefore').height());

    //
    // ($('.userManageListA>li')).each(function(){
    //     var i = $(this).index();
    //     $(this).click(function(){
    //         $('.navVal').text($(this).text());
    //         alert($(this))
    //         // //$('.ueserSet-up').height($('.userContainer li').eq(i).height());
    //         // $('.userContainer').height($('.userContainer li').eq(i).height());
    //         // //alert($('.ueserSet-up').height());
    //         $(this).addClass('active').siblings().removeClass('active');
    //         $('.userContainer>li').eq(i).addClass('shows').siblings().removeClass('shows');
    //         // if (i==1){
    //         //     $('.userContainer').height($('.Safety').height());
    //         //     $('.ueserSet-up').height($('.Safety').height());
    //         //
    //         // }else if(i==0){
    //         //     $('.userContainer').height($('.modifyBefore').height());
    //         //     $('.ueserSet-up').height($('.modifyBefore').height());
    //         // }else if(i==2){
    //         //     $('.userContainer').height($('.address').height());
    //         //     $('.ueserSet-up').height($('.address').height());
    //         // }
    //     })
    //
    //     //------------------点击head修改密码显示账户安全
    //     // $('.changePassword').on('click',function () {
    //     //     $('.userContainer>li').eq(1).addClass('shows').siblings().removeClass('shows');
    //     //     $('.userManageListA>li').eq(1).addClass('active').siblings().removeClass('active');
    //     //     $('.navVal').text("账户安全");
    //     //     $('.userContainer').height($('.Safety').height());
    //     //     $('.ueserSet-up').height($('.Safety').height());
    //     // })
    // })

    //-----------------------------输入框校验提示
function show(con){
    $(con).focus(function(){
        $(this).removeClass('grayshow');
        $(this).removeClass('redshow');
        $(this).addClass('blueshow');
    });
    $(con).blur(function(){
        $(this).removeClass('blueshow');
        if($(this).val()==''){
            $(this).addClass('redshow').removeClass('grayshow');
        }else {
            $(this).addClass('grayshow').removeClass('redshow','blueshow');
        }
    })

}
    show($('#username'));
    show($('#company-name'));
    show($('#address'));
    show($('#business'));
    show($('.assressName'));
    show($('.assressPhone'));
    show($('.assressCityName'));


//-------------------------------------------账户资料修改
//     $('.modify').click(function(){
//         $('.modifyBefore').css('display','none');
//         $('.modifyAfter').css('display','block');
//         $('.accountData').height($('.modifyAfter').height());
//         $('.userContainer').height($('.modifyAfter').height());
//         $('.ueserSet-up').height($('.modifyAfter').height());
//         console.log($('.modifyAfter').height());
//         $("html,body").scrollTop(0);//点击设置页面滚动条位置
//     })
//
//     $('.cancel').click(function(){
//         $('.accountData').height($('.modifyBefore').height());
//         $('.userContainer').height($('.modifyBefore').height());
//
//         $('.modifyBefore').css('display','block');
//         $('.modifyAfter').css('display','none');
//         $("html,body").scrollTop(0);//点击设置页面滚动条位置
//     });
//
//     $('.Storage').click(function(){
//         $('.modifyBefore').css('display','block');
//         $('.modifyAfter').css('display','none');
//         $('.accountData').height($('.modifyBefore').height());
//         $('.userContainer').height($('.modifyBefore').height());
//         $('.ueserSet-up').height($('.modifyBefore').height());
//
//         $("html,body").scrollTop(0);//点击设置页面滚动条位置
//
//
//         $('#usernames').text($('#username').val());//账户姓名
//         $('#name').text($('#username').val());//账户姓名
//
//         $('#company-names').text($('#company-name').val());//公司名称
//         //$('#addresss').text($('#address').val());//地址
//         //$('#provinces').text($('#province').val());//省份
//         //$('#citys').text($('#city').val());//市
//         //$('#districts').text($('#district').val());//区县
//         $('#businesss').text($('#business').val());//主营业务
//         $('#yyzzs')[0].src=$('#yyzz')[0].src;
//         $('#khxkzs')[0].src=$('#khxkz')[0].src;
//         $('#ybnsrzms')[0].src=$('#ybnsrzm')[0].src;
//         $('#wxhxps')[0].src=$('#wxhxp')[0].src;
//         $('#kpxxs')[0].src=$('#kpxx')[0].src;
//         $('#zzjgs')[0].src=$('#zzjg')[0].src;
//         $('#swdjs')[0].src=$('#swdj')[0].src;
//
//     });


//    ------------账户安全




    //----------------------点击修改账号显示修改内容
function Safety(){
    var offon = true;
    $('.modifyButtonA').click(function(){

        if (offon){
            $('.ShowBtnA').removeClass('activeBtn');
            $('.foldBtnA').addClass('activeBtn');
            $('.phoneInputA').css('display','block');
            $('.ueserSet-up').height($('.Safety').height());
            offon = false;
        }else {
            $('.foldBtnA').removeClass('activeBtn');
            $('.ShowBtnA').addClass('activeBtn');
            $('.phoneInputA').css('display','none');
            $('.ueserSet-up').height($('.Safety').height());

            offon = true;
        }

    });
}

    Safety();
//-------------------------------点击修改密码显示修改密码内容快
    function password(){
        var offon = true;
        $('.modifyButtonB').click(function(){

            if (offon){
                $('.ShowBtnB').removeClass('activeBtn');
                $('.foldBtnB').addClass('activeBtn');
                $('.phoneInputB').css('display','block');
                $('.ueserSet-up').height($('.Safety').height());
                offon = false;
            }else {
                $('.foldBtnB').removeClass('activeBtn');
                $('.ShowBtnB').addClass('activeBtn');
                $('.phoneInputB').css('display','none');
                $('.ueserSet-up').height($('.Safety').height());

                offon = true;
            }

        });
    }

    password();


    //--------------------手机号码验证
    function phoneNumber(){
        var number = /^1(3|4|5|7|8)\d{9}$/;//验证手机号
        $('#beforePhone').blur(function(){
            if (number.test($(this).val())){
                $('.phoneMarkA').css('display','block');
                $('.MarkTextA').css('visibility','hidden')

            }else{
                $('.MarkTextA').css('visibility','visible')
                $('.phoneMarkA').css('display','none');

            }
        })



        //------------------------手机号下一步
        $('.nextBtnA').click(function(){
            if (number.test($('#beforePhone').val())&&$('#beforePhone')!=''){
                $('.phoneCheckA').removeClass('showb');
                $('.phoneCheck').addClass('showb');
            }else {
                $('.MarkTextA').css('visibility','visible')
                $('.phoneMarkA').css('display','none');
            }
        });


        //-----------------------------提交修改手机号码
        $('#submitBtn').on('click',function(){
            if($('#phoneNumber').val()!=""&&$('#telText').val()!=""){
               $('.marktexta').css('visibility','visible');
               setTimeout(function () {
                       $('.foldBtnA').removeClass('activeBtn');
                       $('.ShowBtnA').addClass('activeBtn');
                       $('.phoneInputA').css('display','none');
                       $('.ueserSet-up').height($('.Safety').height());
               },3000)
            }
        })

        var passW = /^[\w]{6,20}$/;//验证密码
        $('#beforePassW').blur(function(){
            if(passW.test($(this).val())){
                $('.phoneMarkB').css('display','block');
                $('.MarkTextB').css('visibility','hidden');

            }else {
                $('.MarkTextB').css('visibility','visible');
                $('.phoneMarkB').css('display','none');

            }
        })
            $('.nextBtnB').click(function(){
                if (passW.test($('#beforePassW').val())){
                    $('.passwordCheckA').removeClass('showc');
                    $('.passwordCheck').addClass('showc');
                    //$('.phoneInputB').height($('.passwordCheck').height())
                }
            });
//---------------------------------确认修改密码
        $('#submitBtna').on('click',function(){
            if ($('#passwordA').val()==$('#passwordB').val()){
                $('.passwordMark').css('visibility','visible');
                setTimeout(function () {
                    $('.foldBtnB').removeClass('activeBtn');
                    $('.ShowBtnB').addClass('activeBtn');
                    $('.phoneInputB').css('display','none');
                    $('.ueserSet-up').height($('.Safety').height());
                },3000)
            }else {
                alert('请输入正确密码');
            }
        })

    }
    phoneNumber();





    
    //-------------------------------收获地址

    function map() {
        // 百度地图API功能
        var map = new BMap.Map("allmap");
        var point = new BMap.Point(116.4163340000,40.0018680000);
        var city = document.getElementById("cityName");
        map.centerAndZoom(point,15);
//        map.panBy(214,130);
        function theLocation(){
            var city = document.getElementById("cityName").value;
            if(city != ""){
                map.centerAndZoom(city,11);      // 用城市名设置地图中心点
            }
            // 创建地址解析器实例
            var myGeo = new BMap.Geocoder();
            // 将地址解析结果显示在地图上,并调整地图视野
            myGeo.getPoint(city, function(point){
                if (point) {
                    var x = point.lng;
                    var y = point.lat;
                    map.centerAndZoom(point, 16);
                    map.addOverlay(new BMap.Marker(point));

                    $('#latAndlog').val(x+','+y);
                    console.log(point.lng,point.lat);

                }else{
                    alert("请输入正确地址");
                }
            }, "北京市");
        }
        map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
        var x = 116.4163340000;
        var y = 40.0018680000;
        var ggPoint = new BMap.Point(x,y);
        map.centerAndZoom(ggPoint, 20);
//        map.addControl(new BMap.NavigationControl());//添加缩放按钮
        var markergg = new BMap.Marker(ggPoint);
        map.addOverlay(markergg); //添加谷歌marker
        city.onblur=function(){
            theLocation();
        }
    }

    $('.NewBtn').click(function () {
        $('.addressCon').css('display','block');
        $('.userContainer').height($('.address').height());
        $('.ueserSet-up').height($('.address').height());
        map();

        var number = /^1(3|4|5|7|8)\d{9}$/;//验证手机号
        $('.assressPhone').blur(function(){
            if (number.test($(this).val())){

            }else {
                alert('请输入正确手机号码')
            }
        })


    });
    //--------------------------------添加收货地址
    function append() {

        var number = /^1(3|4|5|7|8)\d{9}$/;//验证手机号
        $('.assressPhone').blur(function(){
            if (number.test($(this).val())){

            }else {
                alert('请输入正确手机号码')
            }
        })

        $('.addressStorage').on('click',function(){
            // var con = "<li class='receiver'>"+$('.assressName').val()+"</li>"+
            //     "<li class='County'>"+$('.assressProvince').val()+"，"+
            //     $('.assressCity').val()+"，"+$('.assressDistrict').val()+"</li>"+
            //     "<li class='street'>"+$('.assressCityName').val()+"</li>"+
            //     "<li class='phoneNum'>"+$('.assressPhone').val()+"</li>"+
            //     "<li class='operating'><span class='addressModify'>修改</span>&nbsp;|&nbsp;<span class='dele'>删除</span></li>";
                if($('.assressName').val()==''||$('.assressPhone').val()==''||$('.assressCityName').val()==''){
                    alert('请输入完整信息');
                }else {
                    $('.addressCon').css('display','none');
                    // $('.addressList').append("<ul class='addressListCon'>"+con+"</ul>");

                }

        });

    }
    append();
    function save() {
        $('.addressSave').on('click',function () {
            $('.addressCon').css('display','none');
            $('.userContainer').height($('.address').height());
            $('.ueserSet-up').height($('.address').height());
        })
    }
    save();
    //--------------------------------删除收货地址

    function dele() {
        $('.addressList').on('click','li .dele',function (ev) {
            i = ev.target;
            var mark = confirm("确认删除该收获地址吗？");
            if (mark==true){
                $(i).parent().parent().remove();
            }
        })
    }

    dele();
    //---------------------------------修改收货地址
    function modify() {
        $('.addressList').on('click','li .addressModify',function (ev) {
            i = ev.target;
            $('.addressCon').css('display','block');
            $('.userContainer').height($('.address').height());
            $('.ueserSet-up').height($('.address').height());
            $('.assressName').val($(i).parent().parent().children('.receiver').text());
            $('.assressPhone').val($(i).parent().parent().children('.phoneNum').text());
            $('.assressCityName').val($(i).parent().parent().children('.street').text());
            console.log($(i).parent().parent().children('.receiver').text());

            map();

        })
    }
    modify();
})



//---------------资质上传

    $(function(){
        function getObjectURL(file) {
            var url = null;
            if (window.createObjectURL != undefined) {
                url = window.createObjectURL(file)
            } else if (window.URL != undefined) {
                url = window.URL.createObjectURL(file)
            } else if (window.webkitURL != undefined) {
                url = window.webkitURL.createObjectURL(file)
            }
            return url
        };

        function imgUpload(file,bg,again){
            $(file).on("change",function(){
                var format = this.value.toLowerCase().split('.');//判断图片格式
                var fileSize = this.files[0].size;
                var srcs = getObjectURL(this.files[0]);   //获取路径
                if(fileSize<1024*1024*2&&(format[format.length-1]=='jpg'||format[format.length-1]=='png')){
                    $(bg).css('display','none');
                    $(this).nextAll(".img2").show();  //fireBUg查看第二次换图片不起做用
                    $(this).nextAll(".img2").attr("src",srcs);    //this指的是input
                    $(again).css('display','block');
                }else {
                    alert('只支持JPG、PNG,大小不超过2M。');
                    return false;
                }
            })
        }
        imgUpload($('.filepathA'),$('.bgA'),$('.againA'));
        imgUpload($('.filepathB'),$('.bgB'),$('.againB'));
        imgUpload($('.filepathC'),$('.bgC'),$('.againC'));
        imgUpload($('.filepathD'),$('.bgD'),$('.againD'));
        imgUpload($('.filepathE'),$('.bgE'),$('.againE'));
        imgUpload($('.filepathF'),$('.bgF'),$('.againF'));
        imgUpload($('.filepathG'),$('.bgG'),$('.againG'));

    })



