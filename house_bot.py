# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# import joblib


# # Load the model




# # Load DataFrame from the joblib file
# df = joblib.load('df.joblib')

# # Load model from the joblib file
# pipe = joblib.load('RidgeModel.joblib')


# # Initialize Streamlit app
# st.title("House Prediction")

# def start(update, context):
#     update.message.reply_text("Welcome to the House Prediction Bot!")
# def handle_message(update, context):
#     user_input = update.message.text

#     # Load the model
#     pipe = joblib.load('RidgeModel.joblib')
#     df = joblib.load('df.joblib')

#     if user_input.lower() == "/start":
#         update.message.reply_text("Welcome to the House Prediction Bot!")
#         return

#     if user_input.lower() == "/predict":
#         update.message.reply_text("Please provide the input values in the format: location, total_sqft, bath, bhk")
#         return

#     # Handle Streamlit-like interaction
#     input_values = user_input.split(',')
#     if len(input_values) == 4:
#         location, total_sqft, bath, bhk = input_values
#         input_data = pd.DataFrame([[location, float(total_sqft), int(bath), int(bhk)]],
#                                   columns=['location', 'total_sqft', 'bath', 'bhk'])
#         predicted_price = int(pipe.predict(input_data)[0])
#         update.message.reply_text(f"The predicted price is {predicted_price}L")
#     else:
#         update.message.reply_text("Invalid input format. Please use: location, total_sqft, bath, bhk")


# # def handle_message(update, context):
# #     user_input = update.message.text

# #     if user_input.lower() == "/start":
# #         update.message.reply_text("Welcome to the House Prediction Bot!")
# #         return

# #     # Handle Streamlit interaction
# #     with st.echo(code_location='below'):
# #         location = st.selectbox("Location", sorted(df['location'].unique()))
# #         bhk = st.selectbox("BHK", df['bhk'].unique())
# #         bathrooms = st.selectbox("Bath", [1, 2, 3, 4])
# #         squarefeet = st.number_input('Enter Square feet')

# #         if st.button('Predict Price'):
# #             input_data = pd.DataFrame([[location, squarefeet, bathrooms, bhk]],
# #                                       columns=['location', 'total_sqft', 'bath', 'bhk'])
# #             predicted_price = int(pipe.predict(input_data)[0])
# #             st.title("The predicted price is " + str(predicted_price) + 'L')
# #             update.message.reply_text(f"The predicted price is {predicted_price}L")

# # def main():
# #     bot_token = "6415811766:AAEuPaQ7rumQgMSu8_9uzAGk44DUy0ts-HE"

# #     updater = Updater(token=bot_token, use_context=True)
# #     dispatcher = updater.dispatcher

# #     dispatcher.add_handler(CommandHandler("start", start))
# #     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# #     updater.start_polling()
# #     updater.idle()

# def main():
#     bot_token = "6415811766:AAEuPaQ7rumQgMSu8_9uzAGk44DUy0ts-HE"

#     updater = Updater(token=bot_token, use_context=True)
#     dispatcher = updater.dispatcher

#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("predict", predicted_price))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()


# if __name__ == "__main__":
#     main()
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
# import pandas as pd
# import joblib

# pipe = joblib.load('RidgeModel.joblib')
# df = joblib.load('df.joblib')

# user_data = {}  

# def start(update, context):
#     update.message.reply_text("Welcome to the House Price Prediction Bot!")

# def handle_message(update, context):
#     user_input = update.message.text

#     if user_input.lower() == "/start":
#         update.message.reply_text("Welcome to the House Price Prediction Bot!")
#         return

#     if user_input.lower() == "/predict":
#         update.message.reply_text("Please provide the input values in the format: location, total_sqft, bath, bhk")
#         user_data[update.message.chat_id] = {}  
#         user_data[update.message.chat_id]['step'] = 1
#         return

    
#     chat_id = update.message.chat_id
#     if chat_id in user_data and user_data[chat_id]['step'] == 1:
#         input_values = user_input.split(',')
#         if len(input_values) == 4:
#             location, total_sqft, bath, bhk = input_values
#             user_data[chat_id]['input'] = [location.strip(), float(total_sqft), int(bath), int(bhk)]
#             user_data[chat_id]['step'] = 2
#             update.message.reply_text("Please confirm the input: "
#                                       f"Location: {location}, Total Sqft: {total_sqft}, Bath: {bath}, BHK: {bhk}. "
#                                       "Reply 'confirm' to proceed.")
#         else:
#             update.message.reply_text("Invalid input format. Please use: location, total_sqft, bath, bhk")

#     elif chat_id in user_data and user_data[chat_id]['step'] == 2:
#         if user_input.strip().lower() == "confirm":
#             input_data = pd.DataFrame([user_data[chat_id]['input']],
#                                       columns=['location', 'total_sqft', 'bath', 'bhk'])
#             predicted_price = int(pipe.predict(input_data)[0])
#             update.message.reply_text(f"The predicted price is {predicted_price}L")
#             del user_data[chat_id]  
#         else:
#             update.message.reply_text("Input not confirmed. Please restart the prediction process with /predict.")

# def main():
#     bot_token = "6415811766:AAEuPaQ7rumQgMSu8_9uzAGk44DUy0ts-HE"

#     updater = Updater(token=bot_token, use_context=True)
#     dispatcher = updater.dispatcher

#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("predict", handle_message))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

import pandas as pd
import joblib

pipe = joblib.load('RidgeModel.joblib')
df = joblib.load('df.joblib')

data = {}

