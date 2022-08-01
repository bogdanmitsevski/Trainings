class Animal {
    constructor (
        public name: string,
    ) {}

    run():void {} //action
}

class Dog extends Animal {
    constructor (
        public name: string,
    ) {
        super(name);
    }

    run(): void {
        console.log("run and smile");
    }
}

class Lion extends Animal {
    constructor (
        public name: string,
    ) {
        super(name);
    }

    run(): void {
        console.log("run and roar");
    }
}