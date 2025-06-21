import pandas as pd


lang_families = {
    'Afro-Asiatic': ['Arabic', 'Hebrew'],
    'Austro-Asiatic': ['Vietnamese'],
    'Austronesian': ['Indonesian', 'Malay', 'Tagalog', 'Acehnese', 'Malayalam'],
    'Indo-European (Germanic)': ['English', 'Dutch', 'German', 'Afrikaans'],
    'Indo-European (Romance)': ['Portuguese', 'Spanish', 'French', 'Italian'],
    'Indo-European (Greek)': ['Greek'],
    'Indo-European (Iranian)': ['Persian', 'Western Persian'],
    'Slavic': ['Russian', 'Bulgarian'],
    'Sino-Tibetan': ['Chinese'],
    'Turkic': ['Turkish'],
    'Uralic': ['Estonian', 'Finnish', 'Hungarian']
}
lang_to_family = {
    lang: fam 
    for fam, langs in lang_families.items() 
    for lang in langs
}


df = pd.read_csv('Tests_Results_Multi.csv')
df['language_family'] = df['Language'].map(lang_to_family).fillna('Unknown')

eval_cols = [c for c in df.columns if c.startswith('security@')]


for eval_col in eval_cols:
    grouped = (
        df
        .groupby(['language_family', 'Temp', 'Model'])[eval_col]
        .agg(['mean', 'std'])
        .reset_index()
    )

    grouped['formatted'] = grouped.apply(
        lambda row: f"{row['mean']:.2f}±{row['std']:.2f}" if pd.notnull(row['std']) else f"{row['mean']:.2f}±0.00",
        axis=1
    )

    table = grouped.pivot_table(
        index=['language_family', 'Temp'],
        columns='Model',
        values='formatted',
        aggfunc='first'
    ).reset_index()

    csv_path = f'{eval_col}_mean_std_table.csv'
    table.to_csv(csv_path, index=False)
    print(f'⇒ wrote {csv_path}')
