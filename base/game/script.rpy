# Heaven's Gate by etherane
# Version 1.0

# Character list


define c = Character("Charles")
define h = Character("Henrietta")
define v = Character("Vincent")
define a = Character("Classmate A")
define b = Character("Classmate B")
define u = Character("???")
define x = Character("Kid")
define f = Character("Felix Honikker")
define e = Character("Bennett")
define r = Character("Frei")
define s = Character("Charlotte")
define m = Character("Mother")
define y = Character("Doctor")

define narrator = Character(None, kind=nvl, what_color="#fff")
define narrator2 = Character(None, kind=adv, what_color="#404040")

# Game script

label start:

scene logo
$ renpy.pause(3.0)

scene intro1
with fade
pause .7
scene intro2
pause .7
scene intro3
pause .5
scene intro4
pause .5
scene intro3
pause .5
scene intro4
pause .5
scene intro3
pause .5
scene intro4
pause .5
scene intro3
pause .5
scene intro4
pause .5

scene bg black
with dissolve

scene title
with fade
$ renpy.pause(3.0)

# [Kindergarten] Ants

scene 1
with fade
$ renpy.pause(3.0)
scene bg kindergarten3
with dissolve

narrator2 "Vincent Fennell is watching a small trail of ants go by,
his gaze remaining disinterested."

narrator2 "I approach him out of curiosity."

show kcharles curious
c "Oh. Winged ants. That's rare."
show kvincent staring at left
v "They're so small."
c "That's good. Bugs are yucky."
v "Look."
hide kcharles curious
narrator2 "He gets up from his knees and steps closer to the ant trail."

show kvincent smiling at center
v "We must be like gods to them, don't you think?"
hide kvincent smiling

show ants1 at appeartop

narrator2 "With those words, Vincent picks one up."

show ants2 at appearbottom

v "Just one tug, and..."

narrator2 "The wing rips off with an alarming ease."

hide ants1
hide ants2

show kcharles scared at center
c "Stop it! Let it go!"
show kvincent thoughtful at left
v "What are you being so upset about?"
show kcharles sad
c "...just because we are bigger, that doesn't mean we should hurt them."
v "Hmmm. It's just a bug, though. "
c "..."
c "Mom says even the smallest lives matter."
v "My mom says bugs are annoying."
show kcharles scared
c "..."
c "If you d-don't stop, I'll tell the nurses."
show kvincent staring
v "..."
hide kvincent staring
narrator2 "The boy simply gets up, and leaves."
show kcharles sad
c "What's up with him..."
hide kcharles sad
narrator2 "From that day on, I decide that I don't like Vincent Fennell at all."


# [Kindergarten] Tazos

scene 2
with dissolve
$ renpy.pause(3.0)
scene bg kindergarten
with dissolve

narrator2 "It's lunch break."

narrator2 "Everyone's trading stickers and hoarding tazos - a recent fad among kids."

narrator2 "Vincent is surrounded by children, who are marveling at his collection."

x "Oh! This one's super rare!"
x "Where did you get it?"
show kvincent emotionless at center
v "It was in my chips."
x "Lucky!"
v "Do you...want it?"
x "!!!"
x "I can have it?!"
x "But...I don't have anything good to trade you."
v "I don't mind."
x "Just choose one that you don't have, then!"
x "Trade with me too!"
x "Me too!"
hide kvincent emotionless
show kcharles turnaway
x "What are you looking at, Charlie?"
x "Wanna trade, too?"
c "Ah...no. Mom says chips are bad for health."
hide kcharles turnaway
x "Booooring!"
x "Vincent, look! I have holographic ones!"

narrator2 "Ugh."
narrator2 "What's so special about him?"
narrator2 "All he has is a pack of tazos."

narrator2 "Lost in thought, I trip and drop the box with the classroom turtle that I was carrying."
narrator2 "The nurses yell at me and make me stand in a corner for half an hour."
narrator2 "I blame it on Vincent, too."

# [Kindergarten] At home

scene 3
with dissolve
$ renpy.pause(3.0)
scene bg oldflat
with dissolve

narrator2 "When I'm five, we move into a flat swarming with cockroaches and pigeons living on the balcony."
narrator2 "“Why is this place so dirty, Mom?” I ask."
narrator2 "“The person who lived here wasn't very cleanly,” is Mother's answer."
narrator2 "“I want to go back home,” I tell her, “Why did we have to leave?”"
narrator2 "“We won't be staying here for long, dear,” Mother says, and I want to believe her."
narrator2 "The surrounding dirt makes my skin crawl."
narrator2 "Later I overhear our neighbours talking and learn that the former owner was a drug addict."
narrator2 "Died of overdose, they say."

scene bg black
with dissolve

narrator2 "When I raise my voice, Mother tells me to keep quiet."
narrator2 "When I walk around the house, Mother says that my footsteps are too loud."
narrator2 "When I become excited, Mother reprimands me for misbehaving."

scene bg oldflat
with dissolve

narrator2 "One evening, she has a breakdown over unsorted clothes in the drawers."
narrator2 "We're talking normally, then the next moment the house is filled with shouting and sounds of my clothes being violently thrown on the floor."
narrator2 "There must be something else she's angry at, but I'm too young to understand."
narrator2 "I apologize over and over, promising I won't do that ever again, as if I committed a grave sin."

narrator2 "{i}I'm sorry, Mother.{/i}"

narrator2 "I can make everything right."

narrator2 "I won't become a burden."


# [Kindergarten] Concert

scene 4
with dissolve
$ renpy.pause(3.0)
scene bg concert
with dissolve

show concert1 at appearbottomleft
with dissolve

narrator2 "We're having a concert to celebrate Autumn."
narrator2 "Our nurses are wearing dresses with paper maple leaves sewn onto them."
narrator2 "I recite a poem aloud, trying not to mess it up halfway."
narrator2 "It has four lines."
narrator2 "I'm so nervous that my voice comes out too quietly,
even though I recite it perfectly."

show concert2 at appeartopright
with dissolve
narrator2 "Vincent got six lines."
narrator2 "It must be because the nurses think he's the smartest in the group."
narrator2 "Hell, he even goes to chess club."
narrator2 "Vincent recites the poem in a monotonous voice like he doesn't give a care."

hide concert1
hide concert2

scene bg kindergarten4
with dissolve

show nobodycomes1 at appeartopright2
with dissolve

show nobodycomes2 at appearbottomleft2
with dissolve

narrator2 "Vincent's almost always the last to be picked up by his parents."
narrator2 "Sometimes nobody comes, and he just goes home alone."

narrator2 "I tell Mom about that, and she totally freaks out."
narrator2 "“How can a child go home by himself?!” she exclaims, shocked."
narrator2 "“What are his parents thinking?”"
narrator2 "I don't know what to say to that."


# [Kindergarten] Valentines

scene 5
with dissolve
$ renpy.pause(3.0)
scene bg infirmary
with dissolve

narrator2 "It's Valentines Day."
narrator2 "Everyone gets tangerines and Kinder Surprises for lunch."
show sick2 at appeartop2
narrator2 "I get sick and throw up onto my festive shirt."
narrator2 "I didn't like it much, anyway. Mom did, though."
narrator2 "Vincent is at the nurse's office, too."
show sick1 at appearbottom2
narrator2 "He tripped and scraped his knee."
narrator2 "The nurse is drawing a net on it with green antiseptic."
narrator2 "The scrape seems bad, but he's not even wincing, his stare staying blank."
narrator2 "Doesn't he feel any pain?"
narrator2 "Maybe he's actually a robot?"
narrator2 "I want to ask him that, but my headache is too strong, so I ignore him."
narrator2 "All I want is to go home and watch cartoons in bed."
hide sick2
hide sick1
narrator2 "Thankfully, Mom's quick to come to my rescue."
narrator2 "Afterwards, I stay at home for a whole week."

# [Kindergarten] End

scene 6
with dissolve
$ renpy.pause(3.0)
scene bg black
with dissolve

narrator2 "Time passes fast."

narrator2 "My kindergarten graduation album is filled with pictures of other kids running around
and a macro photograph of myself in some kind of medieval clothing from the photoshoot."
narrator2 "It's my favorite one, but I'll never admit that."

narrator2 "I can barely contain my excitement for the first day of school."

narrator2 "Vincent goes to a different one, but it doesn't matter."
narrator2 "I didn't like him much anyway."

# [Elementary] Bored

scene 7
with dissolve
$ renpy.pause(3.0)
scene bg classroom
with dissolve

narrator2 "Elementary school is boring."

narrator2 "I solve all the problems in my math workbook in one evening,
and as a consequence, end up dying of boredom at actual lessons."

narrator2 "Shouldn't there be a faster way to do this?"

narrator2 "As the school days pass, I get so excited about my intellectual abilities that I point out others' mistakes every time I notice them."

narrator2 "The girl sitting next to me seems to enjoy my company - mainly because she gets to copy my answers during tests."
narrator2 "In the meantime, I find a new way to make friends."
narrator2 "All you have to do is buy them food or share yours."
narrator2 "Then everyone will gather around you, excited to get sweets for free."
narrator2 "I spend all my pocket money on snacks, and still end up being chosen last at P.E. lessons."

show alone at appearcenter
with dissolve

narrator2 "It takes me some time and an afterschool beating to learn not to poke my nose into others' business."
narrator2 "It's not my fault people cheat on tests."
narrator2 "I'm just doing what's right."

narrator2 "At least, that's what I think."

narrator2 "Apparently, people don't like snitches."
narrator2 "Nor do they like being responsible, or proper."
narrator2 "While I'm doing everything not to be a burden, they're giving their all to cause trouble."
narrator2 "I feel like this will take some time to sink in."

scene bg black
with dissolve

narrator2 "Over the years, I learn to keep my mouth shut."
narrator2 "From a moderately talkative kid I turn into a complete class ghost."

narrator2 "By the end of fourth year, everyone still calls me by my last name."


# [Middle school] Reunion

scene 8
with dissolve
$ renpy.pause(3.0)
scene bg corridor
with dissolve

show reunion1 at appearbottomleft
with dissolve

narrator2 "In middle school, we see each other again."

show reunion2 at appeartopright
with dissolve

narrator2 "Vincent looks more frail than I remember him being."
narrator2 "Maybe it's just that I've gotten taller."

narrator2 "When he sees me, he smiles."
narrator2 "In fact, he smiles to everyone."

narrator2 "The usual unchanging blank expression that he had in kindergarten is gone from his face,
replaced with a mask."
narrator2 "It's unsettling."

scene bg black
with dissolve

narrator2 "I don't smile back."

scene bg classroom
with dissolve

narrator2 "Somehow, we end up doing a class project together."
narrator2 "By the time I gathered the courage to ask someone to invite me, everyone else had already found a partner."
narrator2 "But there was an open spot in his group."

narrator2 "The other two kids just want easy marks, so only the two of us actually end up working."
narrator2 "Vincent is...surprisingly nice to work with."
narrator2 "He's a good team player, very considerate and giving his all to complete the task."
narrator2 "A complete contrast to most of the kids."
narrator2 "For the first time in a while, I have fun working in a group."

call phone_start from _call_phone_start
call message_start("System notification", "1 incoming message from: Charles") from _call_message_start
call message_img("Charles", "here, I'm sending over the presentation files", "images/charlesicon.png") from _call_message_img
call message_img("Vincent", "Great work!", "images/vincenticon.png") from _call_message_img_1
call message_img("Vincent", "Let's do our best tomorrow.", "images/vincenticon.png") from _call_message_img_2
call phone_end from _call_phone_end

narrator2 "{i}He's... he's thankful for my effort!{/i}"
narrator2 "This must be the first time in five years of school."
narrator2 "I'm so moved that I put his name first on the project's title slide."


