class User {
    public name: string
    private age: number | string
    protected nickname: string
    readonly pass: number

    constructor(name: string, age: number | string, nickname: string, pass: number) {
        this.name = name;
        this.age = age,
        this.nickname = nickname,
        this.pass = pass
    }
   
}

let user1 = new User('Bohdan', 21, 'WebDev', 123);
console.log(user1);
console.log(user1.pass);

class User1 {

    constructor(
        public name : string,
        public age : number,
        public nickname : string,
        public pass : number
    ) {
        
    }
   
}


class User2 {
    private age: number;

    constructor (public name: string) {}

        setAge(age: number) {
            this.age = age;
        }

        set myAge(age: number) {
            this.age = age;
        }
}

let user2 = new User2('Bohdan');
console.log(user2.setAge(21));
user2.myAge = 22;
console.log(user2.myAge);
