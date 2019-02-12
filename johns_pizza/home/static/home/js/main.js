
document.addEventListener("DOMContentLoaded", function() {
    const addButtons = document.querySelectorAll('#add-item');
    const addToCart = document.querySelector('#add-to-cart');
    const shoppingCart = document.querySelector('.shopping-cart');

    shoppingCart.addEventListener('click', function(){

    });

    addToCart.addEventListener('click', function(){

    });
    
    addButtons.forEach(button => {
        foodData = [];
        button.addEventListener("click", function(e){
            const buttonID = e.target.getAttribute('data-number');
            heading = document.querySelector(`[data-type='${buttonID}']`);
            foodData.push(heading.innerText);
            const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
            inputs.forEach(item => foodData.push(item.value));
            getPrice(foodData, buttonID);
        });
    })
});

function getPrice(foodData, buttonID) {
    const request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                data = this.responseText;
                data = JSON.parse(data);
                if (data) {
                    price = data.price;
                    updatePrice(price, buttonID);
                }
            }
        }
        request.open('GET', `/${foodData[0]}/${foodData[1]}/${foodData[3]}/${foodData[2]}`, true);
        request.send();
}

function updatePrice(price, buttonID) {
    console.log(price + " " + buttonID);
    const input = document.querySelector(`[data-amount='${buttonID}']`);
    console.log(input);
    input.value = price;
}