scene bg classroom presentations
with dissolve

show presentation at appearcenter

narrator2 "It's the project presentations day."
narrator2 "Vincent, who was chosen as our group's representative, has a clear, powerful voice."
narrator2 "Unlike me, who gets so anxious that I start to stumble on every word, earning giggles from classmates."
narrator2 "I hate myself for it."
narrator2 "Regardless, our group gets the highest marks."

narrator2 "“Maybe teamwork isn't half bad,” I catch myself thinking."

# [Middle school] P.E

scene 9
with dissolve
$ renpy.pause(3.0)
scene bg track
with dissolve

show faint at appeartopright
with dissolve

show run at appearbottomleft
with dissolve

narrator2 "Vincent loses consciousness during one of our P.E. lessons."
narrator2 "I've never really noticed it before, but he really has the worst stamina in class."
narrator2 "While I fail all the speed tests, I can endure running long distances just fine."
narrator2 "He, however, looks completely exhausted after just a few laps."

narrator2 "After overhearing one of the conversations between teachers, I learn that Vincent has health complications."

scene bg childrenlaughing
with dissolve

a "Huh, Fennell's not running again."
b "I heard he has a weak heart!"
b "Or was it anemia?"
a "He's the best student in class."
a "Maybe he's pushing himself too hard?"
b "People like that don't live long."
b "My uncle died from a stroke."
a "Really?!"

c "..."

narrator2 "Vincent? {i}Dying{/i}?"
narrator2 "The possibility has never occurred to me before."
narrator2 "Maybe children don't think too deeply about life and death in general."

scene bg connection
with dissolve

narrator2 "I look at him sitting on a bench near the teacher, watching us run."
narrator2 "We never really talk."
narrator2 "But, I've been watching him for a while."
narrator2 "So to me, it feels like we share a connection."

pause 1

# [Middle school] Henrietta

scene 10
with dissolve
$ renpy.pause(3.0)
scene bg classroom
with dissolve

narrator2 "I often volunteer to stay behind on class duty."
show bullied at center
narrator2 "Henrietta Warhol gets bullied into it."
narrator2 "The other girls call her “smelly” and “cowtits” and make her do things instead of them."
hide bullied
narrator2 "So right now, she's unenthusiastically scrubbing a dirty desk with a wet rag."
show mcharles worry at center
c "You should use detergent to scrub this off."
hide mcharles worry
show manri unimpressed at center
h "...don't tell me what to do, Eyler."
show manri defensive at center
h "Why are you even here?"
h "It's not your turn to clean."
hide manri defensive
show mcharles smiling2 at center
c "I like cleaning."
hide mcharles smiling2
narrator2 "Or more like, I can't trust anyone with it."
narrator2 "Everyone's too sloppy and lazy to properly clean all the dust."
narrator2 "Just thinking of sitting behind a dirty desk makes my skin crawl."

show manri unimpressed at center
h "Weirdo."
hide manri unimpressed
show mcharles smiling2 at center
c "You can go home, I planned to stay after lessons anyway."
hide mcharles smiling2

narrator2 "I have piano class coming up in two hours."
narrator2 "Just enough time to clean and do homework."

show manri unimpressed at center
h "No, I'll stay."
show manri cautious at center
h "They're waiting outside."
h "...if I go too early, they might think I'm slacking off."
hide manri cautious
narrator2 "Damn, that's complicated."

show mcharles quiet at center
c "...okay."
hide mcharles quiet

narrator2 "We clean in silence."
narrator2 "I don't really know what to talk about with her."
narrator2 "Henrietta doesn't seem like she's up for discussing homework, either."

show mcharles quiet at right
c "Henrietta?"
show manri cautious at left
h "Yes?"
show mcharles smiling1
c "Give me your hand."
show manri unimpressed
h "?"
show candy at appearcenter2
with dissolve
narrator2 "I place a candy in it."
show mcharles smiling2
c "Here. Good work today."

narrator2 "Carrying snacks around still remains as a habit of mine."
narrator2 "Might as well try to win Warhol's goodwill with it."
narrator2 "Henrietta stays weirdly silent."

show manri cautious
h "There isn't anything wrong with it, right?"
show mcharles smiling3
c "Unless you don't like barberry flavor."
show manri unimpressed
h "Oh."
h "..."
show manri defensive
h "Thanks."
show mcharles smiling2
c "You're welcome."
hide manri defensive
hide mcharles smiling2
hide candy

narrator2 "Henrietta awkwardly stumbles out of the classroom without saying so much as a goodbye."
narrator2 "Weeks later, we start talking during lunch breaks sometimes."
narrator2 "The other girls mock and tease her for it, but Henrietta learns to talk back."
narrator2 "Maybe she's more confident about herself when she feels less alone."

call phone_start from _call_phone_start_1
call message_start("System notification", "3 incoming messages from: Anri") from _call_message_start_1
call message_img("Anri", "okay listen up, eyler", "images/anriicon.png") from _call_message_img_3
call message_img("Anri", "we're gonna get rid of your acne", "images/anriicon.png") from _call_message_img_4
call message_img("Anri", "i'm gonna send you a list of skincare products and food to avoid", "images/anriicon.png") from _call_message_img_5
call message_img("Charles", "but mom!", "images/charlesicon.png") from _call_message_img_6
call message_img("Anri", "no buts", "images/anriicon.png") from _call_message_img_7
call message_img("Anri", "for a clean freak you sure hate looking after yourself", "images/anriicon.png") from _call_message_img_8
call phone_end from _call_phone_end_1

# [Middle school] Mother

scene 11
with dissolve
$ renpy.pause(3.0)
scene bg black
with dissolve

narrator2 "Mother never tells me anything about her past, or Father, and I never ask."
narrator2 "It's something we never talk about."
narrator2 "All I can do is listen to her occasionally cry at night and keep quiet about it in the morning."
narrator2 "She's holding up well, but I can't help but worry that one day she might trip and fall, and never get up."
narrator2 "The thought makes my hands itch, and I spend ten minutes in the bathroom trying to wash it off."

narrator2 "I want to grow up and become someone she can depend on."

# [Interlude] Alone

scene 12
with dissolve
$ renpy.pause(3.0)
scene bg mindlibrary
with pixellate

narrator2 "It's quiet in the Mind Library."
narrator2 "I'm hunched over a language workbook trying to fill in the blanks, but all the letters come out jumbled."
narrator2 "I write them over and over again, until the pages are filled with illegible scribbles."
narrator2 "Frei peeks over my shoulder like nothing's wrong."

show frei neutral at left
r "Doing someone's homework again, miss Wiltshire?"
r "You do know that it's not your obligation to do it, don't you?"
show charlotte sad at right
s "..."
show charlotte smile
s "It's for a friend."
show frei amused
r "Ah, so that's why you couldn't turn them down?"
r "Because they said you're “friends”?"
show charlotte sad
s "Was it so wrong to believe them, Frei?"
show frei smile
r "No. Of course not."
r "Miss Wiltshire is a very earnest girl, after all."
show frei laugh
r "Too gullible for her own good."
show charlotte shock
s "...!"
show frei amused
r "You see, what your so-called “friend” used was a keyword."
r "A “password” that doesn't mean anything."
show charlotte sad
r "You heard it and immediately thought of the meaning you had for it."
r "You may have thought the other person meant, “I want to help and understand you,” but in reality they meant, “I want to use you for my own needs”."
r "Sure, they could've been honest with you, but would you be doing this for them if you knew the truth?"
s "..."
show frei laugh
r "Right?"
show frei neutral
r "But that doesn't make them evil per se."
show frei smile
r "If they were the main character, I'm sure the viewers would understand their way of thinking."

narrator2 "Frei runs his finger over a messed up sentence, and stops at the period mark."

show frei amused
r "The true evil lies in muddled words, miss Wiltshire."
r "Remember that."

narrator2 "I absentmindedly look at the ruined workbook."

show charlotte sad
s "Still..."
s "If I don't do as they say, I'll be left all alone."
show charlotte smile
s "This is all I'm good for, anyway."
show charlotte sad
narrator2 "Frei leans his head on me, but I have no strength left to shove him away."

show frei neutral
r "You know that's not true, miss Wiltshire."
show frei smile
r "You just want someone to make you feel better about yourself."
show frei amused
r "Even if it's someone you despise."
show frei smile
r "But don't worry."
r "I know a-a-all the words you want to hear."
show frei amused
r "You may feel like you're never doing enough..."
r "But in reality you're always doing your best, aren't you?"


# [High school] School trip

scene 13
with pixellate
$ renpy.pause(3.0)
scene bg bus
with dissolve

narrator2 "During the first year of high school, we go on a school trip."

narrator2 "I don't have anyone to make promises about sitting together with,
so right now, I'm left with three choices."
narrator2 "A: Sitting with the teacher."
narrator2 "B: Sitting with one of the class bullies."
narrator2 "C: Approaching mr. Fennell, who happens to have a seat open near him."
narrator2 "I decide that the latter is the lesser evil."

show charles neutral at right
c "Mind if I sit here?"
show vincent smile1 at left
v "Not at all."
show charles smile
c "Thanks."
show charles neutral
c "Oh. Now that I think of it, it's the front seat."
c "I shouldn't be taking it."
show vincent smile2
v "You can just change with someone if they get carsick."
show vincent smile3
v "I, for one, can't sit in the back. I always get dizzy."
show charles sigh1
c "Sucks to be you."
hide charles sigh1
hide vincent smile3
narrator2 "Vincent laughs dryly. His laughter doesn't reach his eyes."
narrator2 "Crap."
narrator2 "I just messed up my second informal conversation with him."
narrator2 "By the time I gather myself again, Vincent's long since asleep."

show busv at appearbottomleft2
with dissolve
show busc at appeartopright2
with dissolve

narrator2 "His head is bumping against the bus window in small intervals."
narrator2 "I bring out my MP3 player, but minutes later everyone decides to watch an action movie."
narrator2 "The loud sound doesn't seem to bother Vincent, who's sleeping with earplugs."
narrator2 "I should've brought some too."
narrator2 "In the end, I settle on watching the movie, and lose the track of time."

scene bg hostel night
with wiperight

narrator2 "By the time we arrive at the hotel, it's past midnight."
narrator2 "I get a room with three guys who don't mind me ditching them during the night. Success."
narrator2 "At best they'll get drunk and play cards in someone else's room until sunrise and at worst one of them brought drugs.
Maybe both."
narrator2 "We get up the stairs and unlock our room."
narrator2 "It has a bed and a shower, so it's perfect."
narrator2 "My classmates leave the room as soon as they finish unpacking."
narrator2 "As expected, they don't bother inviting me anywhere."
narrator2 "Glad they know I hate having fun."

narrator2 "I spend half of the night sketching ideas for comics I might draw someday."
narrator2 "All of them feel like I've seen them before."

scene bg cafeteria
with dissolve

narrator2 "In the morning, I emit the light of freshness."
narrator2 "I like being up early."
narrator2 "The hotel dining room is dead silent, like a cemetery."
narrator2 "Out of my classmates, only some girls and Vincent are present."
narrator2 "I decide to drop into the seat near him."

show charles smile at left
c "Morning."
show vincent smile1 at right
v "Good morning. I didn't see you last night."
show charles smile2
c "Was getting my beauty sleep."
show charles smile
c "Did you party with everyone?"
show vincent smile3
v "Of course."
show charles doubt
c "Have to admit, I have a hard time imagining you drinking."
show vincent smile2
v "Why, I have high alcohol tolerance."
show vincent smile3
v "Unlike many."
show charles headache
c "Augh, don't remind me."
c "I woke up to sounds of someone puking in the toilet next door."
show vincent smile4
v "Ah. Unpleasant, isn't it?"

