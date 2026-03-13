# Input Files (Only change the path, not the names or text after the '#' leave the r before the quotes.)
IDENTIFICATION_MZML_FILE = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testdataDIA\20240427_HeLa-lysate_5ug_DIA-T2_Good.mzML"  # must be .mzML
PROTEIN_SEQUENCE_FILE = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\The Deuterium Calculator Test Files\Protein.txt"  # Must be .txt
IDENTIFICATION_PARQUET_FILE = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testdataDIA\diann_withmodified\report.parquet" # should be .parquet


# Output Files (Only change the path, not the names or text after the '#' leave the r before the quotes.)
FULL_HDX_OUTPUT = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testDIAdata2out\out1"  # No file extension
RECOMMENDATION_TABLE_1 = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testDIAdata2out\out2"  # No file extension
RECOMMENDATION_TABLE_2 = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testDIAdata2out\out3"  # No file extension
SUMMARY_TABLE = r"C:\Users\piercetf\Projects\TheDeuteriumCalculator-fork\testDIAdata2out\out4"  # No file extension


# Parameters (Only change the numbers and path, not the names or text after the '#'. Defaults given in parenthesis.)
# Step 1 Parameters
NOISE_LIMIT = 10000  # All individual peaks with less than this intensity ignored (10000)
PPM_MATCH_TOLERANCE = 10  # Peaks with less difference than this value matched to sequence (10)
SLIDING_WINDOW_PPM_TOLERANCE = 1  # Peaks with less difference than this value combined within each sliding window (1)
SLIDING_WINDOW_SIZE = 30  # width of sliding window in seconds, should be integer divisible by SLIDE_FRACTION (60)
SLIDE_FRACTION = 3  # Fraction of the window that the window moves each each slide (3)
RETENTION_TOLERANCE = 30  # window of retention times to search for given peptide (+-) (30)
DEUTERIUM_RECOVERY_RATE = 1  # The experimentally determined back exchange rate. (1)
DEUTERIUM_FRACTION = 0.833  # The fraction of D2O used in the experiment. (1)
CONDITION1 = "Free"  # This will be used in single condition experiments
CONDITION2 = "Complex"




# Constants (Change at your own risk; may cause incorrect results)
DEUTERIUM_MASS_DIFFERENCE = 1.00628
MASS_OF_WATER = 18.01528
MASS_OF_HYDROGEN = 1.007276
MINUTES_TO_SECONDS = 60

