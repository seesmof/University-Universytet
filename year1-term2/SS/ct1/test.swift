class Person {
  var name: String
  var age: Int
  
  init(name: String, age: Int) {
    self.name = name
    self.age = age
  }
  
  func sayHello() {
    print("Hello, my name is \(name).")
  }
}

let john = Person(name: "John", age: 30)
john.sayHello()