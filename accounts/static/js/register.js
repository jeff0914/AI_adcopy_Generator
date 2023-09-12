$("form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/auth/users/",
        data: $(this).serialize(),
        success: function () {
            window.location.href = "http://localhost:8000/accounts/login/";
        },
        error: function (data) {
            console.log(data.responseText)
        }
    });
});