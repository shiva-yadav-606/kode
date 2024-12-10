//assignment operators
// if ("2"===2){
//     console.log("true");
// }

// if ("2"!==2){
//     console.log("true");
// }

//ternery operator
// msg=('2'===2)?"true":"false"
// console.log(msg);

//destructuring operators
// let arr=[1,2,3]
// let [a,b,c]=arr
// console.log(a,b,c);

//spread operator
// let arr=[1,2,3,4,5,6]
// let [a,...rest]=arr
// console.log(a,rest);

// let arr1 =[1,2,3,4]
// function add(x,y,z){
//     console.log(x+y+z);
// }
// add(...arr1)

// let arr=[1,2,3]
// let obj={...arr}
// console.log(obj);

// let obj={1:'shiva',2:'sai'}
// console.log({...obj,2:'yadav'});


//1
function compare(x,y){
    if (x==y){
        console.log("equal");
    }
    else {
        if (x<y){
        console.log(y,' is greater');       
        }
        else {
        console.log(x,' is greater');
        }
    }
}
//2
// (x,y)=(1,2)
// x=1;y=3;
// more=(x>y)?console.log(x," is great"):console.log(y," is great")
//3
obj={1:'shiva',2:'sai'}
console.log(obj);
if (1 in obj){
    console.log('yes');
}






