import discord
import requests
import json
import random
import os
from discord import app_commands
from discord.ext import commands
from discord.ui import View,Button
from threading import Timer
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="?")
def get_question(local_list, repeat_list, api_func):
    num = random.randint(0, 1)
    if num == 0:
        # Use local list
        if not local_list: 
            print(f"Refilling {local_list.__name__} from repeats...")
            local_list.extend(repeat_list)  # Refill
            repeat_list.clear()             # Clear repeats

        if not local_list: # If still empty (e.g., first run and no repeats)
              return "Oops, I ran out of questions! Please try another category."

        r1 = random.choice(local_list)
        repeat_list.append(r1)
        local_list.remove(r1)
    else:
        # Use API
        try:
            r1 = api_func()
        except Exception as e:
            print(f"API Error: {e}")
            r1 = "The API seems to be down. Try a local question."
    return r1
class GameButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Truth", style=discord.ButtonStyle.gray, custom_id="persistent_truth")
    async def truth_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        r1 = get_question(Truth, Repeat_Truth, get_truth)
        embed = discord.Embed(title=r1, color=0xe5deca)
        embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
        await interaction.response.send_message(embed=embed, view=self)

    @discord.ui.button(label="Dare", style=discord.ButtonStyle.gray, custom_id="persistent_dare")
    async def dare_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        r1 = get_question(Dare, Repeat_Dare, get_dare)
        embed = discord.Embed(title=r1, color=0xe5deca)
        embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
        await interaction.response.send_message(embed=embed, view=self)

    @discord.ui.button(label="Would You Rather", style=discord.ButtonStyle.gray, custom_id="persistent_wyr")
    async def wyr_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        r1 = get_question(Wyr, Repeat_Wyr, get_wyr)
        embed = discord.Embed(title=r1, color=0xe5deca)
        embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
        await interaction.response.send_message(embed=embed, view=self)

    @discord.ui.button(label="Most Likely", style=discord.ButtonStyle.gray, custom_id="persistent_ml")
    async def ml_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        r1 = get_question(MostLikely, Repeat_MostLikely, get_who)
        embed = discord.Embed(title=r1, color=0xe5deca)
        embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
        await interaction.response.send_message(embed=embed, view=self)

    @discord.ui.button(label="Never Have I Ever", style=discord.ButtonStyle.gray, custom_id="persistent_nhie")
    async def nhie_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        r1 = get_question(Nhie, Repeat_Nhie, get_nhie)
        embed = discord.Embed(title=r1, color=0xe5deca)
        embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
        await interaction.response.send_message(embed=embed, view=self)


