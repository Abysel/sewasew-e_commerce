const nav_links = document.querySelectorAll(".nav")

nav_links.forEach(nav => {
    nav.addEventListener("click", function (e) {
        const navs = document.querySelectorAll(".nav");
        for (const nav of navs) {
            if (nav.classList.contains("active")) {
                nav.classList.remove("active");
            }
        }
        e.target.classList.add("active");

    });

})

const dropdown = document.querySelector('.dropdown')
const select = document.querySelector('.select')
const arrow = document.querySelector('.arrow')
const menu = document.querySelector('.menu')
const options = document.querySelectorAll('.menu .sub')
const selected = document.querySelector('.selected')
//lop

select.addEventListener('click', () => {
    select.classList.toggle('select-clicked');
    arrow.classList.toggle('arrow-rotate');
    menu.classList.toggle('menu-open');
});
options.forEach(option => {
    option.addEventListener('click', () => {
        select.classList.remove('select-clicked');
        arrow.classList.remove('arrow-rotate');
        menu.classList.remove('menu-open');
        options.forEach(option => {
            option.classList.remove('active_category');
        })
        option.classList.add('active_category');
    })
})