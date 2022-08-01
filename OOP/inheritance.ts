class Developer {
    public isDeveloper:boolean;
    constructor(
        public name: string,
        public salary: number,
    ) {
        this.isDeveloper = true;
    }

    getInfo() {
        console.log(this.name);
        console.log(this.salary);
    }
}

class SeniuorDeveloper extends Developer {
    constructor(
        public name: string,
        public salary: number,
    ) {
        super(name,salary);
    }

    teachJuniorDevs(): void {
        console.log(`${this.name} teaches junior Devs`);
    }

}

const developer = new SeniuorDeveloper('Bohdan', 5000);
developer.getInfo();
developer.teachJuniorDevs();
console.log(developer.isDeveloper);