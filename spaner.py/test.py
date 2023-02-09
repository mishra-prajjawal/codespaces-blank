import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize(text, ratio=0.05):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    word_frequencies = nltk.FreqDist(words)
    most_frequent_words = word_frequencies.most_common(100)
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if i not in sentence_scores.keys():
                    sentence_scores[i] = word_frequencies[word]
                else:
                    sentence_scores[i] += word_frequencies[word]
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_sentences = sorted_sentences[:int(len(sorted_sentences) * ratio)]
    selected_sentences = sorted(selected_sentences, key=lambda x: x[0])
    selected_sentences = [sentences[index] for index, score in selected_sentences]
    summary = " ".join(selected_sentences)
    return summary

text ="""
URI[https://en.wikipedia.org/wiki/Oral_sex]
= Oral_sex = 
Oral sex, sometimes referred to as oral intercourse, is sexual activity involving the stimulation of the genitalia of a person by another person using the mouth (including the lips, tongue, or teeth) and the throat. Cunnilingus is oral sex performed on the vulva or vagina, while fellatio is oral sex performed on the penis. Anilingus, another form of oral sex, is oral stimulation of the anus.Oral sex may be performed as foreplay to incite sexual arousal before other sexual activities (such as vaginal or anal intercourse), or as an erotic and physically intimate act in its own right. Like most forms of sexual activity, oral sex can pose a risk for contracting sexually transmitted infections (STIs/STDs). However, the transmission risk for oral sex, especially HIV transmission, is significantly lower than for vaginal or anal sex.Oral sex is often regarded as taboo, but most countries do not have laws which ban the practice. Commonly, people do not regard oral sex as affecting the virginity of either partner, though opinions on the matter vary. People may also have negative feelings or sexual inhibitions about giving or receiving oral sex, or may flatly refuse to engage in the practice.


== Practice ==

Oral sex may be practiced by people of any sexual orientation.


=== Forms ===
Oral sex is sexual activity involving the stimulation of the genitalia of a person by another person using the mouth or throat, and may take various forms. During facesitting the receiver sits on the giver's face and pushes into it with his or her genitals. Oral sex can also be performed by both partners at the same time in the so-called "sixty-nine" position. Spitting and/or swallowing of the ejaculatory fluids or giving a pearl necklace may cause different sexual stimulations. Autofellatio is a possible but rare variant; autocunnilingus may also be possible for women with extremely flexible spines. Irrumation is a forced form of fellatio where the fellated one actively forces his penis into the fellator's mouth.
An act of group sex restricted to one woman giving oral sex to several men is referred to as a gangsuck, blowbang or lineup, all derivatives of the slang term gang bang for group sex. Bukkake and gokkun may also involve oral sex.


=== Preserving virginity ===

Oral sex may be practised to preserve virginity, especially among heterosexual pairings; this is sometimes termed technical virginity (which may include anal sex, mutual masturbation and other non-penetrative sex acts, but excludes penile-vaginal sex). The concept of "technical virginity" or sexual abstinence through oral sex is popular among teenagers.Gay males who regard oral sex as a way of maintaining their virginities view penile-anal penetration as resulting in virginity loss, while other gay males may define oral sex as their main form of sexual activity. By contrast, lesbian pairings commonly view oral sex or fingering as resulting in virginity loss, though definitions of virginity loss vary among lesbians as well.


=== Contraception and safe sex ===
Oral sex alone does not result in pregnancy and heterosexual couples may engage in oral sex for contraception reasons. For conception to take place, sperm from the penis must enter the uterus and fallopian tubes and fertilize the female's egg. In humans, there is no connection between the gastrointestinal system and the reproductive system, and sperm ingested by the woman would be killed and broken down by acids in her stomach and proteins in the small intestine. The breakdown products are then absorbed as a negligible quantity of nutrients. However, there is a potential risk of pregnancy if semen comes in contact with the vaginal area in some way, such as semen in the ejaculate finding its way onto fingers, hands, or other body parts, which then comes in contact with the vaginal area.Oral sex is not necessarily an effective method of preventing sexually transmitted infections (STIs), although some forms of STIs are believed to be less commonly spread in this way, and oral sex has been recommended as a form of safe sex. In the United States, no barrier methods for use during oral sex have been evaluated as effective by the Food and Drug Administration. However, a barrier protection like a condom for fellatio or dental dam for cunnilingus can offer some protection from contact when practicing oral sex.Oral sex should be limited to the protected areas. A makeshift dental dam can be made out of a condom or a latex or nitrile glove, but using a real dental dam is seen as preferable; this is because real dental dams cover a larger area, avoid accidents caused by "slipping" outside the covered area, and avoid the risk that makeshift versions may be accidentally damaged or poked with the scissors during the cutting procedure. Plastic wrap may also be used as a barrier during oral sex, but there exists no conclusive scientific research regarding how effective it may or may not be at preventing disease transmission. Certain kinds of plastic wrap are manufactured to be microwaveable and are designed to have pores that open when heated, but there also exists no scientific research on what effect, if any, this has on disease transmission when used during oral sex. Some people complain that the thickness of the plastic dulls sensation.


=== Prevalence ===
A report issued by the National Center for Health Statistics in 2005 was the basis of an article in the 26 September 2005 issue of Time magazine. The report comes from the results of a computer-administered survey of over 12,000 Americans between the ages of 15 and 44, and states that over half the teenagers questioned have had oral sex. While some headlines have interpreted this as evidence that oral sex among teenagers is "on the rise", this was the first comprehensive study of its kind to examine the matter. The Centers for Disease Control and Prevention (CDC) stated in 2009: "Studies indicate that oral sex is commonly practiced by sexually active male-female and same-gender couples of various ages, including adolescents." Research also indicates that "males are more likely than females to have received oral sex, whereas equal proportions of men and women have given oral sex."


== Health risks and other studies ==


=== Sexually transmitted infections ===
Some sexually transmitted infections (STIs), such as Chlamydia and human papillomavirus (HPV), can be transmitted through oral sex. Any sexual exchange of bodily fluids with a person infected with HIV, the virus that causes AIDS, poses a risk of infection. Risk of STI infection, however, is generally considered significantly lower for oral sex than for vaginal or anal sex, with HIV transmission considered the lowest risk with regard to oral sex.There is an increased risk of STI transmission if the receiving partner has wounds on his or her genitals, or if the giving partner has wounds or open sores on or in his or her mouth, or bleeding gums. Brushing the teeth, flossing, undergoing dental work soon before or after performing oral sex can also increase the risk of transmission, because all of these activities can cause small scratches in the lining of the mouth. These wounds, even when they are microscopic, increase the chances of contracting STIs that can be transmitted orally under these conditions. Such contact can also lead to more mundane infections from common bacteria and viruses found in, around and secreted from the genital regions. Because of the aforementioned factors, medical sources advise the use of condoms or other effective barrier methods when performing or receiving oral sex with a partner whose STI status is unknown.


=== HPV and oral cancer link ===
Links have been reported between oral sex and oral cancer with human papillomavirus (HPV)-infected people. In 2005, a research study at Malmö University's Faculty of Odontology suggested that performing unprotected oral sex on a person infected with HPV might increase the risk of oral cancer. The study found that 36 percent of the cancer patients had HPV compared to only 1 percent of the healthy control group.
Another study in The New England Journal of Medicine suggests a correlation between oral sex and throat cancer. It is believed that this is due to the transmission of HPV, a virus that has been implicated in the majority of cervical cancers and which has been detected in throat cancer tissue in numerous studies. The study concludes that people who had one to five oral sex partners in their lifetime had approximately a doubled risk of throat cancer compared with those who never engaged in this activity and those with more than five oral sex partners had a 250 percent increased risk.


=== Miscarriage reduction ===
Fellatio may reduce the risk of miscarriages by inducing immunological tolerance in the woman by exposure to the proteins in her partner's semen, a process known as paternal tolerance. While any exposure to a partner's semen appears to decrease a woman's chances for the various immunological disorders that can occur during pregnancy, immunological tolerance could be most quickly established through the oral introduction and gastrointestinal absorption of semen. Recognizing that some of the studies potentially included the presence of confounding factors, such as the possibility that women who regularly perform fellatio and swallow semen also engage in more frequent intercourse, the researchers also noted that, either way, "the data still overwhelmingly supports the main theory" behind all their studies—that repeated exposure to semen establishes the maternal immunological tolerance necessary for a safe and successful pregnancy.


== Cultural views ==

Cultural views on oral sex range from aversion to high regard. It, especially fellatio, has been considered taboo, or at least discouraged, in many cultures and parts of the world. Laws of some jurisdictions regard oral sex as penetrative sex for the purposes of sexual offenses with regard to the act, but most countries do not have laws which ban the practice itself, in contrast to anal sex or extramarital sex.
In Ancient Rome, fellatio was considered profoundly taboo. Sexual acts were generally seen through the prism of submission and control. This is apparent in the two Latin words for the act: irrumare (to penetrate orally), and fellare (to be penetrated orally). Under this system, it was considered to be abhorrent for a male to perform fellatio, since that would mean that he was penetrated (controlled), whereas receiving fellatio from a woman or another man of lower social status (such as a slave or debtor) was not humiliating. The Romans regarded oral sex as being far more shameful than, for example, anal sex – known practitioners were supposed to have foul breath and were often unwelcome as guests at a dinner table. This was highlighted in Roman attitudes towards irrumation, in which it was strictly considered a form of oral rape, and any man who irrumated another person was considered to be extremely virile. Irrumatio was so degrading in Roman society in fact that it was often used as a method of punishment.In contrast to historical views on fellatio, cunnilingus is revered as a spiritually fulfilling practice in Chinese Taoism, which regards it as having the ability to enhance longevity. In modern Western culture, oral sex is widely practiced among adolescents and adults.People give various reasons for their dislike of oral sex. Some state that since it does not result in reproduction, it is therefore unnatural. Others find it less intimate because it is not a face-to-face practice, or believe that it is a humiliating or unclean practice; that it is humiliating or unclean are opinions that are, at least in some cases, connected with the symbolism attached to different parts of the body. Opposite these views, people also believe that oral sex "is one of the most intimate behaviors that a couple can engage in because it requires total trust and vulnerability."While commonly believed that lesbian sexual practices involve cunnilingus for all women who have sex with women (WSW), some have an aversion to cunnilingus due to not liking the experience or psychological or social factors, such as finding it unclean. Other WSW believe that it is a necessity or largely defines lesbian sexual activity. Lesbian couples are more likely to consider a woman's dislike of cunnilingus as a problem than heterosexual couples are, and it is common for them to seek therapy to overcome inhibitions regarding it.


== Terminology and slang ==
There are many words which refer to oral sex, including euphemisms and sexual slang. Like all aspects of sexuality, there exists a large number of variations on a theme, a few common ones being:

Giving head – A common American slang term for giving oral sex to either a man or woman is giving head, from the term head job (in contrast to hand job, manual stimulation). A play on the slang term head resulted in the slang term brains, or brain salad surgery, domes or getting domes.
Plate – A once common British rhyming slang for fellate that arose in the gay slang language of Polari that spread in the 1960s. The term is less common today.
Cunnilingus is also sometimes referred to as muff diving, eating out or poon-job, a slang term and a cunnilingus variant of blow job, where poon is short for poontang or punani.
Additionally, in lesbian culture, several common slang terms used are carpet munching, giving lip, lip service or tipping the velvet (a faux-Victorian expression invented by novelist Sarah Waters).Other slang terms for oral sex include going down on (male or female), licking out and muff diving (female), blow job (male), dome (male or female), sucking off (male), playing the skin flute (male recipient), rolling cigars (male recipient), lolly-gagging (gay male-on-male), gaining knowledge (male recipient) and bust down (male). Forced fellatio is often called Egyptian rape or simply Egyptian; this goes back to the time of the Crusades when Mamluks were alleged to force their Christian captives to do this.


== Other animals ==

Oral sex has been observed in the animal kingdom among many species. It has been suggested that there is an evolutionary advantage due to the tendency of primates, non-primates and humans to have oral sex. Fellatio occurs with the fruit bat (Cynopterus sphinx); it has been observed when the bats are mating. These bat pairs spend more time copulating if the female licks the male than if she does not.Unlike many other animals, fish from the genus Corydoras reproduce orally. The  male faces perpendicularly to the female so that she may be able to attach to his reproductive apparatus. He then releases sperm into the mouth of the female, crossing her digestive system and fertilising her eggs. 


== See also ==


== References ==
Explanatory notes
Citations
BibliographyAdams, James N., The Latin Sexual Vocabulary (Johns Hopkins, 1990) ISBN 0-8018-2968-2
Franklin, Jacqueline, The Ultimate Kiss: Oral Lovemaking, A Sensual Guide for Couples (Los Angeles: Media Press, 2001) ISBN 0-917181-17-4


== External links ==

Oral sex and HIV (from CDC)
"""

print(summarize(text,0.3))