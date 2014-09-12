var response_cache = {};

function fill_states(county_id) {
	console.log(county_id);
	console.log(response_cache[county_id]);
  if (response_cache[county_id]) {
    $("#id_state").html(response_cache[county_id]);
  } else {
    $.getJSON("/api/common/states/"+county_id, {},
      function(ret, textStatus) {
        var options = '<option value="" selected="selected">---------</option>';
        for (var i in ret) {
          options += '<option value="' + ret[i].id + '">'
            + ret[i].name + '</option>';
        }
        response_cache[county_id] = options;
        $("#id_state").html(options);
      });
  }
}

$(document).ready(function() {
  console.log('llega');
  $("#id_country").change(function() { fill_states($(this).val()); });
});