MostLikely = [
    "Who is most likely to win an Oscar Award? ",
    "Who is most likely to break some world record?"," Who is most likely to invent something useful?","Who is most likely to be on a commercial?",
    "Who is most likely to become the President of the United States of America?",
    "Who is most likely to write a best seller?",
    "Who is most likely to cause a world war?",
    "Who is most likely not to take a shower for a week?",
    "Who is most likely to move to a different country?",
"Who would make the best couple here?",
    "Who is most likely to make a million dollars?",
    "Who is most likely to become the kindest person in the world?",
    "Who is most likely to have been the first to kiss a guy/a girl?",
    "Who is most likely to appear on some reality show?",
    "Who is most likely to take care of the others when they are sick?",
    "Who is most likely to make some change?",
    "Who is most likely to laugh at the wrong moment?","Who is most likely to cry in a public place?",
    "Who is most likely to do plastic surgery?","Who is most likely to marry without love?",
    "Who is most likely to live in a zoo?",
    "Who is most likely to read every book in a school library?",
    "Who is most likely to abandon a social gathering for no reason?",
    "Who is most likely to successfully get away with murder?",
    "In a horror movie, who would likely die first?",
    "In a horror movie, who would likely die last?",
    "In a horror movie, who would likely be the killer?",
    "Who is most likely to fart and blame it on someone else?",
    "Who is most likely to eat food off the floor?",
    "Who is most likely to end up in a psychiatric hospital?",
    "Who is most likely to be in an open relationship?",
    "Who is most likely to have a tough exterior but be very sensitive?",
    "Who is most likely to become a stripper?",
    "Who is most likely to be the most sarcastic?",
    "Whose joke is most likely to be taken seriously?",
    "Who is most likely to be disappointed over something stupid?",
    "Who is most likely to turn on a friend?",
    "Who is least likely to turn on a friend?",
    "Who is most likely to appear really rude?",
    "Who is most likely to ditch their friends last minute?",
    "Who is most likely to be inherently evil?",
    "Who is most likely to be a psychopath?",
    "Who is most likely to join a secret cult?",
    "Who is most likely to disappear randomly?",
    "Who is most likely to be a sadist?",
    "Who is most likely to have a secret fetish?",
    "Who is most likely to have a child the earliest?",
    "Who is most likely to spend all their money?",
    "Who is most likely to have the highest body count?",
    "Who is most likely the best punster?",
    "Who is most likely to end up in a toxic relationship?",
    "Who is most likely to be the best liar?",
    "Who is most likely to be the worst liar?",
    "Who would most likely live the longest?",
    "Who is most likely to smoke weed?",
    "Who is most likely to end up on the streets?",
    "Who is most likely to be a heartbreaker?",
    "Who is most likely to get killed because of something stupid?",
    "Who is most likely the best at sports?",
    "Who is most likely to lose their temper?",
    "Who is most likely to fall asleep in class?",
    "Who is most likely to be teacher's pet?",
    "Who is most likely to be a supermodel?",
    "Who is most likely to look the most different in 10 years?",
    "Who is most likely to fart and blame it on someone else?",
    "Who is most likely to fit the nerd stereotype?",
    "Who is most likely to fit the 'popular' stereotype?",
    "Who is most likely to fit the 'bad boy/girl stereotype'?",
    "Who is the most intimidating?",
    "Who is most likely to be the loner?",
    "Who is most likely to be the life of the party?",
    "Who is most likely to be the kindest person in the world?",
    "Who would most likely cast in Mean Girls?",
    "Who is most likely to forget important birthdays?",
    "Who is most likely to remember important birthdays?",
    "Who is most likely to be on a dating show?",
    "Who is most likely to steal candy from a kid?",
    "Who is most likely to kidnap children?","Who is most likely to have a snappy comeback?",
"Who is most likely to answer the phone if you call in the middle of a night?",
"Who is most likely to treat your house like their house?",
"Who is most likely to get along better with your parents than you do?",
"Who is most likely to have a crush on your sibling?",
"Who is most likely to throw you a surprise party?",
"Who is most likely to have the best snacks?",
"Who is most likely to drive you somewhere?",
"Who is most likely to say something awkward to a significant other’s parents?",
"Who is most likely to save you from a bad blind date?",
"Who is most likely to hand-make you a birthday present?",
"Who is most likely to try to embarrass you in front of your crush?",
"Who is most likely to make you laugh when you are sad?",
"Who is most likely to take care of you when you are sick?",
"Who is most likely to bake you a birthday cake?",
"Who is most likely to back you up in an argument, even if you are wrong?",
"Who is most likely to give you a nickname?",
"Who is most likely to be the life of the party?",
"Who is most likely to get into shenanigans?",
"Who is most likely to forget to text back?",
"Who is most likely to text back immediately?",
"Who is most likely to forget to return a borrowed item?",
  "Who here are you most intimidated by?",
  "Who is most likely to beat you in an argument?",
  "Who is most likely to mishear the lyrics to a rap song?",
"Who is most likely to make the ideal partner?",
"Who here is marriage material?",
"Who is most likely to serve enemies to lovers trope?",
"Who would you like to see getting married here?",
"Who here is the most attractive?",
"Whose personality do you like the most?",
"Who here would make the best idol?",
"Who is the baby of the group?",
"Who would make the best kids?",
"Who is most likely to get blocked by a celebrity on Twitter?",
"Who is most likely to own a unicorn onesie?",
"Who is most likely to buy scratch off lottery tickets?",
"Who is most likely to be allergic to cashews?",
"Who is most likely to know every word to We Didn’t Start the Fire?",
"Who is most likely to be mistaken for Brad Pitt?",
"Who is most likely to cry at animal adoption commercials?",
"Who is most likely to know how to perform a magic trick?",
"Who is most likely to eat pizza for breakfast?",
"Who is most likely to leave only a handful of cereal in the box?",
"Who is most likely to forget their wallet in a McDonalds?",
"Who is most likely to talk in the movie theater during a movie?",
"Who is most likely to wind up in the ER after getting a papercut?",
"Who is most likely to appear in a music video?",
"Who is most likely to go to Disneyland on every vacation?",
"Who is most likely to backpack across Thailand?",
"Who is most likely to mispronounce the word acai?",
"Who is most likely to be a bitcoin billionaire, if only they could access that old hard drive?",
"Who is most likely to make a cameo in a soap opera?",
"Who is most likely to sneakily eat Doritos in bed?",
"Who is most likely to accidentally tell a customer, “I love you?”",
"Who is most likely to reply to your email within a minute?",
"Who is most likely to forget to mute the microphone during Zoom calls?",
"Who is most likely to teach you a new skill?",
"Who is most likely to calm down an upset client?",
"Who is most likely to bring their dog to the office?",
"Who is most likely to invent a smart new office system?",
"Who is most likely to give the perfect interview?",
"Who is most likely to have forty tabs open at once?",
"Who is most likely to create an app?",
"Who is most likely to have a side hustle?",
"Who is most likely to get a good review from a customer?",
"Who is most likely to have a million dollar idea?",
"Who is most likely to have your back?",
"Who is most likely to nail a presentation?",
"Who is most likely to close a tricky sale?",
"Who is most likely to troubleshoot a tech issue?",
"Who is most likely to start an office pizza pool?",
"Who is most likely to plan a team outing?",
"Who is most likely to be the boss one day?",
"Who is most likely to impulse buy an inflatable dinosaur suit?",
"Who is most likely to argue with their pet?",
"Who is most likely to fake their birthday at a restaurant for free cake?",
"Who is most likely to scream in the middle of a horror movie?",
"Who is most likely to randomly burst out into song?",
"Who is most likely to cheat at a board game?",
"Who is most likely to be a spy?",
"Who is most likely to secretly be three ducks in a trench coat?",
"Who is most likely to be a ninja?",
"Who is most likely to be a secret superhero?",
"Who is most likely to become a meme?",
"Who is most likely to have an evil twin?",
"Who is most likely to faceplant in front of a crowd?",
"Who is most likely to get insulted by a child?",
"Who is most likely to pick their nose when they think nobody is watching?",
"Who is most likely to have a hidden candy stash?",
"Who is most likely to crash a wedding?",
"Who is most likely to be afraid of clowns?",
"Who is most likely to date a celebrity?",
"Who is most likely to hide a zombie bite?",
"Who is most likely to throw a wedding for their dogs?",
"Who is most likely to wear a speedo?",
"Who is most likely to own a pair of mom jeans?",
"Who is most likely to make you laugh?",
"Who is most likely to make you smile?",
"Who is most likely to help you solve an issue?",
"Who is most likely to make you forget your problems?",
"Who is most likely to be a role model for the group?",
"Who is most likely to always take the time to listen?",
"Who is most likely to be a great leader?",
"Who is most likely to save the day?",
"Who is most likely to give you a compliment behind your back?",
"Who is most likely to inspire you?",
"Who is most likely to bring out your best self?",
"Who is most likely to earn a place in history?",
"Who is most likely to show up for moral support?",
"Who is most likely to give you a compliment?",
"Who is most likely to pick out the perfect present?",
"Who is most likely to help a stranger?",
"Who is most likely to make new friends wherever they go?",
"Who is most likely to win a Nobel prize?",
"Who is most likely to change the world?",
"Who is most likely to adopt a rescue pet?",
"Who is most likely to write a bestselling book?",
"Who is most likely to break a world record?",
"Who is most likely to tutor you?",
"Who is most likely to ask a question right before class ends?",
"Who is most likely to loan you a pencil?",
"Who is most likely to do voices when reading out loud?",
"Who is most likely to fall asleep in class?",
"Who is most likely to get a little too competitive in gym class?",
"Who is most likely to snack in class?",
"Who is most likely to panic about failing and then receive an A?",
"Who is most likely to be valedictorian?",
"Who is most likely to play a prank on the teacher?",
"Who is most likely to wait until the last minute to do a project and still get an A?",
"Who is most likely to have a glamorous yearbook photo?",
"Who is most likely to have an awkward yearbook photo?",
"Who is most likely to have a messy desk or locker?",
"Who is most likely to succeed after graduation?",
"Who is most likely to win a big game?",
"Who is most likely to become a teacher one day?",
"Who is most likely to be able to solve multi-digit multiplication problems in their head?",
"Who is most likely to steal a scene in the play?",
"Who is most likely to be an entertaining mascot?",
"Who is most likely to win prom king or prom queen?",
"Who is most likely to recognize you ten years from now?",
"Who is most likely to wear a crazy outfit to prom?",
"Who is most likely to become a CEO at a top company?",
"Who is most likely to have the most children?",
"Who is most likely to run a marathon?",
"Who is most likely to be late for her own wedding?",
"Who is most likely to become a reality TV star?",
"Who is most likely to win a Grammy?",
"Who is most likely to call in sick at work but really be at the beach?",
"Who is most likely to get the most tattoos?",
"Who is most likely to break a world record?",
"Who is most likely to land on the New York Times bestsellers list?",
"Who is most likely to become president?",
"Who is most likely to have sex in public?",
"Who is most likely to become a social media influencer?",
"Who is most likely to spend all weekend binging a new TV series?",
"Who is most likely to never have kids?",
"Who is most likely to meet their S.O. at the gym?",
"Who is most likely to be on the red carpet one day?",
"Who is most likely to live the longest?",
"Who is most likely to adopt the #vanlife lifestyle?",
"Who is most likely to take all their secrets to the grave?",
"Who is most likely to be a member of the local art museum?",
"Who is most likely to own her own farm in the country?",
"Who is most likely to be the first to get married?",
"Who is most likely to accidentally find a portal to another dimension?",
"Who is most likely to cry during a sad movie?",
"Who is most likely to get rid of their smartphone and go back to using a flip phone?",
"Who is most likely to have visited the largest number of countries?",
"Who is most likely to be in the Olympics?",
"Who is most likely to become a millionaire?",
"Who is most likely to move to a foreign country?",
"Who is most likely to show up on your doorstep with soup when you're sick?",
"Who is most likely to not forget your birthday?",
"Who is most likely to be the first one up in the morning on a girls' trip?",
"Who is most likely to become a stand-up comedian?",
"Who is most likely to go for all-you-can-drink mimosas at brunch?",
"Who is most likely to order takeout when they already have leftovers in the fridge?",
"Who is most likely to get a speeding ticket on a road trip?",
"Who is most likely to know exactly what to say when you're feeling sad?",
"Who is most likely to hike the Appalachian Trail?",
"Who is most likely to get married in Vegas?",
"Who is most likely to win a game show?",
"Who is most likely to make it as a contestant on a national talent show?",
"Who is most likely to injure themselves while doing chores in their apartment?",
"Who is most likely to have a new hairstyle the next time you see them?",
"Who is most likely to die first in a scary movie?",
"Who is most likely to go skinny dipping?",
"Who is most likely to actually be a spy?",
"Who is most likely to renovate their entire house?",
"Who is most likely to give all their money to charity?",
"Who is most likely to sneak into the movies?",
"Who is most likely to become a teacher at their high school?",
"Who is most likely to be late for brunch because she stopped to pet a dog?",
"Who is most likely to finish a pint of ice cream in one sitting?",
"Who is most likely to buy more underwear instead of doing laundry?",
"Who is most likely to lead a protest?",
"Who is most likely to lock themselves out of their place?",
"Who is most likely to snore?",
"Who is most likely to know about the hot new restaurant before everyone else?",
"Who is most likely to have a fling while on vacation?",
"Who is most likely to be the first one out on the dance floor?",
"Who is most likely to always have the best snacks?",
"Who is most likely to save you from a bad first date?",
"Who is most likely to DIY something instead of buying it?",
"Who is most likely to eat pizza for breakfast?",
"Who is most likely to tell the waiter it's their birthday for free cake?",
"Who is most likely to make new friends whenever they're out?",
"Who is most likely to adopt their next pet?",
"Who is most likely to spend their Saturday morning volunteering?",
"Who is most likely to be written about in future history books?",
"Who is most likely to win the lottery?",
"Who is most likely to be late for dinner?",
"Who is most likely to be the first to sign up for karaoke?",
"Who is most likely to forget to text back?",
"Who is most likely to text 'on my way' when they're still getting ready?",
"Who is most likely to buy a motorcycle?"

]
Nhie = [
  "Never have I ever cheated on a partner.",
  "Never have I ever cheated on a test.",
  "Never have I ever been hungover.",
  "Never have I ever ghosted someone.",
  "Never have I ever kissed my best friend.",
  "Never have I ever farted in front of guests.",
  "Never have I ever had a crush on a friend's sibling.",
  "Never have I ever broken a bone.",
  "Never have I ever ignored a close friend on purpose.",
  "Never have I ever avoided someone when they really needed me.",
  "Never have I ever lied when I said 'I love you'.",
  "Never have I ever snooped through someone's phone when they weren't around.",
  "Never have I ever liked a friend's ex.",
  "Never have I ever deleted a post because it didn't get enough likes.",
  "Never have I ever kissed more than one person in 24 hours.",
  "Never have I ever pretended to be sick to get out of school.",
  "Never have I ever stood up to a teacher.",
  "Never have I ever fantasised about someone off limits.",
  "Never have I ever read an entire book in a day.",
  "Never have I ever re-gifted a gift.",
  "Never have I ever unfollowed a friend on social media.",
  "Never have I ever lifted weights for a workout.",
  "Never have I ever regretted an apology.",
  "Never have I ever told a lie about my best friend.",
  "Never have I ever started or helped spread a rumour.",
  "Never have I ever gotten stitches.",
  "Never have I ever lied to my parents about where I was going.",
  "Never have I ever pretended to be asleep so I didn't need to help with something.",
  "Never have I ever worn the same workout clothes two days in a row.",
  "Never have I ever not studied for a test.",
  "Never have I ever failed a test.",
  "Never have I ever gotten into a physical fight.",
  "Never have I ever been called a player.",
  "Never have I ever smoked.",
  "Never have I ever laughed so hard I spat out my drink.",
  "Never have I ever used someone else's toothbrush.",
  "Never have I ever been sent to the principal's office.",
  "Never have I ever sang in public.",
  "Never have I ever played a musical instrument.",
  "Never have I ever texted or taken a call at the movies.",
  "Never have I ever convinced a friend to dump a partner.",
  "Never have I ever convinced a partner to dump a friend.",
  "Never have I ever called a partner the wrong name.",
  "Never have I ever gone vegan.",
  "Never have I ever had a lucid dream.",
  "Never have I ever held a grudge longer than a year.",
  "Never have I ever blabbed something I swore to secrecy.",
  "Never have I ever tried a fad diet.",
  "Never have I ever cut my own hair.",
  "Never have I ever been awake for 24 straight hours or more.",
  "Never have I ever accidentally said “I love you” to someone.",
  "Never have I ever snooped through a friend’s room, cabinets or property.",
  "Never have I ever worked with someone I couldn’t stand.",
  "Never have I ever sent nudes.",
  "Never have I ever received nudes.",
  "Never have I ever thought a cartoon character was hot.",
  "Never have I ever seen someone die.",
  "Never have I ever had a wardrobe malfunction.",
  "Never have I ever run for my life.",
  "Never have I ever tried to make an ex jealous.",
  "Never have I ever set a friend up on a date.",
  "Never have I ever hooked up with someone of the same sex or gender.",
  "Never have I ever danced in the rain.",
  "Never have I ever danced on a table.",
  "Never have I ever slept in my car.",
  "Never have I ever had a blistering sunburn.",
  "Never have I ever had food poisoning.",
  "Never have I ever purposely given someone bad advice.",
  "Never have I ever had surgery.",
  "Never have I ever thrown someone else a surprise party.",
  "Never have I ever gone commando.",
  "Never have I ever broken a bone.",
  "Never have I ever peed my pants as an adult.",
  "Never have I ever slid into a stranger’s DMs.",
  "Never have I ever slid into an ex’s DMs.",
  "Never have I ever been in a helicopter.",
  "Never have I ever second-guessed a relationship.",
  "Never have I ever had braces.",
  "Never have I ever had a cavity.",
  "Never have I ever hitchhiked.",
  "Never have I ever lied about my relationship status.",
  "Never have I ever fallen in love at first sight.",
  "Never have I ever thrown up in public.",
  "Never have I ever wished I had kids.",
  "Never have I ever seen something creepy while using public transportation.",
  "Never have I ever sent a sext to the wrong person.",
  "Never have I ever walked in on my parents.",
  "Never have I ever eaten an entire pizza alone.",
  "Never have I ever eaten an entire pack of Oreos in one sitting.",
  "Never have I ever witnessed a crime.",
  "Never have I ever ridden a horse.",
  "Never have I ever fainted.",
  "Never have I ever clogged a toilet.",
  "Never have I ever donated blood.",
  "Never have I ever lurked my partner’s ex on social media.",
  "Never have I ever filmed an intimate moment.",
  "Never have I ever dropped a baby.",
  "Never have I ever shared a news story without reading past the headline.",
  "Never have I ever beaten a video game.",
  "Never have I ever been the subject of a rumor that wasn’t true.",
  "Never have I ever spread a rumor I knew wasn’t true.",
  "Never have I ever cried at a party.",
  "Never have I ever cried in school.",
  "Never have I ever performed onstage.",
  "Never have I ever laughed at a funeral.",
  "Never have I ever given someone a fake phone number.",
  "Never have I ever left a mean YouTube comment.",
  "Never have I ever tried bodybuilding.",
  "Never have I ever shoplifted.",
  "Never have I ever gone more than three days without showering.",
  "Never have I ever went more than a day without brushing my teeth.",
  "Never have I ever blamed someone else for my mistake.",
  "Never have I ever taken credit for someone else’s work.",
  "Never have I ever lost my voice.",
  "Never have I ever stolen something.",
  "Never have I ever had a paranormal experience.",
  "Never have I ever lurked my ex on social media.",
  "Never have I ever lied on social media.",
  "Never have I ever eaten an entire hot pepper.",
  "Never have I ever prank called someone.",
  "Never have I ever lied during this game!",
  "Never have I ever laughed so hard that I peed my pants.",
"Never have I ever danced on a table.",
"Never have I ever cried at the gym.",
"Never have I ever read a blog post before an online recipe.",
"Never have I ever fallen asleep on public transit.",
"Never have I ever tripped while wearing high heels.",
"Never have I ever gone to the bathroom outside.",
"Never have I ever eaten a bug–accidentally or on purpose.",
"Never have I ever picked up a hitchhiker.",
"Never have I ever fed my dinner to the dog when no one was looking.",
"Never have I ever dug through the trash.",
"Never have I ever eaten something off the ground.",
"Never have I ever forgotten a family member’s birthday.",
"Never have I ever bet money I knew I would lose.",
"Never have I ever bumped into a glass door.",
"Never have I ever lost my keys when they were in my hand.",
"Never have I ever lost my phone when it was right in front of me.",
"Never have I ever flashed someone.",
"Never have I ever burped the letters of the alphabet.",
"Never have I ever eaten somebody else’s food.",
"Never have I ever learned a TikTok dance.",
"Never have I ever fallen on my face.",
"Never have I ever embarrassed myself on a date.",
"Never have I ever gone on more than one date in a day.",
"Never have I ever used a dating app.",
"Never have I ever clogged someone’s toilet.",
"Never have I ever picked a wedgie in public.",
"Never have I ever made a cringey social media post.",
"Never have I ever given me a horrible haircut.",
"Never have I ever accidentally set something on fire.",
"Never have I ever walked in on somebody.",
"Never have I ever done more than 100 miles per hour on the highway.",
"Never have I ever had something in my teeth all day long.",
"Never have I ever accidentally said a secret too loud.",
"Never have I ever said something embarrassing on speaker phone.",
"Never have I ever re-gifted a white elephant gift.",
"Never have I ever had a crush on a celebrity.",
"Never have I ever gone on a blind date.",
"Never have I ever faked being sick to go to school.",
"Never have I ever left school at lunchtime.",
"Never have I ever trespassed.",
"Never have I ever pulled an all-nighter.",
"Never have I ever cheated on a test.",
"Never have I ever ignored someone I saw in public.",
"Never have I ever snuck into a festival.",
"Never have I ever broken the law.",
"Never have I ever stolen anything.",
"Never have I ever been sick on my friend/someone else.",
"Never have I ever catfished someone online.",
"Never have I ever butt-dialed my parents.",
"Never have I ever had a crush on a friend’s sibling.",
"Never have I ever stalked an ex on social media.",
"Never have I ever used a fake ID.",
"Never have I ever pulled an all-nighter when I had school or work the next day.",
"Never have I ever had a crush on someone in this room.",
"Never have I ever gotten locked out of my house.",
"Never have I ever edited my selfies.",
"Never have I ever used someone else’s Netflix account."
"Never have I ever owned a video game console.",
"Never have I ever dropped my phone in the toilet.",
"Never have I ever Google searched my name.",
"Never have I ever lost my car keys.",
"Never have I ever used a pickup line.",
"Never have I ever thought a friend’s parent was attractive.",
"Never have I ever cheated on a boyfriend/girlfriend.",
"Never have I ever fake cried to get something I wanted.",
"Never have I ever pretended it was my birthday at a restaurant for free cake.",
"Never have I ever created a fake social media account.",
"Never have I ever written a love letter.",
"Never have I ever moved in with somebody too soon.",
"Never have I ever embarrassed myself in front of my partner.",
"Never have I ever dated someone for their looks.",
"Never have I ever said “I love you” and didn’t mean it.",
"Never have I ever forgotten my partner’s birthday.",
"Never have I ever disliked my partner’s parents.",
"Never have I ever fallen asleep on someone while watching a movie.",
"Never have I ever gone on a blind date.",
"Never have I ever wanted kids.",
"Never have I ever picked my nose.",
"Never have I ever broken someone’s heart.",
"Never have I ever lied to impress someone.",
"Never have I ever texted someone just to tell them I miss them.",
"Never have I ever wanted a cute morning text.",
"Never have I ever had a movie-style romance.",
"Never have I ever fallen in love at first sight.",
"Never have I ever smelled my partner’s clothes.",
"Never have I ever dated a coworker.",
"Never have I ever drunk-dialed someone.",
"Never have I ever flirted with a nurse.",
"Never have I ever watched 50 Shades of Grey.",
"Never have I ever given a massage.",
"Never have I ever lost a bet.",
"Never have I ever played “hooky” from work or school.",
"Never have I ever gotten lost in a foreign country.",
"Never have I ever gotten a tattoo.",
"Never have I ever shot a gun.",
"Never have I ever driven a brand new car.",
"Never have I ever broken up with someone.",
"Never have I ever been dumped.",
"Never have I ever accidentally used someone else’s toothbrush.",
"Never have I ever lived alone.",
"Never have I ever been on a yacht.",
"Never have I ever used a fake ID.",
"Never have I ever had to go to court.",
"Never have I ever lied to a boss.",
"Never have I ever won the lottery.",
"Never have I ever re-gifted a gift I didn’t like.",
"Never have I ever hit a curb.",
"Never have I ever sent a questionable text message.",
"Never have I ever drunk texted my ex.",
"Never have I ever pranked someone.",
"Never have I ever had a video go viral online.",
"Never have I ever slept outdoors.",
"Never have I ever gotten stopped by airport security.",
"Never have I ever wanted to be on a reality TV show.",
"Never have I ever lied about who I was with.",
"Never have I ever left someone on “read.”",
"Never have I ever lied about my age.",
"Never have I ever role played.",
"Never have I ever regretted something.",
"Never have I ever tried to get someone’s attention by doing something stupid.",
"Never have I ever thrown a surprise party.",
"Never have I ever believed in a haunted house.",
"Never have I ever played a slot machine.",
"Never have I ever wasted my money on something.",
"Never have I ever binge-watched a TV series.",
"Never have I ever stood someone up on a date.",
"Never have I ever ghosted someone.",
"Never have I ever spent more than $200 on one piece of clothing.",
"Never have I ever traveled to Europe.",
"Never have I ever tried a fad diet.",
"Never have I ever had a speeding ticket.",
"Never have I ever ghosted someone.",
"Never have I ever given a fake name or age.",
"Never have I ever been sick on a subway or public transport.",
"Never have I ever flown first class.",
"Never have I ever lied to someone in this room.",
"Never have I ever lied on a dating app.",
"Never have I ever drank a Manhattan.",
"Never have I ever smoked a cigarette.",
"Never have I ever fallen in love.",
"Never have I ever stood someone up on a date.",
"Never have I ever met someone famous.",
"Never have I ever snooped through somebody’s stuff.",
"Never have I ever gone multiple days without showering.",
"Never have I ever cussed at the wrong moment.",
"Never have I ever been thrown out of a bar or a club.",
"Never have I ever gone skinny dipping in a pool or ocean.",
"Never have I ever gone out with my friend’s ex.",
"Never have I ever said “I love you” and didn’t mean it.",
"Never have I ever pondered the meaning of my life.",
"Never have I ever regretted my career choice.",
"Never have I ever thought about running away to a deserted island.",
"Never have I ever reinvented my identity.",
"Never have I ever tried to be somebody I’m not.",
"Never have I ever traveled alone.",
"Never have I ever gotten lost in my thoughts.",
"Never have I ever wished I was famous.",
"Never have I ever learned a new language.",
"Never have I ever felt confused.",
"Never have I ever felt insecure about my body.",
"Never have I ever forgotten my birthday.",
"Never have I ever fallen out of love.",
"Never have I ever had a horrible nightmare.",
"Never have I ever dreamed of dating a celebrity.",
"Never have I ever wished I could do something over again.",
"Never have I ever wanted to go back in time.",
"Never have I ever helped a stranger.",
"Never have I ever questioned the purpose of my existence.",
"Never have I ever recorded myself crying.",
"Never have I ever left myself an encouraging voice memo.",
"Never have I ever said affirmations to make myself feel better.",
"Never have I ever eaten an entire pizza by myself.",
"Never have I ever been fascinated with somebody.",
"Never have I ever kissed a stranger.",
"Never have I ever romanticized my life.",
"Never have I ever written a poem.",
"Never have I ever received a love letter.",
"Never have I ever lost interest in something I used to love.",
"Never have I ever gotten bored of a relationship.",
"Never have I ever wanted to go skydiving.",
"Never have I ever felt afraid of the dark.",
"Never have I ever laughed so hard I couldn’t breathe.",
"Never have I ever snooped through my partner’s phone.",
"Never have I ever broken a promise.",
"Never have I ever fallen in love with a fictional character.",
"Never have I ever bullied somebody.",
"Never have I ever been bullied.",
"Never have I ever stayed on the phone for 5 hours straight.",
"Never have I ever thought I was going to drown in the ocean.",
"Never have I ever grabbed the wrong person’s hand in public.",
"Never have I ever mistaken somebody for my partner.",
"Never have I ever seen a ghost.",
"Never have I ever dreamed of somebody who passed away.",
"Never have I ever had a crush on two people at once.",
"Never have I ever wanted to change my gender.",
"Never have I ever thought somebody was shallow.",
"Never have I ever thought I was better than somebody else.",
"Never have I ever wished I was famous.",
"Never have I ever set a goal to make a million dollars.",
"Never have I ever had a spiritual awakening.",
"Never have I ever meditated for an hour straight.",
"Never have I ever believed in manifestation.",
"Never have I ever felt nervous in front of someone in this room."
]

