const menu_icon = document.querySelector('.menu_icon');
const menu = document.querySelector('.menu');
const icon = document.querySelector('.menu_icon i');



menu_icon.addEventListener('click',() => {
    console.log("clicked");
    menu.classList.toggle('menu_active');
    icon.classList.toggle('fa-times');
    // if (icon.classList == 'fa-times')
    // {
    //     icon.classList.add('fa-times');
    //     icon.classList.remove('fa-bars');
    // }
    // else{
    //     icon.classList.remove('fa-times');
    //     icon.classList.add('fa-bars');
    // }




})