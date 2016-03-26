//: Playground - noun: a place where people can play

import UIKit

// A String isn't just a String
//Through the .characters property we can access an array of characters

var password = "Meet me in St. Louis"
for character in password.characters {
    if character == "e" {
        print("found an e!")
    } else {
        
    }
}

// A String can be treated as an NSString
let newPassword = password.stringByReplacingOccurrencesOfString("e", withString:  "3")

