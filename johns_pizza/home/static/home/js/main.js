var userOrders = [];
var userTotal = 0;

document.addEventListener("DOMContentLoaded", function () {
    const addButtons = document.querySelectorAll('#add-item');
    const addToCart = document.querySelectorAll('#add-to-cart');
    const shoppingCart = document.querySelector('.shopping-cart');

    showCart(userOrders);

    shoppingCart.addEventListener('click', function () {
        console.log("Shopping cart clicked...");
        getOrders();
    });

    addToCart.forEach(item => {
        item.addEventListener('click', function (e) {
            let foodData = [];
            const buttonID = e.target.getAttribute('data-cart');
            heading = document.querySelector(`[data-type='${buttonID}']`);
            foodData.push(heading.innerText);
            const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
            inputs.forEach(item => foodData.push(item.value));
            getOrders(userOrders);
            addItemsToCart(foodData);
        });
    });


    addButtons.forEach(button => {
        button.addEventListener("click", function (e) {
            let foodData = [];
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
                if (foodData[4] == '') {
                    price = data.price;
                } else {
                    price = data.price * foodData[4];
                    price = Math.round(price * 100) / 100
                }
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
            data = JSON.parse(data);
            console.log(data.price);
            userTotal = data.price;
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

function addItemsToCart(foodArray) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            data = this.responseText;
            data = JSON.parse(data);
            if (data.result != "success") {
                alert("Something went wrong adding the item to cart.")
            }
        }
    }
    request.open('GET', `addtocart/${foodArray[0]}/${foodArray[1]}/${foodArray[2]}/${foodArray[3]}/${foodArray[4]}`, true);
    request.send();
}




//dom modifiers
function updatePrice(price, buttonID) {
    console.log(price + " " + buttonID);
    const input = document.querySelector(`[data-amount='${buttonID}']`);
    input.value = price;
}

function showCart(orderArray) {
    //make sure array is not empty
    console.log('inside show cart');
    if (orderArray) {
        const dropdown = document.querySelector("#shop-dropdown");
        console.log(orderArray);
        dropdown.innerHTML = `<h6 class="ml-4 mt-2">My Cart</h6><p class="ml-4">Cart Total: \$${userTotal}</p><hr>`;
        orderArray.forEach(food => {
            let listItem = document.createElement('a');
            listItem.className = "dropdown-item";
            listItem.innerText = `${food[0]} ${food[1]} ${food[2]}'s of size ${food[3]} topped with ${food[4]}`;
            dropdown.appendChild(listItem);
        });
    }
}