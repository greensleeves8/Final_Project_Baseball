const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li')


    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    });
    navLinks.forEach((link, index) => {
        link.style.animation = 'navLinkFade 0.5s ease forward ${index / 7}s';
        console.log(index / 7):
    }):
}

navSlide();

const url = "https://en.wikipedia.org/wiki/Major_League_Baseball_logo#/media/File:Major_League_Baseball_logo.svg;