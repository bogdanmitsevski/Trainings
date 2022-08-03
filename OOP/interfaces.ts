interface User {
    name?: string,
    age: number,
 }
 
 const bohdan: User = {
    name: "Bohdan",
    age: 21
 }
 
 
 console.log(bohdan.name);
 
 interface User1 {
    readonly city: string,
    school?: string,
    readonly phoneNumber: number
 }
 
 const michael: User1 = {
    city: "Lutsk",
    school: "mainSchool",
    phoneNumber: 123456789
 }
 
 michael.school = "Lutsk1" //because another elements are readonly
 
 interface User2 {
    readonly city: string,
    school?: string,
    readonly phoneNumber: number,
    [propName: string]: any;
 }
 
 const michael1: User2 = {
    city: "Lutsk",
    school: "mainSchool",
    phoneNumber: 123456789,
    street: "Hnidavska"
 }
 
 console.log(michael1.street);
 
 interface User3 {
    readonly city: string,
    school?: string,
    readonly phoneNumber: number,
    getPass(): string
 }
 
 class bohdanM implements User3 {
    city: string =  "Lutsk";
    school: string = "mainSchool";
    phoneNumber: number = 123;
    getPass() {
       return `${this.city} and ${this.phoneNumber}`;
    }
 
 }
 
 const classDescription = new bohdanM;
 console.log(classDescription.getPass());
 
 interface User4 {
    car: string
 }
 
 interface User5 {
    getPassword(): string
 }
 
 
 class lastClass implements User4, User5 {
    car:string = 'Volvo';
    getPassword() {
       return `${this.car}`;
    }
 }
 
 const classProperty = new lastClass;
 console.log(classProperty.getPassword());
 
 interface User6 {
    name1: string
 }
 
 interface Admin extends User6 {
    age1: number
 }
 
 class adminUser6 implements Admin {
    name1: string = "Bohdan";
    age1: number = 21;
 }
 
 const classProperty1 = new adminUser6;
 console.log(classProperty1.name1);
 