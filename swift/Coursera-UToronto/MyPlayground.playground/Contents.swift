//: Playground - noun: a place where people can play

import UIKit

var str:String?="Hello"

str = nil
str = "Hey"

let constantString = "Hello"

print(str)

let name = "John"

if name.characters.count > 10 {
    print("Long Name")
} else if name.characters.count > 5 {
    print("Medium Name")
}
else {
    print("Short Name")
}

switch name.characters.count {
case 7...10: // pattern matching
    print("10 character name")
case 5..<7:
    print("9 character name")
default:
    print("some length")
}

///////////////////////////////

var number = 0
while number < 10 {
    number * number
    number++
}

///////////////////////////////

for (var number = 0; number < 10; number++) {
    number
}


for number in 0...10 {
    number
}

for number in 0..<10 {
    number
}

for number in [2, 5, 1, 9] {
    number
}


///////////////////////////////

var animals = ["Cow", "Dog", "Bunny"]
animals[0]
animals[1]
animals[2] = "Rabbit"

for animal in animals {
    animal
}

/////////////////////////////// 

var cuteness = ["Cow": "Not very",
               "Dog": "Cute",
               "Bunny": "Very Cute"]

cuteness["Dog"]
cuteness["Cat"] // returns nil

for animal in animals {
    cuteness[animal]
}

///////////////////////////////

func doMath() {
    print("Doing math")
}

doMath()

func doMath2(a:Double, b:Double, operation:String) {
    print("Performing", operation, "on", a ,"and",b)
}

doMath2(2.0, b:1.0, operation:"+")

func perform(operation: String, on a: Double, and b: Double) -> Double {
    print("Performing", operation, "on", a ,"and",b)
    
    var result: Double = 0
    switch operation {
        case "+": result = a + b
        case "-": result = a - b
        case "*": result = a * b
        case "/": result = a / b
        default: print("Bad operation", operation)
    }
    return result
}

perform("hello", on:1, and:2.0)


///////////////////////////////

var image = [
    [3, 7, 10],
    [6, 4, 2],
    [8, 5, 2]
]

func raiseLowerValuesOfImage(inout image: [[Int]]) {
    for row in 0..<image.count {
        for col in 0..<image[row].count {
            image[row][col]
            if (image[row][col] < 5) {
                image [row] [col] = 5
            }
        }
    }
}

raiseLowerValuesOfImage(&image)

let x = 1

if true {print("true")}

if (true) {print("true")}

for i in 0..<5 { print (i) }

let array1 = [1,2,3,4]
let array2 = [1,2,2.5, 3]
//let array3:[Int] = [1,2,2.5,3]
let array4:[Int] = []
let array5 = [Int]()

//////////////////////////

// Optional

var MaybeStr: String? = "hi"

MaybeStr!.characters.count

func performMagic(spell: String) -> String {
    return spell
}

performMagic("disappear")

let magicFunction = performMagic

magicFunction("disappear")

// Closure

var newMagicFunction = {
    (spell: String) -> String in return spell;
}

newMagicFunction("disappear")

// Properties

struct Animal {
    var name: String = ""
    var heightInches = 0.0
    var heightCM: Double {
        get {
            return 2.54 * heightInches
        }
        set(newHeightCM) {
            heightInches = newHeightCM / 2.54
        }
    }
}

var dog = Animal (name: "dog", heightInches: 50)
dog.heightInches
dog.heightCM
dog.heightCM=254
dog.heightCM
dog.heightInches

let noValue:Int? = nil
// let unwrappedValue = noValue!

/*
class SuperNumber: NSNumber {
    override func getValue(value: UnSaveMutablePointer<Void>) {
        super.getValue(value)
    }
}
*/

extension NSNumber {
    func superCoolGetter() -> Int {
        return 5
    }
}

let n = NSNumber(int: 4)
n.superCoolGetter()

protocol dancable {
    func dance()
}

class Person: NSNumber, dancable {
    func dance() {
        
    }
}