LOCATION, TOTAL_SQFT, BATH, BHK, CONFIRM = range(5)

locations = sorted(df['location'].unique())

def start(update, context):
    update.message.reply_text("Welcome to the House Price Prediction Bot enter /predict to predict the house price!")

def predict(update, context):
    update.message.reply_text("Please provide the input values:")
    data[update.message.chat_id] = {}
    data[update.message.chat_id]['step'] = LOCATION

    # Create reply keyboard options with unique locations
    location_options = [[location] for location in locations]
    reply_keyboard = location_options + [['Total Sqft'], ['Bathrooms'], ['BHK']]
    
    update.message.reply_text(
        "Select a location:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return LOCATION

def start(update, context):
    update.message.reply_text("Welcome to the House Price Prediction Bot enter /predict to predict the house price!")

def handle_message(update, context):
    input = update.message.text

    if input.lower() == "/start":
        update.message.reply_text("Welcome to the House Price Prediction Bot!")
        return

    if input.lower() == "/predict":
        update.message.reply_text("Please provide the input values in the format: location, total_sqft, bath, bhk")
        data[update.message.chat_id] = {}  
        data[update.message.chat_id]['step'] = 1
        return

    
    chat_id = update.message.chat_id
    if chat_id in data and data[chat_id]['step'] == 1:
        input_values = input.split(',')
        if len(input_values) == 4:
            location, total_sqft, bath, bhk = input_values
            data[chat_id]['input'] = [location.strip(), float(total_sqft), int(bath), int(bhk)]
            data[chat_id]['step'] = 2
            update.message.reply_text("Please confirm the input: "
                                      f"Location: {location}, Total Sqft: {total_sqft}, Bath: {bath}, BHK: {bhk}. "
                                      "Reply 'confirm' to proceed.")
        else:
            update.message.reply_text("Invalid input format. Please use: location, total_sqft, bath, bhk")

    elif chat_id in data and data[chat_id]['step'] == 2:
        if input.strip().lower() == "confirm":
            input_data = pd.DataFrame([data[chat_id]['input']],
                                      columns=['location', 'total_sqft', 'bath', 'bhk'])
            predicted_price = int(pipe.predict(input_data)[0])
            update.message.reply_text(f"The predicted price is {predicted_price}L")
            del data[chat_id]  
        else:
            update.message.reply_text("Input not confirmed. Please restart the prediction process with /predict.")


def get_location(update, context):
    data[update.message.chat_id]['location'] = update.message.text
    data[update.message.chat_id]['step'] = TOTAL_SQFT
    update.message.reply_text("Enter the total sqft:")

    return TOTAL_SQFT

def get_total_sqft(update, context):
    data[update.message.chat_id]['total_sqft'] = float(update.message.text)
    data[update.message.chat_id]['step'] = BATH
    update.message.reply_text("Enter the number of bathrooms:")

    return BATH

def get_bath(update, context):
    data[update.message.chat_id]['bath'] = int(update.message.text)
    data[update.message.chat_id]['step'] = BHK
    update.message.reply_text("Select the number of bedrooms (BHK):", reply_markup=ReplyKeyboardRemove())

    return BHK

def get_bhk(update, context):
    data[update.message.chat_id]['bhk'] = int(update.message.text)
    data[update.message.chat_id]['step'] = CONFIRM

    reply_keyboard = [['Confirm', 'Cancel']]
    update.message.reply_text(
        f"Location: {data[update.message.chat_id]['location']}\n"
        f"Total Sqft: {data[update.message.chat_id]['total_sqft']}\n"
        f"Bathrooms: {data[update.message.chat_id]['bath']}\n"
        f"BHK: {data[update.message.chat_id]['bhk']}\n\n"
        "Confirm or Cancel?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return CONFIRM

def confirm(update, context):
    chat_id = update.message.chat_id

    if update.message.text.lower() == "confirm":
        input_data = pd.DataFrame([[
            data[chat_id]['location'],
            data[chat_id]['total_sqft'],
            data[chat_id]['bath'],
            data[chat_id]['bhk']
        ]], columns=['location', 'total_sqft', 'bath', 'bhk'])

        predicted_price = int(pipe.predict(input_data)[0])
        update.message.reply_text(f"The predicted price is {predicted_price}L")
    else:
        update.message.reply_text("Input not confirmed. Please restart the prediction process with /predict.")

    del data[chat_id]
    return ConversationHandler.END

def main():
    bot_token = "6415811766:AAEuPaQ7rumQgMSu8_9uzAGk44DUy0ts-HE"

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("predict", predict)],
        states={
            LOCATION: [MessageHandler(Filters.text & ~Filters.command, get_location)],
            TOTAL_SQFT: [MessageHandler(Filters.text & ~Filters.command, get_total_sqft)],
            BATH: [MessageHandler(Filters.text & ~Filters.command, get_bath)],
            BHK: [MessageHandler(Filters.text & ~Filters.command, get_bhk)],
            CONFIRM: [MessageHandler(Filters.text & ~Filters.command, confirm)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conversation_handler)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("predict", handle_message))   
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()



# def start(update, context):
#     update.message.reply_text("Welcome to the House Price Prediction Bot!")

# def predict(update, context):
#     update.message.reply_text("Please provide the input values:")
#     user_data[update.message.chat_id] = {}
#     user_data[update.message.chat_id]['step'] = LOCATION

#     # Define reply keyboard options
#     reply_keyboard = [['Location'], ['Total Sqft'], ['Bathrooms'], ['BHK']]
#     update.message.reply_text(
#         "Select an option:",
#         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
#     )

#     return LOCATION
