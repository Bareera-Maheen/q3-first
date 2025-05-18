import streamlit as st
#  i am gonna use a word streamlit as st for short key word
# and while assigning the function i will assign with same name for easily understandable
# now new thing we will add three parameters in function the value (which value we wanto convert 
# like meter , kilogram, litters , and many more ) , and the second 
# willbe unit form (from which unit we want  to convert) and last one will be unit_to 
# ( to which unit we want in conversion form 
# like  (mili meter, mili gram , mili liter etc)
def unit_convertor( value ,unit_from , unit_to):
    conversion_factors ={
       
            # 1 meter wil be convert in kilometer 

            "meters_kilmeters":0.001,
            # 2 kilometer will be convert in meter
            "kiloimeters_meters":1000,
            # 3 centimeter
            # "centimeter":100,
            # "millimeter":1,
            # "micrometer":0.000001,
            # "nanometer":0.000000001,
            # "mile":0.000621371,
            # kilogram to gram
            "kilgrams_grams":1000,
            # gram to kilogram
            "grams_kilograms":0.001,
            # gram to milligram
            "milligrams_grams":1,

                  
             
    }
    # we will variable with the name of key  and we will define the key with f string 
    #  ( and why we use f string because we want dynamic value)
    # from which value(unit_form) to which value(unit_to) and this is generating unique key for conversion 
    key =f"{unit_from}_{unit_to}"
    if key in conversion_factors:
        # the one key [key] which is stored in square bracket is the key of dictionary which has the 
        # function to storing value of conversion-factors  in  to conversion_factor
        conversion_factor = conversion_factors[key]
        return value * conversion_factor
    else:
        return "we don't have this conversion unit this time try again"
    # now we will some ui from streamlit
st.title("Unit - Convertor")
# now we wil define the variable with streamlit UI 
value = st.number_input("Enter the Value here")
# we will  create the one select box for unit_from
# enter which unit you want to conert and we will put the units we have in our dictionary like(meter andkilometer..etc)
unit_from=st.selectbox("convert from",["meters","kilometers","grams","kilograms","milligrams"])
#  and now box for unit_to 
unit_to=st.selectbox("convert to",["meters","kilometers","grams","kilograms","milligrams"])
#  we will create button to convert the unit
if st.button("convert"):
    # for the result value i will take the function name i have define above and pass the 
    # parameters which we also define the function (value , unit_from , unit_to)
    result=unit_convertor( value,unit_from,unit_to)
    # for show the result we will write a short message with help of streamlit UI
    st.write(f"here is your converted value:{result}")
    # for run the app which we have created we will use  write the commnd interminal
    # streamlit run unit-convertor-main.py


   
   