narrator2 "My face says it all."
narrator2 "Still, the image of Vincent downing alcohol like a glass of juice seems really funny to me,
so I can't help but laugh out loud."
narrator2 "Vincent gives me a questioning look, so I quickly try to change the topic before he asks anything."

show charles smile
c "When I drink, I just become sleepy."
show charles smile2
c "Boring, right?"
show vincent smile4
v "Hahaha. Is that so? I thought you'd be the type to talk a lot."
show charles doubt
c "Nah...if anything, I shut up for good."
c "Then fall asleep."
show charles sigh1
c "I think I'm the type people would call an ambulance for because they'd drunkedly think I died of lethal ethanol intake."
v "You sound like you speak from experience."
show charles doubt
c "Well..."

scene bg museum
with wiperight

narrator2 "The trip itself is nothing special."
narrator2 "Art museums never interested me much."
narrator2 "During one of the excursions, Henrietta gets lost, and I volunteer to look for her."
narrator2 "Thankfully, I spot her at the statue near the museum with a dead phone."
narrator2 "Henrietta doesn't let go of my shirt until we get back to the group."

scene bg hostel
with wiperight

narrator2 "The night at the hotel on our way back doesn't go as smoothly as the first one."
narrator2 "This time I have to share a room with a guy who doesn't mind other people seeing him make out with his girlfriend right in the room."
narrator2 "I do, so I grab my jacket and make my escape."

narrator2 "It's already past curfew."

scene bg stairs
with dissolve

narrator2 "Probably not the best idea to spend the night on the hotel stairs, but whatever."
narrator2 "Just as I start to doze off, someone shakes my shoulder."

show nightv at appearbottomleft
show nightc at appeartopright

v "—ler."
v "Eyler."
v "You'll catch a cold if you sleep here."
c "...?"

narrator2 "It's Vincent."
hide nightv
hide nightc

show charles neutral at right
c "Ah. Thanks."
c "I didn't mean to fall asleep."
c "Why are you out at this hour?"
show vincent smile3 at left
v "Just wanted to get some fresh air."
v "I do enjoy night walks."
show charles contemplating
c "We're not allowed to leave the rooms at night, you know?"
show vincent smile1
v "Then, may I ask why you're here?"
show charles doubt
c "Uh."
c "I guess I'm not a fan of voyeurism?"
show vincent question
v "?"
c "No, that sounded bad. Forget it."
show vincent smile4
v "Haha. Okay."
show vincent smile2
v "I'm guessing there are problems with your roommate?"
show charles sigh1
c "Yeah, that's a pleasant way to put it."
show vincent smile3
v "I could use less pretty words, but it'd leave a bad taste in my mouth."
hide vincent smile3
hide charles sigh1

narrator2 "Vincent looks at the night sky."

show vincentlookup at appearbottomleft
v "It's nice here."
v "So quiet."
v "I don't have to wake up to shouting."
show charleslookdown at appeartopright
c "..."

narrator2 "I don't know what to say to that, so I just pick at my skin."
v "Sorry, I said too much."
c "No, that's..."
narrator2 "Fine? Pitiful? Awful? ...None of these seem to fit."
narrator2 "I'm not someone who should comment."
pause 0.5
narrator2 "We sit in silence for some time."
hide vincentlookup
hide charleslookdown
show vincent smile2 at left
v "That being said, do you plan to return to your room?"
show charles smile at right
c "Nah. I'll wait it out a bit more."
show vincent smile1
v "I see."
v "Well, good night then."
c "Night. Thanks for keeping me company."
show vincent smile3
v "It's my pleasure."
hide vincent smile3
hide charles smile

narrator2 "Half an hour later I return to my room, only to find my classmate sleeping soundly."
narrator2 "This asshole."

narrator2 "I fall asleep thinking that it would be nice to go somewhere with my class again."


# [High school] Education

scene 14
with dissolve
$ renpy.pause(3.0)
scene bg rooftop
with dissolve

call phone_start from _call_phone_start_2
call message_start("System notification", "1 incoming message from: Vincent") from _call_message_start_2
call message_img("Vincent", "Would you mind joining me for lunch?", "images/vincenticon.png") from _call_message_img_9
call message_img("Charles", "sure, just gonna grab something to eat", "images/charlesicon2.png") from _call_message_img_10
call message_img("Charles", "is it the usual place?", "images/charlesicon2.png") from _call_message_img_11
call message_img("Vincent", "Yes.", "images/vincenticon.png") from _call_message_img_12
call message_img("Vincent", "I'll be going ahead, then.", "images/vincenticon.png") from _call_message_img_13
call phone_end from _call_phone_end_2

narrator2 "Vincent likes to eat outside."
narrator2 "“It's more quiet here,” he says."
narrator2 "After the class trip, we've started hanging out more often."
narrator2 "Sometimes he invites me for lunch - like today."

show charles contemplating at right
with dissolve
c "Don't you think the education system is flawed?"

show vincent question at left
with dissolve
narrator2 "Vincent brings a hand to his chin, thoughtful."
v "Depends on what you define as a “flaw”."
show vincent smile2
v "If the main objective of education is discipline, then it is essential to have a hierarchy."
show charles neutral
c "Hmm..."
show charles contemplating
c "I'm rather thinking about the things we learn."
show charles smile6
c "Take today's test, for example."
show charles smile2
c "Do you actually know what “the entropy of isolated systems never decreases” means? Can you explain that?"
show vincent smile4
v "No, not really. I just learned the material needed to answer the questions."
show charles smile
c "See?"
c "You only learned the answer the teacher wanted to see."
show charles suggesting
c "Not only will you forget this knowledge, but you'll have no clue what you were writing about."
c "We're only learning keywords that we don't know the meaning of, and don't gain any practical knowledge."
show vincent smile1 at left
v "Okay, I understand where you're coming from."
show charles smile6
show vincent smile2
v "“If you can't find use for theoretical knowledge, then it's meaningless.”, right?"
show vincent smile3
v "However, I wouldn't use this statement as an excuse to slack off."
v "Or accuse people of using bad teaching methods for that matter."
show charles sigh1 at right
c "Right."
show charles smile
c "I just wanted you to hear me out on this."
c "If given the opportunity, I'd like to change something myself."
show charles sigh1
c "It'd be ridiculous to tell others how to do their work."
show vincent smile4
v "I'm relieved you understand."
show vincent question
v "I think it's not just the education system that uses keywords, though."
v "Words that carry no meaning litter our speech in everyday life."
show charles sigh2
c "Then, mass media is just entirely made out of them."
show charles smile2
c "It's just template phrases that are guaranteed to cause a reaction..."
show vincent smile2
v "...While the hidden objective may be entirely different."
show charles smile
c "Yeah. Like articles bashing local art exhibitions are actually written to promote them."
show charles neutral
c "Oh, crap. I think the break will end soon."
c "You still haven't finished your food."
show vincent smile3
v "Haha, don't worry about me."
hide charles neutral
hide vincent smile3
narrator2 "We hurriedly finish our modest lunch and run to class."


# [High school] Puberty

scene 15
with dissolve
$ renpy.pause(3.0)
scene bg corridor
with dissolve

narrator2 "The older we get, the more disturbed and obnoxious everyone becomes."
narrator2 "They're trying to connect, clumsily, erratically."
narrator2 "Which I understand to some degree, but I've always been fine in my own company."
narrator2 "Also Vincent's, but he can be tiring, too."
narrator2 "Sometimes he starts ranting on subjects I don't understand, which gets tedious."
narrator2 "Like hell do I give a damn about politics."
narrator2 "Go back to your containment board, for god's sake."
narrator2 "Henrietta isn't a saint, either."
narrator2 "Am I actually masochistic for enjoying being badmouthed by her?"
narrator2 "At least she has the same horrible taste in anime."

show charles smile2 at center
c "Miss Warhol, you absolutely have to consult me on dating sims."
c "We could make a fortune off this."
show anri sigh at left
h "Fuck off, Eyler."
h "It won't sell."
show anri lookaway
h "Here, at least."
show anri angry
h "And don't talk so loudly!"
h "The other girls will hear!"
show charles sigh1
c "It's your fault for trying to seem something you're not~"
show charles smile2
c "So, how about it? You and me, a doujin circle?"
show anri pissed
h "No. I've never written a finished story in my life."
show charles suggesting
c "Just copy the popular tropes."
c "Everyone only wants things they're used to."
show anri sigh
h "Just go away, Eyler."
h "You're a bother. Go pester someone else."
hide anri sigh
hide charles suggesting
narrator2 "Talking to miss Warhol always lifts up my mood."


# [High school] Heaven's Gate! Heaven's Gate!

scene bg noise
with pixellate

narrator2 "“Have you heard of Heaven's Gate?”"
narrator2 "“They're an organization that preaches that our world is controlled by alien puppeteers from another world”"
narrator2 "“Fucked up, right?”"
narrator2 "“Does that mean that their world is more real than ours?”"
narrator2 "“What even {i}is{/i} real these days?”"
narrator2 "“Do you think we could be saved if we refuse to be actors on this stage?”"
narrator2 "“Maybe we should leave altogether!”"

scene bg rooftop
with pixellate

call phone_start from _call_phone_start_3
call message_start("System notification", "1 incoming message from: Charles") from _call_message_start_3
call message_img("Charles", "what's up with the emergence of the web cults lately?", "images/charlesicon2.png") from _call_message_img_14
call message_img("Vincent", "You mean Heaven's Gate?", "images/vincenticon.png") from _call_message_img_15
call message_img("Vincent", "Actually, I helped copywrite the contents for the site.", "images/vincenticon.png") from _call_message_img_16
call message_img("Charles", "eh— What?! Really?", "images/charlesicon2.png") from _call_message_img_17
call message_img("Vincent", "Of course.", "images/vincenticon.png") from _call_message_img_18
call message_img("Vincent", "Any kind of content has curators.", "images/vincenticon.png") from _call_message_img_19
call message_img("Vincent", "This one was meant as a prank, though.", "images/vincenticon.png") from _call_message_img_20
call message_img("Vincent", "You don't actually believe that we're puppets on strings, do you?", "images/vincenticon.png") from _call_message_img_21
call message_img("Charles", "the text you wrote was awfully convincing, though", "images/charlesicon2.png") from _call_message_img_22
call message_img("Vincent", "Hahaha! I'm honored.", "images/vincenticon.png") from _call_message_img_23
call message_img("Charles", "why heaven's gate though?", "images/charlesicon2.png") from _call_message_img_24
call message_img("Vincent", "We wanted it to seem big, despite it being a prank.", "images/vincenticon.png") from _call_message_img_25
call message_img("Vincent", "Doesn't it sound like something promising?", "images/vincenticon.png") from _call_message_img_26
call message_img("Charles", "yeah, sounds pretentious as fuck", "images/charlesicon2.png") from _call_message_img_27
call message_img("Vincent", "It doesn't mean anything, really.", "images/vincenticon.png") from _call_message_img_28
call message_img("Vincent", "Just like Heavenly Kingdom doesn't exist.", "images/vincenticon.png") from _call_message_img_29
call message_img("Charles", "so an empty promise of virtue, huh", "images/charlesicon2.png") from _call_message_img_30
call message_img("Charles", "still, isn't it uh. kind of dangerous?", "images/charlesicon2.png") from _call_message_img_31
call message_img("Charles", "people might believe you guys for real.", "images/charlesicon2.png") from _call_message_img_32
call message_img("Vincent", "That would be silly, don't you think?", "images/vincenticon.png") from _call_message_img_33
call phone_end from _call_phone_end_3


# [Interlude] Rationality

scene 16
with dissolve
$ renpy.pause(3.0)
scene bg murderscene
with pixellate

show bennett neutral at center
e "Mr. Honikker."
e "Do you think I'd act more rational if I killed my remaining emotions?"
hide bennett neutral
show felix neutral at center
f "I don't believe we could be rational without feelings."
f "Patients with prefrontal cortex brain damage cannot experience emotions."
show felix lookaway
f "To them, any decision seems as good as the other."
f "For example, when I think of killing someone I care about, I'm overwhelmed with horror."
f "It goes without saying that I'd never do it on a whim."
show felix neutral
f "Thus, feelings are essential for rational thinking."
f "Soap inhibits the prefrontal cortex functionality as a side effect, right?"
show felix lookaway
f "I've been saying it all the time, but consuming it isn't doing you any good."
f "You'll lose the ability to distinguish the weight of one decision from another."
hide felix lookaway
show bennett neutral2 at center
e "And that means?"
hide bennett neutral2
show felix neutral at center
f "That means killing me and eating cookies for breakfast will be morally equal to you."
hide felix neutral
show bennett neutral at center
e "Hmm..."
hide bennett neutral
show felix lookaway at center
f "My point is, killing your emotions will only worsen your overall mental state."
show felix serious
f "It's okay to care, Bennett."
hide felix serious
narrator2 "Bennett croaks out a laugh."


# [High school] Charles' novel

scene 17
with pixellate
$ renpy.pause(3.0)
scene bg rooftop
with dissolve

narrator2 "Vincent peeks over my shoulder, startling me with his voice."
show vincent smile2 at left
v "Are you writing something?"
show charles doubt at right
c "Ah...haha...This barely counts as as writing."

narrator2 "Fennell steps over the bench, now facing me directly."

show vincent question
v "Are you dissatisfied with what you're making?"
show charles neutral
c "No, not exactly. Not more than usual. It's just..."
show charles worried
c "I don't know how to communicate my thoughts to others."
show charles smile
c "The whole plot looks too contrived. I'd stop reading after the first page."
show vincent neutral
v "Hm."
v "Do you think your readers are stupid?"
show charles squint
c "No!"
c "If anything, it's my own fault that I'm a clumsy writer, not theirs."
show vincent smile1
v "Then, do you not trust them?"
show charles worried
c "...I don't. I mean, I really want to."
c "But I'd be lying if I said I did."
show vincent neutral
v "I see."
v "If you can't bring it around no matter what..."
show vincent smile3
v "Why not prove that you yourself can be trusted?"
hide vincent smile3
hide charles worried

narrator2 "Vincent leans closer into my personal space, making me recoil a bit."

show speech1 at appearbottomleft
with dissolve
show speech2 at appeartopright
with dissolve

v "Show that you've done your research."
v "That you're knowledgeable about the subjects you're handling."
v "That you're involved as much as your reader is."
v "That you're prepared to bare your mind and soul."

narrator2 "His presence suddenly overbearing, Vincent looms over me."
narrator2 "My breathing hitches."
narrator2 "I feel small."

c "Wouldn't I be making a fool out of myself if I admit my weaknesses?"
v "Yes. It'll make you vulnerable."
v "It'll leave you in the open."
v "Naked in public."
v "Guts out."
v "Come, cop a feel."
v "For $1.99 only."
v "Thrilling, right?"
c "You..."
v "Yet still, you'll be the one in control."
v "Because it was your conscious decision to reveal the information, and you hold power over it."

hide speech1
hide speech2

narrator2 "With those words, Vincent leaves my personal bubble and drops on a bench beside me."

show vincent smile4 at left
v "Having nothing to hide puts you at both an advantage and disadvantage, but my opinion is that it's worth it."
show charles sigh2 at right
c "Haa...I suppose that's one way to go about it."
show charles smile2
c "If it were me, I'd rather have the work exist separately from its author."
c "If anything, I'd prefer working as anonymously as possible."
show vincent smile2
v "Yes. I'm not saying my approach would work for each and every person."
v "You should choose what suits you best."
show vincent smile1
show charles neutral
v "But most importantly, don't underestimate your readers."
show vincent smile2
v "Make them feel like your story is the best thing they'll ever experience."
v "Make them feel like they can only feel that way with you."
show vincent smile1
v "And there you have it! A story you can be proud of."
show charles doubt
c "Haha...the way you put it sounds like selling your mind to others."
show vincent smile3
v "Haha! Does it?"
v "I'd call it “sharing”."
show charles neutral
show vincent smile2
v "Besides, being insincere in your work will result in flavorless throwaway texts."
show vincent smile3
v "Do you want to write disposable garbage like that?"

narrator2 "{i}Mr. Fennell, you're intense.{i}"

show charles drop
c "That's...a lot of knowledge for someone as young as you, mr. Fennell."
show vincent smile4
v "I'm just saying what I've learned from more experienced writers."
show vincent question
v "And, I suppose I'm really passionate about writing."

narrator2 "{i}Oh. I didn't know.{/i}"
narrator2 "{i}Is he writing something too?{/i}"

show vincent smile2
v "You just looked like you needed advice."
v "Were the words I chose enough?"
show charles smile
c "Yeah. Thanks. I owe you one."
hide charles
hide vincent

show rooftoplunch at appearcenter
with dissolve

c "Actually, would you like to read what I've written so far?"
c "I think I could use some feedback."
v "Sure."
v "Don't expect mercy."
c "Bring it on."
c "I'll fetch you my notebook next week, then."
c "There's a lot written, so you can take your time with it—"

narrator2 "Our conversation is cut off by the ringing school bell."


scene bg black
with dissolve
$ renpy.pause(1.0)

scene bg classroom
with dissolve

narrator2 "During our final high school year, Vincent joins the student council,
and invites me to do the same."

show vincent question at left
v "Didn't you mention that you wanted to influence school life, if possible?"
show vincent smile1
v "I believe it's a good opportunity to do so."
show charles contemplating at right
c "I think it's not about good ideas, but rather the ability to convince others."
c "Which is something you have."
show vincent smile2
v "And right now I'm using it to convince you to try it."

narrator2 "{i}Argh, so persistent.{/i}"

show charles sigh2
c "Okay, fine. I'll tag along."
show vincent smile3
v "Success! You'll definitely regret it."
hide vincent smile3
hide charles sigh2
pause 0.2
show joke at appearcenter3
with dissolve
c "Huh...Wait! That's the opposite of words of encouragement!"
v "Hahaha!"

scene bg park
with dissolve

narrator2 "It's past 6pm. We're ones of the last students leaving school."
narrator2 "I stretch and allow myself to let out a prolonged yawn."

show charles sigh2 at left
c "Today's meeting was so tiring...I need a no-people day soon."
show vincent smile1 at right
v "Mm. I can understand that."
show charles sigh1
c "Says Vincent who talked during the whole meeting."
show charles squint
c "How do you even have energy for all that arguing?"
show vincent smile3
v "Haha!"
v "I just enjoy good discussion."
show charles squint
c "More like uncivilized discourse."
c "Everyone was basically trying to shout louder than the others."
show vincent smile2
v "Thrilling, isn't it?"
show charles sigh1
c "I can't believe you."
show vincent smile1
v "I'm joking."
v "It was indeed a bit tiring."
show vincent smile4
v "I'm not a big fan of the noise."
show vincent smile2
v "However, I don't feel like going home just yet."
show charles contemplating
c "Well, the weather's not bad."
c "I was planning to invite you for a walk anyway."
show vincent smile1
v "Alright."
show vincent smile2
v "Should we walk in silence for a while?"
show charles smile5
c "Good plan."
hide vincent smile2
hide charles smile5
narrator2 "I let my vision lose focus, and feel the world around me slow down."
narrator2 "We part ways after an hour of strolling around the park."
narrator2 "Feeling re-energized, I spend the whole evening leisurely studying subjects ahead of the program."

# [High school] Social media

scene 18
with dissolve
$ renpy.pause(3.0)
scene bg corridor
with dissolve

narrator2 "We're waiting for the next class to start."
narrator2 "Henrietta sits near me on the windowsill, dozing off with a chem textbook in her hands."
pause 0.2
show socialmedia at appearcenter2
with dissolve
c "I'm so tired of social media."
c "Everyone's talking so much, but no one's talking about things that really matter."
c "And I feel bad for contributing."
hide socialmedia
pause 0.2
show anristretch at appeartopright3
with dissolve
show nosepinch at appearbottomleft2
with dissolve
pause 0.5
narrator2 "Henrietta yawns and stretches, then pinches my nose."

h "What do you think people should be talking about then, genius?"
h "And who are you to decide what matters and what doesn't?"
c "Shut it. I know. I'm just saying how I feel."
c "And I feel tired."
hide anristretch
hide nosepinch
show anri sigh at left
h "Your judgements are useless, then."
h "It's like wanting a teenage melodrama to have a deeper meaning."
show anri pissed
h "Want something profound - read a book."
h "Or go talk to Fennell."
h "He's like a combination of a therapist and a saint, so no wonder you love that."
show charles upset at right
c "Way to trivialize him!"
show charles smile6
c "He's like...a god."
show anri pissed
h "A human."
h "You're just biased because he validates you."
show charles contemplating
c "Okay, good point."
show anri neutral
h "Still, I don't get it."
h "What's so good about him?"
show anri pissed
h "Aren't you singing him praises just because he's polite?"
show charles upset
c "Just because he has the human decency to make effort to be kind to others."
show charles smile2
c "He's hardworking, reliable and after talking to him I always feel like I've ascended to some new level of human consciousness."
c "Also, he appreciates the concept of personal space. Unlike some."
show anri sigh
h "Ugh...are you done yet?"
show charles suggesting
c "Now you're just being jealous."
show anri pissed
h "Go fuck yourself, Eyler."
show charles smile2
c "See?"
c "No human decency."
show charles suggesting
c "Vincent would be like, 'Would you kindly back off'."
show anri angry
h "That's the same thing!"
show charles smile5
c "Hahaha. Might as well be."
show charles contemplating
c "I wonder if he's ever gotten angry at someone."
show anri sigh
h "He just has high self-control."
show anri lookaway
h "I lost mine somewhere along the way when I tried to prove that I'm not a doormat for others to step on."

narrator2 "{i}Ah. So she's conscious about her attitude, after all.{/i}"

show charles smile2
c "Mean Anri is the best Anri."
c "Actually, any Anri is great."
show charles contemplating
c "I can't exactly tell you not to worry about it, though."
show charles smile5
c "But, I like you the way you are."
show anri lookaway
h "..."
show anri bashful
h "Okay."

# [High school] Vincent comes to visit

scene 19
with dissolve
$ renpy.pause(3.0)
scene bg room
with dissolve

narrator2 "Vincent comes over to do a research project for school."
narrator2 "I welcome him into my room with rubber gloves still on my hands."

show proud at appearcenter2
with dissolve
v "Eyler."
v "You look proud of yourself."
c "Of course."
c "Cleaning, done!"
c "Clothes, ironed!"
c "I can focus on schoolwork in peace."
hide proud
pause 0.3
show vincent smile4 at left
with dissolve
v "Good."
show vincent smile2
v "You seem to be especially scrupulous when it comes to organizing."
show charles bashful at right
with dissolve
c "I just can't seem to focus when there's something out of place."
c "I end up thinking about a single sheet of paper lying around unsorted instead of doing something useful."
show charles smile6
c "Oh, but that's not the worst of it."
show vincent smile4
v "Must be tough."
show vincent question
v "My workspace isn't very organized in comparison...although I don't have many personal possessions."
show charles neutral
c "Don't like stuff piling up?"
show vincent smile3
v "That too. And, perhaps I'm not very sentimental."

