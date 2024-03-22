from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_market_trend')
def get_market_trend():
    response = jsonify({
        'marketTrend': util.get_market_trend()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_sales_channel')
def get_sales_channel():
    response = jsonify({
        'salesChannel': util.get_sales_channel()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_product_type')
def get_product_type():
    response = jsonify({
        'productType': util.get_product_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_customer_base')
def get_customer_base():
    response = jsonify({
        'customerBase': util.get_customer_base()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_competitor')
def get_competitor():
    response = jsonify({
        'competitor': util.get_competitor()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_marketing_campaign')
def get_marketing_campaign():
    response = jsonify({
        'marketingCampaign': util.get_marketing_campaign()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_financial_health')
def get_financial_health():
    response = jsonify({
        'financialHealth': util.get_finacial_health()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_employee_performance')
def get_employee_performance():
    response = jsonify({
        'employeePerformance': util.get_employee_performance()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_investment_funding')
def get_investment_funding():
    response = jsonify({
        'investmentFunding': util.get_investment_funding()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_customer_feedback')
def get_customer_feedback():
    response = jsonify({
        'customerFeedback': util.get_customer_feedback()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/classify_plan', methods=['POST'])
def classify_plan():
    marketing_budget = float(request.form['marketing_budget'])
    customer_acquisition_cost = float(request.form['customer_acquisition_cost'])
    market_trend = request.form['market_trend']
    sales_channel = request.form['sales_channel']
    product_type = request.form['product_type']
    customer_base = request.form['customer_base']
    sales_competitor = request.form['sales_competitor']
    marketing_campaign = request.form['marketing_campaign']
    financial_health = request.form['financial_health']
    employee_performance = request.form['employee_performance']
    investment_funding = request.form['investment_funding']
    customer_feedback = request.form['customer_feedback']

    marketing_budget = int(marketing_budget)
    customer_acquisition_cost = int(customer_acquisition_cost)

    result = util.classify_plan(marketing_budget, customer_acquisition_cost, market_trend,
                                             sales_channel, product_type, customer_base, sales_competitor,
                                             marketing_campaign, financial_health, employee_performance, investment_funding,
                                             customer_feedback)
    
    plan_result = 'This is a success plan' if result == 1 else 'This is a failure plan'
    
    response = jsonify({
        'classify_plan' : plan_result
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == '__main__':
    print("Starting Python Flask server for plan classification")
    util.load_saved_artifacts()
    app.run()
