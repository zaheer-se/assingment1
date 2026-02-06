import pandas as pd
import argparse

def clean_data(input1, input2, output_path):
    # Step 1: Merge the two files based on respondent IDs
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    
    # Hint 1: Use pandas.merge [cite: 21]
    # Merge respondent_id (file 1) and id (file 2) [cite: 16]
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    
    # Only keep one ID column to avoid redundancy [cite: 17]
    merged_df = merged_df.drop(columns=['id'])
    
    # Step 2: Drop any rows with missing values [cite: 18]
    merged_df = merged_df.dropna()
    
    # Step 3: Hint 2: Use str.contains and the ~ operator 
    # Drop respondents if job value contains 'insurance' or 'Insurance' [cite: 19]
    # The ~ operator indicates NOT 
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    
    # Step 4: Save the cleaned data to the path specified by the user [cite: 20]
    merged_df.to_csv(output_path, index=False)
    
    # Task 3: Print the shape of the output file [cite: 37]
    print(merged_df.shape)

if __name__ == "__main__":
    # Task 2: Setup positional arguments [cite: 14, 15]
    parser = argparse.ArgumentParser()
    parser.add_argument("input1")
    parser.add_argument("input2")
    parser.add_argument("output")
    
    args = parser.parse_args()
    
    clean_data(args.input1, args.input2, args.output)