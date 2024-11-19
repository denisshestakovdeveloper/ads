let currentIndex = 0;

const photoElement = document.getElementById('photo');

function updatePhoto() {
    photoElement.src = photos[currentIndex];
}

document.getElementById('prevBtn').onclick = function () {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : photos.length - 1;
    updatePhoto();
};

document.getElementById('nextBtn').onclick = function () {
    currentIndex = (currentIndex < photos.length - 1) ? currentIndex + 1 : 0;
    updatePhoto();
};

// Инициализируем фото
updatePhoto();


        const modal = document.getElementById("modal");
        const modalImage = document.getElementById("modal-image");

        // Отображаем модальное окно и устанавливаем источник изображения
        function displayModal(img)
        {
            modal.style.display = "block";
            modalImage.src = img.src;
        }

        // Скрываем содержимое модального окна, если пользователь кликнул вне его
        function hideModal()
        {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }