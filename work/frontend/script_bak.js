function fetchReservations() {
    fetch('/reservations')
        .then(response => response.json())
        .then(data => {
            const statusList = document.getElementById('status-list');
            statusList.innerHTML = '';
            data.forEach(reservation => {
                const reservationDiv = document.createElement('div');
                reservationDiv.textContent = `이름: ${reservation.name}, 이메일: ${reservation.email}, 좌석: ${reservation.seat_info}, 날짜: ${reservation.datetime}`;
                statusList.appendChild(reservationDiv);
            });
        })
        .catch(error => console.error('Error fetching reservations:', error));
}

// 페이지 로드 시 예약 현황 가져오기
window.onload = fetchReservations;


// 좌석 클릭 시 예약 예약 폼 보이게 하기
function showForm() {
    const formContainer = document.getElementById('form-container');
    formContainer.style.display = 'block'; // 예약 폼 보이게 하기
}

// 페이지 로드 시 예약 폼 숨기기
window.onload = function() {
    const formContainer = document.getElementById('form-container');
    formContainer.style.display = 'none'; // 예약 폼 숨기기
    fetchReservations(); // 이미 존재하는 예약 현황 불러오기 함수
};


// 버튼 클릭 시 예약 폼 숨기기
function closeForm() {
    document.getElementById('form-container').style.display = 'none';
}


// showForm 함수에서 인자로 받은 좌석 정보를 해당 필드에 설정
function showForm(seatInfo) {
    document.getElementById('seat_info').value = seatInfo;
    document.getElementById('form-container').style.display = 'block';
}
