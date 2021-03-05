// import the data from batter_data.js
const batterData = batters;

// Reference the HTML table using d3
var tbody = d3.select("tbody");

function buildTable(batterData) {
    tbody.html("");
    batterData.forEach((batterDataRow) => {
        let row = tbody.append("tr");
        Object.values(batterDataRow).forEach((val) => {
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
    let filteredBatterData = batterData;
    Object.entries(filters).forEach(([key, value]) => {
        filteredBatterData = filteredBatterData.filter(row => row[key] === value);
    });
    buildTable(filteredBatterData);
}

d3.selectAll("input").on("change", updateFilters);

buildTable(batterData);