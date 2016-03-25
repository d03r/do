/**
 * Created by no on 25/3/16.
 */
// https://github.com/bgando/object-exercises/

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