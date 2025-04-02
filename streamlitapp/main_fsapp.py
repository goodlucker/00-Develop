# main_fsapp()
import streamlit as st
from utils import greeting
from data_processing import add, multiply

# 设置应用程序的标题
st.title("调用多个 Python 文件的 Streamlit 应用")

# 使用 utils.py 中的函数
name = st.text_input("输入你的名字")
if name:
    st.write(greeting(name))

# 使用 data_processing.py 中的函数
num1 = st.number_input("输入第一个数字", value=0)
num2 = st.number_input("输入第二个数字", value=0)

if st.button("计算加法和乘法"):
    sum_result = add(num1, num2)
    product_result = multiply(num1, num2)
    
    st.write(f"{num1} + {num2} = {sum_result}")
    st.write(f"{num1} * {num2} = {product_result}")