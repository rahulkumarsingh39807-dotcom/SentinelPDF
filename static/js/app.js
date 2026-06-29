document.addEventListener("DOMContentLoaded", function () {

    const sidebar = document.getElementById("sidebar");
    const menu = document.getElementById("menu-toggle");

    if (menu) {
        menu.addEventListener("click", function () {
            sidebar.classList.toggle("active");
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener("click", function (e) {

        if (
            window.innerWidth <= 992 &&
            sidebar &&
            !sidebar.contains(e.target) &&
            !menu.contains(e.target)
        ) {
            sidebar.classList.remove("active");
        }

    });

});