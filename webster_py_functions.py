# Webster Functions

import pandas as pd
import numpy as np






# Extract classes from all columns of a data frame
#
# This function will extract the column classes from a data frame, returning a new data frame.
#
# @param dataset A data frame of the data for which we are building a dictionary.
# @return types A dataframe listing column names and their respective classes.
def get_feature_types(dataset):
    # Generate a data frame of column names and types
    feature_types = dataset.dtypes
    feature_types = feature_types.to_frame(name = 'type').reset_index()
    return(feature_types);






# Decorate the bare dicionary
#
# Adds decorators to the barebones dictionary. Adds Keep, Description, Notes columns
#
# @param dictionary A bare dictionary, in dataframe format, including column names and classes
#
# @return dictionary Decorated dictionary
def decorate_dictionary(dictionary):
    dictionary['keep'] = True
    dictionary['description'] = ""
    dictionary['notes'] = ""
    
    return(dictionary);






# Count unique levels
#
# Counts all unique values in a series, used in  the summary_stats function
#
# @param vector The input series
#
# @return count_unique A number, representing the count of unique levels
def count_unique(vector):

    count_unique = len(list(set(vector)))
    return(count_unique);



# Add summary stats
#
# Adds summary stats to the dictionary
#
# @param dataset The dataset for summary stats
#
# @return dataset.stats Data frame of summary statistics
def get_stats(dataset):
    
    num_stats = dataset.describe()
    num_stats = num_stats.transpose()
    num_stats.drop('count', axis = 1, inplace = True)

    # Get unique level counts
    summary_stats = dataset.apply(count_unique)
    summary_stats = summary_stats.to_frame(name = 'unique_levels')
    
    summary_stats = summary_stats.merge(num_stats, how = 'outer', left_index=True, right_index=True)
    
    # Get NA counts
    na_count = dataset.shape[0] - dataset.count()
    na_count = na_count.to_frame(name = 'na_count')
    
    summary_stats = na_count.join(summary_stats)
    
    # Fill in blanks with NaNs
    summary_stats = summary_stats.replace('', np.NaN)
    
    # Extract index
    summary_stats = summary_stats.reset_index()
    
    return(summary_stats);





#' Compile a data dictionary for a data frame
#'
#' Compiles a data dictionary for a data frame input
#'
#' @param dataset The dataframe to generate the dictionary
#' @param name The filename for the dictionary
#' @param path The filepath to locate the dictionary
#'
#' @return dict.temp The dictionary dataframe (Note: Not returned, the function will save the csv dictionary to the desired path)
#'
#' @examples
#' my.dictionary <- websteR::compile_dictionary(iris)
#'
#' @export
def compile_dictionary(dataset, autosave = False):
    # Get types
    dictionary = get_feature_types(dataset = dataset)
    # Decorate
    dictionary = decorate_dictionary(dictionary= dictionary)
    # Add summary_stats
    stats = get_stats(dataset= dataset)
    dictionary = dictionary.set_index('index').join(stats.set_index('index'))
    dictionary = dictionary.reset_index()
    
    # Set column types
    # df[['col2','col3']] = df[['col2','col3']].apply(pd.to_numeric)
    dictionary[['type']] = dictionary[['type']].astype('str')

    # Write CSV if autosave = true
    if autosave == True:
        dictionary.to_csv("./Dictionary.csv", na_rep="NaN")
    
    return(dictionary);




