$(".cart-block").on("click", function () {
  $(".modal").addClass("modal_active");
});
$(".modal_btn").on("click", function () {
  $(".modal").removeClass("modal_active");
});
function on_basket(e) {
  var $parent = $(e).parent();
  $parent.remove();
  //   var id = $parent.children().val();
  // $.ajax({
  //   url: "/cart/",
  //   type: "DELETE",
  //   // contentType:"application/json",
  //   beforeSend: function (xhr) {
  //     xhr.setRequestHeader("X-CSRFToken", csrftoken);
  //   },
  //   data: {
  //     csrfmiddlewaretoken: csrftoken,
  //     id: id,
  //   },
  // });
  //   var element = $(".head_last_cart_text");
  //   var current = parseInt(element.text());
  //   element.text(--current);
  //   var $now = $(".modal_content_product_text_link");
  //   var qt = parseInt($now.text().split(" ")[2]);
  //   --qt;
  //   if (qt === 0) {
  //     $now.text("Корзина пуста");
  //   } else {
  //     $now.text(`В корзине ${qt} товаров`);
  //   }
}
function addToCart(e) {
  $parent = $(e).parent().parent();
  let id = $parent.attr("id");
  $.ajax({
    url: `/cart/add/${id}`,
    type: "GET",
  });
  $(".modal").addClass("modal_active");
}