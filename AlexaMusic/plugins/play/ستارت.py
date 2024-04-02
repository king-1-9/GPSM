from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from AlexaMusic import app as Client
from AlexaMusic import app
from pyrogram.types import InlineKeyboardButton
import config
import asyncio
import random


@app.on_message(filters.command(["hmd"],""))
async def arbic(_, query: CallbackQuery):
    await message.reply_text("مرحبا بك معنا في منصة القرآن الكريم على التيليجرام .\n\n[للملاحظات و الاقتراحات](t.me/J_1_E) , ولا تتردد في زيارة [قناتنا](t.me/i88Y8) .", disable_web_page_preview=True)
        await message.reply_text("كيف تفضل طريقة الاختيار ؟",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت الى مجموعتك ⚡♥",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" الدعم والتواصل ", url=config.SUPPORT_CHAT),
                ],
                [                   InlineKeyboardButton(" طريقه التشغيل ", callback_data="bcmds"),
                    InlineKeyboardButton(" طريقه التفعيل ", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        " الدعم ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " القناة ", url=config.SUPPORT_CHANNEL),
                ],
                [
                    InlineKeyboardButton(
                        " الـمطور ", user_id=config.OWNER_ID 
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
            keyboard=[[KeyboardButton("عشوائي ➰"), KeyboardButton("سأختار 🤍")]], resize_keyboard=True))
