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
				if (response.ok) {
					return response.json();
				}
			})
			.then((data) => {
				if (data.success) {
					window.location.href = data.redirect_url;
				} else {
					document.getElementById("post_errors").innerText = data.error;
				}
			})
			.catch((error) => {
				console.log(error);
			});
	};
});