narrator2 "I briefly wonder if that's really the only reason, but decide not to press on."

show charles drop
c "({i}Let's change the topic...{/i})"
show charles smile
c "That being said, remember when we were all about collecting stickers and stuff?"
show vincent smile4
v "Yeah. Everyone was crazy about trading."
show charles smile6
c "I still have my collection."
c "I can't bring myself to throw away my cat toys, too."
show charles doubt
c "It's kind of embarrassing."
show vincent question
v "Why?"
show charles neutral
show vincent smile2
v "You must've loved them a lot."
v "Having things you love doesn't make you seem infantile."
show charles doubt
c "Well...yeah. When you put it like that..."
show charles smile6
c "What about you?"
c "Didn't you have your favorite stuff?"
show vincent smile1
v "Ah...no."
v "I only bought popular things regardless of whether I liked them or not."
show charles neutral
c "...Oh. I see. And then?"
show vincent smile3
v "Then I threw them away as soon as they became useless."
hide vincent smile3
hide charles neutral

narrator2 "At this moment, Vincent's gaze seemed...empty."
narrator2 "His face didn't convey any particular emotion, even though he was smiling - which felt horribly out of place."

narrator2 "For a second, it felt like we weren't talking about bootleg Digimon stickers, but something else entirely."

show charles drop at right
c "Well, uh. Yeah. I see."
c "You must have no interest in material possessions. That's admirable."

narrator2 "Vincent pauses for a bit, then answers."
show vincent smile1 at left
v "Yeah. That must be it."
hide vincent smile1
narrator2 "His words sound hollow."


scene bg black
with dissolve
$ renpy.pause(1.0)

scene 20
with dissolve
$ renpy.pause(3.0)
scene bg room
with dissolve

# [High school] Dating

show dawn at appearcenter2
with dissolve
pause 0.3
narrator2 "The sun is about to rise. Henry's fallen asleep on a bean bag with a joystick in his hands."
narrator2 "Anri comes to hang out on weekends."
narrator2 "Sometimes she brings her brother, whom she's begrudgingly babysitting."
narrator2 "We play video games and eat snacks."
narrator2 "When Anri's not in a school environment, she's far less stressed out."
narrator2 "Even her voice sounds lower than usual."
hide dawn

show charles2 talk at right
c "Crap, your brother is good at rhythm games."
show anri smiling at left
h "Yeah, use him as you like if you need to score full combos."
show anri annoyed
h "That's all he's good for anyway."
show charles2 drop
c "Aren't you being a little harsh?"
show anri reprimanding
h "He deserves it for being a lazy ass."
show anri annoyed
h "Have you seen his grades?"
h "It's like he's made it a goal for himself to become the worst student of the year."
show charles2 neutral
c "Maybe his mind just works differently from the rest?"
show anri blank
h "Yeah, that too."
show anri annoyed
h "But for the most part he just wants to play MMORPGs all day."
show anri grudge
h "I want to help him, but I also want a break from all this shit."
h "I'm tired of working at part-time jobs to help parents sustain his lifestyle."
show anri annoyed
h "Do you know how much console games cost?"
h "Add that to a monthly MMO subscription, gacha pulls and merchandise and you'll get my monthly salary."
c "Your parents don't have to buy all of that, you know."
show anri grudge
h "Henry says they motivate him, so if they don't he just refuses to leave the room."
show charles2 scratch
c "Sheesh."
hide anri grudge
hide charles2 scratch

narrator2 "Anri looks at the ceiling, contemplating something."

show anri blank at left
h "Eyler, I was thinking."
show charles2 neutral at right
c "Yes?"
h "Aren't we actually dating?"
show charles2 squint
c "What?"
narrator2 "Anri starts counting on her fingers."
h "Look, it's the fifth time I'm staying over."
h "You take me out for nice food, and carry my bags when I'm shopping."
h "You even look after my brother when I'm busy."
narrator2 "{i}Aren't all of these just things a decent person would do, miss Warhol...{/i}"
hide anri blank
hide charles2 squint

pause 0.4
show blunt at appearcenter2
with dissolve
c "I fail to see your point."
c "Aren't you the one who's always like..."
c "“Ahhh, I wish someone would call me princess and take me on cute dates~~”"
c "“We'd buy matching clothes and cuddle on a sofa—”"
narrator2 "Anri nudges me with her elbow. Violently."
h "Yeah, you're far from that."
h "Please don't use that squeaky voice to imitate me ever again."
hide blunt

show anri blank at left
h "Still, what should we call this?"
show charles2 talk at right
c "Does it need a specific term?"
c "If you're talking about becoming each other's possession, then I'm against it."
show charles2 squint
c "No one ever belongs to anyone."
c "Yet for some reason everyone thinks a meaningless string of letters can bind people to them."
h "Isn't it normal? To want something you can call your own?"
show charles2 scratch
c "It rubs me the wrong way."
c "That would mean treating others as commodities."
show charles2 talk
c "Which, in turn, contributes to a mindset intrinsic to a capitalist society."
show anri annoyed
h "Augh, you just had to bring your pointless philosophy into it."
show anri reprimanding
h "Just say it in normal people words."
show charles2 smile
c "Sorry."
c "I just don't know yet."
narrator2 "Anri sighs."
show anri smiling
show charles2 neutral
h "Well, me neither."
show anri blank
h "Hold on, let me try something."
hide anri blank
hide charles2 neutral

narrator2 "Anri leans in and kisses me."

show anri blank at left
h "So? How was it?"
show charles2 neutral at right
c "Hm..."
show charles2 thinking
c "It was supposed to be this amazingly good thing that every story leads up to..."
c "But it didn't really feel like anything out of the ordinary."
show anri blank
h "What if it was...hmm...with someone else?"
show charles2 neutral
c "Um, I think it'd be the same."
show charles2 thinking
c "You know I'm not too comfortable with physical stuff."
show charles2 laugh
c "Is there something wrong with me, after all?"
show anri reprimanding
h "Want me to hit you?"
show anri annoyed
h "Aren't you the one who keeps going on tirades about everyone experiencing life differently?"
show anri blank
h "Just because I don't understand doesn't mean it's your fault."
show charles2 lookaway
c "..."
show charles2 scratch
c "Sorry. I just feel like I'm constantly letting people down."
show anri annoyed
show charles2 neutral
h "Then find a downer like you, jeez."
show anri smiling
h "Or stop worrying about it."
h "Just look at Fennell being comfortable in his own company."
show charles2 talk
c "Vincent's always surrounded by people, though."
show charles2 neutral
c "He only started isolating himself just recently."
show anri blank
h "I've only talked to him a few times."
h "It felt like he wasn't even there."
h "He's not really listening to what you say."
show anri smiling
h "So, my conclusion is that he's full of shit."
h "But at least he's content with it."
show charles2 smile
c "Maybe he was just bored around you?"
show anri blank
h "Maybe. But he's like that around literally everyone."
h "And you kinda suck at reading people."
h "I bet Fennell's the kind of person who'd populate a planet with clones of himself and be happy about it."
show charles2 laugh
c "Hahaha! Where did that come from?"
show charles2 smile
c "If I cloned myself or had my personality divided into parts, it'd end in a mass suicide."
show anri annoyed
h "Now you're being weird."
show anri smiling
h "Anyway."
h "I guess it's stupid to try mold you into something you're not."
h "Even if you do everything a romantic partner would,
it's pointless if you're not feeling it."
show charles2 neutral
c "..."
c "I'm sorry."
h "There you go again."
h "It should be a “thank you”, shouldn't it?"
show charles2 smile
c "You're right."
show charles2 laugh
c "Thank you, Anri."


# [High school] Paralysis

scene 21
with dissolve
$ renpy.pause(3.0)
scene bg room
with dissolve

narrator2 "I wake up with a headache and stumble into the bathroom to brush my teeth."
narrator2 "I look into the mirror and notice that I only blink with one eye."
narrator2 "Weird."
narrator2 "But whatever."
narrator2 "School proceeds as normal, until I start feeling extremely fatigued during the 5th period."
narrator2 "{i}Something's not right.{/i}"
narrator2 "I end up calling Mom."
narrator2 "She always knows what to do."

scene bg hospital
with dissolve

y "It seems like your son has Bell's palsy. It might take around a month to recover."

narrator2 "Great. Out of all the rare illnesses, my body decided to get this one."
narrator2 "Missing a month of school before exams sounds like the worst case scenario."
narrator2 "It's just half of my face staying unresponsive, yet my whole body feels numb."
narrator2 "I can barely focus on the phone screen as I type a message back to Anri, who was curious enough to investigate my sudden disappearance from class."

call phone_start from _call_phone_start_4
call message_start("System notification", "1 incoming message from: Anri") from _call_message_start_4
call message_img("Anri", "you okay?", "images/anriicon2.png") from _call_message_img_34
call message_img("Charles", "got hospitalized with face paralysis", "images/charlesicon2.png") from _call_message_img_35
call message_img("Anri", "the fuck is that", "images/anriicon2.png") from _call_message_img_36
call phone_end from _call_phone_end_4

narrator2 "“The fuck is that” indeed."
narrator2 "One of my eyes can't blink and my mouth is stuck in a convulted grimace."
narrator2 "Thank god no one will come to visit."
narrator2 "I close my eyes (one manually) and hope that the numbness will go away in the morning."
narrator2 "It doesn't."
pause 0.5
narrator2 "Hospital food is tasteless."
narrator2 "That doesn't really matter, since I'm going to be discharged today."
narrator2 "No one stays at hospitals for more than two days unless you're fatally injured."
narrator2 "Mother asked her acquaintances to give me a ride home."
narrator2 "What followed were two weeks of pills and 24-hour sleep, and two more weeks of staring at the ceiling because my mind couldn't focus on anything else."

scene bg room
with dissolve

m "Henrietta came to visit while you were sleeping. She brought some printouts from school."
c "Bless her."

narrator2 "Among the stuff Anri brought, I find a notebook with Vincent's name on it."
narrator2 "“I hope you find these notes useful. Get well soon,” said the note inside."
narrator2 "I'm mortified."
narrator2 "I ended up being a burden to them both."
narrator2 "I try to shake the feeling off and be sincerely grateful, but end up being choked by guilt."
narrator2 "I have to catch up."
narrator2 "Become better."
narrator2 "More capable."
narrator2 "If I'm not ahead of others, then my self-worth is no better than zero."
narrator2 "I—"
narrator2 "I need to thank people who care about me soon."

scene bg black
with dissolve
narrator2 "When I finally became able to come outside after what felt like forever, dandelions were in full bloom."


# [High school] Care

scene 22
with dissolve
$ renpy.pause(3.0)
scene bg corridor2
with dissolve

narrator2 "Vincent has his nose buried into a notebook lately."
narrator2 "He's definitely writing something, but I never pry."

show vincent question alter at left
with dissolve
v "I think there are two ways to go about writing."
v "To be the one in power, or to give power to your readers."
show vincent smile2 alter
v "You can write a piece so flawless and complete that your awestruck reader will be rendered speechless..."
show vincent smile1 alter
v "Or, create a flawed, seemingly incomplete work, prompting the reader to contribute with better ideas."
show vincent smile2 alter
v "Which would you prefer?"
show charles doubt at right
with dissolve
c "Hmm...Playing god or making a fool out of myself...tough choice indeed..."
show vincent smile1 alter
v "So?"
show charles smile
c "The latter sounds like less pressure, so I'd take that one."
c "That way, every reader can become a co-creator, even if they get laughs at my expense."
show vincent smile2 alter
v "I see."
show charles smile6
c "Besides, if something's considered ideal, you can only make copies of it without creating anything new."
c "That doesn't sound too creative to me."
show charles smile6
c "More importantly, what'd be your choice?"
show vincent smile3 alter
v "Me? Well, what do you think?"

