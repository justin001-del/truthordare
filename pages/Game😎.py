import streamlit as st
import random
import pandas as pd
import time

from utils.bg import set_bg_from_local


set_bg_from_local("assets/image.jpeg")

with open("assets/style.css") as f:
    
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
# Inject CSS







if "picker" not in st.session_state:
    st.session_state["picker"]=False

if "how_many" not in st.session_state:
    st.session_state["how_many"]=1

if "players" not in st.session_state:
    st.session_state["players"]=[]

if "u" not in st.session_state:
    st.session_state["u"]=1

if "n" not in st.session_state:
    st.session_state["n"]=1

if "status" not in st.session_state:
    st.session_state["status"]=1

if "statuss" not in st.session_state:
    st.session_state["statuss"]=1

if "mood" not in st.session_state:
    st.session_state["mood"]=False



x=st.button("mild mode",key="mild")
    
y=st.button("pro mode",key="pro")



    
easy_dare=[
    "Speak in a fake accent for the next 3 rounds.",
    "Send a meme to your crush without context.",
    "Try to lick your elbow.",
    "Text someone “I know what you did.” No context.",
    "Wear socks on your hands for the next 10 minutes.",
    "Pretend you're a celebrity in an interview.",
    "Mimic your favorite teacher for 20 seconds.",
    "Talk in slow motion until your next turn.",
    "Tell a story using only emojis and sound effects.",
    "Act like your chair is trying to escape.",
    "Walk like a crab for 30 seconds.",
    "Put something random on your head and keep it there.",
    "Make a romantic speech to your water bottle.",

    "Attempt to dance like a chicken.",
    "Pretend your phone is a baby and rock it to sleep.",
    "Yell 'I love bugs!' out loud right now.",
    "Take a selfie making the weirdest face possible.",
    "Imitate a robot for 30 seconds.",
    " Act like your shoe is a phone.",
    "Walk like a model across the room.",
    "Pretend you're being interviewed about your secret talent.",
    " Set a weird timer and stare at it intensely for 1 minute.",
    " Make a TikTok-worthy reaction face.",
    "Draw a cat using your non-dominant hand.",
    "Name 5 random things that start with 'B'.",
    "Make a superhero pose and hold it for 10 seconds.",
    " Eat a spoonful of Turmeric powder.",
    "Say the alphabet backwards as fast as you can.",
    "Draw something blindfolded and post it on IG.",
    "Try to do a handstand (or pretend to).",
    " Flirt your water bottle like it's your crush.",
    " Do your best fake sneeze.",
    "Whisper everything you say for 2 minutes.",
    "Try to say 'supercalifragilisticexpialidocious' 3x fast.",
    "Take a pretend phone call in a British accent.",
    "Pretend you’re on a cooking show and describe making toast.",
    "Fake sneeze as dramatically as possible.",
    "Act like you're being chased by bees.",
    "Call a random object your best friend for 2 minutes.",
    "Act like you're swimming on dry land.",
    "Bark like a dog every time someone says your name.",
    "Open the last photo on your phone. No explanation.",
    " Say three compliments to the person on you hate most.",
    "Speak only in rhymes for the next 2 rounds.",
    "Text your best friend: “Emergency. Bring Broom stick.”",
    "Reveal the last thing you searched on Google.",
    "Act like a confused time traveler for 1 minute.",
    " Dance to an imaginary beat right now.",
    "Whisper everything for the next 2 rounds.",
    "Invent a handshake using only your elbows.",
    "Do a runway walk like a model on a mission.",
    "Make a duck face and talk for 10 seconds.",
    " Record a 5-second fake cry and send it.",
    "post 'I love broccoli' on your story for 3 minutes.",
    "Put your finger on your nose and spin around 10 times.",
    "Show the 4th photo in your camera roll.",
    "Say a pickup line as dramatically as possible.",
    "Try to do 10 jumping jacks while clapping and yelling.",
    " Attempt to moonwalk across the room.",
    "Hold your breath for 15 seconds.",
    "Balance something on your head for 1 minute.",
    "Speak like a pirate until your next dare.",
    "Do your best impression of a robot in love.",
    "Say a tongue twister 3 times fast.",
    "Pretend to be a cat for 30 seconds."]



hard_dare=[
    " Text your ex or crush: “I still think about you.” No context",""
    "Send a voice note to your crush saying “I had a dream about you 👀.”",
    "Post “I believe in aliens 🛸” on your story. Leave it for 10 minutes.",
    "Call someone and confess a fake crime.",
    "Share the last search in your browser history.",
    "Send “We need to talk.” to your best friend. No follow-up for 30 mins.",
   "Say the most embarrassing username you've ever had online.",
    "Record a TikTok dance (or fake one) and send it to the group.",
    "Go to your Insta/Facebook and like your ex’s 3-year-old post.",
    "Screenshot your DMs and send it to the group (crop names if needed).",
    "Write a public “apology” in your notes and read it dramatically."]





