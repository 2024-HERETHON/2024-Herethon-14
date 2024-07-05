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


//이미지 업로드 및 데이터 전달 함수 구현
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('.fileInput');
    const profileImg = document.querySelector('.profileImg-img');
    const idInput = document.querySelector('.idInput');
    const emailInput = document.querySelector('.emailInput');
    const passwordInput = document.querySelector('.passwordInput');
    const uploadImgBtn = document.querySelector('.uploadImgBtn');
    const saveBtn = document.querySelector('.saveBtn');
    const togglePasswordBtn = document.querySelector('.togglePasswordBtn');
    const togglePasswordBtnImg = document.querySelector('.togglePasswordBtn img')

    //사용자 데이터 불러오기
    fetch('')
        .then(response => response.json())
        .then(data => {
            profileImg.src = data.profile_img_url;
            idInput.value = data.username;
            emailInput.value = data.email;
            passwordInput.value = data.password;
        })
        .catch(error => {
            console.error('프로필 데이터를 가져오는 중 오류 발생:', error);
        });
    
    // 이미지 업로드 버튼 클릭 시 숨겨둔 input file 열기
    uploadImgBtn.addEventListener('click', function() {
        fileInput.click(); 
    });

     // input file 변경 시 프로필 이미지 업데이트 - 저장된 것은 아님! 
     fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader(); 
            reader.onload = function(event) {
                profileImg.src = event.target.result; 
            };
            reader.readAsDataURL(file);
        }
    });

    //비밀번호 토글 기능 구현(보이게 하고 안 보이게 하고)
    togglePasswordBtn.addEventListener('click', function() {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            togglePasswordBtnImg.src = 'images/eyeopen.svg';
        } else {
            passwordInput.type = 'password';
            togglePasswordBtnImg.src = 'images/eyeclose.svg';
        }
    });

    //저장 버튼 눌렀을 때 데이터 서버에 저장하기
    saveBtn.addEventListener('click', function() {
        const profileData = {
            id: idInput.value,
            email: emailInput.value,
            password: passwordInput.value,
            profile_img_url: profileImg.src,
        };

        fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(profileData),
        })
        .then(response => response.json())
        .then(data => {
            console.log('프로필이 성공적으로 업데이트되었습니다:', data);
        })
        .catch(error => {
            console.error('프로필 업데이트 중 오류 발생:', error);
        });
    });
});