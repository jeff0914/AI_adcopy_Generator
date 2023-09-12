$("form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/token/",
        data: $(this).serialize(),
        success: function (data) {
            localStorage.setItem('jwt_token', data.access);
            localStorage.setItem('jwt_token_refresh', data.refresh);
            window.location.href = "http://localhost:8000/accounts/";
        }
    });
});