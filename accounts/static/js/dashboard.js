var jwt_token = localStorage.getItem('jwt_token');
var jwt_token_refresh = localStorage.getItem('jwt_token_refresh');
data = {
    "refresh": jwt_token_refresh
};
$.ajax({
    type: "POST",
    url: "http://localhost:8000//api/token/refresh/",
    data: data,
    success: function (data) {
        localStorage.setItem('jwt_token', data.access);
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/api/adcopy/",
            headers: {
                "Authorization": "Bearer" + " " + localStorage.getItem('jwt_token')
            },
            success: function (data) {
                var result = "";
                for (var i  = 0; i < data.length; i++) {
                    result += "UUID: " + data[i].uuid + "<br> ";
                    result += "User Input: " + data[i].user_input + "<br> ";
                    result += "Generated Text: " + data[i].generated_text + "<br> ";
                    result += "Timestamp: " + data[i].timestamp + "<br>-----<br>";
                }
                $("#result").html(result).css('color', 'blue');
            },
            error: function (data) {
                var result = "please login ";
                $("#result").text(result).css('color', 'red');
            }
        });
    },
    error: function (data) {
        var result = "please login " + data.responseText;
        $("#result").text(result).css('color', 'red');
    }
});