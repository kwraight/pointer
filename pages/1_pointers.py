import streamlit as st

import os
import sys
import json
import subprocess
import altair as alt
import pandas as pd

import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


### introduction
st.title('Pointer App')
st.write('### List of other places')
st.write("---")


##################
### useful funcitons
##################

def GetPorts(nameList):
### todo

    return None


##################
### main part
##################

st.write("---")

st.write("## Pointers")


if "port_dict" not in st.session_state.keys() or st.button("Check ports?"):
    st.session_state['port_dict']=[
        {'name':"grafana", 'port':3000},
        {'name':"listerApp", 'port':8505},
        {'name':"stsApp", 'port':8504}
    ]

thisIP=get_ip()
# st.write("using IP:",thisIP)

for pd in st.session_state['port_dict']:
    st.write(f"__{pd['name']}__ port: {pd['port']}")
    link=f"Try link [here](https://{thisIP}:{str(pd['port'])})"
    st.markdown(link,unsafe_allow_html=True)

