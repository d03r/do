/**
 * Created by no on 25/3/16.
 */
var orderID = 9001;
console.log(orderID);  // 9001

orderID = 1201;
console.log(orderID); // 1201

orderID = "ORD-9001";
console.log(typeof orderID);

var isActive  = true;
console.log(typeof isActive);

var order = {
    orderID: 9001,
    isActive: true
};
console.log(typeof order);

var cancelledOrders = [9001, 9002, 9003];
console.log(typeof cancelledOrders); // array data type is object

var order2 = null;
console.log(typeof order2); // null is also an object

function cancelOrder(orderID) {

}
console.log(typeof cancelOrder); // function

function printOrder() {
    console.log("Printing order.");
}
printOrder();

function printOrder2(orderID) {
    console.log("Printing order: " + orderID);
}
printOrder2('9002');

function calcTotalPrice(quantity, price) {
    console.log("Total price: " + (quantity * price));
}
calcTotalPrice(2, 4.00);

/*
function calcTotalPrice2(quantity, price, currency) {
    console.log(currency);
}
calcTotalPrice2(2, 4.00); // undefined
*/

function calcTotalPrice3(quantity, price) {
    return quantity * price;
}

var totalPrice = calcTotalPrice3(2, 4.00);
console.log(totalPrice);

totalPrice = calcTotalPrice3(3, 3.00);
console.log(totalPrice);

/*
function getOrder() {
    // nothing returned
}
var order = getOrder();
console.log(order);  // undefined
*/

var activateOrder = function() {
    console.log("Order activated");
};
console.log(typeof activateOrder);
activateOrder();

// If and Switch Statements
var total = 99.99;
var freeShipping = false;

if (total >= 100.00)
    freeShipping = true;
else
    freeShipping = false;

console.log(freeShipping);
