for(var i=1;i<=100;i++){
    for(var n=2;n<=i;n++){
        if(i%n==0&&i!=n) {
            break;
        }
        else if(i==n){
            document.write(i+" ");
        }
    }
}