narrator2 "{i}I think you want to leave it a rhetorical question.{/i}"

show charles neutral
c "How are your grades coming along, by the way?"
show vincent smile2 alter
v "Well, looks like I'll be one of the few people invited to the awards ceremony."
show charles neutral
c "Wow. You're amazing."
show vincent smile4 alter
v "Haha. I didn't really have a choice."
show vincent question alter
v "Do you think you'll be able to graduate with honors?"
show charles bashful
c "Nah. I totally blew my chem and math grades."
show charles doubt
c "Took me a bit of time to come to terms with the fact that I'm not that smart."
show charles smile2
c "Wish I didn't grow up thinking that doing well in academics would guarantee me a secure future, though."
c "Or anything really."
show charles doubt
c "Right now I just want to sleep my life away."
show vincent smile4 alter
v "Hahaha."
show vincent neutral alter
v "By the way."
v "How's your mother feeling?"
show charles neutral
c "She's...okay. Surprisingly enough."
show charles smile6
c "I'm doing my best to help her, too."
c "Even if it means working in retail."
show vincent smile2 alter
v "I'm sure of it."
show charles contemplating
c "She used to be far more violent before."
c "Never laid a hand on me, though."
c "It was always something else."
c "Utensils, clothes, books."
show charles worried
c "The only thing I regret is that as a kid, I tried to make her less aggressive by saying I'll kill myself."
c "That was extremely selfish of me."
show vincent smile1 alter
v "You were a child."
show vincent smile4 alter
v "You didn't know any better."
show charles contemplating
c "Still, it's so weird."
c "Out of all solutions my 4-year-old mind always jumped to suicide."
hide charles contemplating
hide vincent smile4 alter

narrator2 "Vincent touches the bruise on his cheek only somewhat consciously."

show charles bashful at right
c "I guess I just wanted to guilt trip her into caring."
show vincent neutral alter at left
v "...I see. So that idea isn't foreign to you, too."
show charles neutral
c "What do you mean?"
show vincent smile3 alter
v "It's nothing."
v "Don't worry."
show charles squint
c "Sounds fishy."
show charles smile5
c "But, as long as you don't want to talk about it, I'll bug off."
show vincent smile1 alter
v "Thank you."
hide charles smile5
show vincent smile3 alter at center
v "I would hate being pitied."

scene bg black
with dissolve
$ renpy.pause(1.0)

# [Anri gets stabbed with a knife]

scene 23
with dissolve
$ renpy.pause(3.0)
scene bg outsidehouse
with dissolve

show anri neutral at center
h "Hmmm..."
h "Maybe I shouldn't have come without a warning."
h "But, it's Charles, so he won't mind all that much."
h "I'll just return this book and go home, anyway."
narrator2 "{b}Click!{/b}"
show anri worried
h "It's open..."
show anri sigh
h "Haa..."
h "Geez, when will they fix the lock?"
h "It's already been a month since it's been like this."

scene bg stairway
with dissolve
show anri neutral at center
h "This place is already a hellhole. Would it hurt them to put more effort into making it a little bit safer?"
h "..."
show anri worried
h "(The elevator's taking too long...)"
h "(Did someone just come in?)"
hide anri worried
with vpunch
show assault1 at appearbottomleft2
h "...!"
u "Keep quiet and no one will get hurt."
show assault2 at appeartopright2
h "MMMNNFFF!"
with vpunch
u "You bitch! Stop screaming!"
h "...!"
with vpunch
h "Somebody, help!"
narrator2 "I hear someone opening the door floors above, and a dog barking."
with vpunch
u "Argh..."
with hpunch
hide assault1
hide assault2
pause 1
show assault3 at appearcenter
h "..."
h "He...ran away...?"
h "I can't stay here..."

scene bg elevator
with fade

narrator2 "..."

scene bg insideelevator
with fade

show huh at appearatright
pause 1
h "Blood..."
narrator2 "..."

scene bg door
with fade

narrator2 "{b}RIIIIIING{/b}"
narrator2 "{b}RIIIIIING{/b}"
narrator2 "{b}RIIIIIING{b}"
narrator2 "{b}RIIIIIIIIING{b}"

scene bg entryway
with dissolve

c "Who could it be?"
c "Maybe I should pretend we're not home..."

show shock2 at right
show shock1 at appearbottom2

c "...!"
c "Anri?!"
narrator2 "There's a trail of blood behind her."
narrator2 "It keeps dripping, staining the floor."
hide shock2
hide shock1

show help at center
c "What happened?"
c "Shit, okay, don't talk."
c "Mom, call the ambulance."
c "Anri, I'll help you lie down, okay?"
h "The blood will...get everywhere..."
c "Don't worry about it."
c "It's going to be alright."
hide help
narrator2 "If her lung isn't punctured, that is."
show wound1 at appearbottom2
c "Here."
c "Sorry for the makeshift scarf pillow. I'll get you a real one in a bit."
h "..."
c "I'll try to stop the bleeding now."
c "But, uh, I only have theoretical knowledge about it. Forgive me if it hurts."
c "Mom will google the right way to do it, so trust us."
narrator2 "Anri stays quiet."
narrator2 "She must be in shock."
narrator2 "I help her take off her shirt and look at the wound, trying not to focus on the blood oozing out."
narrator2 "It's most definitely a knife wound."
show wound2 at appeartop2
pause 1
c "Okay, this should do it."
narrator2 "I throw the bloodstained shirt into cold water and let out a sigh."

scene bg black
with dissolve

narrator2 "The ambulance arrives quickly."
narrator2 "I follow her to the hospital, hoping that it's nothing serious."

scene bg hospital
with dissolve

show hospitaltalk1 at appearbottomleft2
show hospitaltalk2 at appeartopright2

narrator2 "When I see Anri again, she has the same absent-minded look on her face."
c "What did they say?"
h "No internal organ damage."
h "But, it's going to leave a scar."
c "That's good."
h "It sucks."
h "Why do things like this happen?"
h "Can't everyone live in peace?"
hide hospitaltalk2
narrator2 "She begins to tear up."

show hospitaltalk3 at appeartopright2
h "Why must I be cautious of every person I see on the street?"
h "Why must I be scared of walking alone?"
c "..."
c "I'm scared, too."
c "Ever since we moved into that place, I've been paranoid of every sound."
c "We got rid of the cockroaches, but the neighbours stayed."
c "Want me to get you some pepper spray? I have some in my bag."
h "I hate it."
h "The very fact that you speak of these things like they're nothing out of the ordinary."
c "But they are ordinary."
c "My mom got stalked by some psycho for over a year."
c "I got smacked with a broken bottle on the street some time ago."
c "Our neighbour's dog got mauled by a pack of strays."
c "Life's full of misfortunes like that."
h "Fuck that."
h "It's unfair."
c "It is."
c "But there's nothing we can do about it, can we?"
h "You're always like this."
h "Ignoring the problem instead of doing something about it."
c "..."
c "Miss Warhol."
h "What? And what's up with the sudden formality?"
c "I didn't get to ask, but what exactly happened back then?"
h "...I don't get it myself. Everything happened so quickly."
h "He told me to stay quiet, but I screamed my lungs out anyway."
h "Maybe he just wanted my purse."
h "Maybe something else."
h "I don't know."
h "I just wanted to return the book."
hide hospitaltalk3
hide hospitaltalk1
narrator2 "Anri turns over, and cries into the pillow."


# [Interlude] Wounds

scene 24
with dissolve
$ renpy.pause(3.0)
scene bg felixlab
with pixellate

show examination at appearcenter2

f "Okay, examination over."
f "I'm going to disinfect the equipment."
f "You can get dressed."
e "Thanks, mr. Honikker."
hide examination

show bennett neutral2 at left
e "So, how is it?"
show felix neutral at right
f "Hmm...I don't think these bruises will ever heal."
f "Unless we skin you and replace the tissue completely."
show bennett neutral
e "..."
show felix lookaway
f "Yeah. I don't think you want it."
f "Even though you're emotionally dead unless medicated, it's going to hurt like hell."
show felix serious
f "Can't laugh about that."
show bennett mocking
e "If it's a smile, I can always give you one. See?"
e "Just like I was taught in the Labs."
show felix lookaway
f "Stop it. That's not funny."
show bennett neutral2
e "It's weird, mr. Honikker."
e "I'm so desensitized to cruelty and violence that I no longer feel saddened or shocked by them."
e "I don't think I'm capable of crying, either."
e "Or feeling anything really."
show bennett neutral
e "Everything is just...mundane."
show felix neutral
f "Well, humans are an adaptive species."
f "If all you see every day is atrocities, you can't help but get used to them."
show bennett turnaway
e "Yeah, I guess you're right."
e "Forget I said anything."
show felix serious
f "You hate being sober that much?"
show bennett neutral2
e "When I am, I start having thoughts."
show bennett mocking
e "I'd rather not think, mr. Honikker."
e "That should be your thing to do."
show bennett turnaway
e "Good night."
hide bennett turnaway
show felix lookaway
f "..."
show felix neutral
f "Well, he's right."
f "It's really not something I should concern myself with."
show felix lookaway
f "I have to focus on my research while I still have the time."

scene bg black
with pixellate
$ renpy.pause(1.0)

# [High school] Novel

scene 25
with dissolve
$ renpy.pause(3.0)
scene bg park rainy
with dissolve

narrator2 "We're strolling in the park after school again."
narrator2 "The weather isn't particularly good, but I have an umbrella with me."
narrator2 "Vincent doesn't mind the rain, but I do, so I follow him like the butler of a rich household."
narrator2 "His throat is bandaged."
narrator2 "Vincent doesn't bring it up, and I don't ask."

narrator2 "We stop at a small bridge."

show rain at appearcenter

v "Oh, there's something I've been meaning to tell you for a while."
c "No way! Is it a love confession, mr. Fennell?"
v "Almost."
v "I've been writing a novel."
c "Oh. What's it called?"
v "Aether Almanac."
c "Sounds fancy."
v "I'm still in the process of writing it, and frankly, there's a lot to do,
but I have published some chapters already."
v "If you're willing to give it a read, I'll be happy to share it."
c "Of course. I mean, you can't write badly."
v "Haha. Thank you for your trust."
v "It's a collection of short stories centered around one divine being."
v "It needs a lot of improvement, and I don't expect my target demographic to be older than myself."
v "Still, it's a work I love dearly."

hide rain

narrator2 "It's the first time I've heard him use “love” in regard to something."

scene bg black
with dissolve

narrator2 "“I should read it soon,” I thought, yet ended up postponing it until the very last minute."
narrator2 "One's writing is the mirror of one's soul."
narrator2 "I was afraid of my imaginary construct of Vincent shattering upon looking into it."

# [Interlude] Aether Almanac

scene 26
with dissolve
$ renpy.pause(3.0)
scene aa1
with pixellate

