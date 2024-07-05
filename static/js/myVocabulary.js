//박스 클릭 시 구현
let activeBox = null; //활성화 박스 저장 변수

document.querySelectorAll('.box').forEach(box => {
    const line = box.querySelector('.line');
    const wordDiv = box.querySelector('.wordDiv');

    // 각 박스의 wordDiv를 클릭했을 때
    wordDiv.addEventListener('click', function() {
        // 현재 박스가 이미 활성화된 상태인지 확인
        if (box === activeBox) {
            // 이미 활성화된 상태면 아무것도 하지 않게!!!!!
            return;
        }

        // 이전에 활성화된 박스가 있으면 초기화
        if (activeBox !== null) {
            activeBox.querySelector('.wordDiv').classList.remove('highlight');
            activeBox.querySelector('.line').style.display = 'none';
        }

        // 현재 클릭된 박스를 활성화 박스로 설정
        activeBox = box;

        // 현재 클릭된 박스에 highlight 클래스 추가(테두리 css 추가)
        wordDiv.classList.add('highlight');

        // line 요소 보이게 설정
        line.style.display = 'block';
    });
});



//모달창 기능
document.querySelector('.alarmBtn').addEventListener('click', function () { 
    var modal = document.querySelector('.alarm-modal');
    modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
});

document.querySelector('.profileBtn').addEventListener('click', function () {
    var modal = document.querySelector('.profile-modal');
    modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
});

window.onclick = function(event) {
    var alarmModal = document.querySelector('.alarm-modal');
    var alarmBtn = document.querySelector('.alarmBtn');
    if (event.target !== alarmModal && !alarmModal.contains(event.target) && event.target !== alarmBtn) {
        alarmModal.style.display = 'none';
    }

    var profileModal = document.querySelector('.profile-modal');
    var profileBtn = document.querySelector('.profileBtn');
    if (event.target !== profileModal && !profileModal.contains(event.target) && event.target !== profileBtn) {
        profileModal.style.display = 'none';
    }
}