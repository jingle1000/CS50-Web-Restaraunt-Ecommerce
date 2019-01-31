document.addEventListener("DOMContentLoaded", function() {
    const addButtons = document.querySelectorAll('#check-item');
    
    addButtons.forEach(button => {
        button.addEventListener("click", function(e){
            let infoArray = [];
            const buttonID = e.target.getAttribute('data-number');
            const totalField = document.querySelector(`#item-amount-${buttonID}`);
            const foodType = document.querySelector(`[data-type='${buttonID}']`).innerText;
            infoArray.push(foodType);
            const inputs = document.querySelectorAll(`[data-id='${buttonID}']`);
            inputs.forEach(item => infoArray.push(item.value));
            console.log(infoArray);
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
            console.log(url);
            request.open("GET", url, true);
            request.send();
        });
    })
});