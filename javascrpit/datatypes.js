//Question-1 :   Input the distance in Kilometer and Convert into Meter and Centimeter.
// 1km=1000m
// 1km=100000cm
function km(num){
    num=1
    console.log("🚀 ~ file: data type practise.js:6 ~ Q1 ~ num:", num,)
    centi=num*100000
    console.log("🚀 ~ file: data type practise.js:7 ~ Q1 ~ centi:", centi)
    m=num*1000
    console.log("🚀 ~ file: data type practise.js:9 ~ Q1 ~ m:", m)
    console.log(num,"km")
    console.log(m,"meters")
    console.log(centi,"centimeters")

}


//Question-2:    WAP to input radius of a circle and log the area of circle.
//area=(22/7)*r*r
function area(r){
    r=1
    console.log("radius=",r)
    area=(22/7)*r*r
    console.log("area=",area)
}


//Question-6:    WAP to input n numbers and log the average of those number.
function avg(){
    const a=[1,2,3];
    i=1;
    sum=a[0];
    while (i){
        if (i<a.length){
            sum=sum+a[i];
        }
        else{
            break
        }
        i=i+1
    }
    console.log(sum);
    console.log(sum/a.length);
}
//


function amount(){


    x=10
    y=10
    total=x*y
    dis=total*0.1
    remain=total-dis
    console.log("total amount = ",x*y,"\ndiscount amount = ",x*y*0.1,"\namount after discount = ",(x*y)-(x*y*0.1) )
}
