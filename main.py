import streamlit as st
import time

st.title('Streamlit入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ')
expander.write('問合せ内容を書く') 

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text

# conddition = st.slider('あなたの今の調子は？', 0, 100, 5)
# 'コンディション:', conddition

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='kunio matsunaga', use_column_width=True)






