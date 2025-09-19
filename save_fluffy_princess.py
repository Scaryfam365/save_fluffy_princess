import streamlit as st

st.set_page_config(page_title="Mission: Save Princess VANILLA FLUFFFY CAKEEE", layout="centered")

# -------------------------
# --- Intro Page / Title ---
# -------------------------
INTRO_MARKDOWN = """
# HiIIII DAWGGG,BETTT UR SITTING IN FRONT OF ME RN AND TRYNA GUESS WHATS GOING ON?!! LIKE WTFFFFF IS EVEN SAVE PRINCESSS FLU.....

## AND WHATS THISSS MISSION SHI ( NGL HOPEFULLY AMAR SPEAKER E SHUNAI JAI OR KOTHA THO) YEAHH DAWGGG ITS TIME FOR SOMEE ACTIONN 🤯🤯

# TIME TO ROCK MY WORLD!!!!!🥳🥳🥳🥳

### NGLL THIS IS MORE LIKE A QUESTIONNAIREE 

## BUT I HOPEE IT MAKES U CRACK UP FACING MY NONCHALANT ASS

---

# 🚨 Mission : Save Princess VANILLA FLUFFFY CAKEEE 🍰 🚨

## I REALLY LOVE U DAWGG AND HOPEFULLY THIS LITTLE ADVENTURE IS WELL WORTH ITTT!!!!!!!
"""

