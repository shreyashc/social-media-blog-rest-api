const showMoreBtn = document.querySelector(".show-more-btn");
const more = document.querySelector(".more");
const menuToggle = document.querySelector(".menu-toggle");
const bars = document.querySelector("i.fas");
const nav = document.querySelector("nav");
const navLinks = document.querySelectorAll("nav a");

showMoreBtn.addEventListener("click", function () {
    more.style.display = "block";
    this.style.display = "none";
});

menuToggle.addEventListener("click", function () {
    nav.classList.toggle("active");
    bars.classList.toggle("fa-bars");
    bars.classList.toggle("fa-times");
});

navLinks.forEach((link) => {
    link.addEventListener("click", function () {
        nav.classList.toggle("active");
        bars.classList.toggle("fa-bars");
        bars.classList.toggle("fa-times");
    });
});
