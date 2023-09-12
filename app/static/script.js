document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("adForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const userInput = document.getElementById("userInput").value;

        fetch("http://localhost:8000/api/adcopy/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ user_input: userInput }),
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



