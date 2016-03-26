//: Playground - noun: a place where people can play

import UIKit
import Foundation

// Example 1: Bool, Int, Float, Double
class LightSwitch {
    var on: Bool = true
    var dimmer: Double = 3.14159265
}

var livingRoomSwitch = LightSwitch()
livingRoomSwitch.on

// Example 2: Strings and Characters
var dollarSign: Character = "$"
var myFirstSwiftString: String = "mo' money"
var mySecondSwiftString: String = "mo' problems"
var concatenatedString = myFirstSwiftString + ", " + mySecondSwiftString

// Operators
// Example 1: Comparison operators
let ticketPrice = 7.5
let allowance = 10.0
var iceCreamPrice = 3.0

if allowance >= ticketPrice + iceCreamPrice {
    print("Let's go to the movies!")
} else {
    print("Let's watch a movie at home and eat ice cream")
}

// Example 2: Logical operators
var hungry = true
var vegetarian = false

if hungry /* "==true" is not necessary */ {
    print("Let's eat")
} else {
    print("Let's wait")
}

if hungry && !vegetarian {
    print("Let's eat steak!")
} else if hungry && vegetarian {
    print("How about pumpin curry?")
} else {
    print("nevermind")
}

var thereIsPie = true
if hungry || thereIsPie {
    print("Let's eat!")
} else {
    print("Let's wait.")
}

// Example 3: Tenary condition
hungry ? print("Let's eat!") : print("Let's wait.")
hungry || thereIsPie ? print("Let's eat!") : print("Let's wait.")
// Tenary statements can also be used as expressions.
let sandwichPrice = 5.0
var tax = true
var lunchPrice = sandwichPrice + (tax ? 0.50 : 0)


