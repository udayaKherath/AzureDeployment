function onClickedClassifyPlan(){
    console.log("classify plan button clicked");
    var marketBudget = document.getElementById("uiMarketingBudget").value;
    var customerAcquisitionCost = document.getElementById("uiCustomerAcquisitionCost").value;
    var marketTrend = document.getElementById("uiMarketTrend").value;
    var salesChannel = document.getElementById("uiSalesChannel").value;
    var productType = document.getElementById("uiProductType").value;
    var customerBase = document.getElementById("uiCustomerBase").value;
    var competitor = document.getElementById("uiCompetitor").value;
    var marketingCampaign = document.getElementById("uiMarketingCampaign").value;
    var financialHealth = document.getElementById("uiFinancialHealth").value;
    var employeePerformance = document.getElementById("uiEmployeePerformance").value;
    var investmentFunding = document.getElementById("uiInvestmentFunding").value;
    var customerFeedback = document.getElementById("uiCustomerFeedback").value;

    var classifyPlan = document.getElementById("uiClassifyPlan");

    var url = "http://127.0.0.1:5000/classify_plan";

    $.post(url, {
        marketing_budget: parseFloat(marketBudget),
        customer_acquisition_cost: parseFloat(customerAcquisitionCost),
        market_trend: marketTrend,
        sales_channel: salesChannel,
        product_type: productType,
        customer_base: customerBase,
        sales_competitor: competitor,
        marketing_campaign: marketingCampaign,
        financial_health: financialHealth,
        employee_performance: employeePerformance,
        investment_funding: investmentFunding,
        customer_feedback: customerFeedback
    }, function(data, status){
        console.log("Received data:", data);
        console.log("Status:", status);
        classifyPlan.innerHTML = "<h2>" + data.classify_plan.toString();
    });
}




