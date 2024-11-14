document.addEventListener("DOMContentLoaded", () => {
	like_buttons = document.querySelectorAll("#like_button");
	csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
	for (const button of like_buttons) {
		const post_id = button.getAttribute("data-post-id");
		button.onclick = () => {
			fetch("/posts/like", {
				method: "POST",
				body: JSON.stringify({ post_id: post_id }),
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": csrftoken,
				},
			})
				.then((response) => response.json())
				.then((data) => {
					const icon = button.querySelector("i");
					const text = button.querySelector("span");
					if (data.liked) {
						icon.classList.add("text-danger");
					} else {
						icon.classList.remove("text-danger");
					}
					text.innerText = data.liked_amount;
				})
				.catch((error) => {
					console.log(error);
				});
		};
	}
});
