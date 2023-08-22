import os
import numpy as np
import pandas as pd
import re
import plotly.express as px
# customize to simple-white theme
import plotly.io as pio
import pandasplus

META_GROUP = 'meta-group'
pio.templates.default = "simple_white"
from pandas import DataFrame

CONTROL = 'control'
TEST = "test"
GROUP = 'group'
MODEL_NAME = 'model_name'


def is_score_pattern(s):
    pattern = r"\w+\s*:\s*\d+(\.\d+)?\W*"
    return re.fullmatch(pattern, s) is not None

def parse_metrics(file) -> dict:
    metrics = {}
    metrics[MODEL_NAME] = os.path.basename(file).replace("_metrics.txt", "")
    with open (file, "r") as f:
        for line in f.readlines():
            if is_score_pattern(line):
                key, value = line.split(":")
                metrics[key] = float(value.replace("\n", "").lstrip())
    return metrics

def load_results(results_dir : str):
    results = []
    for file in os.listdir(results_dir):
        if file.endswith("_metrics.txt"):
            results.append(parse_metrics(
                os.path.join(results_dir, file))
            )
    return pd.DataFrame(results)


def melt_and_plot(df, group_values = []):
    # Create a bar graph using Plotly Express
    melted_df = pd.melt(df, id_vars=[GROUP],
                        var_name='metric',
                        value_name='value')
    if group_values:
        melted_df = melted_df[melted_df[GROUP].isin(group_values)]
    # Show the graph
    fig = px.bar(melted_df,
                 x='metric', y='value', color=GROUP,
                 color_discrete_map={'control': 'darkturquoise',
                                     'test': 'darksalmon'},
                 title="Difference between Test and Control for Each Metric",
                 labels={'metric': 'Metric', 'difference': 'Difference'},
                 barmode='group', hover_data=['value'])
    fig.show()


def process_results(raw_results : DataFrame):
    raw_results[MODEL_NAME] = raw_results[MODEL_NAME].str.replace("_trim", "")
    raw_results[GROUP] = raw_results[MODEL_NAME].apply(
        lambda x: TEST if 'test' in x else CONTROL
    )
    # Calculate average values for each column
    numeric_cols = raw_results.select_dtypes(include=[np.number]).columns
    avg_test = raw_results[raw_results[GROUP] == TEST][numeric_cols].mean()
    avg_control = raw_results[raw_results[GROUP] == CONTROL][
        numeric_cols].mean()
    # Calculate the difference between the average values
    diff = avg_test - avg_control
    # Calculate the percentage difference between the average values
    diff_percent = diff / avg_control * 100
    # Create a new dataframe with the results
    df = pd.DataFrame([avg_test, avg_control, diff, diff_percent])
    df.drop('ratio', axis=1, inplace=True)
    df[GROUP] = [TEST, CONTROL, 'diff', 'diff_percent']
    return df

def display_results():
    # Display the results
    test_path = 'results-test'
    raw_results = load_results(test_path)
    test_df = process_results(raw_results)
    test_df[META_GROUP] = 'ling'
    control_path = 'results-control'
    raw_results = load_results(control_path)
    control_df = process_results(raw_results)
    control_df[META_GROUP] = 'reg'
    # melt_and_plot(df, group_values=[TEST, CONTROL])
    df = pd.concat([test_df, control_df], axis=0)
    pandasplus.print_full(df)

if __name__ == '__main__':
    # Display the results
    test_path = 'results-test'
    raw_results = load_results(test_path)
    test_df = process_results(raw_results)
    test_df[GROUP] = 'ling-' + test_df[GROUP]
    control_path = 'results-control'
    raw_results = load_results(control_path)
    control_df = process_results(raw_results)
    control_df[GROUP] = 'reg-' + control_df[GROUP]
    df = pd.concat([test_df, control_df], axis=0)
    melt_and_plot(df, group_values=['ling-' +TEST, 'reg-' +TEST,
                                    'reg-'+CONTROL])
    # pandasplus.print_full(df)
