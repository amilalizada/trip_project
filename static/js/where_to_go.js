document.onclick = function (e) {
    if (e.target.closest(".all-options") && e.target.closest(".position-relative").querySelector('.all-option-tables').classList.contains('d-block')) {
        let parentElement = e.target.closest(".position-relative")
        parentElement.querySelector('.all-option-tables').classList.remove("d-block");
        parentElement.querySelector('.all-option-tables').classList.add("d-none");
    }
    else if (e.target.closest(".all-options") && e.target.closest(".position-relative").querySelector('.all-option-tables').classList.contains('d-none')) {
        document.querySelectorAll('.all-option-tables').forEach(function (e) {
            e.classList.remove("d-block");
            e.classList.add("d-none");
        })
        let parentElement = e.target.closest(".position-relative")
        parentElement.querySelector('.all-option-tables').classList.remove("d-none");
        parentElement.querySelector('.all-option-tables').classList.add("d-block");
    }
    else if (!e.target.closest(".all-option-tables")) {
        document.querySelectorAll('.all-option-tables').forEach(function (e) {
            e.classList.remove("d-block");
            e.classList.add("d-none");
        })
    }
}