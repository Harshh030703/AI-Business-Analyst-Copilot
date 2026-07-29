import plotly.express as px


def create_chart(df, chart_type, x_col, y_col=None):

    if chart_type == "Bar Chart":
        return px.bar(df, x=x_col, y=y_col)

    elif chart_type == "Line Chart":
        return px.line(df, x=x_col, y=y_col)

    elif chart_type == "Scatter Plot":
        return px.scatter(df, x=x_col, y=y_col)

    elif chart_type == "Histogram":
        return px.histogram(df, x=x_col)

    elif chart_type == "Box Plot":
        return px.box(df, y=x_col)

    elif chart_type == "Pie Chart":
        return px.pie(df, names=x_col)

    return None
