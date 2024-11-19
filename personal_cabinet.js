function confirmDeleteCard(url) {
    var userConfirmed = confirm("Вы уверены, что хотите удалить объявление?");
    if (userConfirmed) {
        window.location.href = url; // Переход по ссылке, если пользователь нажал "Да"
    }
}