Truth = [
  "When was the last time you lied?",
  "When was the last time you cried?",
  "What's your biggest fear?",
	"What's your biggest fantasy?",
	"Do you have any fetishes?",
	"What's something you're glad your mum doesn't know about you?",
	"Have you ever cheated on someone?",
	"What's the worst thing you've ever done?",
	"What's a secret you've never told anyone?",
	"Do you have a hidden talent?",
  "What is a big misconception about you?",
  "What is something you take pride in?",
	"Who was your first celebrity crush?",
	"What are your thoughts on polyamory?",
	"Have you ever cheated in an exam?",
	"What's the most drunk you've ever been?",
	"Have you ever done something you immediately regretted?",
  "What is something you are not proud of?",
	"What's the most embarrassing thing you've ever done?",
  "What's an embarrassing nickname you have been given to by someone?",
  "What's an embarrassing nickname someone has given to you?",
  "Have you ever fantasised about someone else while being in a relationship?",
  "What's something about you from the past that could have been a massive dealbreaker?",
  "What's something about you that you dislike?",
  "What are your real thoughts on the people you are playing this with?",
	"What's your biggest insecurity?",
	"What's the biggest mistake you've ever made?",
	"What's the most disgusting thing you've ever done?",
	"Who would you like to kiss in this room?",
	"What's the worst thing anyone's ever done to you?",
	"Have you ever had a run in with the law?",
  "What is more important to you? Looks or personality?",
	"What's your worst habit?",
  "What's your ideal type of person, if any?",
	"What's the worst thing you've ever said to anyone?",
  "What's something you have said in the heat of the moment that you regret?",
  "What's the worst thing you've ever been told?",
  "What's something you can proudly say is good about you?",
	"What's the strangest dream you've had?",
  "What's something you would do first if you had all the resources?",
	"Have you ever been caught doing something you shouldn't have?",
  "What are your thoughts on afterlife?",
	"What's your biggest regret?",
  "Would your past self be proud of the current you? Why?",
	"Why did your last relationship break down? (if any)",
	"Have you ever lied ditch someone?",
	"Have you ever led someone on?",
  "What's something about you that people rarely know?",
  "What’s the last lie you told?",
  "When was the last time you cried?",
  "When was the last time you made someone cry?",
  "Name someone you’ve pretended to like but actually couldn’t stand.",
  "What’s been your most physically painful experience?",
  "What bridges are you glad that you burned?",
  "If you met a genie, what would your three wishes be?",
  "What’s one thing you’d do if you knew there no consequences?",
  "What’s the craziest thing you’ve done in front of a mirror?",
  "What’s the meanest thing you’ve ever said about someone else?",
  "What’s something you love to do with your friends that you’d never do in front of your partner?",
  "Who are you most jealous of?",
  "What do your favorite pajamas look like?",
  "Meatloaf says he’d do anything for love, but he won’t do “that.” What’s your “that?”",
  "How many times a week do you wear the same pants?",
  "Would you date your high school crush today?",
  "Where are you ticklish?",
  "Do you believe in any superstitions? If so, which ones?",
  "What’s one movie you’re embarrassed to admit you enjoy?",
  "When’s the last time you apologized? What for?",
  "Have you ever considered cheating on a partner?",
  "Have you ever peed in a pool?",
  "What’s the weirdest place you’ve ever grown hair?",
  "If you were guaranteed to never get caught, who on Earth would you murder?",
  "What’s the cheapest gift you’ve ever gotten for someone else?",
  "What app do you waste the most time on?",
  "What is the youngest age partner you’d date?",
  "What is the oldest age partner you'd date?",
  "Have you ever picked your nose in public?",
  "Which of your family members annoys you the most and why?",
  "What is your greatest fear in a relationship?",
  "What’s your biggest pet peeve about the person you are playing this with?",
  "What’s the longest you’ve gone without brushing your teeth?",
  "Who would you hate to see naked?",
  "Would you break up with your partner for good for $1 million?",
  "Have you ever regretted something you did to get a crush or partner’s attention?",
  "Have you ever ghosted a friend?",
  "Have you ever ghosted a partner?",
  "If you switched genders for a day, what would you do?",
  "How many photo editing apps do you have on your phone?",
  "What’s the most childish thing you still do?",
  "If you had to pick someone in this room to be your partner on a game show, who would it be and why?",
  "What particular physical attribute could make you not want to date a person?",
  "What’s the most embarrassing music you listen to?",
"What’s one thing you love most about yourself?",
"Who is your secret crush?",
"Who is the last person you creeped on social media?",
"When was the last time you wet the bed?",
"What’s your biggest regret?",
"If you had to only ever watch rom coms or only watch scary movies for the rest of your life, which would you choose and why?",
"Where is the weirdest place you've ever gone to the bathroom?",
"Have you ever ghosted on someone?",
"Which player would survive a zombie apocalypse and which would be the first to go?",
"Reveal all the details of your first kiss.",
"What excuse have you used before to get out plans?",
"What's the longest you've ever slept?",
"What’s the shortest you’ve ever slept?",
"Read the last text you sent your best friend or significant other out loud.",
"What's your biggest pet peeve?",
"When was the last time you lied?",
"What five things would you bring to a deserted island?","Which is your favorite Hollywood Chris? Chris Evans, Chris Pratt, Chris Hemsworth or Chris Pine?",
"What's the most embarrassing thing you ever did on a date?",
"What is the boldest pickup line you've ever used?",
"What celebrity do you think you most look like?",
"How many selfies do you take a day?",
"What is one thing you would stand in line an hour for?",
"When was the last time you cried?",
"What's the longest time you've ever gone without showering?",
"What's the most embarrassing top-played song on your phone?",
"What was your favorite childhood show?",
"If you had to change your name, what would your new first name be?",
"If you could be a fictional character for a day, who would you choose?",
"If you could date a fictional character, who would it be?",
"What's your biggest fear?",
"What's one silly thing you can't live without?",
"Where was your favorite childhood vacation spot?",
"What is the weirdest trend you've ever participated in?",
"If you could only listen to one song for the rest of your life, what would you choose?",
"Who do you text the most?",
"Have you ever been fired from a job?",
"If you had to wear only flip flops or heels for the next 10 years, which would you choose?",
"What’s an instant deal breaker in a potential love interest?"
];
def get_truth():
  response=requests.get("https://api.truthordarebot.xyz/v1/truth")
  json_data=json.loads(response.text)
  truth=json_data.get('question')
  return truth