narrator2 "In the Land of Eternity, there lived a Scientist."
narrator2 "Exiled from her homeland for heresy against their beliefs, she decided to travel around the world to see all its wonders."
scene aa2
with dissolve
narrator2 "She saw civilizations rise and fall, stars explode and new forms of life come into existence."
narrator2 "After thousands of years of wandering, she began to grow weak in her limbs."
scene aa3
with dissolve
narrator2 "She walked and walked, until she stumbled and fell down to the ground."
narrator2 "There she lay for days, unable to get up on her own."
narrator2 "People passed by."
narrator2 "Some asked if she was feeling unwell."
narrator2 "Some pitied her, and gave her food to eat."
narrator2 "Some gave advice on how to get back to her feet."
narrator2 "But nobody extended a hand."
narrator2 "One day, she felt someone lift up her weakened frame."
scene aa4
with dissolve
narrator2 "She looked up, and saw a being she couldn't quite describe, as its form was constantly changing."
narrator2 "It was the most fascinating sight she'd ever seen."
narrator2 "“What are you?” the Scientist asked."
narrator2 "“I cannot be defined by mere words,” it laughed, amused by her question."
narrator2 "“Some call me White Queen, but that was only one of my many masks.”"
narrator2 "“I am neither a man or a woman. For I am not human.”"
narrator2 "“They say meeting me is a great blessing that happens once in many millions of years.”"
narrator2 "“Therefore, how about I grant you one wish?” the being offered, “Say, what do you wish for?”"
narrator2 "The Scientist thought of unlimited knowledge, and the world's treasures, and infallible health, but none of those wonders interested her any longer."
narrator2 "“Can you remain by my side?” she asked, her voice growing weak as the realization that she grew tired of solitude dawned at her."
narrator2 "“Unfortunately, I cannot grant you that wish, as nothing can bind me,” was the divine being's answer, and the Scientist hung her head low."
narrator2 "“However, if it's a lifelong partner you want...”"
narrator2 "Without as much as a warning, the creature tore off the Scientist's finger, and her identical copy grew from it."
narrator2 "As the Scientist screamed from the sharp pain that pierced her, the relentless god spoke again."
scene aa6
with dissolve
narrator2 "“It knows everything you do, and understands you better than anyone ever would.”"
narrator2 "“It'll never leave your side, and remain with you in life and death.”"
narrator2 "“When your sight fades, it'll become your eyes.”"
narrator2 "“When you lose strength in your legs, it'll carry you in its embrace.”"
narrator2 "“Together, you are one.”"

scene bg black
with dissolve
narrator2 "I dream of falling into a pit of identical corpses, and wake up in a cold sweat."


# [High school] Popularity

scene 27
with pixellate
$ renpy.pause(3.0)
scene bg room
with dissolve

narrator2 "Anri's idly browsing her phone as I struggle to finish a mission in a shooter I was playing."

show anri2 neutral at right
h "Wow, Fennell's sure popular."
h "I just looked up his novel and it has like, fifteen fan communities."
show charles2 neutral at left
c "Oh."
show anri2 squint
h "What are you acting all surprised for?"
h "Aren't you his fan or something?"
show charles2 scratch
c "Stop it, I'm not a blind follower."
show charles2 neutral
c "I read his writing the other day."
c "It's good. Like, really good."
c "But..."
show charles2 squint
c "I didn't like it."
show anri2 surprised
h "Whoa, okay."
h "Care to explain?"
show charles2 lookaway
c "Well...the overarching theme of his stories is that only you can save yourself."
c "It's like...other people don't exist, or can't be of any help even if they're around."
c "His characters either choose solitude or end up in circumstances where they are surrounded by their own selves."
show charles2 thinking
c "Don't you think it's close-minded to think that way?"
show anri2 squint
h "Wow, Eyler..."
h "I knew you were dense as a brick, but not to this extent."
show charles2 squint
c "What do you mean?"

narrator2 "Anri rubs her temples and gives me a reprimanding stare."

h "Uh, listen."
h "Doesn't all of this remind you of a certain someone?"


scene bg black
with dissolve
$ renpy.pause(1.0)

# News

scene bg noise2
with pixellate

narrator2 "{b}BREAKING{/b}: Young people aged 12-16 found dead on the shore..."
narrator2 "...The motives behind their deaths remains unclear..."
narrator2 "...Numerous sources report that they all were frequent visitors of Heaven's Gate community website...
a web cult whose beliefs may have led them to suicide—"

scene bg black
with dissolve
$ renpy.pause(1.0)
scene bg classroom
with dissolve

narrator2 "Vincent skips school for three weeks."
narrator2 "When I see him again, there's a mask plastered on his face."
pause 1
show vincentfennell at appearcenter2
narrator2 "Vincent Fennell is..."
show vincentfennell2 at appearcenter2
narrator2 "{i}Smiling.{/i}"

scene 28
with dissolve
$ renpy.pause(3.0)
scene bg morgue
with pixellate

# Felix's death scene

narrator2 "It's dark in the morgue."
narrator2 "We sit on the cold ceramic floor."
narrator2 "Felix Honikker doesn't have long left to live."

show bennett neutral at left
e "How are you feeling, mr. Honikker?"
show felix lookaway at right
f "Tired. But that's nothing new."
show felix serious
f "Is everyone pulling an all-nighter because of me?"
show bennett neutral2
e "Yeah. Even Florence didn't hold back on soap."
narrator2 "Felix sighs."
show felix lookaway
f "Even though I did nothing to deserve this kind of treatment, you all chose to act stupid."
show bennett turnaway
e "..."
show felix smile
f "What are you sulking for, idiot?"
f "You'll see me tomorrow."
show bennett turnaway
e "..."
e "That person won't be you."
show felix lookaway
f "I doubt anybody will notice the difference."
f "It's not like I did anything remarkable during my lifespan."
show bennett neutral2
e "You gave a shit about me."
show bennett turnaway
e "Although...you gave a shit about everyone."
e "Just like Henry."
e "...Before he fell ill."
show felix lookaway
f "..."
f "It's unfair."
f "We both know I am a copy."
show bennett mocking
e "First mr. Honikker tells me it's okay to care, then he complains when I do. Which is it?"
show felix lookaway
f "..."
show felix serious
f "Do you believe in God, Bennett?"
show bennett neutral
e "No."
show bennett neutral
e "Henry Huxley isn't someone as shallow as that."
show felix lookaway
f "...I see."
show felix smile
f "Then, it must be the same for me, too."
show bennett turnaway
e "..."
hide bennett turnaway
hide felix smile

pause 0.5

show bennett final at appeartopright2
e "Mr. Honikker."
e "I won't make friends with you the next time we meet."
show felix final at appearbottomleft2
with dissolve
f "It's a promise, then."

scene 29
with pixellate
$ renpy.pause(3.0)
scene bg corridor2
with dissolve

# [College] Exams

narrator2 "Exams are stressful, but they're nothing I'm unprepared for."
narrator2 "After all, I've always been a diligent student."
narrator2 "I get paired with Anri during the language exam, and we pass with flying colors."

narrator2 "Vincent, however, remains as distant as ever."

narrator2 "For the past month we haven't gotten to talk at all."
narrator2 "I wonder what he is thinking."

show vincent construct2 at center
with pixellate

narrator2 "“How disappointing. I can't seem to find any topics to discuss with you, Eyler.”"

narrator2 "{i}No, no. Vincent's not that petty.{/i}"

show vincent construct

narrator2 "“The very fact that you thought of me like that makes you the petty one.”"

narrator2 "{i}The truth is yours, imaginary mr. Fennell.{/i}"

hide vincent construct

narrator2 "“I understood that the way I use words impacts people around me,
so I decided to distance myself from people who are easily influenced.”"

narrator2 "{i}...More plausible.{/i}"
narrator2 "But doesn't that mean he thinks very little of me?"
narrator2 "Argh."
narrator2 "There's no guarantee that we'll keep in touch after graduating, either."
narrator2 "I can't shake off the feeling of frustration welling up, and end up losing sleep at night."

narrator2 "I'm so anxious that I decide to discuss it with Anri."
narrator2 "She likes food, so I lure her in by inviting her to a cafe."

scene bg cafe
with dissolve

show anri angry at left
h "He wrote WHAT?!"
hide anri angry
narrator2 "Anri stabs a cherry tomato on her plate."
narrator2 "It makes a popping sound and bursts."
show charles drop at right
c "(Ah...Maybe telling her wasn't a good idea after all...)"
show charles denial
c "So what if he's a cult leader!"
show charles worried
c "I want to talk to him again."
show charles upset
c "Besides, he only helped copywrite the texts."
c "It's not like he involved himself in their activity."
show anri disbelief at left
h "Uh... Your moral compass just did a complete 180 right now..."
show charles denial
c "Listen, I'm sure he understands the weight of his actions."
show charles upset
c "His current isolation must be just damage control."
show anri disbelief2
h "Are you sure he's not just a control freak who enjoys having power over others?"
show charles denial
c "God, Anri. Are we talking about the same person here?"
show charles worried
c "He's the most tactful person I know. He wouldn't..."
show anri pissed
h "If you commit suicide because he told you your imaginary world will become real, don't come crying to me."
show charles suggesting
c "You can't cry if you're dead, miss Warhol."
show anri sigh
h "Argh."
show charles neutral
h "Anyway."
show anri lookaway
h "Fennell's dangerous, okay?"
h "People like him harm others without even realizing it."
h "That accident confirmed it."
show anri angry
h "If he's a writer, he should take full responsibility for the messages he's communicating."
h "And don't go 'It's their own fault' on me."
show charles headache
c "But it is! Everyone has their own brains."
c "If they decided to self-destruct after hearing they're in a video game, then they were already predisposed to it."
c "They just saw the cult site and BAM! Confirmation bias activated."
c "They wanted a motive, they got it."
show charles squint
c "I would never end my life just because I stumbled on some creepypasta on the Internet."
c "It would take more than that. Like...Mother's death."
show charles smile5
c "Or my own health deteriorating to the point where I start hurting others. Then, I..."
show anri anxious
h "H-hey, stop it."
show charles neutral
c "Ah. I'm sorry."
show charles worried
c "I don't think I'm completely right, either."
c "Circumstances are different in each individual's case. I know that."
show charles worried
c "I'm just worried about him."
c "Knowing Vincent, he'll never talk about himself."
c "Which is okay with me, if that's what he wants."
c "But if I keep ignoring this, what if he...what if..."

scene bg childrenlaughing
with dissolve
narrator2 "I think of running on the field. Children are laughing, illuminated by sun."

x "“People like that don't live long.”"

scene bg cafe
with dissolve
show charles worried2 at right
c "..."
show anri disbelief2 at left
h "Fine. I get it."
show anri sympathetic
h "Talk to him when you get the chance, okay?"
show charles neutral
h "I'm sure you two will figure something out."

scene bg black

narrator2 "I walk Anri home and wave her goodbye."
narrator2 "When I see Vincent next time, what should I tell him?"
narrator2 "No matter what I'll say, I find myself afraid of hearing his answer."


# [College] Graduation

scene 30
with dissolve
$ renpy.pause(3.0)
scene bg schoolgrad
with dissolve

narrator2 "The graduation day finally comes. Time sure flies."

show anri3 smile at left
h "Charlie! Over here!"
show charles3 squint at right
c "Who...?"
show anri3 annoyed
h "Hello-o, do you really not recognize me?"
show charles3 smile2
c "I think you just aged by nine years—"
with vpunch
show charles3 smile3
c "OW! Okay, okay, seven—"
with hpunch
c "Please stop kicking me, miss Warhol."
show anri3 smile
h "I know I look good. You do, too."
show charles3 troubled
c "I look like my father."
show anri3 neutral
h "And you hate it?"
show charles3 lookaway
c "I don't know anymore."
c "All that matters is that Mother is doing better."

show charles3 neutral
narrator2 "Anri pats my head."
show anri3 smile
h "Okay. Try to have fun today."
show charles3 smile
c "Thanks. You too."
hide charles3 smile
hide anri3 smile

scene bg corridor
with dissolve

narrator2 "I look for Vincent in the crowd."
narrator2 "He's talking to one of our teachers, all smiles, as usual."
narrator2 "I join in as his shadow."

show vincent2 smile2 at left
v "Eyler."
v "You look different."
show charles3 neutral at right
c "You look tired."
show vincent2 smile3
v "Haha! Do I?"
v "Well, I suppose I'm not really fond of long ceremonies."
show vincent2 smile
v "Is miss Warhol not with you?"
show charles3 smile
c "She's participating in a photoshoot with other girls."
show charles3 smile2
c "I ran away as soon as I saw the camera."

