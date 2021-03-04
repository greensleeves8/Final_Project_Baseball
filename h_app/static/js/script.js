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

//Create tab for Background knowledge 

function openTab(event, TabName) {
  
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(TabName).style.display = "block";
    evt.currentTarget.className += " active";
  }