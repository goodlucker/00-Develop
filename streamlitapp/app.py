#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Rick.Xu
import streamlit as st
st.title('Interactive Presentation with Streamlit')
st.header('Introduction')
st.write('This is a simple interactive presentation using Streamlit.')
st.header('Data Visualization')
st.write('Here you can add some data visualization.')
# Example: Interactive widget
number = st.slider('Pick a number', 0, 100)
st.write(f'You selected: {number}')