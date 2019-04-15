import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_properties_2016():
    return pd.read_sql('SELECT pr.*, pred.logerror, pred.transactiondate, act.airconditioningdesc, arc.architecturalstyledesc, bct.buildingclassdesc, hst.heatingorsystemdesc, plut.propertylandusedesc, sty.storydesc, tyco.typeconstructiondesc\
    FROM predictions_2016 as pred\
    LEFT JOIN properties_2016 as pr USING (parcelid)\
    LEFT JOIN airconditioningtype as act USING (airconditioningtypeid)\
    LEFT JOIN architecturalstyletype as arc USING (architecturalstyletypeid)\
    LEFT JOIN buildingclasstype as bct USING (buildingclasstypeid)\
    LEFT JOIN heatingorsystemtype as hst USING (heatingorsystemtypeid)\
    LEFT JOIN propertylandusetype as plut USING (propertylandusetypeid)\
    LEFT JOIN storytype as sty USING (storytypeid)\
    LEFT JOIN typeconstructiontype as tyco USING (typeconstructiontypeid)\
    WHERE latitude IS NOT NULL OR longitude IS NOT NULL;', get_connection('zillow'))

def get_properties_2017():
    return pd.read_sql('SELECT pr.*, pred.logerror, pred.transactiondate, act.airconditioningdesc, arc.architecturalstyledesc, bct.buildingclassdesc, hst.heatingorsystemdesc, plut.propertylandusedesc, sty.storydesc, tyco.typeconstructiondesc\
    FROM predictions_2017 as pred\
    LEFT JOIN properties_2017 as pr USING (parcelid)\
    LEFT JOIN airconditioningtype as act USING (airconditioningtypeid)\
    LEFT JOIN architecturalstyletype as arc USING (architecturalstyletypeid)\
    LEFT JOIN buildingclasstype as bct USING (buildingclasstypeid)\
    LEFT JOIN heatingorsystemtype as hst USING (heatingorsystemtypeid)\
    LEFT JOIN propertylandusetype as plut USING (propertylandusetypeid)\
    LEFT JOIN storytype as sty USING (storytypeid)\
    LEFT JOIN typeconstructiontype as tyco USING (typeconstructiontypeid)\
    WHERE latitude IS NOT NULL OR longitude IS NOT NULL;', get_connection('zillow'))

def get_zillow_csv():
    df_2016 = get_properties_2016()
    df_2017 = get_properties_2017()
    zillow = df_2016.append(df_2017, ignore_index=True)
    export_csv = zillow.to_csv(r'../Clustering/zillow_properties.csv', index=False)
    return export_csv

# def get_zillow_csv():
#     df_2016 = get_properties_2016()
#     df_2017 = get_properties_2017()
#     zillow = df_2016.append(df_2017, ignore_index=True)
#     export_csv = zillow.to_csv(r'zillow_properties.csv', index=False)
#     return export_csv

# def get_logerror_2016():
#     return pd.read_sql('SELECT *\
#     FROM predictions_2016;', get_connection('zillow'))

# def get_logerror_2017():
#     return pd.read_sql('SELECT *\
#     FROM predictions_2017;', get_connection('zillow'))

# def get_properties_2016_csv():
#     df = get_properties_2016()
#     export_csv = df.to_csv(r'properties_2016.csv')
#     return export_csv

# def get_properties_2017_csv():
#     df = get_properties_2017()
#     export_csv = df.to_csv(r'properties_2017.csv')
#     return export_csv

# def get_logerror_2016_csv():
#     df = get_logerror_2016()
#     export_csv = df.to_csv(r'predictions_2016.csv')
#     return export_csv

# def get_logerror_2017_csv():
#     df = get_logerror_2017()
#     export_csv = df.to_csv(r'predictions_2017.csv')
#     return export_csv