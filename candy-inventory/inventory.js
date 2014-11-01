/**
 * Candy Bag Inventory
 * ================================================================================================
 * So to help out all the trick or treaters we need to develop a tool to help inventory their candy 
 * haul for the night. You will be given a text file that contains a listing of every piece of candy
 * in the bag. Your challenge is to develop a solution to inventory the candy and print out a summary
 * of how much candy you got.
 * 
 * You must answer these basic questions:
 * - How many pieces of candy did you get
 * - How much of each type
 * - What percentage of total candy does that type occupy
 *
 * Strategy:
 *
 * 1. Read candy bag file into array, split by new lines
 * 2. Iterate candy array, incrementing the count for each candy type
 * 3. Iterate again (is this necessary?), calculating the percentage of each candy type
 * 4. Display list of candy
 *
 */
"use strict";

var fs = require('fs');
var _  = require('underscore');

var inventory = {};

inventory.init = function () {
    fs.readFile("./bag.txt", { encoding: "utf8" }, function (err, data) {
        if (err) {
            throw new Error(err);
        }
        
        var bag = _.compact(data.split("\n"));
        
        inventory.calculateCandyTypeCount(bag);
    });
};

inventory.calculateCandyTypeCount = function (bag) {
    var candyTypeCounts = {};
    
    _.each(bag, function (value, key) {
        if (typeof candyTypeCounts[value] === "undefined") {
            candyTypeCounts[value] = 0;
        }
        
        candyTypeCounts[value]++;
    });
    
    inventory.calculateTotalPercentages({
        bag: bag,
        candyTypeCounts: candyTypeCounts
    });
};

inventory.calculateTotalPercentages = function (options) {
    var total  = options.bag.length;
    var output = []; 
    var count;
    
    _.each(options.candyTypeCounts, function (value, key) {
        count = options.candyTypeCounts[key];
        
        output.push({
            candy     : key,
            count     : count,
            percentage: ((count / total) * 100).toFixed(1)
        });
    });
    
    inventory.printOutput({
        total : total,
        output: output
    });
};

inventory.printOutput = function (options) {
    console.log("Total candies: " + options.total);
    
    _.each(options.output, function (value, key) {
        console.log([value.candy, value.count, value.percentage + "%"].join(" :: "));
    });
};

inventory.init();

module.exports = inventory;










