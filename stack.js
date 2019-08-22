//stack practice

class Stack {
  constructor() {
    //underscore means dont use outside of the class or object, in python this = self
    this._data = [];
  }
  push(element) {
    //adds an element to the _data array
    this._data.push(element);
  }
  //pop gets rid of element on top of stack
  pop() {
    return this._data.pop();
  }
  top() {
    return this._data[this._data.length - 1];
  }
  size() {
    return this._data.length;
  }
  isEmpty() {
    return this.size() === 0;
  }
}

// Testing
s = new Stack();
s.push(1);
s.push(2);
s.push(3);
console.log("pop", s.pop());
console.log("size", s.size());
console.log("isEmpty", s.isEmpty());
console.log("pop", s.pop());
console.log("top", s.top());
console.log("pop", s.pop());
console.log("isEmpty", s.isEmpty());

//reverse a word
word = "apple";

ns = new Stack();

//push letters into stack
word.split(" ").forEach(l => {
  ns.push(l);
  console.log(l);
});

newWord = "";
size = ns.size();
for (let i = 0; i < size; i++) {
  newWord += ns.pop();
}

console.log(newWord);
