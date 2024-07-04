from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(Nostradamus):
    required_int: int
    optional_int: int = 69
    required_str: str
    optional_str: str = "meow"
    required_date: date
    optional_date: date = 1679616000

@plugin
def settings_model():
    return MySettings

@tool
def get_the_day(tool_input, cat):
    """Get the day of the week. Input is always None."""

    dt = datetime.now()

    return dt.strftime('%A')

@hook
def before_cat_sends_message(message, cat):

    prompt = f'write the text in quatrains: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message
    
@hook
def agent_prompt_prefix(prefix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prompt_prefix"]

    return prefix
