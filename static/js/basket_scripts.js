window.onload = function() {
    addEvent()
}

addEvent = () => {
    inputs = document.querySelectorAll('input[type="number"]');
    inputs.forEach((input) => input.addEventListener('click', (event) => changeBasket()));
}

changeBasket = () => {
        let basket = document.querySelector('.inc_basket_items')
        fetch(`/basket/edit/${event.target.name}/${event.target.value}/`, {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                    }
                })
            .then(response => response.json())
            .then(response => {
                basket.innerHTML = response.result;
            })
            .then(() => addEvent());
}




