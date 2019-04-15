import env
import pandas as pd

def reindex_zillow(df):
    return df.reindex_axis(['parcelid',
 'logerror',
 'bedroomcnt',
 'bathroomcnt',
 'calculatedfinishedsquarefeet',
 'transactiondate',
 'yearbuilt',
 'fips',
 'latitude',
 'longitude',
 'airconditioningtypeid',
 'airconditioningdesc',
 'architecturalstyletypeid',
 'architecturalstyledesc',
 'basementsqft',
 'buildingclasstypeid',
 'buildingqualitytypeid',
 'buildingclassdesc',
 'calculatedbathnbr',
 'decktypeid',
 'finishedfloor1squarefeet',
 'finishedsquarefeet12',
 'finishedsquarefeet13',
 'finishedsquarefeet15',
 'finishedsquarefeet50',
 'finishedsquarefeet6',
 'fireplacecnt',
 'fullbathcnt',
 'garagecarcnt',
 'garagetotalsqft',
 'hashottuborspa',
 'heatingorsystemtypeid',
 'heatingorsystemdesc',
 'lotsizesquarefeet',
 'poolcnt',
 'poolsizesum',
 'pooltypeid10',
 'pooltypeid2',
 'pooltypeid7',
 'propertycountylandusecode',
 'propertylandusetypeid',
 'propertylandusedesc',
 'propertyzoningdesc',
 'rawcensustractandblock',
 'regionidcity',
 'regionidcounty',
 'regionidneighborhood',
 'regionidzip',
 'roomcnt',
 'storytypeid',
 'storydesc',
 'threequarterbathnbr',
 'typeconstructiontypeid',
 'typeconstructiondesc',
 'unitcnt',
 'yardbuildingsqft17',
 'yardbuildingsqft26',
 'numberofstories',
 'fireplaceflag',
 'structuretaxvaluedollarcnt',
 'taxvaluedollarcnt',
 'assessmentyear',
 'landtaxvaluedollarcnt',
 'taxamount',
 'taxdelinquencyflag',
 'taxdelinquencyyear',
 'censustractandblock'], axis=1) 

def drop_land_listings(df):
    df.drop(df[df['bedroomcnt'] == 0.0].index, inplace=True)
    df.drop(df[df['bathroomcnt'] == 0.0].index, inplace=True)
    df.drop(df[df['unitcnt'] >= 2.0].index, inplace=True)
    df.drop(df[(df['propertylandusedesc'] != 'Single Family Residential') &\
      (df['propertylandusedesc'] != 'Mobile Home') &\
      (df['propertylandusedesc'] != 'Manufactured, Modular, Prefabricated Homes')].index, inplace=True)
    return df

def convert_num_to_categorical(df):
    list_of_cols = ['fips', 'airconditioningtypeid', 'architecturalstyletypeid', 'decktypeid', 'fireplacecnt', 'hashottuborspa', 'poolcnt', 'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'propertylandusetypeid', 'regionidcounty', 'storytypeid', 'threequarterbathnbr', 'typeconstructiontypeid', 'unitcnt', 'numberofstories', 'fireplaceflag', 'assessmentyear']
    for col in list_of_cols:
        df[[col]] = df[[col]].astype('category')
    return df

def convert_numerical_object_to_int(df):
    df['transactiondate'] = pd.to_numeric(df.transactiondate.str.replace('-', ''))
    cols_to_numeric = ['transactiondate']
    for col in cols_to_numeric:
        df[[col]] = df[[col]].astype(int)
    return df