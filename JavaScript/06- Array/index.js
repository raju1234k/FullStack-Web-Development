
//OBJECT 

let obj={
    myname:"Raju",
    age:22,
    weight:54,
    sex:"Male",
    myname1:function(){
        console.log("Er. Raju Jayvant");
    }
}

// for (key in obj){
//     console.log(key ," ", obj[key]);
// }
console.log(obj)  
obj.myname1()

//SHIFT AND UNSHIFT METHOD

let array=['raju','kumar','surya','kuma']
array.unshift('raju');
console.log(array);

//SPLICE METHOD

console.log(array.splice(1,2));


// MAP METHOD

let arr=[20,25,30];
let ans =arr.map((Number)=>{
})
console.log(ans);

// FILTER METHOD

let arra=[1,2,3,'raju','kumar'];
let Finalans=arra.filter((value)=>{
    if(typeof (value) =='string'){
        return true;
    }
    else{
        return false;
    }
  
});
console.log(Finalans);


let Array=[1,2,3,4,5,6,7,8]
let Ans=Array.filter((value)=>{
    if((value)%2==0){
        return true
    }
})
console.log(Ans);

// MAP METHOD 

let firstArray=[10,20,30]
let answer =firstArray.map((Number)=>{
       return Number*Number
})
console.log(answer);


// REDUCE METHOD 


let secondArray=[10,20,30,40]
let ansWer=secondArray.reduce((acc,curr)=>{
    return acc+curr
},0)
console.log(ansWer);

// FOR EACH METHOD

let ThirdArray=[6,7,2,8,1,9]
let len=ThirdArray.length
for(let index=0;index < len;index++){
    console.log(ThirdArray[index]);
}


// FOR EACH METHOD


array.forEach((value,index)=>{
    console.log("number",value,"index no",index);
}) 


// SORT , INDEXOF , FIND METHOD 


array.sort()
console.log(array);
console.log(array.indexOf(1));
console.log(array.find((element) => element > 8));

let fourthArray=[1,2,3,4,5,6]
fourthArray.forEach((value,index)=>{
        console.log(value,index);
})


// FOR OF METHOD 


let finalArray=[10,20,30,40]
for (value of finalArray){
    console.log(value);
}

let string="raju"
for(val of string){
    console.log(val);
}