def get_dare():
  response=requests.get("https://api.truthordarebot.xyz/api/dare")
  json_data=json.loads(response.text)
  dare=json_data.get('question')
  return dare
def get_wyr():
  response=requests.get("https://api.truthordarebot.xyz/api/wyr")
  json_data=json.loads(response.text)
  wyr=json_data.get('question')
  return wyr
def get_who():
  response=requests.get("https://api.truthordarebot.xyz/api/paranoia")
  json_data=json.loads(response.text)
  who=json_data.get('question')
  return who
def get_nhie():
  response=requests.get("https://api.truthordarebot.xyz/api/nhie")
  json_data=json.loads(response.text)
  nhie=json_data.get('question')
  return nhie
Dare = [
  "Send names of five of the cutest people in your contact list. You have to ask them if they think you're cute.",
  "Send the last message with your partner.",
  "Send an audio of you singing Rick Roll.",
  "Send an audio of you doing a makeup tutorial voiceover.",
  "Send a screenshot of your phone history from the last 24 hours...",
  "Send an audio of you reading out a movie scene.",
  "Name one thing you like and dislike about the person (people) you are playing this with.",
  "Rate everyone according to personality on a 1-10 scale.",
  "Rate everyone according to looks on a 1-10 scale.",
  "Post a picture of a cow on your instagram story without caption.",
  "Post a poll on your Instagram between 'Become a fish' and 'Become a bird'.",
  "Text someone you know but text rarely 'I don't think I can stand you anymore.",
  "Show the newest and oldest picture on your phone gallery.",
  "Text the 4th person in your DMs 'I never liked you anyway'.",
  "Text someone you know 'LMFAOOOOOOOOOOOO' without context and don't respond.",
  "Send a random doge meme to the first 5 people in your messages and do not respond.",
  "Go on Facebook and change your relationship status every hour for the entire day.",
  "Text your best friend asking if they have enough toilet paper in their bathroom.",
  "Set your relationship status on Facebook as 'In a relationship' tagging a celebrity.",
  "Text your best friend 'I think I really might be gay/straight.'",
  "Draw a smiley face on your big toenail and send the picture of that toe to the last group chat you messaged in.",
  "Make up a hilarious story of your dream and post in on any social media for 24 hours.",
  "Message the top 5 people in your DMs that you have to tell them an important secret.",

]

