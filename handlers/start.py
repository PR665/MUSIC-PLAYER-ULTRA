from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> 🤔HELLO KAY RE VAJAV KI 🤣🐥 {message.from_user.first_name}!</b>

I AM 😑**PM*😑 MUSIC PLAYER , AN OPEN SAURCE THAT LETS YOU PLAY MUSIC IN YOUR TELEGRAAM GROUPS .

💢THE BUTTONS BELOW TO KNOW ABOUT ME, NO ANY SUPPORT AVAILABLE IN GROUP OR CHANNELS 😑.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ 👿SAURCE CODE 👿", url="https://instagram.com/mr_purushottam_m/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬GROUP🤣", url="https://t.me/RDX_P"
                    ),
                    InlineKeyboardButton(
                        "🤣CHANNEL🔈", url="https://t.me/RDX_P"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ I WANT TO SEARCH FOR A YOUTUBE 📸 VIDEO?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ YES", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "NO ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
