//1
// function sum(a,b,c){
//     return a+b+c
// }
// shiv=[1,2,3]
// sai=[1,1,1]
// yadav=[2,2,2]
// console.log(sum(...shiv));
// console.log(sum(...sai));
// console.log(sum(...yadav));

//2

// const name=(q)=>{
//     console.log('hello',q );
// }
// //3
// const power=(a,b)=>{
//     console.log(a**b);
// }

// //4
// let a=5
// const display=()=>{
//     console.log('global= ',a);
//     a=10
//     const display2=()=>{
//         console.log('given local = ',a);
//         console.log('given times 2= ',a*2);
//     }
//     display2()
// }

//5
// const factouter=(a)=>{
//     sum=a
//     i=1;
//     const fact=()=>{
//         sum=sum*(a-i);
//         i+=1;
//         if (i==a){
//             console.log(sum);
//         }
//         else {
//             fact()
//         } 
//     }
//     fact()
// }

//4
a=2
const num=()=>{
    return a
}
const square=()=>{
    return (a**2); 
}
const cube=()=>{
    return (num()*square());
}
console.log(num())
console.log(square())
console.log(cube())

