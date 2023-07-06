$(".cart-block").on("click", function () {
  $(".modal").addClass("modal_active");
});
$(".modal_btn").on("click", function () {
  $(".modal").removeClass("modal_active");
});
//function on_basket(e) {
//  var $parent = $(e).parent();
//  $parent.remove();
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
//}
function addToCart(e) {
  $parent = $(e).parent().parent();
  let id = $parent.attr("id");
  $.ajax({
    url: `/cart/add/${id}`,
    type: "GET",
    success: function(data) {
    if (!data.exist) {
      console.log(data);
      let $container = $(".modal_content");
      $container.prepend(`<div id= "${data.id}" class="modal_content_product">
      <div class="modal_content_product_wrap">
        <img
          src="${data.photo_url}"
          alt=""
          class="modal_content_product_wrap_img"
        />
      </div>
      <div class="modal_content_product_descr">
        <b>${data.name}</b>
        <br />
      </div>
      <div class="modal_content_product_menu">
        <button
          class="modal_content_product_menu_btn"
          onclick="on_decrement(this)"
        >
          -
        </button>
        <div class="modal_content_product_menu_item">
        ${data.quantity}
        </div>
        <button
          class="modal_content_product_menu_btn"
          onclick="on_increment(this)"
        >
          +
        </button>
      </div>
      <p class="modal_content_product_price">${data.price}</p>
      <input id="spacer_id" type="hidden" name="id" value="${data.id}" />
      <input
        id="spacer_price"
        type="hidden"
        name="price"
        value="${data.price}"
      />
      <button
        class="modal_content_product_backet"
        onclick="deleteItem(this)"
      >
        <img
          src="{% static 'base/img/trash.svg' %}"
          alt="trash"
          class="modal_content_product_backet_img"
        />
      </button>
    </div>`);
    }else{
    const price = $(e).children(".modal_content_product_price").text())
    price = parseInt(price)
    }},
  });
  $(".modal").addClass("modal_active");
}

//if (условие) {
//если условие тру, то код исполняется внутри скобок
//} else {
//этот код исполняется если условие фолс
//}

function deleteItem(e) {
  $parent = $(e).parent();
  let id = $parent.attr("id");
  $parent.remove();


  $.ajax({
    url: `/cart/delete/${id}`,
    type: "GET",
  });

}

function on_decrement(e) {
  $parent = $(e).parent().parent();
  let id = $parent.attr("id");
  $.ajax({
    url: `/cart/decrement/${id}`,
    type: "GET",
  });
  /*           <div id= "{{ item.id }}" class="modal_content_product">
            <div class="modal_content_product_wrap">
              <img
                src="{{ item.photo_url }}"
                alt=""
                class="modal_content_product_wrap_img"
              />
            </div>
            <div class="modal_content_product_descr">
              <b>{{item.name}}</b>
              <br />
            </div>
            <div class="modal_content_product_menu">
              <button
                class="modal_content_product_menu_btn"
                onclick="on_decrement(this)"
              >
                -
              </button>
              <div class="modal_content_product_menu_item">
                {{item.quantity}}
              </div>
              <button
                class="modal_content_product_menu_btn"
                onclick="on_increment(this)"
              >
                +
              </button>
            </div>
            <p class="modal_content_product_price">{{ item.total_price }}</p>
            <input id="spacer_id" type="hidden" name="id" value="{{item.id}}" />
            <input
              id="spacer_price"
              type="hidden"
              name="price"
              value="{{item.price}}"
            />
            <button
              class="modal_content_product_backet"
              onclick="deleteItem(this)"
            >
              <img
                src="{% static 'base/img/trash.svg' %}"
                alt="trash"
                class="modal_content_product_backet_img"
              />
            </button>
          </div> */
  $parent2 = $(e).parent();
  cout = $parent2.children(".modal_content_product_menu_item");
  cout_int = parseInt(cout.text());
  cout.text(cout_int-1);
}

function on_increment(e) {
    addToCart(e);
    $parent = $(e).parent();
    cout = $parent.children(".modal_content_product_menu_item");
    cout_int = parseInt(cout.text());
    cout.text(cout_int+1);
}

function modal_content_product_price(e) {

}