

function send_form_data(form , Status , path ) {
    console.log("Inside " , path)

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        Status.textContent = "Sending data";

        try {
            const form_data = new FormData(form);
            const json_data = JSON.stringify(
                Object.fromEntries(form_data.entries())
            );

            const response = await fetch(path, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: json_data,
            });

            if (!response.ok) throw new Error(" Server Error");
            Status.textContent =
                "✅ Form submitted successfully (no page reload)";
        } catch {
            Status.textContent = "❌ Error submitting form";
        }
    });
}

export { send_form_data }