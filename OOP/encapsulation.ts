class Developer1 {
    public isDeveloper:boolean;
    constructor(
        protected name: string,
        public salary: number,
    ) {
        this.isDeveloper = true;
    }

    getInfo() {
        console.log(this.name);
        console.log(this.salary);
    }
}

class JuniorDeveloper1 extends Developer1 {
    constructor(
        protected name: string,
        public salary: number,
    ) {
        super(name,salary);
    }

    getName(): string {
        return this.name;
    }
}
const developer1 = new Developer1('Bohdan', 5000);
const juniorDeveloper1 = new JuniorDeveloper1('BOHDAN',1000);
console.log('name',juniorDeveloper1.getName());