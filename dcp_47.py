#Given February 13, 2020

#Given an array of numbers representing the stock prices of a company
#in chronological order, write a function that calculates the maximum
#profit you could have made from buying and selling that stock once.
#You must buy before you can sell it.

#For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
#could buy the stock at 5 dollars and sell it at 10 dollars.

def maxProfit(prices : list):
    #if there are less than 2 prices, the function cannot calculate the
    #max profit made from buying and selling the stock once
    assert(len(prices) >= 2), "Error: List of prices is not long enough!"

    #in a case with the smallest possible list, the only possibility
    #is to return the last value - first value
    lowestBuy = prices[0]
    indexLowestBuy = 0
    
    for i in range(len(prices)):
        #the lowest buy price wouldn't be at the end because we wouldn't
        #be able to sell after the end
        if i != len(prices) - 1:
            if prices[i] < lowestBuy:
                lowestBuy = prices[i]
                indexLowestBuy = i

    #highest sell can only be determined after lowest buy is found...
    highestSell = prices[indexLowestBuy + 1]
    for i in range(indexLowestBuy + 1, len(prices)):
        if prices[i] > highestSell:
            highestSell = prices[i]
        
    return highestSell - lowestBuy


if __name__ == "__main__":
    print(maxProfit([3, 1]))
    print(maxProfit([9, 11, 8, 5, 7, 10]))
    print(maxProfit([19, 2, 4, 20, 24, 200, 18, 202]))
    print(maxProfit([2, 9, 1]))