TD = Truth + Dare

Wyr = [
  "Would you rather have the ability to see 10 minutes into the future or 150 years into the future?",
  "Would you rather have telekinesis (the ability to move things with your mind) or telepathy (the ability to read minds)?",
  "Would you rather team up with Wonder Woman or Captain Marvel?",
  "Would you rather be forced to sing along or dance to every single song you hear?",
  "Would you rather find true love today or win the lottery next year?",
  "Would you rather be in jail for five years or be in a coma for a decade?",
  "Would you rather have another 10 years with your partner or a one-night stand with your celebrity crush?",
  "Would you rather be chronically under-dressed or overdressed?",
  "Would you rather have everyone you know be able to read your thoughts or for everyone you know to have access to your Internet history?",
  "Would you rather lose your sight or your memories?",
  "Would you rather have universal respect or unlimited power?",
  "Would you rather give up air conditioning and heating for the rest of your life or give up the Internet for the rest of your life?",
  "Would you rather swim in a pool full of Nutella or a pool full of maple syrup?",
  "Would you rather labor under a hot sun or extreme cold?",
  "Would you rather stay in during a snow day or build a fort?",
  "Would you rather buy 10 things you don’t need every time you go shopping or always forget the one thing that you need when you go to the store?",
  "Would you rather never be able to go out during the day or never be able to go out at night?",
  "Would you rather have a personal maid or a personal chef?",
  "Would you rather have Beyoncé’s talent or Jay-Z‘s business acumen?",
  "Would you rather be 11 feet tall or nine inches tall?",
  "Would you rather date someone 4'5 or 6'11?",
  "Would you rather be an extra in an Oscar-winning movie or the lead in a box office bomb?",
  "Would you rather communicate only in emoji or never be able to text at all ever again?",
  "Would you rather be royalty 1,000 years ago or an average person 100 years into the future?",
  "Would you rather lounge by the pool or on the beach?",
  "Would you rather wear the same socks for a month or the same underwear for a week?",
  "Would you rather watch nothing but Hallmark Christmas movies or nothing but horror movies?",
  "Would you rather always be half an hour minutes late or always be an hour early?",
  "Would you rather commit a crime and live in fear of getting caught or be jailed for a crime you did not commit?",
  "Would you rather spend a week in the forest or a night in a real haunted house?",
  "Would you rather find a rat in your kitchen or a roach in your bed?",
  "Would you rather have a pause or a rewind button in your life?",
  "Would you rather always have a full phone battery or a full gas tank?",
  "Would you rather lose all your teeth or lose a day of your life every time you kissed someone?",
  "Would you rather drink from a toilet or pee in a litter box?",
  "Would you rather be forced to live the same day over and over again for a full year, or take 3 years off the end of your life?",
  "Would you rather never eat watermelon ever again or be forced to eat watermelon with every meal?",
  "Would you rather get a paper cut every time you turn a page or bite your tongue every time you eat?",
  "Would you rather oversleep every day for a week or not get any sleep at all for four days?",
  "Would you rather die in 20 years with no regrets or live to 100 with a lot of regrets?",
  "Would you rather get trapped in the middle of a food fight or a water balloon fight?",
  "Would you rather walk to work in heels or drive to work in reverse?",
  "Would you rather spend a year at war or a year in prison?",
  "Would you rather die before or after your partner?",
  "Would you rather have a child every year for 20 years or never have any children at all?",
  "Would you rather take amazing selfies but look terrible in all other photos or be photogenic everywhere but in your selfies?",
  "Would you rather be gassy on a first date or your wedding night?",
  "Would you rather be able to take back anything you say or hear any conversation that is about you?",
  "Would you rather have skin that changes color based on your emotions or tattoos appear all over your body depicting what you did yesterday?",
  "Would you rather hunt and butcher your own meat or never eat meat again?",
  "Would you rather lose all of your friends but keep your BFF or lose your BFF but keep the rest of your buds?",
  "Would you rather have people spread a terrible lie about you or have people spread terrible but true tales about you?",
  "Would you rather walk in on your parents or have them walk in on you?",
  "Would you rather be the absolute best at something that no one takes seriously or be average at something well respected?",
  "Would you rather have a third nipple or an extra toe?",
  "Would you rather have to wear every shirt inside out or every pair of pants backward?",
  "Would you rather win $25,000 or your best friend win $100,000?",
  "Would you rather be in history books for something terrible or be forgotten completely after you die?",
  "Would you rather travel the world for free for a year or have $50,000 to spend however you please?",
  "Would you rather go back to the past and meet your loved ones who passed away or go to the future to meet your children or grandchildren to be?",
  "Would you rather stay the age you are physically forever or stay the way you are now financially forever?",
  "Would you rather be alone all your life or surrounded by really annoying people?",
  "Would you rather give up your cellphone for a month or bathing for a month?",
  "Would you rather spend a day cleaning your worst enemy’s house or have your crush spend the day cleaning your house?",
  "Would you rather spend a year entirely alone or a year without a home?",
  "Would you rather have to buy all used underwear or all used toothbrushes?",
  "Would you rather have a photographic memory or an IQ of 200?",
  "Would you rather forget your partner’s birthday or your anniversary every year?",
  "Would you rather be beautiful and stupid or unattractive but a genius?",
  "Would you rather have seven fingers on each hand or seven toes on each foot?",
  "Would you rather have super-sensitive taste buds or super-sensitive hearing?",
  "Would you rather be always stuck in traffic but find a perfect parking spot or never hit traffic but always take forever to park?",
  "Would you rather ask your ex or a total stranger for a favor?",
  "Would you rather eat only pizza for a year or not eat any pizza for five years?",
  "Would you rather sleep in a doghouse or let stray dogs sleep in your bed?",
  "Would you rather be able to speak any language or be able to communicate with animals?",
  "Would you rather have all of your messages and photos leak publicly or never use a cellphone ever again?",
  "Would you rather run at 100 mph or fly at 20 mph?",
  "Would you rather have to wear sweatpants everywhere for the rest of your life or never wear sweatpants again?",
  "Would you rather have 10,000 spoons when all you need is a knife or always have a knife but never be able to use spoons?",
  "Would you rather detect every lie you hear or get away with every lie you tell?",
  "Would you rather be the funniest person in a room or the smartest person in a room?",
  "Would you rather people knew all the details of your finances or all the details of your love life?",
  "Would you rather listen to your least-favorite song on a loop for a year or never listen to any music at all for a year?",
  "Would you rather go vegan for a month or only eat meat and dairy for a month?",
  "Would you rather clean up someone else’s vomit or someone else’s blood?",
  "Would you rather end every phone call with “I love you” or accidentally call your partner the wrong name during a fight?",
  "Would you rather hear a comforting lie or an uncomfortable truth?",
  "Would you rather be locked for a week in a room that’s overly bright or a room that’s totally dark?",
  "Would you rather someone see all the photos in your phone or read all your text messages?",
  "Would you rather be half your height or double your weight?",

"Would you rather be the only person who speaks out of their butt or be the only person who doesn’t speak out of their butt?",

"Would you rather live with a barnyard of animals in your house or live in the barn with the animals?",

"Would you rather listen to one song for the rest of your life or never be allowed to listen to the same song twice?",

"Would you rather clean the same mess in the kitchen everyday or not be allowed to clean up the mess at all?",

"Would you rather chew your toenails off or someone else’s fingernails?",

"Would you rather have no one come to your wedding or your funeral?",

"Would you rather get rich in a way that disappoints your family or just make enough money to live?",

"Would you rather have no internet or no cell phone?",

"Would you rather go back in time to meet your ancestors or go into the future to meet your great-grandchildren?",

  "Would you rather get a tattoo or a lip piercing?",

"Would you rather be homeless or in prison?",

"Would you rather your friend or your boss falls in love with you?",

"Would you rather know the date of your death or the cause of your death?",

"Would you rather receive cleaning supplies or a weighing scale as a present?",

"Would you rather never brush your teeth or never brush your hair again (no shaving!)?",

"Would you rather tell your partner you’re having an affair or have them tell you they’re having an affair?",

  "Would you rather have front row tickets to a musician you’ve never heard of or listen to your favorite band perform from the parking lot?",

"Would you rather eat fast food everyday or never eat at any restaurant again?",

"Would you rather live in a new country every month or never go on vacation again?",

"Would you rather give birth to conjoined twins or to sextuplets?",

"Would you rather live somewhere it rains most days or somewhere it never rains ever?",

"Would you rather dumpster dive for food or ask customers outside a restaurant to buy you a meal?",

"Would you rather have hands for feet or feet for hands?",

"Would you rather kill a cow or butcher it afterwards?",

"Would you rather live in a mountain cabin with no human contact or a big city studio apartment with no personal space?",

"Would you rather read your mother’s teenage diary or read your teenage diary to your mother (if you didn’t keep a diary, just imagine what kind of embarrassing things you would have written)?",

"Would you rather go to an intimate birthday party for someone you don’t know or organize a huge party for a close friend?",

  "Would you rather get diarrhea on vacation or the day of a big presentation at work?",

"Would you rather celebrate your birthday every week or never celebrate your birthday again (but still age at the same rate)?",

"Would you rather move in with your elderly parents or hard partying roommates?",

"Would you rather eat animal brains or intestines?",

"Would you rather work cleaning up toxic waste or as a mortician’s assistant?",

"Would you rather eat mystery leftovers that have been in the fridge too long or a stranger’s leftovers that they left on their plate at a restaurant?",

"Would you rather walk to work in the snow everyday or in 40°C weather?",

"Would you rather wear a crass, sexually suggestive uniform to work or an extremely stuffy, uncomfortable uniform?",

"Would you rather your parents arrange your marriage or marry your most recent ex?",

"Would you rather tell your boss everything about your last night out on the town or tell your mom?",

"Would you rather have to cook the big holiday meal every year or clean up and do the dishes afterward?",

"Would you rather go to jail for a crime you didn’t commit or someone else go to jail for a crime you committed?",

  "Would you rather sniff butts like a dog when you meet someone new or eat dog food every night for dinner?",

"Would you rather watch the news or stoner movies for 24 hours straight?",

"Would you rather marry the most boring person you know or the most intense and demanding person you know?",

"Would you rather get caught looking at something “adult only” online by your parents or by your boss?",

"Would you rather punch a wall full force or get punched in the chest?",

"Would you rather eat nothing but salad or nothing but dessert for a week?",

  "Would you rather live right next to a huge stadium or the airport?",


"Would you rather go to a rave and stay till the last song or go to a bar and stay till last call?",

"Would you rather go on a silent nonspeaking retreat for a week or go on a long weekend vacation with someone who never shuts up?",

"Would you rather ride a skateboard or walk on your hands everywhere you went?",

"Would you rather swim with sharks or spend the night in a forest with mountain lions?",

  "Would you rather bounce off of every surface you touch or never be able to jump again?",

'Would you rather have taste buds covering your hands or not taste food and drink again?'

,"Would you rather have skin like sandpaper or skin like jelly?"

  'Would you rather make a beeping noise when you’re stressed or cry confetti when you’re sad?',

'Would you rather be allergic to animals or to your favourite foods?',

'Would you rather be a psychic that nobody believes or have superpowers that you can’t use properly?',

'Would you rather not be able to swim or not be able to run?',

'Would you rather become your favourite character or win the lottery?',

'Would you rather have a pet dragon that doesn’t understand you or a pet zebra that always listens?'

'Would you rather fight a mermaid or a polar bear?',

'Would you rather only be able to sleep for three hours a night or have to run a marathon each week with shoes that are too tight?',

'Would you rather turn into a dog every time you sneeze or a buffalo every time you hiccup?',

'Would you rather only be able to laugh at inappropriate times (and have to) or have to sing when someone claps?',

'Would you rather have your name constantly mispronounced or constantly forgotten?',

'Would you rather produce shocks when you went near technology or hear squelching noises when you’re trying to focus?',

'Would you rather only be able to eat food that began a B or an M?',

'Would you rather be followed everywhere by someone playing the flute or be surprised daily by someone playing a tuba?',

'Would you rather have a toaster for a head or a cactus for a spine?',

'Would you rather your drinks had the texture of porridge or only be able to drink your least favourite drink?',

'Would you rather belong to a family of strict bears or nonchalant hippos?',

'Would you rather have knives for toes or have spaghetti for body hair?',

'Would you rather have to ride a snail everywhere or have to wear rollerblades (with a wonky wheel) everywhere you go?'
]
Anything = Truth + Dare + MostLikely + Nhie + Wyr
Repeat_Truth = []
Repeat_Dare = []
Repeat_TD = []
Repeat_Nhie = []
Repeat_MostLikely = []
Repeat_Wyr = []
Repeat_Anything = []

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('party games <3'))
    
    # This is CRITICAL. It registers the persistent view class.
    bot.add_view(GameButtonView()) 

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# This command is unchanged
@bot.tree.command(description='Send a message anonymously through the bot.')
async def anon(interaction: discord.Interaction, message: str):
    await interaction.response.send_message("Your anonymous message has been sent!", ephemeral=True)
    
    embed = discord.Embed(
        title="Anonymous message",
        description=message,
        color=0xe5deca
    )
    await interaction.channel.send(embed=embed)

