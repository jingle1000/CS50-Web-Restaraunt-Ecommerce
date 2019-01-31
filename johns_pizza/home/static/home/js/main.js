document.addEventListener("DOMContentLoaded", function() {
    const checkButtons = document.querySelectorAll('#check-item');
    const addButtons = document.querySelectorAll('#add-item');
    const orderCart = document.querySelector("#order-cart");
    const dropdown = document.querySelector('#dropdown-cart');
    //if the check price buttons are clicked
    checkButtons.forEach(button => {
        button.addEventListener("click", function(e){
            results = getInputs(e, 'data-number');
            totalField = results[1];
            infoArray = results[0];
            const request = new XMLHttpRequest();
            request.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    data = this.responseText;
                    data = JSON.parse(data);
                    data = JSON.parse(data.food);
                    if (data[0] == undefined) {
                        totalField.value = "Sorry, We are out of stock of that item."
                    }
                    price = data[0].fields.price;
                    if (infoArray[4] === "") {
                        totalField.value = price;
                    } else {
                        totalField.value = price * infoArray[4];
                    }
                    
                }
            }
            let url = `food/${infoArray[0]}/${infoArray[1]}/${infoArray[3]}/${infoArray[2]}`;
            request.open("GET", url, true);
            request.send();
        });
    });
    // if an add to cart button is clicked
    addButtons.forEach(item => item.addEventListener('click', function(e){
        results = getInputs(e, 'data-order');
        totalField = results[1];
        infoArray = results[0];
        console.log(infoArray);
        const request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                data = this.responseText;
                data = JSON.parse(data);
                console.log(data);
            }
        }
        let url = `create-user-order/${infoArray[0]}/${infoArray[1]}/${infoArray[3]}/${infoArray[2]}`;
        request.open("GET", url, true);
        request.send();
    }));
    //if the cart button is clicked
    dropdown.addEventListener('click', function(e){
        orderCart.innerHTML = '';
        const request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                data = this.responseText;
                data = JSON.parse(data);
                data = data.orders
                data.forEach(i => {
                    let aElem = document.createElement('a');
                    aElem.classList = "dropdown-item";
                    aElem.innerText = `${i[0]} ${i[1]} ${i[2]} ${i[4]}`;
                    orderCart.appendChild(aElem);
                });

            }
        }
        let url = `get-orders/`;
        request.open("GET", url, true);
        request.send();
    });
    function getInputs(e, attributeName) {
        let infoArray = [];
        const buttonID = e.target.getAttribute(attributeName);
        const totalField = document.querySelector(`#item-amount-${buttonID}`);
        const foodType = document.querySelector(`[data-type='${buttonID}']`).innerText;
        infoArray.push(foodType);
        const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
        inputs.forEach(item => infoArray.push(item.value));
        return [infoArray, totalField];
    }
});