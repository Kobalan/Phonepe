# 1.Importing Libraries
import mysql.connector as sql
import pandas as pd
import requests
import json
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import babel.numbers as bn
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

# 2.Establishing the connection

db = sql.connect(host="localhost",user="root",password="kobalan",auth_plugin="mysql_native_password",database="phonepe")
cursor = db.cursor()  #creating a cursor object    

# -------------------------------------------------------------------------------------------------------------------------------------------------------#

# 3.Setting up page configuration

st.set_page_config(page_title= "Phonepe Pulse Data Visualization | By M.Kobalan",
                   layout= "wide",
                   initial_sidebar_state= "expanded")

SELECT = option_menu(
    menu_title = None,
    options = ["Home","Top Charts","About Project"],
    # icons =["house","bar-chart","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "yellow","size":"cover", "width": "100"},
        "icon": {"color": "black", "font-size": "20px"},   
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#4.Menu-1 Home_Page

if SELECT == "Home":

    components.html(
        """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {box-sizing: border-box;}
    body {font-family: Verdana, sans-serif;}
    .mySlides {display: none;}
    img {vertical-align: middle;}

    /* Slideshow container */
    .slideshow-container {
    max-width: 10000px;
    position: relative;
    margin: auto;
    }

    /* The dots/bullets/indicators */
    .dot {
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    transition: background-color 0.6s ease;
    }

    .active {
    background-color: #717171;
    }

    /* Fading animation */
    .fade {
    animation-name: fade;
    animation-duration: 1.5s;
    }

    @keyframes fade {
    from {opacity: .4} 
    to {opacity: 1}
    }

    /* On smaller screens, decrease text size */
    @media only screen and (max-width: 300px) {
    .text {font-size: 11px}
    }
    </style>
    </head>
    <body>

    <div class="mySlides fade">
    <img src="https://www.phonepe.com/webstatic/7091/static/bab93065eae063d167f5ea2699093877/c1679/hp-banner-pg.jpg" style="width:100%">
    </div>

    <div class="mySlides fade">
    <img src="https://www.phonepe.com/webstatic/7091/static/c30266c687af963c38a81c3891726ca9/27fce/hp-banner-pb.jpg" style="width:100%">
    </div>
    <br>

    <div class="mySlides fade">
    <img src="https://www.phonepe.com/webstatic/7091/static/6eba1bff4e20e9bc2aa276c2fe94659f/c608a/hp-banner-aa.png" style="width:100%">
    </div>
    <br>

    <div class="mySlides fade">
    <img src="https://www.phonepe.com/webstatic/7091/static/6f6a045306a14491bf6aa948f2dab1eb/30c3d/partner-section-desk.png" style="width:100%">
    </div>

    
    <div style="text-align:center">
    <span class="dot"></span> 
    <span class="dot"></span> 
    <span class="dot"></span> 
    </div>

    <script>
    let slideIndex = 0;
    showSlides();

    function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
    }
    </script>
    </body>
    </html> 
        """,
        height=600,
    )

    col1,col2 = st.columns(2)
    with col1:
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
        <div class="mySlides fade">
        <div class="numbertext">3 / 3</div>
        <video autoplay="" loop="" muted="" poster="/static/fast-secure-video-poster-v3-6f33427d52f42e474727f7442b029c59.png" playsinline=""><source src="https://www.phonepe.com/webstatic/7091/videos/page/home-fast-secure-v3.mp4" type="video/mp4"></video>
            <source src="https://www.phonepe.com/webstatic/7091/videos/page/home-fast-secure-v3.mp4" type="video/mp4">
        </video>
        </div>
        </head>
        </html>
            """,
            height=600,)
    with col2:
       components.html("""
                    <html>
                    <body>
                    <h1 style="font-family:Neutro; font-size:80px"> About Phonepe </h1>
                    <p style="font-family:Neutro; font-size:25px">
                        PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru, Karnataka,India. <br> PhonePe was founded in December 2015,by Sameer Nigam, Rahul Chari and Burzin Engineer.<br> The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016.<br>
                        The PhonePe app is accessible in 11 Indian languages.<br> It enables users to perform various financial transactions such as sending and receiving money, recharging mobile and DTH, making utility payments, conducting in-store payments</h1>
                    </p>
                    </body>
                    </html>
                    """,
                        height=800,)
    col3,col4=st.columns(2)
    
    with col3:
        components.html("""
                    <html><body><h1 style="font-family:Neutro; font-size:60px"> Founder and CEO </h1></body></html>""",)
        st.image("f1.jpg")
    with col4:
        components.html("""
                    <html><body><h1 style="font-family:Neutro; font-size:60px">  </h1></body></html>""",)
        st.image("af.png")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Menu-2 TOP CHARTS
if SELECT=="Top Charts":
    
    type=st.sidebar.selectbox("TYPE",("TRANSACTION","INSURANCE","USER"))

    def comma_Seperator(num):               # FOR ALL_TRANSACTION TOTAL VALUE
        result=bn.format_currency(num,'INR',locale="en_IN")
        v=len(result)-3
        formatted_Value=result[1:v]
        return formatted_Value
    
#TYPE= Transaction
    if type=="TRANSACTION":  

        def mcrores(number):                        #FOR TOTAL PAYMENT VALUE
            return '₹'+'{:,.0f} Cr'.format(round(number / 10000000))
        
        def count_Convert (number):             #FOR SIDEBAR TABLE VALUE
            if len(number)>=8:
                    return '{:,.2f} Cr'.format(int(number) / 10000000)
            elif len(number)==7 or len(number)==6:
                    return '{:.2f}L'.format(int(number) / 100000)
    
       #Getting the user Input
        Year =['2018','2019','2020','2021','2022','2023','2024']
        default_y = Year.index("2020")
        year = st.sidebar.selectbox(':violet[YEAR]', Year,key='year',index=default_y)
        quarter=st.sidebar.selectbox(":violet[QUARTER]",("1","2","3","4"))
        
        hide_streamlit_style = """ <html> <body> <h1 style="font-family:Neutro; font-size:50px"> TRANSACTION </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    #Getting the Transaction Details
        cursor.execute(f'select * from agg_transaction')
        df_Trans1=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans2=df_Trans1[(df_Trans1['Year']==int(year)) & (df_Trans1['Quarter']==int(quarter))]
        df_Trans2= df_Trans2.groupby("State")[["Transaction_count", "Transaction_amount"]].sum().sort_values(by='Transaction_count',ascending=False)
        df_Trans2.reset_index(inplace= True)
        df_Trans2['State'] = df_Trans2['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Daman & Diu")
    
    #Calculating and Formatting the Average,ALL Transaction and Total Payment Value 
        df_Trans2['Avg.Transaction Value']=df_Trans2['Transaction_amount']//df_Trans2['Transaction_count']
        df_Trans2['Avg_Transaction_Value'] = df_Trans2['Avg.Transaction Value'].apply(lambda x: round(x)).apply(lambda x: "₹{:,.0f}".format(x))
        df_Trans2['All Transaction'] = df_Trans2['Transaction_count'].apply(lambda x:comma_Seperator(x) )
        df_Trans2['Total Payment Value'] = df_Trans2['Transaction_amount'].apply(lambda x: round(x)).apply(lambda x: mcrores(x))
        

    #Transaction_Map................

        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data= json.loads(response.content)
        states_name= [feature["properties"]["ST_NM"] for feature in data["features"]]
        
        hide_streamlit_style = """ <html><body><h1 style="font-family:Neutro; font-size:40px"> MAP VIEW </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        if len(df_Trans2)==0:
                hide_streamlit_style = """ <html><body> <h1 style="font-family:Neutro; font-size:40px; color:red"> NO DATA TO SHOW 😞</h1></body></html> """
                st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        else:
            fig= px.choropleth(df_Trans2, geojson= data, locations= "State", featureidkey= "properties.ST_NM",
                                        color= "Transaction_amount", color_continuous_scale= "turbo",
                                        range_color= (df_Trans2["Transaction_amount"].min(),df_Trans2["Transaction_amount"].max()),
                                        hover_name= "State",
                                        hover_data={'All Transaction':True,'Total Payment Value':True,'State':False,'Avg_Transaction_Value':True,'Transaction_amount':False},
                                        fitbounds= "locations",width =1400, height= 800)
            fig.update_geos(visible =False)
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)
            
            hide_streamlit_style = """ <html> <body> <h1 style="font-family:Neutro; font-size:40px"> STATE WISE BAR CHART </h1></body></html>  """                     
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    #Transaction_State Wise BAR
        state=df_Trans2.State.tolist()
        count1=df_Trans2.Transaction_count.tolist()
        fig1 =go.Figure(data=[go.Bar(x=state, y=count1, name="State", marker=dict(color='black'), orientation="v"),
            ],
        layout=go.Layout(xaxis=dict(title="STATE"), yaxis=dict(title="USAGE"),font=dict( family="Neutro",size=30,color="RebeccaPurple",variant="small-caps", )
            ))
        fig1.update_layout(width=1200,height=800, )
        st.plotly_chart(fig1)

    #Transaction_District Wise Bar.....................
        hide_streamlit_style = """ <html><body><h1 style="font-family:Neutro; font-size:40px"> DISTRICT WISE BAR CHART </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        col1,col2=st.columns([1,3])
        with col1:
            result=st.selectbox("Choose a State :",state )
        
            cursor.execute(f'select State,District,sum(Transaction_amount) as Total_Payment_value,sum(Transaction_count) as Total_Transaction  from map_transaction where year={year} and quarter={quarter} group by district,State order by Total_Payment_value desc')
            df_Trans3=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
            df_Trans4=df_Trans3[df_Trans3['State']==result]
            district=df_Trans4.District.tolist()
            count2=df_Trans4.Total_Transaction.tolist()
            fig2=go.Figure(data=[go.Bar(x=district, y=count2,  name="District",marker=dict(color='blue'),  orientation="v"),
            ],
            layout=go.Layout(xaxis=dict(title="DISTRICT"), yaxis=dict(title="USAGE"), font=dict( family="Neutro",size=30,color="RebeccaPurple",variant="small-caps", )                                          
            ))
            fig2.update_layout(barmode="stack")
            fig2.update_layout( width=1200, height=600,)
            st.plotly_chart(fig2)

    #Transaction_PincodeWise Bar.....................

        hide_streamlit_style = """ <html><body><h1 style="font-family:Neutro; font-size:40px"> PINCODE WISE BAR CHART </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        cursor.execute(f'select State,Pincode,sum(Transaction_amount) as Total_Payment_value,sum(Transaction_count) as Total_Transaction  from top_transaction where year={year} and quarter={quarter} group by Pincode,State order by Total_Payment_value desc')
        df_Trans5=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans6=df_Trans5[df_Trans5['State']==result]
        pincode1=df_Trans6.Pincode.tolist()
        pincode2=[str(i) for i in pincode1]
        count3=df_Trans6.Total_Transaction.tolist()
        fig3=go.Figure(data=[go.Bar(x=pincode2,y=count3, name="Pincode", marker=dict(color='brown'), orientation="v"),
        ],
        layout=go.Layout(xaxis=dict(title="Pincode",type='category'), yaxis=dict(title="USAGE"), font=dict(family="Neutro", size=30, color="RebeccaPurple", variant="small-caps", )                                          
        ))
        fig3.update_layout(barmode="stack")
        fig3.update_layout( width=800,height=600,)
        st.plotly_chart(fig3)
        
    #Transaction Type Wise Bar.....................

        hide_streamlit_style = """ <html><body> <h1 style="font-family:Neutro; font-size:40px"> TRANSACTION TYPE WISE BAR CHART </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        cursor.execute(f'select State,Transaction_type,sum(Transaction_amount) as Total_Payment_value,sum(Transaction_count) as Total_Transaction  from agg_transaction where year={year} and quarter={quarter} group by Transaction_type,State order by Total_Payment_value desc')
        df_Trans5=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans6=df_Trans5[df_Trans5['State']==result]
        trans1=df_Trans6.Transaction_type.tolist()
        trans2=[str(i) for i in trans1]
        count4=df_Trans6.Total_Transaction.tolist()
        fig4=go.Figure(data=[go.Bar(x=trans2,y=count4, name="Transaction_type",  marker=dict(color='orange'), orientation="v"),
        ],
        layout=go.Layout(xaxis=dict(title="Transaction_type"), yaxis=dict(title="USAGE"),font=dict( family="Neutro",size=30,color="RebeccaPurple",variant="small-caps", )                                          
        ))
        fig4.update_layout(barmode="stack")
        fig4.update_layout(width=800,height=600,)
        st.plotly_chart(fig4)

    #Brand Wise Bar.....................

        hide_streamlit_style = """ <html><body> <h1 style="font-family:Neutro; font-size:40px"> BRAND WISE BAR CHART </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        cursor.execute(f'select State,brand,sum(Transaction_count) as Total_Transaction  from agg_user where year={year} and quarter={quarter} group by brand,State order by Total_Transaction desc')
        df_Trans5=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans6=df_Trans5[df_Trans5['State']==result]
        brand1=df_Trans6.brand.tolist()
        brand2=[str(i) for i in brand1]
        count5=df_Trans6.Total_Transaction.tolist()
        fig5=go.Figure(data=[go.Bar( x=brand2,y=count5, name="Brand", marker=dict(color='violet'), orientation="v" ),
        ],
        layout=go.Layout( xaxis=dict(title="BRAND"),yaxis=dict(title="USAGE"),font=dict(family="Neutro", size=30,  color="RebeccaPurple", variant="small-caps",)                                          
        ))
        fig5.update_layout(barmode="stack")
        fig5.update_layout( width=800,height=600,)
        st.plotly_chart(fig5)

    # SideBar Table..................

        col1, col2, col3 = st.sidebar.columns([1,1,1])
        with col1:
            f1=st.button('State')
        with col2:
            f2=st.button('District')
        with col3:
            f3=st.button('Pincode')
           
        if f1:
            st.sidebar.markdown("Top 10 States")
            cursor.execute(f"select State, sum(Transaction_count) as Total from agg_transaction where year = {year} and quarter = {quarter} group by State order by Total desc limit 10")
            df_State1= pd.DataFrame(cursor.fetchall(), columns=['State','Total_Transaction'])    #For Showing Datas in the Table 
            df_State2=df_State1.copy()
            df_State2['State']=[i.upper() for i in df_State2['State']]
            df_State2['Total_Transaction']=df_State2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))   #For Showing the Converted data 
            if len(df_State1)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_State2)
            
        if f2:
            st.sidebar.markdown("Top 10 Districts")
            cursor.execute(f"select District, sum(Transaction_count) as Total from map_transaction where year = {year} and quarter = {quarter} group by District order by Total desc limit 10")
            df_District1 = pd.DataFrame(cursor.fetchall(), columns=['District','Total_Transaction'])    #For Showing Datas in the Table
            df_District2=df_District1.copy()
            df_District2['District']=[i.upper() for i in df_District2['District']]
            df_District2['Total_Transaction']=df_District2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))  #For Showing the Converted data 
            if len(df_District2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_District2)

        if f3:
            st.sidebar.markdown("Top 10 Pincodes")
            cursor.execute(f"select Pincode, sum(Transaction_count) as Total from top_transaction where year = {year} and quarter = {quarter} group by Pincode order by Total desc limit 10")
            df_Pincode1 = pd.DataFrame(cursor.fetchall(), columns=['Pincode','Total_Transaction'])  #For Showing Datas in the Table
            df_Pincode2=df_Pincode1.copy()
            df_Pincode2['Total_Transaction']=df_Pincode2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))    #For Showing the Converted data
            if len(df_Pincode2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_Pincode2)
                  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Insurance
    elif type=="INSURANCE":

        def total_Count(number):                        #FOR TOTAL PREMIUM VALUES
            if len(number)>=8:
                return '₹'+'{:,.0f} Cr'.format(round(int(number) / 10000000))
            elif len(number)==7 or len(number)==6:
                 return '{:.0f}L'.format(int(number) / 100000)
            elif len(number)==5 or len(number)==4:
                 return '{:.0f}K'.format(int(number) / 1000)
            else:
                return number
            
        def count_Convert (number):                 #FOR SIDEBAR TABLE
            if len(number)>=8:
                    return '{:,.2f} Cr'.format(int(number) / 10000000)
            elif len(number)==7 or len(number)==6:
                    return '{:.2f}L'.format(int(number) / 100000)
            elif len(number)==5 or len(number)==4:
                    return '{:.2f}K'.format(int(number) / 1000)
            else:
                    return number
 
     #Getting the user input  .................

        Year =['2020','2021','2022','2023','2024']
        default_y = Year.index("2021")
        year = st.sidebar.selectbox(':violet[YEAR]', Year,key='year',index=default_y)
        quarter=st.sidebar.selectbox(":violet[QUARTER]",("1","2","3","4"))
        
        hide_streamlit_style = """ <html> <body><h1 style="font-family:Neutro; font-size:50px"> INSURANCE </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        cursor.execute(f'select * from agg_insurance')
        df_Trans1=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans2=df_Trans1[(df_Trans1['Year']==int(year)) & (df_Trans1['Quarter']==int(quarter))]
    
        df_Trans2= df_Trans2.groupby("State")[["Transaction_count", "Transaction_amount"]].sum().sort_values(by='Transaction_count',ascending=False)
        df_Trans2.reset_index(inplace= True)
        df_Trans2['State'] = df_Trans2['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Daman & Diu")

    #Calculating and Formatting the Average,ALL Transaction and Total Payment Value 
        df_Trans2['Avg.Transaction Value']=df_Trans2['Transaction_amount']//df_Trans2['Transaction_count']
        df_Trans2['Avg Premium Value'] = df_Trans2['Avg.Transaction Value'].apply(lambda x: round(x)).apply(lambda x: "₹{:,.0f}".format(x))
        df_Trans2['Insurance Policies Nos.'] = df_Trans2['Transaction_count'].apply(lambda x: round(x)).apply(lambda x: comma_Seperator(x))
        df_Trans2['Total Premium Value'] = df_Trans2['Transaction_amount'].apply(lambda x: round(x)).apply(lambda x: total_Count(str(x)))
        

    #Insurance_Map................

        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data= json.loads(response.content)
        states_name= [feature["properties"]["ST_NM"] for feature in data["features"]]

        hide_streamlit_style = """ <html><body><h1 style="font-family:Neutro; font-size:40px"> MAP VIEW </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        if len(df_Trans2)==0:
                hide_streamlit_style = """ <html><body> <h1 style="font-family:Neutro; font-size:40px; color:red"> NO DATA TO SHOW 😞</h1></body></html>"""
                st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        else:
            fig= px.choropleth(df_Trans2, geojson= data, locations= "State", featureidkey= "properties.ST_NM",
                                        color= "Transaction_amount", color_continuous_scale= "Viridis",
                                        range_color= (df_Trans2["Transaction_amount"].min(),df_Trans2["Transaction_amount"].max()),
                                        hover_name= "State",
                                        hover_data={'Insurance Policies Nos.':True,'Total Premium Value':True,'State':False,'Avg Premium Value':True,'Transaction_amount':False},
                                        fitbounds= "locations",width =1400, height= 800)
            fig.update_geos(visible =False)
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)
            
            hide_streamlit_style = """<html><body> <h1 style="font-family:Neutro; font-size:40px"> STATE WISE BAR CHART </h1></body></html>"""
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    #Transaction_State Wise BAR
        state=df_Trans2.State.tolist()
        count1=df_Trans2.Transaction_count.tolist()
        fig1 =go.Figure(data=[go.Bar(x=state,  y=count1,  name="State",  marker=dict(color='black'), orientation="v"),
            ],
        layout=go.Layout(xaxis=dict(title="STATE"),yaxis=dict(title="USAGE"), font=dict( family="Neutro", size=30, color="RebeccaPurple", variant="small-caps", )                       
        ))
        fig1.update_layout(width=1200, height=800, )
        st.plotly_chart(fig1)

    #Transaction_District Wise Bar.....................
        hide_streamlit_style = """<html><body> <h1 style="font-family:Neutro; font-size:40px"> DISTRICT WISE BAR CHART </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        col1,col2=st.columns([1,3])
        with col1:
            result=st.selectbox("Choose a State :",state )

            state=df_Trans2.State.tolist()
            cursor.execute(f'select State,District,sum(Transaction_amount) as Total_Payment_value,sum(Transaction_count) as Total_Transaction  from map_insurance where year={year} and quarter={quarter} group by district,State order by Total_Payment_value desc')
            df_Trans3=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
            df_Trans4=df_Trans3[df_Trans3['State']==result]
            district=df_Trans4.District.tolist()
            count2=df_Trans4.Total_Transaction.tolist()
            fig2=go.Figure(data=[go.Bar(x=district,y=count2,  name="District",  marker=dict(color='blue'), orientation="v"),
                ],
            layout=go.Layout( xaxis=dict(title="DISTRICT"),yaxis=dict(title="USAGE"),font=dict( family="Neutro", size=30,color="RebeccaPurple",variant="small-caps", )                                          
            ))
            fig2.update_layout(barmode="stack")
            fig2.update_layout(width=1200, height=600,)
            st.plotly_chart(fig2)

    #Transaction_PincodeWise Bar.....................

        hide_streamlit_style = """ <html><body><h1 style="font-family:Neutro; font-size:40px"> PINCODE WISE BAR CHART </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        cursor.execute(f'select State,Pincode,sum(Transaction_amount) as Total_Payment_value,sum(Transaction_count) as Total_Transaction  from top_insurance where year={year} and quarter={quarter} group by Pincode,State order by Total_Payment_value desc')
        df_Trans5=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans6=df_Trans5[df_Trans5['State']==result]
        pincode1=df_Trans6.Pincode.tolist()
        pincode2=[str(i) for i in pincode1]
        count3=df_Trans6.Total_Transaction.tolist()
    
        fig3=go.Figure(data=[go.Bar(x=pincode2,  y=count3, name="Pincode",  marker=dict(color='brown'),  orientation="v"),
                 ],
        layout=go.Layout(xaxis=dict(title="PINCODE",type='category'), yaxis=dict(title="USAGE"), font=dict( family="Neutro", size=30, color="RebeccaPurple", variant="small-caps", )              
        ))
        fig3.update_layout( width=600,height=600, )
        st.plotly_chart(fig3)

    
     #SIDE BAR For Insurance.................................   
        col1, col2, col3 = st.sidebar.columns([1,1,1])
        with col1:
            f1=st.button('State')
        with col2:
            f2=st.button('District')
        with col3:
            f3=st.button('Pincode')
        
        if f1:
            st.sidebar.markdown("Top 10 States")
            cursor.execute(f"select State, sum(Transaction_count) as Total from agg_insurance where year = {year} and quarter = {quarter} group by State order by Total desc limit 10")
            df_State1= pd.DataFrame(cursor.fetchall(), columns=['State','Total_Transaction'])    #For Showing Datas in the Table 
            df_State2=df_State1.copy()
            df_State2['State']=[i.upper() for i in df_State2['State']]
            df_State2['Total_Transaction']=df_State2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))   #For Showing the Converted data 
            if len(df_State1)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_State2)
        if f2:
            st.sidebar.markdown("Top 10 Districts")
            cursor.execute(f"select District, sum(Transaction_count) as Total from map_insurance where year = {year} and quarter = {quarter} group by District order by Total desc limit 10")
            df_District1 = pd.DataFrame(cursor.fetchall(), columns=['District','Total_Transaction'])    #For Showing Datas in the Table
            df_District2=df_District1.copy()
            df_District2['District']=[i.upper() for i in df_District2['District']]
            df_District2['Total_Transaction']=df_District2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))  #For Showing the Converted data 
            if len(df_District2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_District2)
            
        if f3:
            st.sidebar.markdown("Top 10 Pincodes")
            cursor.execute(f"select Pincode, sum(Transaction_count) as Total from top_insurance where year = {year} and quarter = {quarter} group by Pincode order by Total desc limit 10")
            df_Pincode1 = pd.DataFrame(cursor.fetchall(), columns=['Pincode','Total_Transaction'])  #For Showing Datas in the Table
            df_Pincode2=df_Pincode1.copy()
            df_Pincode2['Total_Transaction']=df_Pincode2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))    #For Showing the Converted data 
            if len(df_Pincode2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_Pincode2) 
           

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#User
    elif type=="USER":
        
        hide_streamlit_style = """<html> <body> <h1 style="font-family:Neutro; font-size:40px"> USER </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        def total_Count(number):
            if len(number)>=8:
                return '₹'+'{:,.0f} Cr'.format(round(int(number) / 10000000))
            elif len(number)==7 or len(number)==6:
                 return '{:.0f}L'.format(int(number) / 100000)
            elif len(number)==5 or len(number)==4:
                 return '{:.0f}K'.format(int(number) / 1000)
            else:
                return number
            
        def count_Convert (number):
            if len(number)>=8:
                    return '{:,.2f} Cr'.format(int(number) / 10000000)
            elif len(number)==7 or len(number)==6:
                    return '{:.2f}L'.format(int(number) / 100000)
            elif len(number)==5 or len(number)==4:
                    return '{:.2f}K'.format(int(number) / 1000)
            else:
                    return number
 
        #Getting the user Input

        Year =['2018','2019','2020','2021','2022','2023','2024']
        default_y = Year.index("2020")
        year = st.sidebar.selectbox(':violet[YEAR]', Year,key='year',index=default_y)
        quarter=st.sidebar.selectbox(":violet[QUARTER]",("1","2","3","4"))
        
        cursor.execute(f'select * from agg_user')
        df_Trans1=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans2=df_Trans1[(df_Trans1['Year']==int(year)) & (df_Trans1['Quarter']==int(quarter))]
    
        df_Trans2= df_Trans2.groupby("State")[["Transaction_count", "Percentage"]].sum().sort_values(by='Transaction_count',ascending=False)
        df_Trans2.reset_index(inplace= True)
        df_Trans2['State'] = df_Trans2['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Daman & Diu")  
        df_Trans2['Percentage']=df_Trans2['Percentage'].apply(lambda x: x*100).apply(lambda x: '{:,.0f}%'.format(int(x)))
        df_Trans2['All_Transaction'] = df_Trans2['Transaction_count'].apply(lambda x: round(x)).apply(lambda x: comma_Seperator(x))

    #User_Map................

        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data= json.loads(response.content)
        states_name= [feature["properties"]["ST_NM"] for feature in data["features"]]
       
        hide_streamlit_style = """<html><body><h1 style="font-family:Neutro; font-size:40px"> MAP VIEW </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        if len(df_Trans2)==0:
            hide_streamlit_style = """<html> <body>  <h1 style="font-family:Neutro; font-size:40px; color:red"> NO DATA TO SHOW 😞</h1></body></html>"""
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        else:
            fig= px.choropleth(df_Trans2, geojson= data, locations= "State", featureidkey= "properties.ST_NM",
                                        color= "Transaction_count", color_continuous_scale= "ylorrd",
                                        range_color= (df_Trans2["Transaction_count"].min(),df_Trans2["Transaction_count"].max()),
                                        hover_name= "State",
                                        hover_data={'Transaction_count':False,'State':False,'Percentage':True,'All_Transaction':True},
                                        fitbounds= "locations",width =1400, height= 800)
            fig.update_geos(visible =False)
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)

    #Transaction_State Wise BAR.........................      
        hide_streamlit_style = """<html> <body> <h1 style="font-family:Neutro; font-size:40px"> STATE WISE BAR CHART </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        state=df_Trans2.State.tolist()
        count1=df_Trans2.Transaction_count.tolist()
        fig1 =go.Figure(data=[go.Bar( x=state,  y=count1, name="State", marker=dict(color='black'),  orientation="v"),
            ],
        layout=go.Layout( xaxis=dict(title="STATE"),  yaxis=dict(title="USAGE"), font=dict( family="Neutro", size=30, color="RebeccaPurple", variant="small-caps",)                       
        ))
        fig1.update_layout( width=1200, height=800,)
        st.plotly_chart(fig1)

    #Transaction_District Wise Bar.....................
        hide_streamlit_style = """ <html>  <body> <h1 style="font-family:Neutro; font-size:40px"> DISTRICT WISE BAR CHART </h1></body></html> """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        col1,col2=st.columns([1,3])
        with col1:
            result=st.selectbox("Choose a State :",state )
            state=df_Trans2.State.tolist()
            cursor.execute(f'select State,District,sum(appOpens) as Total_Appopen,sum(registeredUsers) as Total_Transaction  from map_user where year={year} and quarter={quarter} group by district,State order by Total_Appopen desc')
            df_Trans3=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
            df_Trans4=df_Trans3[df_Trans3['State']==result]
            district=df_Trans4.District.tolist()
            count2=df_Trans4.Total_Transaction.tolist()
            fig2=go.Figure(data=[go.Bar(x=district, y=count2,  name="District",marker=dict(color='blue'),orientation="v"),
            ],
            layout=go.Layout( xaxis=dict(title="DISTRICT"), yaxis=dict(title="USAGE"),font=dict( family="Neutro",size=30,color="RebeccaPurple",variant="small-caps", )                                          
            ))
            fig2.update_layout(barmode="stack")
            fig2.update_layout( width=1200,height=600, )
            st.plotly_chart(fig2)

    #Transaction_PincodeWise Bar.....................

        hide_streamlit_style = """<html><body><h1 style="font-family:Neutro; font-size:40px"> PINCODE WISE BAR CHART </h1></body></html>"""
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        
        cursor.execute(f'select State,Pincode,sum(Registered_users) as Total_Registered_Users  from top_Users where year={year} and quarter={quarter} group by Pincode,State order by Total_Registered_Users desc')
        df_Trans5=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        df_Trans6=df_Trans5[df_Trans5['State']==result]
        pincode1=df_Trans6.Pincode.tolist()
        pincode2=[str(i) for i in pincode1]
        count3=df_Trans6['Total_Registered_Users'].tolist()
    
        fig3=go.Figure(data=[go.Bar(x=pincode2, y=count3,  name="Pincode",marker=dict(color='brown'), orientation="v"),
                 ],
        layout=go.Layout(xaxis=dict(title="PINCODE",type='category'),yaxis=dict(title=" USAGE"), font=dict( family="Neutro", size=30,color="RebeccaPurple", variant="small-caps",)              
        ))
        fig3.update_layout(barmode="stack")
        fig3.update_layout( width=600, height=600,)
        st.plotly_chart(fig3)

    
    #SIDEBAR FOR User.......................

        col1, col2, col3 = st.sidebar.columns([1,1,1])
        with col1:
            f1=st.button('State')
        with col2:
            f2=st.button('District')
        with col3:
            f3=st.button('Pincode')
        
        if f1:
            st.sidebar.markdown("Top 10 States")
            cursor.execute(f"select State, sum(Transaction_count) as Total from agg_user where year = {year} and quarter = {quarter} group by State order by Total desc limit 10")
            df_State1= pd.DataFrame(cursor.fetchall(), columns=['State','Total_Transaction'])    #For Showing Datas in the Table 
            df_State2=df_State1.copy()
            df_State2['State']=[i.upper() for i in df_State2['State']]
            df_State2['Total_Transaction']=df_State2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))   #For Showing the Converted data 
            if len(df_State1)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_State2) 
        if f2:
            st.sidebar.markdown("Top 10 Districts")
            cursor.execute(f"select District, sum(registeredUsers) as Total from map_user where year = {year} and quarter = {quarter} group by District order by Total desc limit 10")
            df_District1 = pd.DataFrame(cursor.fetchall(), columns=['District','Total_Transaction'])    #For Showing Datas in the Table
            df_District2=df_District1.copy()
            df_District2['District']=[i.upper() for i in df_District2['District']]
            df_District2['Total_Transaction']=df_District2['Total_Transaction'].apply(lambda x: count_Convert(str(x)))  #For Showing the Converted data 
            if len(df_District2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_District2) 
            
        if f3:
            st.sidebar.markdown("Top 10 Pincodes")
            cursor.execute(f"select Pincode, sum(Registered_users) as Total from top_Users where year = {year} and quarter = {quarter} group by Pincode order by Total desc limit 10")
            df_Pincode1 = pd.DataFrame(cursor.fetchall(), columns=['Pincode','Total_Users'])  #For Showing Datas in the Table
            df_Pincode2=df_Pincode1.copy()
            df_Pincode2['Total_Users']=df_Pincode2['Total_Users'].apply(lambda x: count_Convert(str(x)))    #For Showing the Converted data 
            if len(df_Pincode2)==0:
                st.sidebar.markdown("NO DATA ENTRIED")
            else:    
                st.sidebar.table(df_Pincode2) 


#----------------------------------------------------------------------------------------------------------------------#
#Menu-4

col1,col2=st.columns([3,3])

#ABOUT THIS PROJECT

if SELECT == "About Project":
    with col1:
        st.image("ab.PNG")
        
#FAQ[Frequently Asked Questions]
    with col2:
         components.html("""
                    <html> <body>
                    <h1 style="font-family:Neutro; color:blue;font-size:50px"> About this Project </h1>
                    <p style="font-family:Neutro; font-size:25px">
                        <b>Project_Title</b>: <br>Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly <br>
                        <b>Technologies_Used</b> :<br> Github Cloning, Python, Pandas, MySQL, Streamlit, and Plotly. <br>
                        <b>Dataset: <br></b> https://github.com/PhonePe/pulse#readme <br>
                        <b>Domain </b> : Fintech <br>
                        <b>Problem Statement:</b>: <br>The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics.<br>
                         The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.<br>
                        <b>Author</b> : M.KOBALAN <br>
                        <b>Linkedin</b> :https://www.linkedin.com/in/kobalan-m-106267227/
                    </p>
                    </body>  </html>  """, height=800,)
        
       