# This command is unchanged
@bot.tree.command(description='Provides a list of all commands with their functions.')
async def help(interaction):
    embed=discord.Embed(title="List of Commands", description="This is a list of all the commands you can give to the bot.", color=0xe5deca, url="https://discord.com/api/oauth2/authorize?client_id=891296558920925255&permissions=120832&scope=bot")
    embed.set_footer(text="Thank you for using Party Games Bot! To invite the bot to another server, you can click on the title URL.",icon_url="https://www.vhv.rs/dpng/d/418-4188276_transparent-tumblr-circle-png-transparent-png-tumblr-beige.png")
    embed.add_field(name="`help`", value="Sends a list of all commands.", inline=False)
    embed.add_field(name="`who`", value="Sends a who's most likely to question.", inline=False)
    embed.add_field(name="`nhie`", value="Sends a Never Have I ever question.", inline=False)
    embed.add_field(name="`truth`", value="Sends a truth question.", inline=False)
    embed.add_field(name="`dare`", value="Sends a dare.", inline=False)
    embed.add_field(name="`td`", value="Sends a truth or a dare.", inline=False)
    embed.add_field(name="`wyr`", value="Sends a Would You Rather question.", inline=False)
    embed.add_field(name="`rdm`", value="Sends a question from any random game.", inline=False)
    embed.add_field(name="`anon`", value="Respond to a question without revealing your identity.", inline=False)
    await interaction.response.send_message(embed=embed)

