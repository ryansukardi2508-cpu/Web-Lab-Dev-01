import streamlit as st
import info
st.title("What Type of Friend Are You?")
st.subheader("Answer the questions below to find out what type of friend you are!")
choices = ""
animal = st.radio("Choose which animal best fits you!", ["Penguin", "Dolphin", "Lion", "Gecko"],
                  captions=[
                      "Likes Cold Tempertures and Hugging.",
                      "Likes swimming and clapping their fins",
                      "Likes to hunt and very prideful",
                      "Likes to go at their own pace and be quiet",
                      ],
                  )
if (animal == "Penguin"):
    st.image(info.penguin_image)
elif (animal == "Dolphin"):
    st.image(info.dolphin_image)
elif (animal == "Lion"):
    st.image(info.lion_image)
elif (animal == "Gecko"):
    st.image(info.gecko_image)
st.write(f"You've selected {animal}!")
st.write("---------------------------------------")
st.image(info.friends_image)
st.write("Do you believe in ghosts!")
option_1 = st.selectbox("Yes or No!",
                        ("Yes", "No"),
                        key="question_1"
                    )
st.write(f"You've selected {option_1}!")

st.write("Do you like Dogs!")
option_2 = st.selectbox("Yes or No!",
                        ("Yes", "No"),
                        key="question_2",
                    )
st.write(f"You've selected {option_2}!")


st.write("Do you like traveling!")
option_3 = st.selectbox("Yes or No!",
                        ("Yes", "No"),
                        key="question_3",
                    )
st.write(f"You've selected {option_3}!")
st.write("---------------------------------------")
st.image(info.brain_image)
optimistic = st.select_slider(
    "How Optimistic Are You! (1-10)",
    options=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        ],
    )
st.write(f"You've selected {optimistic}!")
st.write("---------------------------------------")
st.image(info.number_image)
number = st.number_input("Pick a number between 1-100?",
                         min_value=0,
                         max_value=100
                    )
st.write(f"The number you selected is {number}")
st.write("---------------------------------------")
st.image(info.cake_image)
birthday = st.date_input("When's your birthday")
month = birthday.month
st.write("Your brithday is:", birthday)

st.write("---------------------------------------")
if animal == "Dolphin" and month <= 6:
    choices += "choice1"
elif option_2 == "Yes" and optimistic in ["2", "4", "6", "8", "10"]:
    choices += "choice2"
elif option_3 == "No" and number >= 50:
    choices += "choice3"
elif animal == "Penguin" and option_1 == "Yes" and number < 50:
    choices += "choice4"
elif animal == "Gecko" and option_2 == "No":
    choices += "choice5"
elif month >= 6 and optimistic in ["1", "5", "9"]:
    choices += "choice6"
elif animal == "Lion" and option_1 == "Yes":
    choices += "choice7"
elif number <= 50 and option_3 == "No":
    choices += "choice8"
elif animal == "Lion" and option_1 == "No":
    choices += "choice9"
elif animal == "Penguin" and option_2 == "Yes":
    choices += "choice10"
elif month <= 6 and optimistic in ["1", "2", "3", "4", "5"]:
    choices += "choice11"
elif number >= 50 and month <= 5:
    choices += "choice12"
elif animal == "Gecko" and number >= 50:
    choices += "choice13"
elif animal == "Dolphin" and optimistic in ["6", "7", "8", "9", "10"]:
    choices += "choice14"
elif number <= 50 and option_1 == "Yes":
    choices += "choice15"
elif option_2 == "Yes" and option_3 == "No":
    choices += "choice16"
else:
    choices += "choice17"
    
def choiceButton():
    if choices in ["choice1", "choice2", "choice3", "choice4", "choice17"]:
        st.header("The Therapist")
        st.write("Everyone comes to you for advice.")
        st.image(info.therapist_image)
        st.badge("Caregiver", color="green")
    elif choices in ["choice5", "choice6", "choice7", "choice8"]:
        st.header("The Comedian")
        st.write("You keep the group laughing.")
        st.image(info.comedian_image)
        st.badge("Class Clown", color="pink")
    elif choices in ["choice9", "choice10", "choice11", "choice12"]:
        st.header("The Protector")
        st.write("You always have your friends' backs.")
        st.image(info.protector_image)
        st.badge("Guardian", color="red")
    elif choices in ["choice13", "choice14", "choice15", "choice16"]:
        st.header("The Reliable One")
        st.write("People know they can count on you.")
        st.image(info.reliable_image)
        st.badge("Count On Me", color="blue")

if st.button("Click me! To find your results!"):    
    choiceButton()
