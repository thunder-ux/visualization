import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
st.title("Advanced School Management Data Visualization")
#Sidebar for user options 
st.sidebar.title('Options')
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    #  Load the dataset
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.write(df.head())
    st.write("### Data Preview")
    st.write(df.tail())
    #Let user select type of plot
    plot_type = st.sidebar.selectbox(
        "Select Plot Type",
        ["Scatter Plot", "Bar Plot", "Box Plot", "Heatmap", "Violin Plot", "Pair Plot"]
    )
    #Select x and y axis coulmns for applicable plot types
    if plot_type != "Heatmap" and plot_type != "Pair Plot":
        st.sidebar.write("### Select Axes")
        x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)
    #Plot customization options
    if plot_type != "Heatmap" and plot_type != "Pair Plot":
        st.sidebar.write("### Customization Options")
        color = st.sidebar.selectbox("Choose Color",["blue", "green", "red", "purple", "orange"])
        size = st.sidebar.slider("Point Size", 1, 10, 5)
        grid = st.sidebar.checkbox("Show Grid", True)
    #Plot the selected graph
    st.write("### Plot Preview")
    plt.figure(figsize=(10,6))
    #Scatter Plot
    if plot_type == "Scatter Plot":
        sns.scatterplot(x=x_axis, y=y_axis, data=df, color=color, s=size * 10)
        if grid:
            plt.grid()
            st.pyplot(plt)
    #Violin Plot
    elif plot_type == "Violin Plot":
        sns.violinplot(x=x_axis, y=y_axis, data=df, color=color)
        if grid:
            plt.grid()
            st.pyplot(plt)