from matplotlib.pyplot import plot
import streamlit as st
import pandas as  pd
import plotly.express as px
import math
import altair as alt



st.set_page_config(layout = "wide")
with st.expander("Prolog"):
    st.write("""
            DATA
            LIVERPOOL SEASON 2022/2023
        """)

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vROcIrUdyEOKaO4H7Rm7O7ccrfbeEkvab9Oa9pzG-FLFtoxLt6DLj01Qpyouhs2hY9yxX3O6qSJ9feS/pub?gid=1037807105&single=true&output=csv')

df

st.title('Scatter Plot: Jumlah Gol')

data_sorted = df.sort_values(by='Gls', ascending=False)
data_sorted = df[df["Gls"].notnull() & (df["Gls"] != 0)]

player = data_sorted['Player']
gols = data_sorted['Gls']

fig = px.scatter(data_frame=data_sorted, x=player, y=gols)
st.plotly_chart(fig)

total_gls = df["Gls"].sum()
# Menampilkan hasil
total_gls

# Menghitung jumlah gol berdasarkan kelompok posisi
jumlah_gol = data_sorted.groupby("Pos")["Gls"].sum().reset_index()

# Mengurutkan kelompok posisi berdasarkan jumlah gol secara menurun
jumlah_gol = jumlah_gol.sort_values(by="Gls", ascending=False)

# Mengatur urutan kelompok posisi untuk pengkodean warna
posisi_order = jumlah_gol["Pos"].tolist()

# Mengurutkan data berdasarkan urutan kelompok posisi
data = data_sorted[data_sorted["Pos"].isin(posisi_order)]
data_sorted = df[(df["Gls"].notnull()) & (df["Gls"] != 0) | (df["Ast"].notnull()) & (df["Ast"] != 0)]
scatter_plot = alt.Chart(data_sorted).mark_circle().encode(
    x="Gls",
    y="Ast",
    color="Player",
    tooltip=["Player", "Gls", "Ast"]
).interactive()

# Menampilkan scatter plot
st.altair_chart(scatter_plot, use_container_width=True)


# Reshape data
data_sorted2 = pd.melt(data, id_vars='Player', value_vars=['Gls', 'Ast'], var_name='Attribute')
# Bar chart
chart1 = alt.Chart(data_sorted2).mark_bar().encode(
    x=alt.X('Attribute:N', sort=['Gls', 'Ast'], title='Attribute'),
    y=alt.Y('value:Q', title='Value'),
    column=alt.Column('Player', spacing=15),
    color=alt.Color('Attribute:N', legend=alt.Legend(title='Attribute', labelColor='red')),  # Mengubah warna bar dan teks pada legenda
    tooltip=['Player', 'Attribute', 'value'],
).properties(
    title='Bar Chart of Goals (Gls) and Assists (Ast) by Player',
    width=75,
    height=300
).configure_text(
    color='red'  # Mengubah warna teks menjadi putih
)
# Render chart using Streamlit
st.altair_chart(chart1)

# Data
data = pd.DataFrame({
    'Player': ['Player A', 'Player B', 'Player C', 'Player D'],
    'Goals': [10, 8, 5, 12],
    'Assists': [6, 4, 7, 3],
    'MinutesPlayed': [900, 1200, 800, 1000]
})
# Scatter plot
scatter_plot = alt.Chart(data).mark_circle().encode(
    x='Goals:Q',
    y='Assists:Q',
    size='MinutesPlayed:Q',
    color='Player:N',
    tooltip=['Player', 'Goals', 'Assists', 'MinutesPlayed']
).properties(
    title='Scatter Plot of Goals vs Assists',
    width=500,
    height=400
)
# Render chart using Streamlit
st.altair_chart(scatter_plot, use_container_width=True)



import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# URL gambar dari GitHub
url = "https://github.com/syahruaru/Visualization-data-pendidikan-bekasi/blob/main/Virgil%20van%20Dijk.png?raw=true"

# Mengambil gambar dari URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Menampilkan gambar menggunakan Streamlit
st.image(img, caption='Gambar')



