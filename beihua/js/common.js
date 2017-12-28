/*
 * Created by songs on 2016/11/25.
 */
function isPlaceholer(){
    var input = document.createElement("input");
    return "placeholder" in input;
};
function placeholder(input){
    var text = input.attr('placeholder'),
        defaultValue = input.defaultValue;
    if(!defaultValue){
        input.val(text).addClass("phcolor");
    }
    input.focus(function(){
        if(input.val() == text){
            $(this).val("");
        }
    });
    input.blur(function(){
        if(input.val() == ""){
            $(this).val(text).addClass("phcolor");
        }
    });
    //输入的字符不为灰色
    input.keydown(function(){
        $(this).removeClass("phcolor");
    });
};
//当浏览器不支持placeholder属性时，调用placeholder函数
if(!isPlaceholer()){
    $('input').each(function(){
        text = $(this).attr("placeholder");
        if($(this).attr("type") == "text"){
            placeholder($(this));
        }
    });
};