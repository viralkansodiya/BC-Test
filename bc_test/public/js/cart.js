frappe.ready(() => {
    if (typeof webshop !== "undefined" && webshop.webshop.shopping_cart) {
        frappe.provide("webshop.webshop.shopping_cart");
		shopping_cart = webshop.webshop.shopping_cart;
        // Override the place_order function
		shopping_cart.place_order = function(btn) {
        shopping_cart.freeze();

		return frappe.call({
			type: "POST",
			method: "bc_test.utils.cart.place_order",
			btn: btn,
			callback: function(r) {
				if(r.exc) {
					shopping_cart.unfreeze();
					var msg = "";
					if(r._server_messages) {
						msg = JSON.parse(r._server_messages || []).join("<br>");
					}

					$("#cart-error")
						.empty()
						.html(msg || frappe._("Something went wrong!"))
						.toggle(true);
				} else {
					$(btn).hide();
					if(r.message.coupon_code){
						window.location.href = '/coupon_order/?sales_order=' + encodeURIComponent(r.message.sales_order);
					}
					else{
						window.location.href = '/orders/' + encodeURIComponent(r.message.sales_order);
						console.log(r.message)
					}
				}
			}
		});
	};
}
});