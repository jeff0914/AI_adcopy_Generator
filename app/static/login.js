document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("loginForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        fetch("/api/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username: username, password: password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.access) {
                console.log("Token obtained:", data.access);
            } else {
                console.log("Failed to obtain token:", data);
            }
        })

        .catch((error) => {
            console.error("Error:", error);
        });
    });
});
