var response_cache_cities = {};

function fill_cities(state_id) {
	console.log(state_id);
	console.log(response_cache_cities[state_id]);
  if (response_cache_cities[state_id]) {
    $("#id_city").html(response_cache_cities[state_id]);
  } else {
    $.getJSON("/api/common/cities/"+state_id, {},
      function(ret, textStatus) {
        var options = '<option value="" selected="selected">---------</option>';
        for (var i in ret) {
          options += '<option value="' + ret[i].id + '">'
            + ret[i].name + '</option>';
        }
        response_cache_cities[state_id] = options;
        $("#id_city").html(options);
      });
  }
}

$(document).ready(function() {
  $("#id_state").change(function() { fill_cities($(this).val()); });
});