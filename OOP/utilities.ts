//readOnly
interface User {
    name: string;
 }
 
 const user: Readonly<User> = {
    name: 'Bohdan',
 }
 
 console.log(user.name);
 
 
 //required
 
 interface Props {
    a?: number;
    b?: string;
 };
 
 const obj: Props = {a:5};
 const obj2: Required <Props> = {a:5, b:"abc"};
 console.log(obj2);
 
 //record
 
 interface PageInfo {
    title: string
 }
 
 type Page = 'home'|'about'|'contact';
 
 const x: Record <Page, PageInfo> = {
    about: { title: 'about'},
    contact: { title: 'contact'},
    home: { title: 'home'},
 }
 
 //Pick
 
 interface Todo {
    title:string;
    description: string;
    completed: boolean;
 }
 
 type TodoPreview = Pick<Todo, 'title' | 'completed' >;
 
 const todo: TodoPreview = {
    title: 'Clean car',
    completed: false,
 };
 
 //omit
 
 interface Todo1 {
    title:string;
    description: string;
    completed: boolean;
 }
 
 type Todo1Preview = Omit<Todo, 'description' >;
 
 const todo1: Todo1Preview = {
    title: 'Clean room',
    completed: false,
 }