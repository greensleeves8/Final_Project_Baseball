// import the data from pitcher_data.js
const pitcherData = pitchers;

// Reference the HTML table using d3
var tbody = d3.select("tbody");

function buildTable(pitcherData) {
    tbody.html("");
    pitcherData.forEach((pitcherDataRow) => {
        let row = tbody.append("tr");
        Object.values(pitcherDataRow).forEach((val) => {
            let cell = row.append("td");
            cell.text(val);
            }
        );
    });
}
var filters = {};

function updateFilters() {
    let changedElement = d3.select(this);
    let elementValue = changedElement.property("value");
    let filterId = changedElement.attr("id");
    if (elementValue) {
        filters[filterId] = elementValue;
    }
    else {
        delete filters[filterId];
    }
    filterTable();
}

function filterTable() {
    let filteredPitcherData = pitcherData;
    Object.entries(filters).forEach(([key, value]) => {
        filteredPitcherData = filteredPitcherData.filter(row => row[key] === value);
    });
    buildTable(filteredPitcherData);
}

d3.selectAll("input").on("change", updateFilters);

buildTable(pitcherData);