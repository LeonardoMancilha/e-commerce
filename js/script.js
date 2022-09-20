let menu_items = document.getElementById('menuitems');
menu_items.style.maxHeight = "0px";

function menutoggle() {
    if (menu_items.style.maxHeight === '0px') {
        menu_items.style.maxHeight = '200px';
    }
    else {
        menu_items.style.maxHeight = '0px';
        }
}

let product_image = document.getElementById('product-image');
let small_image = document.getElementsByClassName('small-image');
small_image[0].onclick = function () {
    product_image.src = small_image[0].src;
}
small_image[1].onclick = function () {
    product_image.src = small_image[1].src;
}
small_image[2].onclick = function () {
    product_image.src = small_image[2].src;
}
small_image[3].onclick = function () {
    product_image.src = small_image[3].src;
}

const year = document.getElementsByClassName('year');
const actualYear = new Date();
year[0].innerHTML = actualYear.getFullYear();

function register() {
    let login_form = document.getElementsByClassName('login-form')[0];
    let register_form = document.getElementsByClassName('register-form')[0];
    let indicator = document.getElementsByClassName('indicator')[0];
    register_form.style.transform = 'translateX(0px)';
    login_form.style.transform = 'translateX(0px)';
    indicator.style.transform = 'translateX(100px)';
}

function login() {
    let login_form = document.getElementsByClassName('login-form')[0];
    let register_form = document.getElementsByClassName('register-form')[0];
    let indicator = document.getElementsByClassName('indicator')[0];
    register_form.style.transform = 'translateX(300px)';
    login_form.style.transform = 'translateX(300px)';
    indicator.style.transform = 'translateX(0px)';
}
