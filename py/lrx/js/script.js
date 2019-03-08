$.ajax({
    url: 'js/data.json',
    type: 'get',
    dataType: 'json'
})
    .done(function(data) {
        if(data.code == 200){
            console.log(data);
            // alert(data.result.length);//10条数据
            $('.list').empty();//先清空列表
            //模拟搜索联想，循环插入新列表
            for(var i=0; i<data.data.length; i++){
                var $li = $('<li><img src="'+data.data[i].imgUrl+'"><b>'+data.data[i].price+'</b><br><a href="#">'+data.data[i].name+'</a> <input type="submit" value="添加到购物车"></li>');
                $li.appendTo('.list');
            }
        }
    })
    .fail(function() {
        alert('连接超时！请重试');
    });