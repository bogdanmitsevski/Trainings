abstract class Car {       //cannot create class exemplar
    constructor (
        protected owner: string,
        protected speed: number,
        protected year: number
    ) {}

    public drive () {}
    public repair () {}
}

class Volvo extends Car {
    constructor (
        protected owner: string,
        protected speed: number,
        protected year: number
    ) {
        super(owner,speed,year);
    }

    drive() {
        console.log(`The Volvo car has speed ${this.speed} speed`);
    }

    repair() {
        console.log('The Volvo car has been repaired');
    }
}

const VolvoCar = new Volvo('Volvo company',250, 2013);
VolvoCar.drive();
VolvoCar.repair();