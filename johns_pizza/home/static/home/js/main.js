var userOrders = [];

document.addEventListener("DOMContentLoaded", function () {
    const addButtons = document.querySelectorAll('#add-item');
    const addToCart = document.querySelector('#add-to-cart');
    const shoppingCart = document.querySelector('.shopping-cart');

    showCart(userOrders);

    shoppingCart.addEventListener('click', function () {
        console.log("Shopping cart clicked...");
        getOrders();
    });


    addToCart.addEventListener('click', function () {
        getOrders();
    });

    addButtons.forEach(button => {
        foodData = [];
        button.addEventListener("click", function (e) {
            const buttonID = e.target.getAttribute('data-number');
            heading = document.querySelector(`[data-type='${buttonID}']`);
            foodData.push(heading.innerText);
            const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
            inputs.forEach(item => foodData.push(item.value));
            getPrice(foodData, buttonID);
        });
    })
});

//api routes
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

function getOrders() {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            userOrders = [];
            data = this.responseText;
            data = JSON.parse(data)
            data = data.orders;
            data.forEach(food => {
                console.log(food);
                userOrders.push(food);
            });
            showCart(userOrders);
        }
    }
    request.open('GET', `/getorders`, true);
    request.send();
}


//dom modifiers
function updatePrice(price, buttonID) {
    console.log(price + " " + buttonID);
    const input = document.querySelector(`[data-amount='${buttonID}']`);
    console.log(input);
    input.value = price;
}

function showCart(orderArray) {
    //make sure array is not empty
    console.log('inside show cart');
    if (orderArray) {
        const dropdown = document.querySelector("#shop-dropdown");
        console.log(orderArray);
        dropdown.innerHTML = '';
        orderArray.forEach(food => {

            let listItem = document.createElement('a');
            listItem.className = "dropdown-item";
            listItem.innerText = `${food[0]}: ${food[1]} ${food[2]}'s of size ${food[3]} topped with ${food[4]}`;
            dropdown.appendChild(listItem);
        });
    } 
}