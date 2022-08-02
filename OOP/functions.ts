const createPassword = (name: string,age?: number | string) => 
console.log(`${name} ${age}`);

createPassword('Bohdan', 21);

const createSkills = (name: string, ...skills: Array <string>) =>
console.log(`${name} knows ${skills.join()}`);

createSkills('Bohdan', 'JS','TS', 'Python', 'OOP');

const voidFunc = (): void =>{
    console.log('voidFunction');
}

voidFunc();

const msg = 'hello';
const error = (msg: string): never => {
    throw new Error(msg);
};

let myFunc;
function oldFunc(name?: string):void {
    console.log(`Hello, nice to meet you, ${name}`);
}

myFunc = oldFunc;
myFunc('Bohdan');