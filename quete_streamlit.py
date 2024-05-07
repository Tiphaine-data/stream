import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Welcome!')

st.write("Je n'ai pas réussi à mettre une selectbox avec les continents, j'abandonne...")


url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url, sep =",")


df_num = df.select_dtypes(include='number').corr()

viz = sns.heatmap(df_num,cmap ="YlGn")
viz.set_title("Correlation Map of Car Features", pad=20)

st.pyplot(viz.figure)

# we generate a color palette with Seaborn.color_palette()
pal = sns.color_palette(palette='coolwarm', n_colors=12)

# in the sns.FacetGrid class, the 'hue' argument is the one that is the one that will be represented by colors with 'palette'
g = sns.FacetGrid(data = df, row='year', hue='year', aspect=15, height=0.75, palette=pal)

# then we add the densities kdeplots for each year
g.map(sns.kdeplot, 'cylinders',
      bw_adjust=1, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)

# here we add a horizontal line for each plot
g.map(plt.axhline, y=0,lw=2, clip_on=False)

g.fig.suptitle("Density of Car Cylinders by Year of Manufacture",
               fontsize=15,
               fontweight='bold',
               ha='center',y=1.05)

st.pyplot(g.figure)



import streamlit as st
import pandas as pd
import plotly.express as px

# Titre de l'application Streamlit
st.title("MPG vs. Year by Continent")

# Création des widgets qui changeront le graphique
selected_continent = st.selectbox("Choose a Continent:", ['US', 'Japan', 'Europe'])

# Filtrage des données en fonction du continent sélectionné
filtered_df = df[df['continent'] == selected_continent]

# Création du graphique Plotly Express
fig = px.line(filtered_df, x='year', y='mpg', title=f"MPG over Years in {selected_continent}")

# Affichage du graphique Plotly dans Streamlit
st.plotly_chart(fig)




fig1 = px.bar(df, x="year", y="hp", color='continent', barmode='group')

fig1.update_layout(title="Engine Power by Year and Continent")

st.plotly_chart(fig1)