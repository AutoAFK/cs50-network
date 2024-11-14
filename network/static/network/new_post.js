document.addEventListener("DOMContentLoaded", () => {
	document.getElementById("postForm").onsubmit = (event) => {
		event.preventDefault();
		const form = event.target;
		const formData = new FormData(form);
		fetch(form.action, {
			method: "POST",
			body: formData,
			headers: {
				"X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
					.value,
			},
		})
			.then((response) => {
				if (response.status !== 201) {
					response.json().then((data) => {
						document.getElementById("post_errors").innerText = message.message;
					});
				} else {
					document.getElementById("post_body").value = "";
				}
			})
			.catch((error) => {
				console.log(error);
			});
	};
});
