/**
 * Created by no on 25/3/16.
 */

// https://github.com/bgando/array-exercises/

var animal = {}; // Create a variable, name it animal, and assign it an object literal.

// With Dot Notation…
animal.username = 'Blackie' // Add a property called username and assign it a value.

console.log(animal)
console.log(animal.username) // Ensure that your username property exists in animal by inspecting it in the console.

// With Bracket Notation…

animal['tagline'] = 'Feed me' // Add a property called tagline and give it a value.
console.log(animal.tagline)// Check that your property exists in the animal object by inspecting it in the console.

var noises = []; // //Create a variable called noises and assign it an empty array []
animal.noises = noises;
//Add the noises array to your object.
console.log(animal);

// Loop
// Loop through the properties of your animal object.
var count = 0;
for (var key in animal) {
    count++;
    if (key == 'username') {
        console.log('Hi my name is ' + animal[key])
    } else if (key == 'tagline') {
        console.log('I like to say ' + animal[key])
    }
}


// Create an array.

// Create a variable called noiseArray and assign it to an array literal. Place at least one element in the array.
var noiseArray = ['zzzz'];

noiseArray.unshift('hiss'); // Add a noise to the beginning of the noiseArray.
noiseArray.push('Woff');// Add another noise to the end of the noiseArray.

// Using Bracket Notation…
// add another noise to the end.
noiseArray[3] = 'Meow';

// index starts from 0 so the last index is 1 less than the length
console.log(noiseArray.length);

// Nest the Array in the Object
// Put the noiseArray inside the animal object on the noises property. Your result should look like this:
animal.noises = noiseArray
console.log(animal)