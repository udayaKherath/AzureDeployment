import json
import pickle
import numpy as np

__marketTrend = None
__salesChannel = None
__productType = None
__customerBase = None
__competitor = None
__marketingCampaign = None
__finacialHealth = None
__employeePerformance = None
__investmentFunding = None
__customerFeedback = None
__data_columns = None
__model = None



def get_market_trend():
    return __marketTrend

def get_sales_channel():
    return __salesChannel

def get_product_type():
    return __productType

def get_customer_base():
    return __customerBase

def get_competitor():
    return __competitor

def get_marketing_campaign():
    return __marketingCampaign

def get_finacial_health():
    return __finacialHealth

def get_employee_performance():
    return __employeePerformance

def get_investment_funding():
    return __investmentFunding

def get_customer_feedback():
    return __customerFeedback


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __marketTrend
    global __salesChannel
    global __productType
    global __customerBase
    global __competitor
    global __marketingCampaign
    global __finacialHealth
    global __employeePerformance
    global __investmentFunding
    global __customerFeedback


    with open("./server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __marketTrend = __data_columns[2:5]
        __salesChannel = __data_columns[5:8]
        __productType = __data_columns[8:11]
        __customerBase = __data_columns[11:14]
        __competitor = __data_columns[14:17]
        __marketingCampaign = __data_columns[17:20]
        __finacialHealth = __data_columns[20:23]
        __employeePerformance = __data_columns[23:25]
        __investmentFunding = __data_columns[25:27]
        __customerFeedback = __data_columns[27:30]
    
    
    global __model
    with open("./server/artifacts/plan_classifier_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")


def classify_plan(Marketing_Budget, Customer_Acquisition_Cost, Market_Trend, Sales_Channel, 
                  Product_Type, Customer_Base, Competitor, Marketing_Campaign,
                  Financial_Health, Employee_Performance, Investment_Funding, Customer_Feedback):

    try:
       market_trend_index = __data_columns.index(Market_Trend.lower())
       Sales_Channel_index = __data_columns.index(Sales_Channel.lower())
       Product_Type_index = __data_columns.index(Product_Type.lower())
       Customer_Base_index = __data_columns.index(Customer_Base.lower())
       Sales_Competitor_index = __data_columns.index(Competitor.lower())
       Marketing_Campaign_index = __data_columns.index(Marketing_Campaign.lower())
       Financial_Health_index = __data_columns.index(Financial_Health.lower())
       Employee_Performance_index = __data_columns.index(Employee_Performance.lower())
       Investment_Funding_index = __data_columns.index(Investment_Funding.lower())
       Customer_Feedback_index = __data_columns.index(Customer_Feedback.lower())
    except:
       market_trend_index = -1
       Sales_Channel_index = -1
       Product_Type_index = -1
       Customer_Base_index = -1
       Sales_Competitor_index = -1
       Marketing_Campaign_index = -1
       Financial_Health_index = -1
       Employee_Performance_index = -1
       Investment_Funding_index = -1
       Customer_Feedback_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Marketing_Budget
    x[1] = Customer_Acquisition_Cost
    if market_trend_index >= 0:
        x[market_trend_index] = 1

    if Sales_Channel_index >= 0:
        x[Sales_Channel_index] = 1

    if Product_Type_index >= 0:
        x[Product_Type_index] = 1

    if Customer_Base_index >= 0:
        x[Customer_Base_index] = 1

    if Sales_Competitor_index >= 0:
        x[Sales_Competitor_index] = 1

    if Marketing_Campaign_index >= 0:
        x[Marketing_Campaign_index] = 1

    if Financial_Health_index >= 0:
        x[Financial_Health_index] = 1

    if Employee_Performance_index >= 0:
        x[Employee_Performance_index] = 1

    if Investment_Funding_index >= 0:
        x[Investment_Funding_index] = 1

    if Customer_Feedback_index >= 0:
        x[Customer_Feedback_index] = 1

    return __model.predict([x])[0]


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_market_trend())
    #print(get_sales_channel())
    #print(get_product_type())
    #print(get_customer_base())
    #print(get_competitor())
    #print(get_marketing_campaign())
    #print(get_finacial_health())
    #print(get_employee_performance())
    #print(get_investment_funding())
    print(get_customer_feedback())

    #print(classify_plan(159404, 667, 'Market_Trend_Stable', 'Sales_Channel_Online', 'Product_Type_Clothing', 'Customer_Base_Medium','Competitor_Low', 'Marketing_Campaign_Failed','Financial_Health_Healthy', 'Employee_Performance_0', 'Investment_Funding_1', 'Customer_Feedback_Negative')) 

"""
    print(classify_plan(159404, 667, 'Market_Trend_Stable', 'Sales_Channel_Direct', 'Product_Type_Clothing', 
                  'Customer_Base_Medium','Competitor_Low', 'Marketing_Campaign_Failed',
                  'Financial_Health_Healthy', 'Employee_Performance_0', 'Investment_Funding_1', 
                  'Customer_Feedback_Negative'))
    
    print(classify_plan(10000, 667, 'Market_Trend_Stable', 'Sales_Channel_Direct', 'Product_Type_Clothing', 
                  'Customer_Base_Medium','Competitor_Low', 'Marketing_Campaign_Failed',
                  'Financial_Health_Healthy', 'Employee_Performance_0', 'Investment_Funding_1', 
                  'Customer_Feedback_Negative'))
    

    print(classify_plan(155057, 724, 'Market_Trend_Stable', 'Sales_Channel_Online', 'Product_Type_Electronics', 
                        'Customer_Base_Medium','Competitor_Low', 'Marketing_Campaign_Failed',
                        'Financial_Health_Healthy', 'Employee_Performance_1', 'Investment_Funding_1', 
                        'Customer_Feedback_Negative'))
"""