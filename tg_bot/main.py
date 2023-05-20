from pyrogram import Client, filters
from pyrogram.types import Message
import io
import sys

api_id = "your api id get it from https://my.telegram.org/apps"
api_hash = "your api hash get it from https://my.telegram.org/apps"

app = Client("bot token get it from bot father", api_id=api_id, api_hash=api_hash)

 #Handler for /eval command
@app.on_message(filters.command("eval"))
async def evaluate_code(client: Client, message: Message):
    # Extract the code from the message
    code = message.text.split(" ", maxsplit=1)[1]

    try:
        # Redirect standard output to a variable
        stdout = io.StringIO()
        sys.stdout = stdout

        # Execute the code
        exec(code)

        # Restore standard output
        sys.stdout = sys.__stdout__

        # Get the captured output
        output = stdout.getvalue()

        # Send the output back to the group
        await message.reply(f"Result: {output}")
    except Exception as e:
        # If there's an error, send the error message back to the group
        client.send_message(
            chat_id=message.chat.id,
            text=f"Error: {str(e)}",
            reply_to_message_id=message.message_id
        )

# Start the client
app.run()