// document.addEventListener('DOMContentLoaded', () => {
    
//     const text = localStorage.getItem('poemShare');
//     const display = document.querySelector('.comment-area');

//     if (text) {
//         display.textContent = text;
//     }
//     else {
//         display.textContent = '감상이 아직 없습니다.'
//     }
// }) 



    // 답글달기 버튼

document.addEventListener("DOMContentLoaded", () => {
    const reply = document.querySelector('.reply');
    const replyInputBox = document.querySelector('.reply-input-box');

    reply.addEventListener("click", () => {
        if (replyInputBox.style.display === "none" || replyInputBox.style.display === "") {
            replyInputBox.style.display = "block";
        }
        else {
            replyInputBox.style.display = "none";
        }
    }) 
})

    // edit 버튼 

document.addEventListener("DOMContentLoaded", () => {
    const edit = document.querySelector('.edit');
    const editList = document.querySelector('.edit-list');

    edit.addEventListener("click", () => {
        if (editList.style.display === "none" || editList.style.display === "") {
            editList.style.display = "block";
        }
        else {
            editList.style.display = "none";
        }
    }) 
})


// 댓글 저장하기 버튼

// document.addEventListener("DOMContentLoaded", function() {
//     const replyButton = document.querySelector(".reply-button");
//     const replyInput = document.querySelector(".reply-input");
//     const replyList = document.querySelector(".reply-list");

//     replyButton.addEventListener("click", function() {
//         const commentText = replyInput.value.trim();

//         if (commentText !== "") {
//             const newComment = document.createElement("div");
//             newComment.className = "comment";
//             newComment.textContent = commentText;

//             replyList.appendChild(newComment);

//             replyInput.value = "";
//         }
//     });
// });