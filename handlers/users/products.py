from aiogram import types
from keyboards.inline.buttons import *
from loader import dp



@dp.callback_query_handler(text = "iwatch")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/iwatch.jpg")
    caption = """
π Nomi: βοΈ Apple Watch
π° Narxi: 850000
π Mahsulot haqida ma'lumotlar:πππ

πΈiWatch
πΈIshlashlari tez
πΈQotmaydi
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("iwatch"))
    await call.message.delete()



@dp.callback_query_handler(text = "drone")
async def dron_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/dron.jpg")
    caption = """
π Nomi: π© Dron 521
π° Narxi: 450000
π Mahsulot haqida ma'lumotlar:πππ

π© Dron sotiladi
π© Uchish tezligi ham yaxshi
π© Zaryadkasi 8 soatga yetadi
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("dron"))
    await call.message.delete()



@dp.callback_query_handler(text = "microphone")
async def microphone_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/microphone.jpg")
    caption = """
π Nomi: π Mikrofon
π° Narxi: 900000
π Mahsulot haqida ma'lumotlar:πππ

π§© Gamerlar va blogerlar uchun yangi mikrafon
π§© Ovozni tiniq yozadi
π§© RGB 
π O'zbekiston bo'ylab bepul yetkazib beramiz β
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("microphone"))
    await call.message.delete()


@dp.callback_query_handler(text = "keyboard")
async def keyboard_handler(call: types.CallbackQuery):
    rasm = "https://techbroll.com/wp-content/uploads/2020/04/A6408408-scaled.jpg"
    caption = """
π Nomi: β¨οΈ RGB-Klaviatura
π° Narxi: 1 200 000 so'm 
π Mahsulot haqida ma'lumotlar:πππ

π§© Gamerlar va blogerlar uchun yangi rgb-klaviatura
π§© Tez ishlaydi
π§© RGB
π§© 7 xil rangda yonadi
    """
    # photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard")
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard"))
    await call.message.delete()

@dp.callback_query_handler(text = "costum")
async def keyboard_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/costum.jpg")
    caption = """
π Nomi: Erkaklar uchun kostyum-shim
π° Narxi: 1 200 000 so'm 
π Mahsulot haqida ma'lumotlar:πππ

π§© Yigitlar uchun oqshom to'y libosi
π§© Yangi
π§© Ko'ylagi ham bor
π§© Qora
    """
    # photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard")
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("costum"))
    await call.message.delete()

@dp.callback_query_handler(text = "coat")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/palto.jpg")
    caption = """
π Nomi: Ayollar uchun qishki palto
π° Narxi: 1 800 000
π Mahsulot haqida ma'lumotlar:πππ

πΈ Qish uchun yaxshi libos
πΈ Qizil rangda
πΈ Garantiyasi ham bor
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("coat"))
    await call.message.delete()

@dp.callback_query_handler(text = "bag")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/sumka.jpg")
    caption = """
π Nomi: Ayollar uchun sumka
π° Narxi: 500 000
π Mahsulot haqida ma'lumotlar:πππ

πΈ Yaxshi narsa
πΈ Kattagina sumka
πΈ Qora rangda
πΈ Charmdan qilingan
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("bag"))
    await call.message.delete()
# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "hamburger")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://e7.pngegg.com/pngimages/121/878/png-clipart-whopper-cheeseburger-veggie-burger-hamburger-mcdonald-s-big-mac-burger-beef.png"
    caption = """
π Nomi: π Gamburger
π° Narxi: 12 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("hamburger"))
    await call.message.delete()

@dp.callback_query_handler(text = "lavash")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://w7.pngwing.com/pngs/16/539/png-transparent-taco-shawarma-fast-food-doner-kebab-hamburger-hot-dog-jamon-food-recipe-street-food.png"
    caption = """
π Nomi: π Gamburger
π° Narxi: 20 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("lavash"))
    await call.message.delete()


@dp.callback_query_handler(text = "hotdog")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://www.downloadclipart.net/large/hot-dog-png-transparent.png"
    caption = """
π Nomi: π Gamburger
π° Narxi: 15 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("hotdog"))
    await call.message.delete()







@dp.callback_query_handler(text = "pitsa")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://catherineasquithgallery.com/uploads/posts/2021-03/1614548182_9-p-pitstsa-na-belom-fone-13.jpg"
    caption = """
π Nomi: π Gamburger
π° Narxi: 35 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("pitsa"))
    await call.message.delete()

