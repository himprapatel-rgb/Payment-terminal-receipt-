import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def make_receipt(data):
    w, h = 400, 850
    img = Image.new('RGB', (w, h), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font_reg = ImageFont.load_default()
        font_bold = ImageFont.load_default()
    except:
        font_reg = font_bold = ImageFont.load_default()

    draw.text((200, 40), "Southern Cross", anchor="mm", fill=0)
    draw.text((200, 60), "Southern Cross Central", anchor="mm", fill=0)
    draw.text((200, 100), "Wicklow", anchor="mm", fill=0)
    
    y = 170
    draw.text((20, y), f"DATE: {data['date']}", fill=0)
    draw.text((20, y+25), f"TIME: {data['time']}", fill=0)
    draw.text((20, y+50), f"TERMINAL: {data['terminal']}", fill=0)
    
    y = 350
    draw.line((20, y, 380, y), fill=0, width=2)
    draw.text((20, y+20), "TOTAL AMOUNT", fill=0)
    draw.text((380, y+20), f"€{data['amount']}", anchor="ra", fill=0)
    draw.line((20, y+55, 380, y+55), fill=0, width=2)
    draw.text((200, y+100), "APPROVED", anchor="mm", fill=0)
    return img

st.title("Receipt Generator")
d = st.text_input("Date", "04/02/2026")
t = st.text_input("Time", "10:11:38")
a = st.text_input("Amount (€)", "45.00")
term = st.text_input("Terminal ID", "195474001")

if st.button("Generate"):
    st.image(make_receipt({"date": d, "time": t, "amount": a, "terminal": term}))
