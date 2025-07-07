import streamlit as st
from utils.bg import set_bg_from_local






set_bg_from_local("assets/image.jpeg")

with open("assets/style.css") as f:
    
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

st.text_input("😌",placeholder="Enter your name here for better experience")

st.markdown('''***\n
            🎮 Welcome to DareYou – A Multiplayer Truth or Dare Game Engine!\n
            ✅ Host Mode: Create game for multiple players\n
            ✅ Player Mode: Upload your game and take turns getting embarrassed\n
            
            🎉 Warning: May cause laughter, awkwardness, or lasting friendships***''')




with st.expander("click here to know how the app runs"):
    q=["Choose an option","click here to know about host mode","click here to know about player mode"]
    v=st.selectbox("clcik here to know your mode",q)
    i=q.index(v)

    if i==1:
        st.info('''
            
Enter the number of players — whether it's 3 or 13, we support the chaos.

Set the number of rounds each player gets — that’s how many truth/dare prompts you’ll generate per person.

Download the generated CSV so each player can upload it on their turn.
            
Watch as the app randomly assigns dares and truths to each player.

Celebrate your genius. You just created a mini truth/dare game night with zero prep.



''')
        
    if i==2:
            st.info('''
Upload the CSV file sent to you by the picker.

You’ll see your group name and number of dares/truths encoded in the filename.

Use the buttons in the “get your dare” and “get your truth” sections.

And you have to alternate between truth or dare , no one is chosing truth twice same goes for dare

Each time you click hit button the other set of randomised pair is created, you’ll move to the next dare/truth.

Then press the button with your player id to reveal your challenge!

 embrace the awkwardness.





''')
            


with st.sidebar:
     
     st.markdown (" Your tiny listner..")
     their_notes=st.text_area(" Try journaling your madness and have a memo that remind you of this  👇👇",height=150)
     

     if their_notes:
          their_file=their_notes.encode()
          st.download_button(
               label="download you notes",
               data=their_file,
               file_name="my_memory.txt",
               mime="text/plain"
          )
     
st.markdown("#### Not intrested in reading paragraphs on how the app works here's a Q/A session")
f=st.button("Q/A session")

if f:
     st.markdown("oops still didn't update it ")

st.markdown("Click the sidebar to view the game session")

