



function education_toggle(edu_id){
    console.log(edu_id+'_info');

    var element = document.querySelector('.'+edu_id+'_info');
    element.classList.toggle('show');
}