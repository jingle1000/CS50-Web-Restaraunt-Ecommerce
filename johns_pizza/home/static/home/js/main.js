document.addEventListener("DOMContentLoaded", function() {
    const addButtons = document.querySelectorAll('#add-item');
    
    addButtons.forEach(button => {
        button.addEventListener("click", function(e){
            const buttonID = e.target.getAttribute('data-number');
            const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
            inputs.forEach(item => console.log(item.value));
        });
    })
});