# All game commands are now simple: get a question, send the embed and view.
@bot.tree.command(description="Sends a 'Who's Most Likely To' question.")
async def who(interaction):
  r1 = get_question(MostLikely, Repeat_MostLikely, get_who)
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.",icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a 'Never Have I Ever' question.")
async def nhie(interaction):
  r1 = get_question(Nhie, Repeat_Nhie, get_nhie)
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a 'truth' question.")
async def truth(interaction):
  r1 = get_question(Truth, Repeat_Truth, get_truth)
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a dare.")
async def dare(interaction):
  r1 = get_question(Dare, Repeat_Dare, get_dare)
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a truth or a dare.")
async def td(interaction):
  # 50/50 chance for truth or dare
  if random.randint(0, 1) == 0:
      r1 = get_question(Truth, Repeat_Truth, get_truth)
  else:
      r1 = get_question(Dare, Repeat_Dare, get_dare)
      
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a random question from all available types of questions.")
async def rdm(interaction):
  # Pick one of the 5 game types at random
  num = random.randint(0, 4)
  if num == 0:
      r1 = get_question(Truth, Repeat_Truth, get_truth)
  elif num == 1:
      r1 = get_question(Dare, Repeat_Dare, get_dare)
  elif num == 2:
      r1 = get_question(Wyr, Repeat_Wyr, get_wyr)
  elif num == 3:
      r1 = get_question(MostLikely, Repeat_MostLikely, get_who)
  else: # num == 4
      r1 = get_question(Nhie, Repeat_Nhie, get_nhie)

  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

@bot.tree.command(description="Sends a 'Would You Rather' question.")
async def wyr(interaction):
  r1 = get_question(Wyr, Repeat_Wyr, get_wyr)
  embed=discord.Embed(title=r1, color=0xe5deca)
  embed.set_footer(text=f"Requested by {interaction.user.name}.", icon_url=f"{interaction.user.avatar}")
  await interaction.response.send_message(embed=embed, view=GameButtonView())

def read_token():
    with open("token.txt", "r") as f:
        lines=f.readlines()
        return lines[0].strip()
print("Starting bot...")
bot.run(os.getenv("TOKEN"))