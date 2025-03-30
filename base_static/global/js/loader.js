export default (function() {
    document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("loader").style.display = "flex";

        window.addEventListener("load", function () {
            document.getElementById("loader").style.display = "none";
        });
    });
})();