truths = [
    "What's a lie you've told that no one knows about?",
    "Have you ever pretended to like a gift you actually hated?",
    "What's the weirdest dream you've ever had?",
    "Who's your current weirdest crush?",
    "What’s something you’d never admit out loud… until now?",
    "What’s your most used emoji?",
    "Have you ever Googled your own name?",
    "What was your last deleted photo?",
    "If your pet could talk, what would it roast you for?",
    "What song are you secretly obsessed with?",
    "Have you ever lied about finishing an assignment you didn’t start?",
    "What’s something completely random that makes you cry?",
    "Do you stalk your own posts to check who viewed them?",
    "If your brain had tabs open, what's one tab you'd never show anyone?",
    "What’s your favorite insult that you’d never say out loud?",
    "Have you ever fake-texted to avoid a convo if so when ?",
    "Have you talked to yourself in the mirror today and what?",
    "What’s one thing you regret buying?",
    "What's your go-to excuse when you don’t want to hang out?",
    "Have you ever faked laughing at someone’s joke, if so when?"
]
truths += [
    "Have you ever had a crush on a teacher?",
    "What’s the biggest lie you've told in the past week?",
    "What’s a secret you’re still hiding from your family?",
    
    "Have you ever checked someone else’s phone without permission?",
    "Who’s the last person you stalked on social media?",
    "What’s a weird thing you do when no one’s watching?",
    "Have you ever catfished someone just for fun?",
    "What’s your most cringe childhood moment?",
    "What’s your guilty pleasure snack combo?",
    "Have you ever accidentally sent a message to the wrong personif so when and what?",
    "What's the longest you've gone without showering?",
    "Have you ever secretly rooted for someone to fail?",
    "Have you ever imagined a dramatic exit scene for yourself if so when?",
    "Have you ever made up a story just to sound cooler?",
    "What’s something you've done out of jealousy?",
    "What's your most irrational fear?",
    "If your life were a movie, what would it be called?",
    "What's the weirdest compliment you've ever received?",
    "Have you ever rejected a friend request just to feel powerful?"
]
truths += [
    "Have you ever eaten something off the floor if so when and what ?",
    "What’s the dumbest thing you’ve done while sleep-deprived?",
    "Have you ever practiced a dramatic speech alone in your room?",
    "What’s your signature fake excuse?",
    "Have you ever laughed at something serious and felt horrible after?",
    "If someone went through your camera roll, what’s the first thing you’d panic over?",
    "Have you ever made up a fact in an argument just to win?",
    "What’s the most ridiculous thing you’ve cried about?",
    "What’s something embarrassing you secretly love?",
    "Have you ever worn the same clothes two days in a row without washing?",
    "What's the worst lie you believed as a kid?",
    "Have you ever recorded yourself just to hear how you sound?",
    "Have you lied in a Truth or Dare game before?",
    "Have you ever imagined you were in a music video while walking alone?",
    "Have you ever sent a risky text and blamed it on 'autocorrect'?",
    "What’s the most embarrassing thing in your search history?",
    "Have you ever Googled how to be cool?",
    "Do you sometimes rehearse arguments in your head?",
    "Have you ever rewatched a fight just to pick new comebacks?",
    "What's your personal villain origin story?"
]
truths += [
    "What’s one insecurity you rarely talk about?",
    "What’s a compliment you still remember to this day?",
    "When was the last time you cried over something silly?",
    "What’s a dream you gave up on and why?",
    "What’s something you wish you were better at?",
    "Have you ever felt like the side character in your friend group?",
    "Who’s the one person who made you feel seen?",
    "What do you pretend not to care about but secretly do?",
    "Have you ever apologized for something just to end the fight?",
    "When’s the last time you felt proud of yourself?",
    "What’s a memory you replay when you’re feeling down?",
    "Who’s someone you miss more than you admit?",
    "Have you ever stayed in a situation you should’ve left?",
    "What’s your secret comfort ritual?",
    "When’s the last time you felt truly understood?",
    "What’s one truth you’ve been avoiding?",
    "Do you feel like you’re living your story or someone else’s?",
    "What’s something you'd say to your younger self?",
    "What’s something you wish people knew about you?",
    "When’s the last time you felt fearless?"
]




welcome=["Let the sound of your chaos silence the city", "Why should you play this Game?, It's better than doom scrolling"," Wishing you a nice game 🎲"]

#This app uses [Google Fonts](https://fonts.google.com/) via `<link>` tags to enhance visual appeal. All fonts used are free and open-source under the SIL Open Font License.





q=["Welcome","Host mode😎","Player mode 😁"]
sb=st.radio("who are you?",q,key="G")

def dar3():
    if x:
        dare=easy_dare
    else:
        dare=hard_dare
    c=random.choice(dare)
    return c

def tru3():
    t=random.choice(truths)
    return(t)

            
if sb==q[0]:
   o=random.choice(welcome)
   st.markdown(
    f"""
    <div style='text-align: center; font-size: 25px; font-weight: bold; font-family:monospace;'>
       {f''' \n 
        {o}'''}
    </div>
    """,
    unsafe_allow_html=True
)
    

