
$('.books').ready( function() {

  });


$(document).ready({




})
function cart(){
$.ajax({
     url : "http://127.0.0.1:8000/api/addtocart",
     dataType: "json",
     success : function (data) {}


         });

}


function Search()
{
var a = $('.search').val();
$.ajax({
     url : "http://127.0.0.1:8000/api/books/search?name="+a,
     dataType: "json",
     success : function (data) {
     var url_temp = ''

    $('.books').empty();
         for (var i=0; i<data.length; i++)
         {
             if (data[i] !== null) {
                 var pk = data[i].pk;

                 $books = '<form method="POST" action = "http://127.0.0.1:8000/index">'+
                          getCookie('csrftoken')+
                     '<div class="col-md-3 col-xs-5 prod">\n' +
                     '                        <!-- BEGIN books -->\n' +
                     '                           <div class="product">\n' +
                     '                              <div class="product-img">\n' +
					 '  		                    <img height="250px" src="'+data[i].image+'" alt="">\n' +
					 '                              </div>' +
					 '                              <div class="product-body">\n' +
					 '                               <p class="product-category">' +data[i].category + '</p>\n' +
					 '                               <h3 class="product-name">'+data[i].name +'</a></h3>\n' +
					 '                               <h3 class="product-name">'+data[i].author + '</a></h3>\n' +
					 '                               <h4 class="product-price">'+data[i].price+'$</h4>\n' +
					 '                               <div class="product-rating">'+'</div> \n' +
					 '                               <div class="product-btns">\n' +
					 '			<button class="add-to-wishlist"><i class="fa fa-heart-o"></i><span class="tooltipp">add to wishlist</span></button>\n' +
					 '			<button class="add-to-compare"><i class="fa fa-exchange"></i><span class="tooltipp">add to compare</span></button>\n' +
					 '			<button class="quick-view"><i class="fa fa-eye"></i><span class="tooltipp">quick view</span></button>\n' +
					 '     </div>\n'+
					 ' </div>\n' +
					 '		<div class="add-to-cart">\n'+
					 '		<button type = "submit" class="cart add-to-cart-btn"><i class="fa fa-shopping-cart"></i> Buy Now</button>\n' +
					 '		</div>\n '+
					 '	</div>'+
					 '<input type="hidden" name = "book_id" value="'+data[i].pk+'" >'+
					 '<input type="hidden" name = "book_price" value="'+data[i].price+'" >'+

					 '</form>';

                 $('.books').append($books);
             }
             else{
                 continue;
            }
         }
            }
         });
}



function Cat_Search(a)
{
$.ajax({
     url : "http://127.0.0.1:8000/api/books/cat/?category="+a,
     dataType: "json",
     success : function (data) {
     var url_temp = ''

    $('.books').empty();
         for (var i=0; i<data.length; i++)
         {
             if (data[i] !== null) {
                 var pk = data[i].pk;

                 $books = ' <div class="col-md-3 col-xs-5 prod">\n' +
                     '                        <!-- BEGIN books -->\n' +
                     '                           <div class="product">\n' +
                     '                              <div class="product-img">\n' +
					 '  		                    <img height="250px" src="'+data[i].image+'" alt="">\n' +
					 '                              </div>' +
					 '                              <div class="product-body">\n' +
					 '                               <p class="product-category">' +data[i].category + '</p>\n' +
					 '                               <h3 class="product-name">'+data[i].name +'</a></h3>\n' +
					 '                               <h3 class="product-name">'+data[i].author + '</a></h3>\n' +
					 '                               <h4 class="product-price">'+data[i].price+'$</h4>\n' +
					 '                               <div class="product-rating">'+'</div> \n' +
					 '                               <div class="product-btns">\n' +
					 '			<button class="add-to-wishlist"><i class="fa fa-heart-o"></i><span class="tooltipp">add to wishlist</span></button>\n' +
					 '			<button class="add-to-compare"><i class="fa fa-exchange"></i><span class="tooltipp">add to compare</span></button>\n' +
					 '			<button class="quick-view"><i class="fa fa-eye"></i><span class="tooltipp">quick view</span></button>\n' +
					 '     </div>\n'+
					 ' </div>\n' +
					 '		<div class="add-to-cart">\n'+
					 '		<button onclick="cart()" class="cart add-to-cart-btn"><i class="fa fa-shopping-cart"></i> Buy Now</button>\n' +
					 '		</div>\n '+
					 '	</div>';

                 $('.books').append($books);
             }
             else{
                 continue;
            }
         }
            }
         });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
