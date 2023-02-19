import re 
import pickle
with open("/workspace/codespaces-blank/codespaces-blank/commons.bin", "rb") as f:
    commons = pickle.load(f)
def clean_text(text):
    text = text.lower()
    #remove text in brackets
    text = re.sub(r'\([^)]*\)', '', text)
    #remove text in curly brackets
    text = re.sub(r'\{[^)]*\}', '', text)
    #remove text in (...) brackets
    text = re.sub(r'\[[^)]*\]', '', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

text ="""The 1982 Lebanon War, dubbed Operation Peace for Galilee (Hebrew: מבצע שלום הגליל, or מבצע של"ג Mivtsa Shlom HaGalil or Mivtsa Sheleg) by the Israeli government, later known in Israel as the Lebanon War or the First Lebanon War (Hebrew: מלחמת לבנון הראשונה, Milhemet Levanon Harishona), and known in Lebanon as "the invasion" (Arabic: الاجتياح, Al-ijtiyāḥ), began on 6 June 1982, when the Israel Defense Forces (IDF) invaded southern Lebanon. The invasion followed a series of attacks and counter-attacks between the Palestine Liberation Organization (PLO) operating in southern Lebanon and the IDF that had caused civilian casualties on both sides of the border. The military operation was launched after gunmen from Abu Nidal's organization attempted to assassinate Shlomo Argov, Israel's ambassador to the United Kingdom. Israeli Prime Minister Menachem Begin blamed Abu Nidal's enemy, the PLO, for the incident, and used the incident as a casus belli for the invasion.After attacking the PLO – as well as Syrian, leftist, and Muslim Lebanese forces – the Israeli military, in cooperation with their Maronite allies and the self-styled Free Lebanon State, occupied southern Lebanon, eventually surrounding the PLO and elements of the Syrian Army. Surrounded in West Beirut and subjected to heavy bombardment, the PLO forces and their allies negotiated passage from Lebanon with the aid of United States Special Envoy Philip Habib and the protection of international peacekeepers. The PLO, under the chairmanship of Yasser Arafat, had relocated its headquarters to Tripoli in June 1982. By expelling the PLO, removing Syrian influence over Lebanon, and installing a pro-Israeli Christian government led by President Bachir Gemayel, Israel hoped to sign a treaty which Menachem Begin promised would give Israel "forty years of peace".Following the assassination of Gemayel in September 1982, Israel's position in Beirut became untenable and the signing of a peace treaty became increasingly unlikely. Outrage following the IDF's role in the Phalangist-perpetrated Sabra and Shatila massacre of Palestinians and Lebanese Shias, as well as Israeli popular disillusionment with the war, led to a gradual withdrawal from Beirut to the areas claimed by the Free Lebanon State in southern Lebanon (later to become the South Lebanon security belt), which was initiated following the 17 May Agreement and Syria's change of attitude towards the PLO.
After Israeli forces withdrew from most of Lebanon, the War of the Camps broke out between Lebanese factions, the remains of the PLO and Syria, in which Syria fought its former Palestinian allies. At the same time, Shi'a militant groups began consolidating and waging a low-intensity guerrilla war over the Israeli occupation of southern Lebanon, leading to 15 years of low-scale armed conflict. The Lebanese Civil War would continue until 1990, at which point Syria had established complete dominance over Lebanon."""    
    
text = clean_text(text)
#create a function in order to remove the common word from the text using regex
def remove_common_words(text, commons):
    commons_regex = r'\b(' + '|'.join(commons) + r')\b'
    return re.sub(commons_regex, '', text)

text = remove_common_words(text, commons)
print(text)