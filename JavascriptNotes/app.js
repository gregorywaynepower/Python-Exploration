var carClass = function(name, company, doors, price) {
    this.name = name
    this.company = company
    this.doors = doors
    this.price = price
    this.greetings = function() {
        console.log("Hi, Welcome to Car Masters will you like to drive a " + this.name + " it's a brand new " + this.comany + " for the price of " + this.price + "!")
    }
}

var accord = {
    name : "Accord",
    company : "Honda",
    doors : 4,
    price : 4000
}

console.log(accord.name)

var bmw = new carClass('M3', 'BMW', 2, '$35000')
var honda = new carClass('civic', 'honda', 2, '$25000')
var benz = new carClass('eclass', 'benz', 2, '$75000')
var audio = new carClass('quatro', 'audi', 2, '$65000')

console.log(benz.doors)
