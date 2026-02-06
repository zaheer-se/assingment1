import pandas as pd
import argparse

def clean_data(input1, input2, output_path):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    
    merged_df = merged_df.drop(columns=['id'])
    
    merged_df = merged_df.dropna()

    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    
    merged_df.to_csv(output_path, index=False)
    
    print(merged_df.shape)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input1")
    parser.add_argument("input2")
    parser.add_argument("output")
    
    args = parser.parse_args()
    
    clean_data(args.input1, args.input2, args.output)