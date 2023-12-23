import os
from telegram import ParseMode
from telegram.ext import Updater
from config import config
import time


startup_txt = "🆙 <b>آماده سوارکاری</b> 🆙"
login_txt = "✅ یه نفر با آیپی <code>{ip}</code> بعد از {t} دقیقه سوارم شد."
fast_login_txt = "✅ یه نفر با آیپی <code>{ip}</code> درجا سوارم شد."
logout_txt = "🛑 سوارکار، <code>{ip}</code> بعد از {t} دقیقه پیاده شد."
_ip = None
_old = []
begin = time.time()
end = None


updater = Updater(
    config.BOT_TOKEN,
    request_kwargs = {
        'proxy_url': config.P_URL,
        'urllib3_proxy_kwargs': {
            'username': config.P_USER,
            'password': config.P_PASS,
        }
    }
)


try:
    message = updater.bot.send_message(
        chat_id=config.CID, 
        text=startup_txt,
        parse_mode=ParseMode.HTML
    )
    _start = True
except Exception as e:
    print(e)
    _start = False


while _start:
    output = os.popen('netstat -an | findstr ":9192" | findstr "ESTABLISHED"').read().strip()
    while '  ' in output:
        output = output.replace('  ', ' ')
    _new = output.split(' ')

    if _old != _new:
        if len(_new) == 1:
            _end = time.time()
            if (_end-begin) < 60:
                updater.bot.delete_message(
                    chat_id=_cid,
                    message_id=_mid
                )
                _cid=None
                _mid=None
            else:
                end=_end
                message = updater.bot.send_message(
                    chat_id=config.CID,
                    text=logout_txt.format(ip=_ip, t=int((end-begin)//60)),
                    parse_mode=ParseMode.HTML
                )
                _cid = message.chat.id
                _mid = message.message_id
            _ip = None
        else:
            if _new[2].split(':')[0] != _ip:
                _ip = _new[2].split(':')[0]
                end = time.time()
                if (end-begin) < 60:
                    message = updater.bot.send_message(
                        chat_id=config.CID,
                        text=fast_login_txt.format(ip=_ip),
                        parse_mode=ParseMode.HTML
                    )
                else:
                    message = updater.bot.send_message(
                        chat_id=config.CID, 
                        text=login_txt.format(ip=_ip, t=int((end-begin)//60)),
                        parse_mode=ParseMode.HTML
                    )
                _cid = message.chat.id
                _mid = message.message_id
        begin=end
        _old = _new
            
    time.sleep(1)
