document.addEventListener("DOMContentLoaded", function () {

    const menu = document.getElementById("menu-toggle");

    const sidebar = document.getElementById("sidebar");

    if (menu && sidebar) {

        menu.addEventListener("click", function () {

            sidebar.classList.toggle("active");

        });

    }

});