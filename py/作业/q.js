var a = 0;
    for(var i=1;i<=150;i++){
        if(i%3==0){
            a =i+"s"+ " ";
            document.write(a + " " + "<br>");
            continue;
        }
        if(i%5==0){
            a =i+"w"+ " ";
            document.write(a + " " + "<br>");
            continue;
        }
        if(i%7==0){
            a =i+"q"+ " ";
            document.write(a + " " + "<br>");
            continue;
        }
        a += i;
        document.write(i + " " + "<br>");
    }