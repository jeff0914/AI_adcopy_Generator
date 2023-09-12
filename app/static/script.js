document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("adForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const userInput = document.getElementById("userInput").value;

        //  localStorage get refresh token
        const refreshToken = localStorage.getItem('jwt_token_refresh');

        // refresh access token
        fetch("http://localhost:8000/api/token/refresh/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ refresh: refreshToken }),
        })
        .then(response => response.json())
        .then(data => {
            // update localStorage  access token
            localStorage.setItem('jwt_token', data.access);

            // use new access token 
            return fetch("http://localhost:8000/api/adcopy/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('jwt_token')}`
                },
                body: JSON.stringify({ user_input: userInput }),
            });
        })
        .then(response => response.json())
        .then(data => {
            
            document.getElementById("generatedText").value = data.generated_text;
        })
        .catch(error => {
           
            console.error("Error:", error);
        });
    });
});