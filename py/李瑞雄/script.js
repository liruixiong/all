$(function () {
    $('#btn1').click(function () {
        var txt01 = $('#txt1').val();
        var txt02 = $('#txt2').val();
        var $li = $('<li><span>' + txt01 + '</span><span>' + txt02 + '</span><a href="javascript:;" class="del">删除</a></li>');
        $li.appendTo('#list');
    });
    $('#list').delegate('a', 'click', function () {
        var handler = $(this).attr('class');
        switch (handler) {
            case 'del':
                var txt = $(this).parent().children(':first').html();
                if (confirm('你确定要删除"' + txt + '"吗？')) {
                    $(this).parent().remove();
                }
                break;
        }
    });
});