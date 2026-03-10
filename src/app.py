import streamlit as st
import pandas as pd
import plotly.express as px

from utils import format_currency
from models import Expense
from database import create_table, add_expense, get_expenses
from analytics import create_dataframe, expenses_by_category

# cria tabela se não existir
create_table()

st.title("💰 DevFinance AI")

st.subheader("Adicionar gasto")

title = st.text_input("Descrição")

category = st.selectbox(
    "Categoria",
    ["Comida", "Transporte", "Lazer", "Outros"]
)

amount = st.number_input(
    "Valor",
    min_value=0.0,
    step=1.0
)

date = st.date_input("Data")

# botão
if st.button("Adicionar"):

    expense = Expense(title, category, amount, str(date))

    add_expense(
        expense.title,
        expense.category,
        expense.amount,
        expense.date
    )

    st.success("Gasto adicionado!")

# buscar dados
data = get_expenses()

if data:

    df = create_dataframe(data)

    st.subheader("Tabela de gastos")

    df["amount"] = df["amount"].apply(format_currency)

    st.dataframe(df)

    st.subheader("Gastos por categoria")

    category_data = expenses_by_category(create_dataframe(data))

    fig = px.pie(
        values=category_data.values,
        names=category_data.index,
        title="Distribuição de gastos"
    )

    st.plotly_chart(fig)