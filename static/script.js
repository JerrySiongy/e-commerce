//select elements
const productsEl = document.querySelector(".products");
const cartItemsEl = document.querySelector(".cart-items");
const subtotalEl = document.querySelector(".subtotal");
const totalItemsInCartEl = document.querySelector(".total-items-in-cart");

//render products
function renderProducts() {
    products.forEach((product) => {
        productsEl.innerHTML += `
        <div class="item m-2">
			<div class="item-container item-img">
				<div class="card">
					<img src="${product.imgSrc}" alt="${product.name}" />
						<div class="card-body">
							<div class="desc">
								<ul class="list-group list-group-flush">
									<li class="list-group-item">
										<h2>T-shirt 1</h2>
									</li>
									<li>
										<h2><small>$</small>29.99</h2>
									</li>
								</ul>
							</div>
						</div>

						<div class="card-body">
							<a href="#" class="card-link">Card link</a>
							<a href="#" class="card-link">Another link</a>
						</div>
				</div>
				<div class="add-to-wishlist">
						<img src="static/images/icons/heart.png" alt="add to wish list" />
				</div>
				<div class="add-to-cart" onclick ="addToCart(${product.id})" >
						<img src="static/images/icons/bag-plus.png" alt="add to cart" />
				</div>
			</div>
		</div>
        `;
    });
}

renderProducts();

//cart array
let cart =JSON.parse(localStorage.getItem("CART")) || [] ;
updateCart();

// add to cart
function addToCart(id){
	//check if product already exists in cart
	if(cart.some((item) => item.id === id )){
		changeNumberOfUnits("plus", id)
	}else{
		const item = products.find((product) => product.id === id)
	cart.push({
		...item,
		numberOfUnits : 1
	});
	}

updateCart();
}

//update cart

function updateCart(){
	renderCartItems();
	renderSubTotal();

	//save cart to local storage
	localStorage.setItem("CART", JSON.stringify(cart)); 
}

//calculate and render subtotal
function renderSubTotal(){
	let totalPrice = 0, totalItems = 0;

	cart.forEach((item) =>{
		totalPrice += item.price * item.numberOfUnits;
		totalItems += item.numberOfUnits;
	});

	subtotalEl.innerHTML = `Subtotal (${totalItems} items): $${totalPrice.toFixed(2)}`;
	totalItemsInCartEl.innerHTML = totalItems;
}

//render Cart items
function renderCartItems(){
	cartItemsEl.innerHTML =""; //clear cart element
	cart.forEach((item) =>{
		cartItemsEl.innerHTML += `
		<div class="cart-item">
						<tr>
							<th scope="row">1</th>
							<td>
								<div class="item-info" onclick ="removeCartItem(${item.id})">
									<div class="card border border-0" style="width: 50px; height: 65px;">
										<img src="${item.imgSrc}" alt="${item.name}" />
									</div>
									<div class="card-body">
										<p class="card-text">${item.name}</p>
									</div>
								</div>
							</td>
							<td>
								<div class="unit-price"><small>$</small>${item.price}</div>
							</td>
							<td>
								<div class="units">

									<p class="number"><span class="btn minus" onclick="changeNumberOfUnits('minus',${item.id})">-</span>${item.numberOfUnits}
									<span class="btn plus" onclick="changeNumberOfUnits('plus', ${item.id})">+</span></p>
								</div>
							</td>
						</tr>
					</div>
		`
	});	
}

//remove item from cart
function removeCartItem(id){
	cart = cart.filter((item) => item.id !== id );

	updateCart();

}


//change number of units for an item
function changeNumberOfUnits(action, id){
	cart = cart.map((item) =>{

		let numberOfUnits = item.numberOfUnits;

		if(item.id === id){
			if(action ==="minus" && numberOfUnits > 1){
				numberOfUnits --;
			}else if(action === "plus" && numberOfUnits < item.instock){
				numberOfUnits ++;
			}
		}
		return {
			...item,
			numberOfUnits,
		}
	});

	updateCart();
}