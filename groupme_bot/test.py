import unittest
import bot


class MessageProcessing(unittest.TestCase):
    def _message(self, text, response):
        # Handle single strings
        if type(response) != list:
            response = [response]
        message = bot.Message(text=text)
        self.assertEqual(bot.process_message(message), response)

    def _command(self, command, text, response):
        self._message(bot.PREFIX + command + " " + text, response)

    def test_empty(self):
        self._message("This shouldn't trigger anything.", [])

    def test_invalid_command(self):
        self._command(
            "this_is_not_a_real_command",
            "some content",
            "Command not found. Use !help to view a list of commands.",
        )

    def test_static(self):
        for key in bot.static_commands:
            self._command(key, "", bot.static_commands[key])

    def test_morse(self):
        self._command("morse", "SOS", "...   ---   ...")


if __name__ == "__main__":
    unittest.main()