# -------------------------
# --- Questions Data ------
# -------------------------
QUESTIONS = [
    {
        "q": "1. If Im Blue 🔵  and Your Red 🔴:",
        "opts": [
            ("I wanna kiss your neck and Make you purple all over ??",
             "Oh tainnaaaaaaaaa. I think Im good🥹🥹"),
            ("I want U to kiss my neck And Make my neck Purple All over??",
             "Sure Lets Pretend Im blue and ur red. And Lock in dawg💋💋💋"),
            ("IDKK",
             "NO WAYYY DAWGG HAD TO ADD THIS OPTION NGLL 🤦‍♀️🤦‍♀️"),
            ("Cuddles",
             "If U lock In On this ONEEE THEN THATS MEE NGLL ( I Literally Fw this one dawg)I jst wanna hug u dawg🫂🫂"),
        ],
    },
    {
        "q": "2. Favourite Nickname That I call U 🗣?",
        "opts": [
            ("Fluffy cake",
             "BWHAHAHAHA HEHEHEH YEAHH DAWG ALWAYSSS 🍰🍰🍰"),
            ("Baby",
             "UMMM SUREEE But Ig Sometimes u literally look like one LIKE WHEN UR SLEEEPING AND MAKE THOSE CUTE AHH NOISEESSSS.(Music to my ears 🤩)"),
            ("Jaanu",
             "ACTUALLY HAVENT STARTED IT YET THAT MUCHHH BUT IM GONNA START CALLING U THAT AFTER WE WATCHH Aashiqui 2 together 🤗🤗(HEHEHE IF YKYK)"),
            ("DAWG",
             "( NO WAYY IT REMINDS ME WHEN U FIRST MENTIONED THIS Word And I went like Who says DAWG IN 2025 and guess where we ended up 🤤🤤)"),
        ],
    },
    {
        "q": "3. Favourite Song From Our Playlist (FLUFFY AND TAKKU 4EVER)  : P",
        "opts": [
            ("Amar Jaan",
             "NGLL I FIRST HEARD THIS SONG FROM UR NOTE AND GOT REALLY HOOKED UP AND GOT INTO IT DAWG Whenever I see the music Video IT just reminds me one day us prolly 👰🏼‍♀️💍 🤵🏾‍♂️"),
            ("Tumi",
             "NGLL ME WHENEVER I THINK ABOUT OR SEE SOME COUPLE ACTING REALLY FUNNY ON THE ROAD.This just reminds me of us dawg The dumb shi we only do together Like picking paddle rickshaws 🛺🛺 cuz its slow. To Playing A dumb childs toy in Shimanto Elevator 🫠🫠HEHEHEHE"),
            ("Tera Hone Laga Hooon",
             "I remember that Night in June 14. Ig U dropped a vm outta nowhere singing this song And Idk i felt so special then dawg💘💘💘.Made a special place in my heart ngl.💌💌"),
            ("Jo tum Mere Ho",
             "Yeah DAWGG THIS LITERALLY OUR SONG. Our Number 1 LOVE ANTHEMMM♾️♾️.Hope this Song Keeps burning in our heart Like A moth to a flame ❤️‍🔥❤️‍🔥."),
            ("This Is What Falling In love feels like",
             "Im glad it was u all along 😍😍😍"),
        ],
    },
    {
        "q": "4. Favourite Thing I Do TO U ☺️?",
        "opts": [
            ("Katukutu",
             "IK HOW MUCH U LOVE THIS DAWGGG 😏😏AND Since ur so shy About It I just go on my own 🥲🥲.(Bro be Reading this And Saying Khub hoilo)"),
            ("Wrapping my arms around You",
             "SURE DAWGG we be walking wrapping my hand around ur shoulder like ur my homie or something and also managing ur cute🐱kitty bagg.And Followed By some shurshuri HEHEHEHE.IDK WRITING THIS Makes me wanna be with u so muchh rnn.I Hope u choose this first.😹😹😹"),
            ("Hugging",
             "This is actually idk I feel really sad Cuz every time dawg we be hug its like at the end of date bae.Like I dont wanna say goodbye 😿.I hope We hug At the start of the date of this time HEHEHE.Putting a bet on it"),
            ("Squishing",
             "HEHEHEHEHE I LOVE THISSS UR SO CUTEEE😌😌😌.Literally My Fav part.I be like Can I?Can I? and U be like 😒😒And say sure go ahead .HEHEHEHE"),
            ("Kisses",
             "OMGGG YESS DAWGG IK EITA CHOOSE KORBBAAA.MY GUESSING GAME REALLY GOOD.IKRRR.Bro be 🙂‍↔️🙂‍↔️ like this before shi and after bro be like🤭🤭HEHEHEHEHEHE"),
        ],
    },
    {
        "q": "5. Biggest Sideye to-",
        "opts": [
            ("Me Making Weird Hand movements",
             "HEHEHEHEH bro def eita choose korbe .🙄🙄Bro when Im making any hand sign Followed by a wtf bhai or wth bhai HEHEHE"),
            ("Saying Shi with double meanings",
             "LIKEEE BHAIII U ALWAYS choose the One thats sus .Like bhai Its not even deep Yet U still Make it deep and be like, I think Ami thik asi😭😭😭"),
            ("Suggesting Too out Of Topic stuff",
             "Bro Just Gives me AWKWARD LIKEE EITA KI BOLLO O T_T :P. Like U gotta chill"),
            ("Telling too much Stuff about Shi if ykyk",
             "Bro eita pore bolbee JE KI SHI HAEE?!HAE?!! Ami janina Ki shi >DEFF EITAA BLBEEE"),
        ],
    },
    {
        "q": "6. Favourite Followup I Copy of Yours - ?",
        "opts": [
            ("Tai na",
             "I think bro GONNA LOCK IN THIS ONE.IM SO INVESTED IN THIS JE I ACTUALLY USE IT.DAMN DAWG CHANGED MY LIFE🙀🙀🙀🙀,BUTTERFLY EFFECT PEAK HERE"),
            ("Right.Bujhte parlam Bishoyta",
             "YEAHHH RIGHHTTT DAAWGGG 😳😳😳.RIIIIIIIIGGGGHHTT (with the taaan) obviously.Bujhte parsoo?"),
            ("Khub Hoilo",
             "HAEEEE KHUBB HOISEE"),
            ("IDK",
             "HEHEHEHEHEHEHE,FELT LIKE I SHOULDDD ADD THIISSS"),
            ("beshi expectations bhalo na",
             "IKRRRR ASHOLEIII.EXPECTING DAWGG GONNA LIKE THISS"),
        ],
    },
    {
        "q": "7. How much do u think I LOVE U?",
        "opts": [
            ("More than U",
             "HEHEHEHE OBVIOUSLY BRO NOT GONNA PRESS ON THIS .IT'd be scary if bro did tho T_T"),
            ("Obsessesive Jaantush er motn",
             "HEHEHE BRO MIGHT LOCK IN ON THISS ONEE SOMETHINGG TELLLS ME .SO I ADDED THISS HEHEHEHEHE"),
            ("Like Wes did",
             "YEAHH I'd Definitely pour my heart For u like Wes did"),
        ],
    },
    {
        "q": "8. Last but not least,LASTLYYY WILL U CONSIDER STAYING WITH THIS OBSESSED ASS For the rest of ur life?",
        "opts": [
            ("Yes",
             "OMLLL OMGGG 😳😳🫨🫨🫨YESS DAWGGG SUREEEEE.SAMEE ME to"),
            ("No",
             "UMM TAI NA EITA PICK KORSO.IG END OF THE ROAD FOR YA FAM .HERE LIES -FLUFFY CAKE (A WONDERFUL SOUL)"),
            ("IDK",
             "NO DONT DOO THIS.YOU CANT!!!!U CANT"),
            ("DEKHA JABE",
             "BRO WOUD DEFINITELY PICK THIS TO PLAY SAFE.(HIGHKEY JUST SAY YES)"),
        ],
    },
]

