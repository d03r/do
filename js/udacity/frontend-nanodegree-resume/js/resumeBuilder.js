/*
This is empty on purpose! Your code to build the resume will go here.
 */
/*
$("#main").append(["Dr. N. Oo. "]);
//[string].replace([old],[new])

var awesomeThoughts ="I am AWESOME!";
var funThoughts = awesomeThoughts.replace("AWESOME", "a coder");
$("#main").append(funThoughts);
*/

//////
var name ="Dr. N. Oo"
var role ="Software Engineer"
var formattedName = HTMLheaderName.replace("%data%",name);
var formattedRole = HTMLheaderRole.replace("%data%",role);

$("#header").append(formattedName);
$("#header").append(formattedRole);

//$("#header").prepend(formattedName);
//$("#header").prepend(formattedRole);