function onPageLoad() {
    console.log("document loaded");

    // Fetch market trend data
    var marketTrendUrl = "http://127.0.0.1:5000/get_market_trend";
    $.get(marketTrendUrl, function(marketTrendData, status) {
        console.log("got response for get_market_trend request");
        if (marketTrendData) {
            var marketTrend = marketTrendData.marketTrend;
            var uiMarketTrend = $('#uiMarketTrend');
            uiMarketTrend.empty();
            for (var i in marketTrend) {
                var opt = new Option(marketTrend[i]);
                uiMarketTrend.append(opt);
            }
        }
    });

    // Fetch sales channel data
    var salesChannelUrl = "http://127.0.0.1:5000/get_sales_channel"; // Update the URL accordingly
    $.get(salesChannelUrl, function(salesChannelData, status) {
        console.log("got response for get_sales_channel request");
        if (salesChannelData) {
            var salesChannel = salesChannelData.salesChannel;
            var uiSalesChannel = $('#uiSalesChannel');
            uiSalesChannel.empty();
            for (var i in salesChannel) {
                var opt = new Option(salesChannel[i]);
                uiSalesChannel.append(opt);
            }
        }
    });

    // Fetch product type data
    var productTypeUrl = "http://127.0.0.1:5000/get_product_type"; // Update the URL accordingly
    $.get(productTypeUrl, function(productTypeData, status) {
        console.log("got response for get_product_type request");
        if (productTypeData) {
            var productType = productTypeData.productType;
            var uiProductType = $('#uiProductType');
            uiProductType.empty();
            for (var i in productType) {
                var opt = new Option(productType[i]);
                uiProductType.append(opt);
            }
        }
    });

    // Fetch customer base data
    var customerBaseUrl = "http://127.0.0.1:5000/get_customer_base"; // Update the URL accordingly
    $.get(customerBaseUrl, function(customerBaseData, status) {
        console.log("got response for get_customer_base request");
        if (customerBaseData) {
            var customerBase = customerBaseData.customerBase;
            var uiCustomerBase = $('#uiCustomerBase');
            uiCustomerBase.empty();
            for (var i in customerBase) {
                var opt = new Option(customerBase[i]);
                uiCustomerBase.append(opt);
            }
        }
    });

    // Fetch competitor data
    var competitorUrl = "http://127.0.0.1:5000/get_competitor"; // Update the URL accordingly
    $.get(competitorUrl, function(competitorData, status) {
        console.log("got response for get_competitor request");
        if (competitorData) {
            var competitor = competitorData.competitor;
            var uiCompetitor = $('#uiCompetitor');
            uiCompetitor.empty();
            for (var i in competitor) {
                var opt = new Option(competitor[i]);
                uiCompetitor.append(opt);
            }
        }
    });

    // Fetch marketing campaign data
    var marketingCamaignUrl = "http://127.0.0.1:5000/get_marketing_campaign"; // Update the URL accordingly
    $.get(marketingCamaignUrl, function(marketingCampaignData, status) {
        console.log("got response for get_marketing_campaign request");
        if (marketingCampaignData) {
            var marketingCampaign = marketingCampaignData.marketingCampaign;
            var uiMarketingCampaign = $('#uiMarketingCampaign');
            uiMarketingCampaign.empty();
            for (var i in marketingCampaign) {
                var opt = new Option(marketingCampaign[i]);
                uiMarketingCampaign.append(opt);
            }
        }
    });

    // Fetch financial health data
    var financialHealthUrl = "http://127.0.0.1:5000/get_financial_health"; // Update the URL accordingly
    $.get(financialHealthUrl, function(financialHealthData, status) {
        console.log("got response for get_financial_health request");
        if (financialHealthData) {
            var financialHealth = financialHealthData.financialHealth;
            var uiFinancialHealth = $('#uiFinancialHealth');
            uiFinancialHealth.empty();
            for (var i in financialHealth) {
                var opt = new Option(financialHealth[i]);
                uiFinancialHealth.append(opt);
            }
        }
    });

    // Fetch employee performance data
    var employeePerformanceUrl = "http://127.0.0.1:5000/get_employee_performance"; // Update the URL accordingly
    $.get(employeePerformanceUrl, function(employeePerformanceData, status) {
        console.log("got response for get_employee_performance request");
        if (employeePerformanceData) {
            var employeePerformance = employeePerformanceData.employeePerformance;
            var uiEmployeePerformance = $('#uiEmployeePerformance');
            uiEmployeePerformance.empty();
            for (var i in employeePerformance) {
                var opt = new Option(employeePerformance[i]);
                uiEmployeePerformance.append(opt);
            }
        }
    });

    // Fetch investment funding data
    var investmentFundingUrl = "http://127.0.0.1:5000/get_investment_funding"; // Update the URL accordingly
    $.get(investmentFundingUrl, function(investmentFundingData, status) {
        console.log("got response for get_investment_funding request");
        if (investmentFundingData) {
            var investmentFunding = investmentFundingData.investmentFunding;
            var uiInvestmentFunding = $('#uiInvestmentFunding');
            uiInvestmentFunding.empty();
            for (var i in investmentFunding) {
                var opt = new Option(investmentFunding[i]);
                uiInvestmentFunding.append(opt);
            }
        }
    });

    // Fetch customer feedback data
    var customerFeedbackUrl = "http://127.0.0.1:5000/get_customer_feedback"; // Update the URL accordingly
    $.get(customerFeedbackUrl, function(customerFeedbackData, status) {
        console.log("got response for get_customer_feedback request");
        if (customerFeedbackData) {
            var customerFeedback = customerFeedbackData.customerFeedback;
            var uiCustomerFeedback = $('#uiCustomerFeedback');
            uiCustomerFeedback.empty();
            for (var i in customerFeedback) {
                var opt = new Option(customerFeedback[i]);
                uiCustomerFeedback.append(opt);
            }
        }
    });
}



window.onload = onPageLoad;
