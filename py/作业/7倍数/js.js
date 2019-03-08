var max=0;
var sum=0;

for(var i=1;i<=100;i++){
    if(i%7==0){
    max +=i;
    sum +=1;
    }
}
document.write(max+"<br>");
document.write(sum);