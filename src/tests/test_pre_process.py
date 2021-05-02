import sys
from pathlib import Path

from utils.textMod import clean, preProcess, removeURLs, spellCheck

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_pre_process():
    sentence = "Screw you @davidbrussee! I only have 3 weeks..."
    assert preProcess(sentence).lower() == "screw you i only have 3 weeks"


def test_remove_url():
    sentence = "feels strong contractions but wants to go out.  http://plurk.com/p/wxidk"
    assert removeURLs(
        sentence) == "feels strong contractions but wants to go out.  "


def test_spell_check():
    sentence = "I'm sorri, at leest it's Friday?"
    assert spellCheck(sentence).lower() == "i'm sorry at least it's friday"


def test_clean_and_stem():
    text = "building sites to open again after four months of closure"
    text = clean(text)
    assert text.lower() == "build site open month closure"


def test_clean_text():
    text = ".... Python is great and challenging! #preprocessing @testing !?;:"
    text = preProcess(text)
    text = removeURLs(text)
    text = spellCheck(text)
    text = clean(text)
    assert text.lower() == "python great challenge"


def test_wrong():
    sentence = (
        "very nice very cool, king of the castle, king of the castle, I have a chair"
    )
    text = preProcess(sentence)
    text = removeURLs(text)
    text = spellCheck(text)
    assert text != "very nice very cool king castle chair"
