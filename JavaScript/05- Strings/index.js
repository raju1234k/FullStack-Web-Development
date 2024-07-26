let myName="Raju"
let MySurname="Jayvant"

//REPLACE 
// console.log(myName.replace("Raju","ER. RAJU"))

// console.log(myName.includes("Raju"));

let fullName=`${myName} ${MySurname}`
// console.log(typeof fullName);
// console.log(fullName.__proto__);
// console.log(fullName);
//Constructor of string

// let completeName=new String("RAJU JAYVANT")
// console.log(completeName[0])
// console.log(completeName.substring(0,8))
// console.log(completeName.toLocaleLowerCase());
// console.log(completeName.__proto__);

// Charactor Position 
// console.log(completeName.charAt(1));

// console.log(completeName.indexOf('Y'));

// console.log(myName.slice(-7,5))

// TRIM TO CUT EMPTY SPACES 

// let str="       raju       "
// console.log(str.trim());
// console.log(str.trimStart())
// console.log(str.trimEnd());


let firstaname=`Raju 
kumar
surya
er 
raju 
jayvant `
let secondname='kumar'
console.log(length(firstaname))
console.log(firstaname)
console.log(firstaname + secondname)

let op1='Raju'
let op2='KUMAR'

let ans=`${op1}${op2}`
console.log(ans)
console.log(op1.length)
console.log(op1.toUpperCase())
console.log(op2.toLowerCase())
console.log(typeof(ans))
// indexing AND Slicing 

let nam='RAJU'
console.log(nam[0])
console.log(nam[1])
console.log(nam.substring(0,2))

let one='er raju jayvant '
let shdh=one.split(' ')
console.log(shdh)
console.log(shdh.join('"  "'))


console.log('For loop')
for(i=1;i<=10;i++){
    console.log(2*i)
}

console.log('while loop')
let j=1;
while(j<=10){
    console.log(2*j);
    j++;
}


console.log('do while loop')
let i=1;
do{
  console.log(2*i);
  i++;
}
while(i<=10)
let name1='Raju Kumar'
console.log(name1.substring(0))

let str='hello ji "\kaise"\ ho sare';
console.log(str.split(' '))
console.log(typeof(str))


