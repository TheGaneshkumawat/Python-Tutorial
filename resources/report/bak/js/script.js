// load the amCharts chart's config from a JSON file
var amChartsConfig = new am4core.DataSource();
amChartsConfig.url = "json/config.json";
amChartsConfig.load();

// create the amChart chart using the JSON config
var chart
amChartsConfig.events.on("done", function(ev) {
  chart = am4core.createFromConfig(
    config = amChartsConfig.data,
    container = "chart",
    chart_type_class = "PieChart"
  );
});