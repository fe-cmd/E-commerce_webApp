import json
from account.models import Address
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from orders.models import Order, OrderItem

from .models import DeliveryOptions



@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "checkout/delivery_choices.html", {"deliveryoptions": deliveryoptions})


@login_required
def cart_update_delivery(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = cart.cart_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response


@login_required
def delivery_address(request):

    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    addresses = Address.objects.filter(customer=request.user).order_by("-default")

    if "address" not in request.session:
        session["address"] = {"address_id": str(addresses[0].id)}
    else:
        session["address"]["address_id"] = str(addresses[0].id)
        session.modified = True

    return render(request, "checkout/delivery_address.html", {"addresses": addresses})


@login_required
def payment_selection(request):

    session = request.session
    if "address" not in request.session:
        messages.success(request, "Please select address option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    return render(request, "checkout/payment_selection.html", {})


####
# PayPal
####


from .paypal import PayPalClient


@login_required
def payment_complete(request):
    PPClient = PayPalClient()
    body = json.loads(request.body)
    payment_id = body.get("orderID")  # This should match the PayPal payment ID returned after approval
    user_id = request.user.id

    payment = PPClient.get_payment(payment_id)

    if not payment or not payment.success():
        return JsonResponse({"error": "Payment not found or failed"}, status=400)

    # Extract details
    payer_info = payment.payer.payer_info
    transactions = payment.transactions[0]
    shipping = transactions.item_list.shipping_address

    total_paid = transactions.amount.total

    cart = Cart(request)
    order = Order.objects.create(
        user_id=user_id,
        full_name=f"{payer_info.first_name} {payer_info.last_name}",
        email=payer_info.email,
        address1=shipping.line1,
        address2=shipping.city,
        postal_code=shipping.postal_code,
        country_code=shipping.country_code,
        total_paid=total_paid,
        order_key=payment.id,
        payment_option="paypal",
        billing_status=True,
    )
    order_id = order.pk

    for item in cart:
        OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

    return JsonResponse("Payment completed!", safe=False)

@login_required
def payment_successful(request):
    cart = Cart(request)
    cart.clear()
    return render(request, "checkout/payment_successful.html", {})