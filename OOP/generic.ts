//generic
const getter = <T,>(data:T):T=>data
console.log(getter(10));
console.log(getter<string>('text').length);

//Generic Class
class User<T> {
   constructor (
      public name: T,
      public age: T

   ) {}
   
   public getPass(): string {
      return `${this.name}${this.age}`;
   }
}

const user = new User('Bohdan','21');
console.log(user.getPass());

class User1 <T,K> {
   constructor (public name: T, public age: K) {}
   
   public getPass():string {
      return `${this.name}${this.age}`;
   }
}

const user1 = new User1("Bohdan", 21);
console.log(user1.getPass());

class User2 <T,K extends number> {
   constructor (public name: T, public age: K) {}
   
   public getPass():string {
      return `${this.name}${this.age}`;
   }

   public getSecret(): number {
      return this.age*2;
   }
}

const user2 = new User2('Bohdan',21);
console.log(user2.getSecret());



