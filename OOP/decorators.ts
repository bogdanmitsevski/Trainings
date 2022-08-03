//class Decorator
const logClass = (constructor: Function) =>{
    console.log(constructor);
 }
 
 @logClass
 class User {
    constructor (
       public name:string,
       public age: number
    ) {}
 
    public getPass():string {
       return `${this.name}${this.age}`;
    }
 }
 
 const user = new User('Bohdan',21);
 console.log(user.getPass());
 
 //class Property
 
 const logProperty = (target: Object, propertyKey: string | symbol) => {
    console.log(propertyKey);
 }
 
 class User1 {
       @logProperty
       public secret: number;
    constructor (
       public name: string,
       public age: number,
       secret: number
    )
    {
       this.secret = secret;
    }
 
     public getPass():string {
       return `${this.name}${this.age}`;
    }
 }
 
 // Method Decorator
 
 const logMethod = (target: Object, propertyKey: string | symbol, descriptor: PropertyDescriptor) => {
    console.log(propertyKey);
 }
 
 class User2 {
    constructor (
       public name:string,
       public age: number,
    ) {}
 
    @logMethod
    public getPass():string {
       return `${this.name}${this.age}`;
    }
 }
 
 //get/set Decorator
 
 const logSet = (target: Object, propertyKey: string | symbol, descriptor: PropertyDescriptor) =>{
    console.log(propertyKey);
 }
 
 class User3 {
    constructor (
       public name:string,
       public age:number,
    )
    {}
    @logSet
    set myAge(age:number) {
       this.age = age;
    }
 }
 
 // applying Factory Decorator 
 
 const enumerable = (value : boolean) => {
    return (
       target: any,
       propertyKey: string | symbol,
       descriptor: PropertyDescriptor
    ) => {
       descriptor.enumerable = value;
    };
 }
 
 class User4 {
    constructor (
       public name:string,
       public age: number
    ) {}
    @enumerable(false)
    public getPass():string {
       return `${this.name}${this.age}`;
    }
 }
 
 // example of two fabric Decorators
 const first = () => {
    console.log('first() completing');
    return(target: any, propertyKey: string | symbol, descriptor: PropertyDescriptor) => {
       console.log('first() called');
    };
 }
 
 const second = () => {
    console.log('second() completing');
    return(target: any, propertyKey: string | symbol, descriptor: PropertyDescriptor) => {
       console.log('second() called');
    };
 }
 
 class User5 {
    constructor (
       public name:string,
       public age: number
    ) {}
    @first()
    @second()
    public getPass():string {
       return `${this.name}${this.age}`;
    }
 }