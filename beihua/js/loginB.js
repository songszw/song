/**
 * Created by dong on 2016/10/17.
 */
//---------------------------资质预览
$(function(){
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
//-----------------------------选择城市
$(function(){
    //--------------------------展示省份
    $.each(province,function(k,p){
        var option = "<option value='"+ p.ProID+"'>"+ p.ProName+"</option>";
        $('#province').append(option);
    })
    $('#province').change(function(){
        var selValue = $(this).val();
        $('#city option:gt(0)').remove();
        $('#district option:gt(0)').remove();
        //-----------------------展示城市
        $.each(city,function(k,p){
            if (p.ProID==selValue){
                var option = "<option value='"+ p.CityID+"'>"+ p.CityName+"</option>"
                $('#city').append(option);
            }
        })
        $('#city').change(function(){
            var selValue = $(this).val();
            $('#district option:gt(0)').remove();
            //----------------------展示区县
            $.each(District,function(k,p){
                if(p.CityID==selValue){
                    var option = "<option value='"+ p.Id+"'>"+ p.DisName+"</option>"
                    $('#district').append(option);
                }
            })
        })
    })
})
//---------------------------选择企业类型
//$(function(){
//    $('#myselect_val').click(function(){
//        $('#myselect_list').css('display','block');
//    });
//    $('#myselect_list li').click(function(){
//        $('#myselect_val').html($(this).html());
//        $(this).addClass('myselect_show').siblings().removeClass('myselect_show');
//        $('#myselect_list').css('display','none');
//    })
//
//});


//---------------------------关注产品

$(function(){
    $('.attentionButton').on('click',function(){
        $(this).css('display','none');
        $('.attentionCon').css('overflow','visible');
        $('.attention').height($('.attentionShow').height());
    })
        $('.attentionShow li').each(function(){
            $(this).attr('onoff','true');
            var i = null;
            $(this).on('click', function () {
                if($(this).attr('onoff')=='true'){
                    i +=1;
                    $(this).addClass('active');
                    $(this).attr('onoff','false');
                }else{
                    i -=1;
                    $(this).removeClass('active');
                    $(this).attr('onoff','true')
                }
            })
        })

    // $('#submit').click(function () {
    //
    //     if($('#khxkz').attr('src')==!''&&){
    //         alert(1);
    //     }else {
    //         alert(2)
    //     }
    // })

})
