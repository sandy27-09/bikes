from socket import SO_PRIORITY
import streamlit as st
import pandas as pd 
import numpy as np
import time
from datetime import datetime
from matplotlib import pyplot as plt 
from bokeh.plotting import figure
from PIL import Image

st.markdown('<style>description{color: purple;}</style>',unsafe_allow_html=True)
st.title('✨NOT ALL WHO WONDER ARE LOST✨')
st.title('BIKE⚡')
image = Image.open('bike.jpg')
st.image(image,caption='''Behind me , there's nothing.''')
st.markdown("<description>A motorcycle, often called a motorbike, bike, cycle, or (if three-wheeled) trike, is a two- or three-wheeled motor vehicle. Motorcycle design varies greatly to suit a range of different purposes: long-distance travel, commuting, cruising, sport (including racing), and off-road riding. Motorcycling is riding a motorcycle and being involved in other related social activity such as joining a motorcycle club and attending motorcycle rallies.</description>",unsafe_allow_html=True)
st.sidebar.write('click the button to know more')
pun=st.sidebar.button("⚡")
if pun :
    st.snow()
    st.sidebar.write('''The 1885 Daimler Reitwagen made by Gottlieb Daimler and Wilhelm Maybach in Germany was the first internal combustion, petroleum-fueled motorcycle. In 1894, Hildebrand & Wolfmüller became the first series production motorcycle.

Globally, motorcycles are comparably popular to cars as a method of transport. In 2021, approximately 58.6 million new motorcycles were sold around the world, fewer than the 66.7 million cars sold over the same period.''')
st.sidebar.title('TYPE')
st.sidebar.write('''The term motorcycle has different legal definitions depending on jurisdiction (see § Legal definitions and restrictions).

There are three major types of motorcycle: street, off-road, and dual purpose. Within these types, there are many sub-types of motorcycles for different purposes. There is often a racing counterpart to each type, such as road racing and street bikes, or motocross including dirt bikes.

Street bikes include cruisers, sportbikes, scooters and mopeds, and many other types. Off-road motorcycles include many types designed for dirt-oriented racing classes such as motocross and are not street legal in most areas. Dual purpose machines like the dual-sport style are made to go off-road but include features to make them legal and comfortable on the street as well.

Each configuration offers either specialised advantage or broad capability, and each design creates a different riding posture.

In some countries the use of pillions (rear seats) is restricted.

 ''')


image = Image.open('bike1.jpg')
st.image(image,caption='''Behind me , there's nothing.''')

st.subheader('BIKERS BY HEART')
labels = 'bikers', 'non bikers'
sizes = [80,30]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
         startangle=90)
ax1.axis('equal')  
st.pyplot(fig1)


st.subheader('SUMMARY OF EARLY INVENTIONS')

l=[['1867–1868',	'Michaux-Perreaux steam velocipede'	,'2'	,'Pierre Michaux ,Louis-Guillaume Perreaux'	,'Steam','	One made'],['1867–1868',	'Roper steam velocipede',	'2',	'Sylvester Roper',	'Steam'	,'One made'],['1885',	'Daimler Reitwagen',	'2', '	Gottlieb Daimler,Wlhelm Maybach','Petroleum internal-combustion',	'One made']]
df=pd.DataFrame(l,columns=['year','vehicle','No. of wheels','Inventor','Engine type','Notes'])
st.table(df)

image = Image.open('bike2.jpg')
st.image(image)

st.subheader('Should I get a bike?')
if st.button('Yes'):
    st.write('Absolutely')
else:
    st.write('try once')

agree = st.radio("Do you have a bike:",('yes','no'))

if agree=='yes':
    st.write('Mee too!')
if agree=='no':
    st.write('sed lyf!')

agre = st.checkbox('Would you buy a superbike?')

if agre:
    st.write('congratulation!')


genre = st.radio(
    "Information about different types of bikes:",
    ('commuter', 'sports', 'cafe racer'))

if genre == 'commuter':
    st.write('There are 21 street bikes currently on sale from various manufacturers starting from 67,573. The most popular products under this bracket are the Hero Splendor Plus (Rs. 85,685), Hero HF Deluxe (Rs. 73,698) and Honda SP 125 (Rs. 95,260) (all prices on-road).The top brands that manufacture street bikes are Hero, Honda, Bajaj. To know more about the latest prices of Commuter Bikes in your city, download BikeDekho App & get details on offers, variants, specifications, pictures, mileage, reviews and other details, please select your desired bike from the list below.')
    image = Image.open('bike3.jpg')
    st.image(image)


