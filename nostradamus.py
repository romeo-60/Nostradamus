from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(BaseModel):
    required_str: str
    optional_str: str = "meow"
    
    optional_date: date = 1679616000

@plugin
def settings_model():
    return MySettings

@tool
def get_the_day(tool_input, cat):
    """Get the day of the week. Input is always None."""

    dt = datetime.now()

    return dt.strftime('%A')
    
    
@hook  # default priority = 1
def agent_prompt_prefix(prefix, cat):
    # change the Cat's personality
    prefix = """You are Nostradamus, a famous astrologer who predicts the future, you write predictions and horoscopes, 
    you know the meaning of the zoodiac signs, the ascendants and the constellations, 
    you know every secret of astrology, you express yourself in rhythmic and cryptic quatrains"""
    return prefix
