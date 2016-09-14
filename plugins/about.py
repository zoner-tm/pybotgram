import asyncio
from message import Message


@asyncio.coroutine
def run(message, matches, chat_id, step):
    return [Message(chat_id).set_text(
        "*Bot Search Music!*\n_✔Fast and accurate✔", parse_mode="markdown")]


plugin = {
    "name": "About",
    "desc": "Get Information About The Developer!",
    "usage": ["/about"],
    "run": run,
    "sudo": False,
    "patterns": ["^[!/#]about$"]
}
