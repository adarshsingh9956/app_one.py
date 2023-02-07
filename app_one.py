import streamlit  as st

st.title("Demo App")

n1 = st. number_input("enter number")
n2 = st. number_input("enter another number")
add = st.button("Add")
subtract = st.button("subtract")
mul = st.button("multiply")
div = st.button("Divide")
exponent=st.button("exponent")



if add:
    r = int(n1)+int(n2)
    st.success(r)
if subtract:
    r = int(n1)-int(n2)
    st.success(r)
if mul:
    r = int(n1)*int(n2)
    st.success(r)
if div:
    r = int(n1)/int(n2)
    st.success(r)
if exponent:
    r = int(n1)**int(n2)
    st.success(r)
