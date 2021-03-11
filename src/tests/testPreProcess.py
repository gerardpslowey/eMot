import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import preProcess, removeURLs, removeRepetitions, spellCheck

def main():
    reviews = ["hellooooo @john, what is up? #monday", 
    "This move is good and cool", 
    "very nice very cool, king of the castle, king of the castle, I have a chair",
    "coronavirus has caused major turmoil recently", 
    "Eoghan mcDermott has left 2fm after six years following allegations of assault",
    "@tiffanylue i know  i was listenin to bad habit earlier and i started freakin at his part =[",
    "Layin n bed with a headache  ughhhh...waitin on your call...",
    "Funeral ceremony...gloomy friday...",
    "wants to hang out with friends SOON!",
    "@dannycastillo We want to trade with someone who has Houston tickets, but no one will.",
    "Re-pinging @ghostridah14: why didn't you go to prom? BC my bf didn't like my friends",
    "I should be sleep, but im not! thinking about an old friend who I want. but he's married now. damn, &amp; he wants me 2! scandalous!",
    "http://www.djhero.com/ is down",
    "Charlene my love. I miss you",
    "I'm sorry  at least it's Friday?",
    "cant fall asleep",
    "Choked on her retainers",
    "Ugh! I have to beat this stupid song to get to the next  rude!",
    "@BrodyJenner if u watch the hills in london u will realise what tourture it is because were weeks and weeks late  i just watch itonlinelol",
    "Got the news",
    "The storm is here and the electricity is gone",
    "@annarosekerr agreed",
    "So sleepy again and it's not even that late. I fail once again.",
    "@PerezHilton lady gaga tweeted about not being impressed by her video leaking just so you know",
    "How are YOU convinced that I have always wanted you? What signals did I give off...damn I think I just lost another friend",
    "@raaaaaaek oh too bad! I hope it gets better. I've been having sleep issues lately too",
    "Wondering why I'm awake at 7am,writing a new song,plotting my evil secret plots muahahaha...oh damn it,not secret anymore",
    "No Topic Maps talks at the Balisage Markup Conference 2009   Program online at http://tr.im/mL6Z (via @bobdc) #topicmaps",
    "I ate Something I don't know what it is... Why do I keep Telling things about food",
    "so tired and i think i'm definitely going to get an ear infection.  going to bed &quot;early&quot; for once.",
    "On my way home n having 2 deal w underage girls drinking gin on da bus while talking bout keggers......damn i feel old",
    "@IsaacMascote  i'm sorry people are so rude to you, isaac, they should get some manners and know better than to be so lewd!",
    "Damm servers still down  i need to hit 80 before all the koxpers pass me",
    "Fudge.... Just BS'd that whole paper.... So tired.... Ugh I hate school.....  time to sleep!!!!!!!!!!!",
    "I HATE CANCER. I HATE IT I HATE IT I HATE IT.",
    "It is so annoying when she starts typing on her computer in the middle of the night!",
    "@cynthia_123 i cant sleep",
    "I missed the bl***y bus!!!!!!!!",
    "feels strong contractions but wants to go out.  http://plurk.com/p/wxidk",
    "SoCal!  stoked. or maybe not.. tomorrow",
    "Screw you @davidbrussee! I only have 3 weeks...",
    "@ether_radio yeah :S i feel all funny cause i haven't slept enough  i woke my mum up cause i was singing she's not impressed :S you?",
    "I need skott right now",
    "has work this afternoon"]

    for sentence in reviews:
        sent = preProcess(sentence)
        sent = removeURLs(sent)
        sent = removeRepetitions(sent)
        print(spellCheck(sent))

    text = ".... Python is great and challenging! #preprocessing @testing !?;:"
    text = preProcess(text)
    text = removeURLs(text)
    text = removeRepetitions(text)
    text = spellCheck(text)
    #print(text)
    assert text == "python great challenging"

    text2 = "Layin n bed with a headache ughhhh... waiteng on a takeaway. happy dayz"
    text2 = preProcess(text2)
    text2 = removeURLs(text2)
    text2 = removeRepetitions(text2)
    text2 = spellCheck(text2)
    # print(text2)
    assert text2 == "laying i bed headache ugh waiting takeaway happy day"

if __name__ == '__main__':
    main()