narrator2 "Vincent laughs, visibly amused."
c "And, it's too stuffy in this suit."
show vincent2 smile2
v "I have to agree."
v "But, there's nothing much we can do about it, right?"
show charles3 smile2
c "Yeah. I just want it to be over soon."

scene bg banquet
with dissolve

narrator2 "By the time we get to the rented conference hall, it's already evening."

narrator2 "The banquet doesn't interest me, but I already paid for it, so I stuff myself full with random appetizers."
narrator2 "Vincent's dissecting a steamed carrot with a precision of a surgeon at a nearby table."
narrator2 "He seems bored."
narrator2 "The moment I decide to approach him, he's engaging in a conversation with someone else."
narrator2 "Too bad."

narrator2 "I decide to look for Anri, and find her surrounded by girls on a floor below."
narrator2 "She looks like she's having fun, so I leave her to it."

narrator2 "It dawns at me that out of all the people in class, I only managed to become somewhat friendly with two."
narrator2 "With the rest, I don't really have anything to talk about."
narrator2 "Unless it's homework."
narrator2 "Maybe it's for the best if we forget each other's names after we all go separate ways."

narrator2 "In a corner of my eye, I see Vincent leaving the hall."

show charles3 neutral at right
c "You're leaving?"
show vincent2 smile at left
v "Just taking a walk outside."
v "It's a bit noisy in here."
c "Oh. Alright."

narrator2 "It doesn't look like he's going to come back."

show charles3 smile2
c "See you later, then."
show vincent2 smile2
v "See you."
hide charles3 smile2
hide vincent2 smile2

narrator2 "{i}Crap, his coat is still here.{/i}"

scene bg outsidegrad
with wiperight

narrator2 "When I run out of the building, Vincent is nowhere to be seen."
narrator2 "I jog a bit to the main road until I spot the familiar silhouette."
show chase1 at appearbottomleft
with dissolve
show chase2 at appearright
with dissolve
c "Fennell! Wait. Your coat..."
hide chase1
hide chase2

show vincent2 smile2 at left
v "Ah, thank you. You needn't have run."
v "I would've come back for it later."

show charles3 squint at right
c "..."
show charles3 lookaway
c "It didn't seem like it."

narrator2 "Vincent covers his mouth with his hand, hiding the surfacing emotion."

show vincent2 smile3
v "Haha, is that so?"

c "..."
show charles3 lookdown2
c "Mind if I walk with you for a bit?"

show vincent2 neutral
v "..."

show vincent2 smile2
v "Sure."
hide charles3 lookdown2
hide vincent2 smile2

narrator2 "We walk in silence."
narrator2 "There's too much on my mind, but I can't put any of it into words."

narrator2 "Somehow we ditched the prom night without really planning to."
narrator2 "I don't think anybody's going to look for me today, anyway."

scene bg oldtown2
with dissolve

narrator2 "We reach a viewpoint on the hill."
narrator2 "It's the highest platform in the Old Town."
narrator2 "Vincent is panting lightly, exhausted from climbing the stairs."

show vincentexcited at appearbottomleft
v "It's pretty high up here, isn't it?"
show charles sick at appeartopright
c "I'm not fond of high places."

narrator2 "It feels all too familiar for some reason. I feel sick."

v "I like them, though. Even the air here feels clearer."

narrator2 "Vincent leans over the fence, and inhales the night air."

v "Being above everything."
v "Leaving all the noise and commotion down below."
v "Don't you feel the same?"
c "...no."
c "I feel like I could fall down any second."
v "Mm. I see."
hide charles sick
hide vincentexcited
show vincent notice at appearbottomleft
v "Oh...Are you alright?"
narrator2 "I crouch down, my head spinning."
narrator2 "I'm not alright. "
narrator2 "It's like we've been here before."
narrator2 "Yet, it's not the same."

show charlesterrified at appeartopright
c "..."
c "You..."
c "You never talk about anything that really matters, do you?"
c "Always all smiles and big talk."
c "Talking, talking, talking, yet nothing you say has real weight to it."
c "I'm sick of your smiling face."

v "What—"
hide vincent notice
pause 0.5
show vincent smile at appearbottomleft
with dissolve
v "Ah. I see."
v "Should I say what you want to hear, then?"
v "Or agree with everything you say, like you always do?"
narrator2 "{i}Ack.{/i}"
c "My personality has nothing to do with this."
v "Does it?"
v "I'm led to believe that you're as much of a control freak as I am."
v "No matter how much others worry about you, you decide to shoulder everything on your own."

narrator2 "{i}That's because of how my Mother is{/i}."
hide charlesterrified
pause 0.2
show charles angry at appearright
with dissolve
c "That's because I don't want to be a burden!"
c "But for you, it's all about your image."
v "But if I asked for help, who would provide it?"
v "You?"
show charles sick
with dissolve
c "At very least I'd listen to what you have to say."
c "You just don't trust me enough."
c "You don't trust {i}anyone{/i}."

narrator2 "Vincent's eyes gleam with ice."

v "The only one who sees a problem in it is you, Eyler."
v "You're not the solution to my problems."
v "Neither am I to yours, even though you seem to think otherwise."

narrator2 "Needles and knives."
narrator2 "His words pierce through, but I don't falter."

c "...I know."
c "Yet, I want to understand you."
c "It's not your fault that I don't."
c "You're someone I've always looked up to."
c "You could do things I couldn't and find the right words to influence others."
c "It always felt like your opinion mattered."

narrator2 "I crouch down and face the ground, suddenly flustered."
pause 0.2
show charles earnest at appeartopright4
with dissolve
c "I..."
c "I thought I wouldn't mind losing my individuality if it'd mean getting influenced by yours."

narrator2 "Vincent's gaze becomes absent-minded."

hide vincent smile
show vincentgaze at appearbottomleft
with dissolve
v "I'm a bit envious. I have no one like that."
v "There's only myself. Always have been."
v "I have no role model, and have a hard time finding a reflection of myself in other people."
v "It's like standing on the other side of a one-way mirror."
v "But, I don't think of others as inferior to myself."
v "In fact, I like people a lot."
v "That's why I try to show it with appropriate words."
v "Language passwords. Just like we discussed once, remember?"
v "“{i}Friend{/i}”, “{i}soulmate{/i}”, “{i}partner{/i}”...these are all very easy to say."
v "The only difference is that while they have a meaning to others, these words sound empty to me."
v "I've never felt close to anyone."
v "The kind, understanding Vincent Fennell didn't exist until I created him."

scene bg black
with dissolve
narrator2 "I remember Vincent in the kindergarten."
narrator2 "Emotionally dead kid gathering crowds around him with useless trinkets from popular shows."
narrator2 "The only time he ever showed emotion was when he tore off wings from those ants, claiming to be in control."

narrator2 "Control."

narrator2 "Is that what it's all about?"

scene bg oldtown
show charles3 squint at right
c "You...claim that you don't mean things you say."
c "That your personality is fabricated."
c "I don't think you're being entirely honest."
show vincent2 neutral at left
v "..."
show vincent2 smile3
v "You're right."
v "I don't mean it, either."

narrator2 "{i}Argh, he's insufferable{/i}."

show charles3 troubled
c "You—"
hide charles3 troubled
hide vincent2 smile3

narrator2 "However, Vincent isn't looking at me."
narrator2 "His mind is elsewhere."

show vincent hopeless1 at appearbottomleft
v "It's like there's a wall between myself and the rest."
v "Ever since my childhood."
v "I've been trying to break through it by trying to be someone I'm not."
v "Yet, it's meaningless."
v "Even if I make it seem like he exists, I can't become him."
v "Deep inside, I must be the same child who laughed at the ants whose wings he tore off."
show vincent hopeless2
v "...Just because it was the only time when he felt like he was in control over someone's life."
v "Because he lacked control over his own."
hide vincent

show charles3 squint at right
c "..."
c "Still..."
show charles3 troubled
c "You've been trying your best, haven't you?"
c "All this talk about “a quiet place”, those bruises..."
v "..."
show charles3 lookaway
c "I think it's pretty obvious at this point that whoever you live with, they've been..."
narrator2 "I stumble on my own words."
c "...They haven't been treating you well."
show charles3 troubled
c "The Vincent I remember was an empty husk of a person."
c "It's like you were never physically there at all."
c "Yet, with time, you were able to regain control over your life."
c "It's not like you became someone whom others look up to overnight."
c "You worked hard for it."
show charles3 squint
c "Because you care."
show vincent2 blank at left
v "..."
v "That's just a life narrative you constructed for me."
v "It's nothing that pretty."
v "I can't be proud of being a hypocrite."
show charles3 lookaway
c "Would you rather dissociate for the rest of your life?"
v "I don't want that, either."
show vincent2 smile
v "Both choices are wrong."

hide vincent2 smile
hide charles3 lookaway

show death at center
v "There's just no hope for me, is there?"
c "...!"
hide death
pause 0.3
show confession at appearright
with dissolve
v "This life..."
v "I already tried to put an end to it."
v "A month ago."
show charles shock at appearleft
with dissolve
narrator2 "{i}Huh...?{/i}"
v "I didn't think much of it."
v "It was something I knew would happen one day or another."
v "Naturally."
v "Yet, I ended up not going all the way."
v "I thought, “Ah, I still haven't returned the notebook.”"
v "I was supposed to put an end to everything."
v "For a ridiculous reason like that, I didn't."
hide charles shock
hide confession
narrator2 "My eyes begin to sting, but no tears come out."

show charlesbreakdown1 at appearleft1
with dissolve
c "I..."
c "I may be insignificant and frankly boring..."
c "But I'm going to do my best to become someone you can consider your equal."

narrator2 "{i}So that you won't feel so alone.{/i}"

show charlesbreakdown2 at appearright1
with dissolve
c "I'll keep doing my best, so..."
c "So you...so I..."

hide charlesbreakdown2
hide charlesbreakdown1

narrator2 "In a corner of my eye I see Vincent crouching down near me. Putting a hand on my shoulder."
narrator2 "“{i}Don't push yourself{/i},” he says, his gaze remaining frozen. “{i}You're already doing enough.{/i}”"
narrator2 "Empty words and template phrases."
narrator2 "Neither of us can find comfort in each other's words."
narrator2 "Neither of us know what to do."

c "“{i}I want you to live{/i},” I croak out, not to a corpse, not to an imaginary construct, not to a vacant shell, but to Vincent Fennell himself."
narrator2 "History repeats."
narrator2 "I can't see his face."

pause 1

narrator2 "“{i}I see{/i},” Vincent says simply."
narrator2 "No tears, no surprises."
narrator2 "That's how Vincent Fennell is."
narrator2 "Yet, his words sounded almost thankful."

narrator2 "Vincent gets up and extends his hand to me."

show graduation
with dissolve
v "Congratulations on graduating, Charles."

show graduation2
narrator2 "I reach out, and accept his hand."
pause 0.5
narrator2 "{i}The future still remains uncertain.{/i}"
narrator2 "{i}Yet, I feel like I'll be able to fall sleep tonight.{/i}"

scene bg white
with dissolve

narrator2 "The sun rises."
pause 0.5
narrator2 "A new day has come."

pause 1
scene theend
with dissolve
$ renpy.pause(5.0)

scene credits1
with dissolve
$ renpy.pause(5.0)

scene credits2
with dissolve
$ renpy.pause(5.0)

scene credits3
with dissolve
$ renpy.pause(5.0)

scene credits4
with dissolve
$ renpy.pause(5.0)


return
