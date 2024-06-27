document.addEventListener("DOMContentLoaded" , function(){
    const toggle = document.querySelector(".nav-bar");
    const btn = document.querySelector(".btn");
    const dropdown = document.querySelector(".active")

    let isOpen = false;


    btn.addEventListener("click", (event) => {
        event.preventDefault();
        isOpen = !isOpen;

        if(!toggle.classList.contains('toggle')){
            toggle.classList.add('toggle')
            dropdown.classList.add('dropdown')
        }else{
            toggle.classList.remove('toggle')
            dropdown.classList.remove('dropdown')
        }

        console.log(isOpen)
    })

});