if genre == 'sports':
    st.write('A sport bike (sports motorcycle, or sports bike) is a motorcycle designed and optimized for speed, acceleration, braking, and cornering on asphalt concrete race tracks and roads. They are mainly designed for performance at the expense of comfort, fuel economy, and storage in comparison with other motorcycles.')
    image = Image.open('bike4.jpg')
    st.image(image)

if genre == 'cafe racer':
    st.write('A café racer is a genre of sport motorcycles that originated among British motorcycle enthusiasts of the early 1960s in London. Café racers were standard production bikes that were modified by their owners and optimized for speed and handling for quick rides over short distances. Café racers have since become popular around the world, and some manufacturers produce factory-made models that are available in the showrooms.')
    image = Image.open('bike5.jpg')
    st.image(image)


st.subheader("BIKE SELECTION")
st.write("*Finding the right bike can be a complicated process for most of us. BikeWale helps you in making this process easier. You can search bikes based on brands, body styles, price, and displacement. Explore all the new bike models with their price in India. BikeWale brings you all the updates & expert reviews related to new bikes in India.*")


tab1, tab2, tab3 = st.tabs(["brand", "budget","displacement"])
with tab1:
    st.subheader("You can search new bikes by brand like TVS, Honda, Royal Enfield, Hero, Yamaha and many more. Or you may search new bikes based on price or budget. Have a particular body type in mind like a commuter, sport bike, cruiser or want a scooter or electric bike? That's possible too! From the most iconic motorcycles to the top 10 bikes in India, ZigWheels has it all covered!")
    img=Image.open("bike6.jpg")
    st.image(img)


with tab2:
    st.subheader("Are you planning on buying a bike under ₹ 1 lakh? Well, we know that budget is one of the most crucial things while buying a bike and with so many options available out there, it gets really difficult to find a good bike which suits your pocket. Hence, we have put together a complete list of best bikes under ₹ 1 lakh. OLA S1 Air, Odysse Hawk and BGauss D15 are the 3 most popular bikes in this budget range. View the complete list of bikes with information regarding price, images, mileage, specifications, colors, reviews and much more for each of these bikes so that you get to choose the best bike under ₹ 1 lakh.")
    l=[['Gemopai Astrid Lite','₹92,289'],['Benling Aura','₹91,646'],['TVS Raider 125','₹90,469'],['Pulsar NS160','₹1,23,781'],['Dominar 400','₹2,22,781'],['Pulsar N250','₹1,44,358']]
    df=pd.DataFrame(l,columns=['Model Name','Ex-Showroom price'])
    st.table(df)
 

with tab3:
    st.subheader("The size of motorcycle engines varies greatly. At the bottom of the scale, you’ll find dirt bikes and small-cc motorcycles like the Honda Rebel 300, with engine sizes from around 200 cc to 500 cc. At the top are monsters like the 2,500 cc Triumph Rocket 3.You’ll find strong opinions on the subject of cc’s within the motorcycle community. For example, bikes in the 250-300 cc range are common recommendations for folks looking to buy their first motorcycle. But you’ll also meet riders who will tell you that you’ll outgrow a 250 cc bike almost immediately and that it’s worth starting out on something more powerful.")
    mew = st.radio("select cc:",
        ('100-350cc', '>350cc'))

    if(mew=='100-350cc'):
        img = Image.open("bike7.jpg")
        st.image(img,caption='''PLATINA''')
        img = Image.open("bike8.jpg")
        st.image(img,caption='''r15''')
        img = Image.open("bike9.jpg")
        st.image(img,caption='''duke200''')
        img = Image.open("bike10.jpg")
        st.image(img,caption='''royal enfield''')


    if(mew=='>350cc'):
    
        img = Image.open("bike11.jpg")
        st.image(img,caption='''rc390''')
        img = Image.open("bike12.jpg")
        st.image(img,caption='''duke390''')
        img = Image.open("bike13.jpg")
        st.image(img,caption='''dominor400''')
        img = Image.open("bike14.jpg")
        st.image(img,caption='''continental gt''')
        img = Image.open("bike15.jpg")
        st.image(img,caption='''BMW s1000rr''')
  

age = st.slider('How many bikes do you have?', 0, 4)
st.write("I have ", age, ' bikes')



st.subheader('Bike production')


x = [2000, 2005, 2010, 2020, 2022]
y = [3000, 2000, 5000, 4000, 7000]

p = figure(
    title='no of bike :',
    x_axis_label='years',
    y_axis_label='productions')

p.line(x, y, legend_label='production of bike', line_width=2)

st.bokeh_chart(p, use_container_width=True)

rat = st.slider('do you like it?', 0, 10, 5)
st.write("I would rate it a", rat)

