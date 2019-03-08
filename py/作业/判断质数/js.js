 var num = prompt("请输入一个数:");
            var flag = true;
            while(num<=1 || isNaN(num)){
                alert("这个数不合法");
                var num = prompt("请重新输入：");
            }
                for(var i = 2 ; i<num ; i++){
                    if(num%i == 0){
                        var flag = false;
                        break;
                    }
                 }
            if(flag){
            alert(num+"是质数");
            }else{
                alert("这个数不是质数");
            }