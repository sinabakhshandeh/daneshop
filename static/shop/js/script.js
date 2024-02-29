$(document).ready(function() {

    function createDynamicAlert() {
        var dynamicAlert = `
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>Product added to Cart</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`;
        $('#alert').append(dynamicAlert);
    }

    function removeDynamicAlert() {
        $('#alert').empty();
    }




    $("#addToCart").click(function(event) {
        event.preventDefault();
        var username = $("#username").val();
        var product_slug = $("#product_slug").val();
        var quantity = $("#quantity").val();
        var csrftoken = $("input[name='csrfmiddlewaretoken']").val().trim();

        $.ajax({
            url: "/cart/add/item/",
            type: "POST",
            data: {
                username: username,
                product_slug: product_slug,
                quantity: quantity,
                csrfmiddlewaretoken:csrftoken
            },

            success: function(response) {
                if (response == "success"){
                    console.log("tada");
                    createDynamicAlert();
                    setTimeout(removeDynamicAlert, 1000);
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});
