from aiogram import types
from loader import *
from data.products import *
from data.config import *



@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(
            shipping_query_id=query.id,
            ok = False,
            error_message="Chet elga yetkazib bera olmaymiz"
        )
    elif query.shipping_address.city.lower()=="tashkent":
        await bot.answer_shipping_query(
            shipping_query_id=query.id, 
            shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
            ok=True
        )
    else:
        await bot.answer_shipping_query(
            shipping_query_id=query.id,
            shipping_options=[REGULAR_SHIPPING, PICKUP_SHIPPING],
            ok=True
        )



@dp.pre_checkout_query_handler()
async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id, ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id, text = "š„³ Xaridingiz uchun tashakkur. š")
    await bot.send_message(chat_id=ADMINS[0],
                            text=f"š Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}ā\n"
                                f"š ID: {pre_checkout_query.id}\n"
                                f"šāāļø Telegram user: {pre_checkout_query.from_user.first_name}\n"
                                f"š Username: @{pre_checkout_query.from_user.username}\n"
                                f"š Xaridor: {pre_checkout_query.order_info.name}\nš± Telefon: {pre_checkout_query.order_info.phone_number}")