# pH Helper function
def count_specific_ph_columns_with_ranges(df: pd.DataFrame, count_column: str = 'pH_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific pH levels (pH 1 to pH 6) in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of pH columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # Generate the list of specific pH levels to look for
    specific_ph_levels = [f'pH {i}' for i in range(1, 11)]  # Assuming pH levels from 1 to 10

    # Identify columns containing any of the specific pH levels in their names
    ph_columns = df.columns[df.columns.str.contains('|'.join(specific_ph_levels))]

    # Count the number of identified 'ph' columns
    df[count_column] = len(ph_columns)
    
    
    return df

# Inject Helper function
def count_specific_Inject_columns_with_ranges(df: pd.DataFrame, count_column: str = 'Inject_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Inject levels (Inject 1 to Inject 12) in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Inject columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # Generate the list of specific Inject levels to look for
    specific_Inject_levels = [f'Inject {i}' for i in range(1, 13)]  # Assuming Inject levels from 1 to 12

    # Identify columns containing any of the specific Inject levels in their names
    Inject_columns = df.columns[df.columns.str.contains('|'.join(specific_Inject_levels))]
    
    # Count the number of identified 'Inject' columns
    df[count_column] = len(Inject_columns)
    
    return df

# Apparence helper function
def count_specific_Apparence_columns(df: pd.DataFrame, count_column: str = 'Apparence_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Apparence levels (Apparence 1 to Apparence 6) in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Apparence columns.

    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    # List of specific Apparence levels to look for
    specific_Apparence_levels = [f'Apparence {i}' for i in range(1, 11)]  # Assuming Apparence levels from 1 to 10
    
    # Identify columns containing any of the specific Apparence levels in their names
    Apparence_columns = df.columns[df.columns.str.contains('|'.join(specific_Apparence_levels))]
    
    # Count the number of identified 'Apparence' columns
    df[count_column] = len(Apparence_columns)
    
    return df

# Apparence_Piston_échelle helper function
def count_specific_Apparence_Piston_échelle_columns(df: pd.DataFrame, count_column: str = 'Apparence_Piston_échelle_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Apparence levels (Apparence 1 to Apparence 6) in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Apparence columns.

    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    # List of specific Apparence levels to look for
    specific_Apparence_levels = [f'Apparence Piston-échelle {i}' for i in range(1, 13)]  # Assuming Apparence Piston-échelle  levels from 1 to 12
    
    # Identify columns containing any of the specific Apparence levels in their names
    Apparence_columns = df.columns[df.columns.str.contains('|'.join(specific_Apparence_levels))]
    
    # Count the number of identified 'Apparence' columns
    df[count_column] = len(Apparence_columns)
    
    return df

# Lido helper function
def count_specific_Lido_columns_with_ranges(df: pd.DataFrame, count_column: str = 'Lido_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Lido levels (Lido 1 to Lido 20) in their names and creates multiple new columns
    for the count of these columns, and the count of columns with values within and outside the range [0.20, 0.35]

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Lido columns.
    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # List of specific Lido levels to look for
    specific_Lido_levels = [f'Lido {i}' for i in range(1, 21)]  # Assuming Lido levels from 1 to 20
    
    # Identify columns containing any of the specific Lido levels in their names
    Lido_columns = df.columns[df.columns.str.contains('|'.join(specific_Lido_levels))]
    
    # Count the number of identified 'Lido' columns
    df[count_column] = len(Lido_columns)
    
    return df
    

# DMA helper function
def count_specific_DMA_columns(df: pd.DataFrame, count_column: str = 'DMA_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific DMA levels in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of DMA columns.

    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    # List of specific DMA levels to look for
    specific_DMA_levels = [f'DMA {i}' for i in range(1, 11)]  # Assuming DMA levels from 1 to 11
    
    # Identify columns containing any of the specific DMA levels in their names
    DMA_columns = df.columns[df.columns.str.contains('|'.join(specific_DMA_levels))]
    
    # Count the number of identified 'DMA' columns
    df[count_column] = len(DMA_columns)
    
    return df

# LQAS helper function
def count_specific_LQAS_columns(df: pd.DataFrame, count_column: str = 'LQAS_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific LQAS levels (LQAS 1 to LQAS 6) in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of LQAS columns.

    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    # List of specific LQAS levels to look for
    specific_LQAS_levels = [f'LQAS {i}' for i in range(1, 11)] 
    
    # Identify columns containing any of the specific LQAS levels in their names
    LQAS_columns = df.columns[df.columns.str.contains('|'.join(specific_LQAS_levels))]
    
    # Count the number of identified 'LQAS' columns
    df[count_column] = len(LQAS_columns)
    
    return df

# NaHa/mg/ml helper function
def count_specific_NaHAml_columns_with_ranges(df: pd.DataFrame, count_column: str = 'NaHAml_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific NaHA mg/ml levels in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of NaHA/ml columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # List of specific NaHA mg/ml levels to look for
    specific_NaHAml_levels = [f'NaHA_ml {i}' for i in range(1, 11)]
    
    # Identify columns containing any of the specific NaHA_ml levels in their names
    NaHAml_columns = df.columns[df.columns.str.contains('|'.join(specific_NaHAml_levels))]
    
    # Count the number of identified 'NaHA/ml' columns
    df[count_column] = len(NaHAml_columns)
    
    return df

# NaHa/mg/g helper function
def count_specific_NaHA_mg_g_columns_with_ranges(df: pd.DataFrame, count_column: str = 'NaHA_mg_g_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific NaHA_mg_g levels in their names and creates multiple new columns
    for the count of these columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of NaHA_mg_g columns.
    
    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # List of specific NaHA_mg_g levels to look for
    specific_NaHA_mg_g_levels = [f'NaHA_g {i}' for i in range(1, 11)]
    
    # Identify columns containing any of the specific NaHA_mg_g levels in their names
    NaHA_mg_g_columns = df.columns[df.columns.str.contains('|'.join(specific_NaHA_mg_g_levels))]
    
    # Count the number of identified 'NaHA_mg_g' columns
    df[count_column] = len(NaHA_mg_g_columns)
    
    return df

def count_specific_CaHAP_columns(df: pd.DataFrame, count_column: str = 'CaHAP_Quant_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific CaHAP Quantity levels in their names
    and creates a new column with this count.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of CaHAP Quant columns.

    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    # List of specific CaHAP Quant levels to look for
    specific_CaHAP_Quant_levels = [f'CaHAP_Q_{i}' for i in range(1, 13)]  # Updated to include levels 1 to 12
    
    # Identify columns containing any of the specific CaHAP_Quant levels in their names
    CaHAP_Quant_columns = df.columns[df.columns.str.contains('|'.join(specific_CaHAP_Quant_levels))]
    
    # Count the number of identified 'CaHAP_Quant' columns (expected to be 10 as per your requirement)
    df[count_column] = len(CaHAP_Quant_columns)
    
    return df


# Rheo helper function
def count_specific_Rheo_columns(df: pd.DataFrame, count_column: str = 'Rheo_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Rheo levels.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Rheo levels columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # Generate the list of specific Rhéo levels to look for
    specific_rhéo_levels = [f'Rhéo_{i}' for i in range(1, 20)]
    
    # Identify columns containing any of the specific Rhéo levels in their names
    rhéo_columns = df.columns[df.columns.str.contains('|'.join(specific_rhéo_levels))]
    
    # Count the number of identified 'Rhéo_' columns
    df[count_column] = len(rhéo_columns)
    
    
    return df

# Osmo helper function
def count_specific_Osmo_columns(df: pd.DataFrame, count_column: str = 'Osmo_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific Osmo levels.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Osmo levels columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # Generate the list of specific Osmo levels to look for
    specific_osmo_levels = [f'Osmo {i}' for i in range(1, 11)]
    
    # Identify columns containing any of the specific Osmo levels in their names
    osmo_columns = df.columns[df.columns.str.contains('|'.join(specific_osmo_levels))]
    
    # Count the number of identified 'Osmo' columns
    df[count_column] = len(osmo_columns)
    
    return df

# CaHAP Ident helper function
def count_specific_CaHAP_Ident_columns(df: pd.DataFrame, count_column: str = 'CaHAP_Ident_samplesize_count') -> pd.DataFrame:
    """
    Counts the number of columns that match specific CaHAP_Ident levels.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    count_column (str): The name of the new column to store the count of Osmo levels columns.

    Returns:
    pd.DataFrame: The DataFrame with the new columns added.
    """
    # Generate the list of specific CaHAP_Ident levels to look for
    specific_CaHAP_Ident_levels = [f'CaHAP Ident. {i}' for i in range(1, 11)]
    
    # Identify columns containing any of the specific CaHAP Ident. levels in their names
    CaHAP_Ident_columns = df.columns[df.columns.str.contains('|'.join(specific_CaHAP_Ident_levels))]
    
    # Count the number of identified 'CaHAP Ident.' columns
    df[count_column] = len(CaHAP_Ident_columns)
    
    return df

