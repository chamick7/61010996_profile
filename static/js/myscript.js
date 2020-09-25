


var menu_list = document.querySelectorAll('.nav_menu a');

menu_list.forEach(list => {
    list.addEventListener('click',closenav);
    
})



function education_toggle(edu_id){
    console.log(edu_id+'_info');

    var element = document.querySelector('.'+edu_id+'_info');
    element.classList.toggle('show');
}


function shownav(){
    var menu = document.querySelector('.nav_menu');

    menu.classList.toggle('show');
}

function closenav(){
    var menu = document.querySelector('.nav_menu');

    menu.classList.remove('show');
}