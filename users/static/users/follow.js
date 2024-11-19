document.addEventListener("DOMContentLoaded", () => {
	btn = document.getElementById("follow-btn");
	csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	btn.onclick = () => {
		user_id = btn.dataset.userId;
		fetch(`/user/${user_id}/follow`, {
			method: "POST",
			headers: {
				"X-CSRFToken": csrf_token,
				"Content-Type": "application/json",
			},
		});
	};
});
