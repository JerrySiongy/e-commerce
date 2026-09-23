//select elements
const productsEl = document.querySelector(".products");


//render products
function renderProducts() {
	products.forEach((product) => {
		productsEl.innerHTML += `
        <div class="col-sm-12 col-md-3 item">
			<div class="item-container item-img">
				<div class="card">
					<img src="${product.imgSrc}" style="height:290px;" alt="${product.name}" />
						<div class="card-body">
							<div class="desc">
								<ul class="list-group list-group-flush">
									<li class="list-group-item">
										<p>${product.name}</p>
									</li>
									<li>
										<p style="color:black;">${product.description}</p>
									</li>
								</ul>
							</div>
						</div>
						<div class="card-body">
							<a href="#" class="card-link">Price: <small>$</small>${product.price}</a>
							<a href="#" class="card-link">In stock: ${product.instock}</a>
						</div>
				</div>
				<div class="add-to-cart" onclick ="addToCart(${product.id})" >
						<img src="static/images/icons/bag-plus.png" alt="add to cart"/>
				</div>
			</div>
		</div>
        `;
	});
}

renderProducts();
