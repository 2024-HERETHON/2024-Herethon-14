// 답글달기 버튼 클릭하면 인풋창 나오게 하는 거

document.addEventListener("DOMContentLoaded", () => {
    const replyBtns = document.querySelectorAll('.reply-btn');
    const replyInputContainers = document.querySelectorAll('.reply-input-container');

    replyBtns.forEach((btn, index) => {
        btn.addEventListener("click", () => {
            const replyInputContainer = replyInputContainers[index];
            if (replyInputContainer.style.display === "none" || replyInputContainer.style.display === "") {
                replyInputContainer.style.display = "flex";
            } else {
                replyInputContainer.style.display = "none";
            }
        });
    });
});

