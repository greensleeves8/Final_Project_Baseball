const url = "https://raw.githubusercontent.com/greensleeves8/Final_Project_Baseball/main/Resources/Revised_CSV/Player_Names.csv?raw=True";

// Creating function for dropdown selector
function init() {
    var selector = d3.select("#selDataset");

    d3.csv(url).then((data) => {
         console.log(data);
        var sampleNames = data;
        sampleNames.forEach((sample) => {
            selector.append("option").text(sample.playerID).property("value", sample.playerID);
            // console.log(sample);
        });
    })
}

init();

// Function to print the newly selected playerID
function optionChanged(newSample) {
    console.log(newSample);
};