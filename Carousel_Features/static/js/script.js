// Create a function to automate image scrolling
// var counter = 1;

// function jumboScroller() {
//     document.getElementById('radio' + counter).checked = true;
//     counter++;
//     if (counter > 5) {
//         counter = 1;
//     }
// };

// Dataset manipulation
const url = "https://raw.githubusercontent.com/greensleeves8/Final_Project_Baseball/main/Resources/HallOfFame.csv";

function init() {
    var selector = d3.select("#selDataset");

    d3.csv(url).then((data) => {
        // console.log(data);
        var sampleNames = data;
        sampleNames.forEach((sample) => {
            selector.append("option").text(sample.playerID).property("value", sample.playerID);
            // console.log(sample);
        });
    })
}

init();

function optionChanged(newSample) {
    console.log(newSample);
};

