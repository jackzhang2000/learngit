(function () {
    "use strict";
        $(document).ready(function () {
            $.get('SRKW.yaml')
            .done(function (data) {
              console.log('File load complete');
              console.log(jsyaml.load(data));
              var jsonString = JSON.stringify(data);
              console.log(jsonString);
              console.log($.parseJSON(jsonString));
          });
        });
    }());