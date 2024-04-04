from math import floor
import streamlit as st

def check_time(time):
    time_splits = time.split(':')
    time_split_end = time_splits[-1].split('.')
    time_splits.pop()
    time_splits.extend(time_split_end)
    time_splits = [int(t) for t in time_splits]
    if time_splits[0] > 99 or time_splits[0] < 0 or time_splits[1] > 59 or time_splits[1] < 0 or time_splits[2] > 59 or time_splits[1] < 0 or time_splits[3] > 99 or time_splits[1] < 0:
        return False
    return True

def convert_to_seconds(time):
    time_splits = time.split(':')
    time_split_end = time_splits[-1].split('.')
    time_splits.pop()
    time_splits.extend(time_split_end)
    time_splits = [int(t) for t in time_splits]
    seconds = time_splits[0] * 3600 + time_splits[1] * 60 + time_splits[2] + time_splits[3] * 0.01
    return seconds

def seconds_to_hours(time):
    return round(time/3600,5)

def seconds_to_time(time):
    hours = int(time // 3600)
    time -= hours * 3600
    minutes = int(time // 60)
    time -= minutes * 60
    seconds = int(floor(time))
    decimals = int(round(time - seconds, 2) * 100)
    hours = f'{hours:02}'    
    minutes = f'{minutes:02}'    
    seconds = f'{seconds:02}'
    decimals = f'{decimals:02}'
    return f'{hours}:{minutes}:{seconds}.{decimals}'

def predict_time(time, base_distance, prediction_distance, multiplier = 1.045):
    if base_distance > prediction_distance:
        predicted_time = time * (prediction_distance/base_distance) / multiplier
    else:
        predicted_time = time * (prediction_distance/base_distance) * multiplier
    return predicted_time

#avg speed, avg pace, per km and per mile, prediction for all other races
def three_k_stats(time):
    avg_time_per_km = seconds_to_time(time / 3)
    avg_time_per_mile = seconds_to_time(time / 1.86411)
    avg_speed_km_per_h = round(3 / seconds_to_hours(time), 2)
    avg_speed_mile_per_h = round(1.86411 / seconds_to_hours(time), 2)
    mile_prediction = predict_time(time, 3, 1.60934)
    km_prediction = predict_time(mile_prediction, 1.60934, 1)
    five_k_prediction = predict_time(time, 3, 5)
    ten_k_prediction = predict_time(five_k_prediction, 5, 10)
    half_marathon_prediction = predict_time(ten_k_prediction, 10, 21.0975)
    marathon_prediction = predict_time(half_marathon_prediction, 21.0975, 42.195)
    return avg_time_per_km, avg_time_per_mile, avg_speed_km_per_h, avg_speed_mile_per_h, seconds_to_time(km_prediction), seconds_to_time(mile_prediction), seconds_to_time(five_k_prediction), seconds_to_time(ten_k_prediction), seconds_to_time(half_marathon_prediction), seconds_to_time(marathon_prediction)


def five_k_stats(time):
    avg_time_per_km = seconds_to_time(time / 5)
    avg_time_per_mile = seconds_to_time(time / 3.10686)
    avg_speed_km_per_h = round(5 / seconds_to_hours(time), 2)
    avg_speed_mile_per_h = round(3.10686 / seconds_to_hours(time), 2)
    three_k_prediction = predict_time(time, 5, 3)
    mile_prediction = predict_time(three_k_prediction, 3, 1.60934)
    km_prediction = predict_time(mile_prediction, 1.60934, 1)
    ten_k_prediction = predict_time(time, 5, 10)
    half_marathon_prediction = predict_time(ten_k_prediction, 10, 21.0975)
    marathon_prediction = predict_time(half_marathon_prediction, 21.0975, 42.195)
    return avg_time_per_km, avg_time_per_mile, avg_speed_km_per_h, avg_speed_mile_per_h, seconds_to_time(km_prediction), seconds_to_time(mile_prediction), seconds_to_time(three_k_prediction), seconds_to_time(ten_k_prediction), seconds_to_time(half_marathon_prediction), seconds_to_time(marathon_prediction)


def ten_k_stats(time):
    avg_time_per_km = seconds_to_time(time / 10)
    avg_time_per_mile = seconds_to_time(time / 6.21371)
    avg_speed_km_per_h = round(10 / seconds_to_hours(time), 2)
    avg_speed_mile_per_h = round(6.21371 / seconds_to_hours(time), 2)
    five_k_prediction = predict_time(time, 10, 5)
    three_k_prediction = predict_time(five_k_prediction, 5, 3)
    mile_prediction = predict_time(three_k_prediction, 3, 1.60934)
    km_prediction = predict_time(mile_prediction, 1.60934, 1)
    half_marathon_prediction = predict_time(time, 10, 21.0975)
    marathon_prediction = predict_time(half_marathon_prediction, 21.0975, 42.195)
    return avg_time_per_km, avg_time_per_mile, avg_speed_km_per_h, avg_speed_mile_per_h, seconds_to_time(km_prediction), seconds_to_time(mile_prediction), seconds_to_time(three_k_prediction), seconds_to_time(five_k_prediction), seconds_to_time(half_marathon_prediction), seconds_to_time(marathon_prediction)


def half_marathon_stats(time):
    avg_time_per_km = seconds_to_time(time / 21.0975)
    avg_time_per_mile = seconds_to_time(time / 13.10937873)
    avg_speed_km_per_h = round(21.0975 / seconds_to_hours(time), 2)
    avg_speed_mile_per_h = round(13.10937873 / seconds_to_hours(time), 2)
    ten_k_prediction = predict_time(time, 21.0975, 10, 1.03)
    five_k_prediction = predict_time(ten_k_prediction, 10, 5)
    three_k_prediction = predict_time(five_k_prediction, 5, 3)
    mile_prediction = predict_time(three_k_prediction, 3, 1.60934)
    km_prediction = predict_time(mile_prediction, 1.60934, 1)
    marathon_prediction = predict_time(time, 21.0975, 42.195, 1.06)
    return avg_time_per_km, avg_time_per_mile, avg_speed_km_per_h, avg_speed_mile_per_h, seconds_to_time(km_prediction), seconds_to_time(mile_prediction), seconds_to_time(three_k_prediction), seconds_to_time(five_k_prediction), seconds_to_time(ten_k_prediction), seconds_to_time(marathon_prediction)


def marathon_stats(time):
    avg_time_per_km = seconds_to_time(time / 42.195)
    avg_time_per_mile = seconds_to_time(time / 26.2187575)
    avg_speed_km_per_h = round(42.195 / seconds_to_hours(time), 2)
    avg_speed_mile_per_h = round(26.2187575 / seconds_to_hours(time), 2)
    half_marathon_prediction = predict_time(time, 42.195, 21.0975, 1.035)
    ten_k_prediction = predict_time(half_marathon_prediction, 21.0975, 10)
    five_k_prediction = predict_time(ten_k_prediction, 10, 5)
    three_k_prediction = predict_time(five_k_prediction, 5, 3)
    mile_prediction = predict_time(three_k_prediction, 3, 1.60934)
    km_prediction = predict_time(mile_prediction, 1.60934, 1)
    return avg_time_per_km, avg_time_per_mile, avg_speed_km_per_h, avg_speed_mile_per_h, seconds_to_time(km_prediction), seconds_to_time(mile_prediction), seconds_to_time(three_k_prediction), seconds_to_time(five_k_prediction), seconds_to_time(ten_k_prediction), seconds_to_time(half_marathon_prediction)

st.set_page_config(page_title='Running Analyzer', page_icon='icon.ico', layout='wide')

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col_1, col_2, col_3, col_4, col_5 = st.columns([1.2,0.8,1.5,2,1.5])

with col_1:
    st.image('icon.png', width=200)
    st.title('')
    selected_distance = st.selectbox(label='Distance', options=['3K', '5K', '10K', 'Half marathon', 'Marathon'], placeholder='5K')
    time_input = st.text_input('Time', value='00:15:00.00', help=f'Enter the time in this format: \n\n **HH\:MM\:SS\.00** \n\n You can replace zeros with actual decimals.')

    if check_time(time_input):
        if selected_distance == '3K':
            three_k_time = time_input
            avg_km, avg_mile, avg_kmp, avg_mph, km_time, mile_time, five_k_time, ten_k_time, half_marathon_time, marathon_time = three_k_stats(convert_to_seconds(time_input))
        elif selected_distance == '5K':
            five_k_time = time_input
            avg_km, avg_mile, avg_kmp, avg_mph, km_time, mile_time, three_k_time, ten_k_time, half_marathon_time, marathon_time = five_k_stats(convert_to_seconds(time_input))
        elif selected_distance == '10K':
            ten_k_time = time_input
            avg_km, avg_mile, avg_kmp, avg_mph, km_time, mile_time, three_k_time, five_k_time, half_marathon_time, marathon_time = ten_k_stats(convert_to_seconds(time_input))
        elif selected_distance == 'Half marathon':
            half_marathon_time = time_input
            avg_km, avg_mile, avg_kmp, avg_mph, km_time, mile_time, three_k_time, five_k_time, ten_k_time, marathon_time = half_marathon_stats(convert_to_seconds(time_input))
        elif selected_distance == 'Marathon':
            marathon_time = time_input
            avg_km, avg_mile, avg_kmp, avg_mph, km_time, mile_time, three_k_time, five_k_time, ten_k_time, half_marathon_time = marathon_stats(convert_to_seconds(time_input))
    col_1_1, col_1_2 = st.columns(2)
    with col_1_1:
        st.title('Per km', anchor='stat_description')
        st.title(avg_km, anchor='stat')
        st.title(f'{avg_kmp:.2f} kph', anchor='stat')
    with col_1_2:
        st.title('Per mile', anchor='stat_description')
        st.title(avg_mile, anchor='stat')    
        st.title(f'{avg_mph:.2f} mph', anchor='stat')   

with col_3:
    st.title("1K", anchor="distance")
    st.title("Mile", anchor="distance")
    st.title("3K", anchor="distance")
    st.title("5K", anchor="distance")
    st.title("10K", anchor="distance")
    st.title("Half marathon", anchor="distance")
    st.title("Marathon", anchor="distance")

with col_4:
    st.title(km_time, anchor='distance')
    st.title(mile_time, anchor='distance')
    st.title(three_k_time, anchor='distance')
    st.title(five_k_time, anchor='distance')
    st.title(ten_k_time, anchor='distance')
    st.title(half_marathon_time, anchor='distance')
    st.title(marathon_time, anchor='distance')

# with col_4:
#     st.title('These are just estimated times based on your entered time.', anchor='disclaimer')