# -------------------------
# --- Session State -------
# -------------------------
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None]*len(QUESTIONS)
if 'selected_msg' not in st.session_state:
    st.session_state.selected_msg = ""

# -------------------------
# --- Styles -------------
# -------------------------
st.markdown("""
<style>
h1.shiny{
    background: linear-gradient(90deg, #ffd700, #ff69b4, #00ffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# Color palette for buttons
BUTTON_COLORS = ["#ff4d4d", "#4d79ff", "#4dff88", "#ffd24d", "#ff66b3"]

# -------------------------
# --- App Logic ----------
# -------------------------
if st.session_state.step == 0:
    st.markdown(INTRO_MARKDOWN)
    if st.button("🚀 Start Mission"):
        st.session_state.step += 1
        st.experimental_rerun()

elif st.session_state.step <= len(QUESTIONS):
    q_index = st.session_state.step - 1
    question = QUESTIONS[q_index]
    st.markdown(f"### {question['q']}")

    # Display colored buttons
    for i, (opt, msg) in enumerate(question['opts']):
        color = BUTTON_COLORS[i % len(BUTTON_COLORS)]
        if st.button(opt, key=f"{q_index}_{i}"):
            st.session_state.answers[q_index] = opt
            st.session_state.selected_msg = msg
            st.session_state.step += 1
            st.experimental_rerun()

    if st.session_state.selected_msg:
        st.markdown(f"💬 {st.session_state.selected_msg}")

# -------------------------
# --- Final Success Page ---
# -------------------------
else:
    st.markdown("## End of the Road?\n\n**NOT YET!!!!!!!!**")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "I JUST WANNA SAY DAWGG HOPEFULLY U ENJOYED THIS.FROM WATCHING TO SUNRISE TOGETHER AND WAKING UP DURING SUNSETZZ FROM our afternoon nap. "
        "I hope we can continue keep twinning like this. And make sure our hearts are entwined like a match made in heaven."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Song lyrics in custom font
    st.markdown(
        "<div style=\"font-family:'Courier New', monospace; font-size:16px; color:#222; background-color:#f0f0f0;"
        "padding:10px; border-radius:8px;\">"
        "A great singer once said -<br>"
        "<em>Jo tum mere ho<br>"
        "Toh main kuch nahi maangoon duniya se<br>"
        "Aur tum ho hi nahi<br>"
        "Toh main jeena nahi chahoon duniya mei</em>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Many peoples broken hearts paragraph (bold + highlight)
    st.markdown(
        "<div style='background-color:#ffd166; color:#000; padding:12px; border-radius:10px; font-weight:bold;'>"
        "Many peoples broken heart That broke into million piece Turned to a billion pieces after listening to this Song. "
        "But For us Dawg It contains a totally different meaning. "
        "It teaches Us to never let go And We fucking exist for each other<WE FUCKING Do. "
        "So TWINN HOPEFULLY U SURVIVED THIS LONG AHH ORDEALL"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Mission paragraph (bold + highlight)
    st.markdown(
        "<div style='background-color:#9b6cff; color:white; padding:12px; border-radius:10px; font-weight:bold;'>"
        "MISSION : RESCUE PRINCESSS VANILLA FLUFFY CAKE FINALLY SUCCESSFULL"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Closing lines
    st.markdown("Byee dawg")
    st.markdown("I love You always♾️♾️")
    st.markdown("<br>", unsafe_allow_html=True)

    # Shiny celebration
    st.markdown("<h1 class='shiny'>🎉 YOU COMPLETED THE MISSION! 🎉</h1>", unsafe_allow_html=True)
    st.balloons()

    # Restart button
    if st.button("🔁 Restart Mission"):
        st.session_state.step = 0
        st.session_state.selected_msg = None
        st.session_state.answers = [None] * len(QUESTIONS)
        st.experimental_rerun()