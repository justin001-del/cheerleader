import streamlit as st
import random 
from utils.bg import set_bg_from_local  


set_bg_from_local("assets/img.jpeg") 


st.title("🌈 Your Pocket Cheerleader: Kris")

with open("assets\style.css") as f:
    
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)


responses=["To be honest with you, I can't fix this problem. But remember neither the problem nor you is invincible, Time passes problems fade so as you use you time wise ",
           "That's hard to hear, But don't quit, I'm sure you'll make your future self proud ",
           "How brave you are ? naming it already makes it half lighter. don't worry move you got this",
           "You aren't weak to feel like this, you are a human, and a warrior too. kudos for not quitting yet ",
           "Even the dakest night eventually give way to dawn, This is feeling won't last, So hey you got this",
            "I want to say that I'm not good enough to handel that but you are,.. feel proud about it",
            "That's a lot you are going through, Time flies , so as your problems",
            "Your problems are hard to solve but i want to remind you, you're harder than that",
            "You're an incredibly strong and resilient person ,I truly believe you'll get through this",
            "Your feelings are valid, But I'm sure you have enough strength not to quit "
           
           ]




name=st.text_input("Hi there! what is your Name?")
if name:
    pass
else:
    name="warrior🌙"
issue=st.text_input("What's Bothering you lately?")




if name and issue:
    share=st.button("✨ Cheer Me Up")
    if  share:
        a=random.choice(responses)
        st.markdown(f'''Read your problem again \n 
        ["{issue}"], \n 
        It exists.. So does you.. I know it is hard but please don't run. Face it ''')
    
        st.markdown(f'''😊 \n 
         So hey {name}, Here's what I want to say ...\n
         {a}''')
        st.markdown("*Recovery habits 🪴😌*")
        st.markdown("💡 Try journaling your thoughts tonight")
        st.markdown("🧘 Do 5 minutes of deep breathing, no pressure")
        st.markdown("📚 Pick one page from your fav book and read it")


else:
    st.write("Hey 😊, I can't Judge you ,Just say what you want. ")


