The ultimate goal of this assignment is to search for a profitable trading strategy. In particular, we want you to study the provided historical data, and try to find a trading strategy which you would be comfortable to trade with your own money on unobserved data. Similarly, we would like you to give a solid reasoning why your trading strategy is good (imagine you want to persuade someone else to put their money into your trading), given that you find one.

___________________________________________________

Imagine you are trading a certain asset. Historical prices of the asset at times "t" can be found in the first column of the file “FP_models.csv”. Assume no trading fees and perfectly liquid market - there is always someone to buy from you or to sell you for the given market price no matter the amount.

You have 100k and three models at your disposal - model A, model B and model C. All three of the models tell you what the "fair price" for that asset should be at the given time. In particular, models A,B,C at time “t” might influence your trading decision at time “t” – it is up to you to figure out how exactly. You can find these prices in their respective columns of “FP_models.csv”.


As a part of your solution, you should be able to provide answers and the source code for these questions:
1. How would you decide which model does a better job at helping you trade?
2. How would you assess the profitability of your strategy in the given period?
3. How would your strategy / profit change with a fee 0.01% per trade? Could you find a profitable trading strategy now?


There is no “correct” solution to this assignment. There are only “wrong” ones and “better”/”worse” ones. An example of the wrong solution would be coming up with an unprofitable trading strategy while thinking it is profitable. Beware, it is entirely possible that no profitable strategy exists based on the provided data.
	•	