if sb==q[1]:

    players=[]
    names=[]

    pl=round(st.number_input("how many players are there?",key="play"))
    if pl==0:
        st.write("seriously")
        st.stop()
    
 

    for i in range(1,pl+1):
        key1=f"player{i}"
        name=st.text_input(f"name for player{i}",key=f"name_input_{i}")
        key2=f"{name}"
        names.append(name)
       
        players.append(key1)
    
        st.session_state["players"]=players
        p=st.session_state.get("players","oops")

    

    
    st.session_state["picker"]=True
    if st.session_state["picker"]==True:
        
    
        group_no=random.randint(300000,300599)


        how_many=round(st.number_input("how many round you want for each player", key="rounds"))
        st.session_state["how_many"]=how_many
        dare_many=(round(how_many/2))+2
        
       
        def call():
            all_dares=[]
            


            for v in range(1, pl+1):
                player_name=(f"player{v}")
                namees=names[v-1]
                player_dares=[player_name,namees]
                for i in range(1,dare_many+1):
                    result=dar3()
                    player_dares.append(result)
           
                    
                    
                all_dares.append(player_dares)
    

            columns=["players"]+["names"]+[f"dare{i}" for i in range(1, dare_many + 1)]
            df=pd.DataFrame(all_dares,columns=columns) 
            
        
            all_truths=[]
            for v in range(1, pl+1):
                player_name=(f"player{v}")
                player_dares=[player_name]
                for i in range(1,dare_many+1):
                    result=tru3()
                    player_dares.append(result)
                all_truths.append(player_dares)
                

            
            
    

            columns=["players"]+[f"true{i}" for i in range(1, dare_many + 1)] 
            df_2=pd.DataFrame(all_truths,columns=columns) 
            

            
            

            final_df=pd.merge(df,df_2, on="players")
            
        

           
            csv=final_df.to_csv().encode("utf-8")
            st.download_button(label="click here to download the result as CSV", data=csv, file_name= f"{group_no}{dare_many}.csv", mime="text/csv",key="down")
            st.markdown("#### Once ur done click back to player option")

        


        call()




if sb==q[2]:
    
    uploaded_file=st.file_uploader("drop the file here ",key="upload")
    if uploaded_file:
        st.success("file uploaded")
        df_read=pd.read_csv(uploaded_file)
    
        file_name = uploaded_file.name
        name_only = file_name.replace(".csv", "")
        
        s=name_only[-1]

        


        
        
        if "players" in df_read.columns:


            with st.expander("get ur dare "):
                but=st.button("hit me if all the players have played their 1st round in here and i'll offer you a poliet dare ")
                try:
                    ready=[]
                    if but:
                        st.session_state["u"]+=1
                    for player in df_read["players"]:
                        player_coun=df_read[df_read["players"]==player]
                        m=player_coun.iloc[0,2]
                        

                        k=f"dare{st.session_state["u"]}"
                        
                        
                    
                        l=player_coun[k].iloc[0]
                        p1=st.checkbox(f"{m}'s dare")
                        if p1:
                            st.write(l)
                            st.session_state["status"]=1
                            ready.append(st.session_state["status"])
                            #st.write(ready) 
                        else:
                            st.session_state["status"]=0
                            ready.append(st.session_state["status"])
                            #st.write(ready) 
                        st.write(st.session_state["status"])
                    if all(ready)==1:
                        st.write("okay now hit the button ")
                    elif all(ready)!=True:
                        st.warning("one truth and one dare alternatively to have good or else u may run out of dare soon")

                except Exception as e:
                    st.write("Oops! out of dare visit truth and ")

            with st.expander("get ur true "):
                bute=st.button("hit me if all the players have played their 1st round in here and i'll offer you a poliet truth ")
                try:
                    readyy=[]
                    if bute:
                        st.session_state["n"]+=1
                    for player in df_read["players"]:
                        player_coun=df_read[df_read["players"]==player]
                        m=player_coun.iloc[0,2]
                        

                        k=f"dare{st.session_state["n"]}"
                        
                        
                    
                        l=player_coun[k].iloc[0]
                        p1=st.checkbox(f"{m}'s truth")
                        if p1:
                            st.write(l)
                            st.session_state["statuss"]=1
                            ready.append(st.session_state["statuss"])
                            #st.write(ready) 
                        else:
                            st.session_state["statuss"]=0
                            ready.append(st.session_state["statuss"])
                            #st.write(ready) 
                        st.write(st.session_state["statuss"])
                    if all(readyy)==1:
                        st.write("okay now hit the button ")
                    elif all(readyy)!=True:
                        st.warning("one truth and one dare alternatively to have good or else u may run out of dare soon")

                except Exception as e:
                    st.write("Oops! out of truth  ")
            st.markdown(f''' 😊 \n
            For each player {s} dares and {s} truths are assigned \n 
            so no one can escape embarassment''')

            com=st.button("game completed") 
            if com==True: 
                
                st.balloons()
            if st.checkbox("🔍 Show Debug Console"):
                st.subheader("Dev Console")
                st.write("Session State:", st.session_state)

            


