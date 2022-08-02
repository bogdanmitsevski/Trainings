console.log(typeof 42);
const sentence = "Bohdan";
console.log(`My name is ${sentence}`);
console.log(typeof sentence);
const newUser = () => {
    console.log(sentence);
}

newUser();

let list = [1,2,3];
console.log(list);

let multipleArray = [1,2,3, "Bohdan", true];
console.log(multipleArray);
console.log(typeof multipleArray);

type Name = string;
let id: Name;
id = "hello";
console.log(typeof id);