$(document).ready(function() {
    console.log("example-select.js  ready!");

    ExampleSelect.init();
});

var ExampleSelect = {

    init: () => {
        console.log("ExampleSelect.init");
        $('#exampleDataSelect').on('change', function() {
          $('#id_parameters').val(this.value);

          const text = $('#exampleDataSelect option:selected').text().trim();
          $('#id_description').val(text);
        });
    },
};