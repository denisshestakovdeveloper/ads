function confirmNavigation(url) {
    var userConfirmed = confirm("Вы уверены, что хотите удалить изображение?");
    if (userConfirmed) {
        window.location.href = url; // Переход по ссылке, если пользователь нажал "Да"
    }
}
