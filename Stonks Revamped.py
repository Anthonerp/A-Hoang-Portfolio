### WELCOME TO STONKS V.2 ###

from PIL import Image, ImageTk
from random import randint
from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt


win = False
money = 1000
moneyOverTime = [1000]
profit = 0
turnList = [0]
turn = 0
bullMarket = False
bearMarket = False


class Company(): #For all of the companies of the game
    
    global money
    global moneyOverTime
    global profit
    global turn
    
    
    
    def __init__(self, name, upValue, downValue, upChance, cost, stability, initCost): #Constructor to create the companies
        
        self.stockOwned = 0
        self.pastCost = [initCost]
        self.rollUpBonus = False
        self.rollDownBonus = False
        self.upValue = upValue
        self.downValue = downValue
        self.upChance = upChance
        self.cost = cost
        self.name = name
        self.stability = stability
        self.priceChange = 0
        self.turnList = [0]
        
    def buy(self, amount): #When the buy button is pressed
            
        global money
        global profit
        global moneyOverTime    
    
        self.stockOwned += amount
        money  -= (self.cost * amount)
        profit -= (self.cost * amount)
     
        if(money < 0): #For when the user doesn't have enough money
        
            self.stockOwned -= amount
            money += (self.cost * amount)
            messagebox.showwarning(title = "UH OH!", message = "YOU COULDN'T AFFORD THE STONK, NERD!")
            
    def sell(self, amount): #When the sell button is pressed
    
        global money
        global profit  
        global moneyOverTime 
 
        self.stockOwned -= amount
        money += (self.cost * amount)
        profit += (self.cost * amount)   
        
        
        if(self.stockOwned < 0):
            
            self.stockOwned += amount
            money -= (self.cost * amount)
            messagebox.showwarning(title = "UH OH!", message = "YOU TRIED TO SELL STOCKS YOU DIDNT HAVE! THATS CALLED FRAUD!")
    
    
    def change(self, turns): #To change the stock prices and roll for random events, also a child algorithm
        
        ceoFirstNames = ["Gregory","Jeff","BeefBoss","Rowley","Luke","Rae","Shaniqua","Obi-Wan","Finn","Katara","Aang","Sokka","Zuko","Iroh","Rosscoe"]
        ceoLastNames = ["Heffly","Skywalker","Kenobi","King","Johnson","Vader","of Arendel","of Memelandia","the Third","the Magician","the Massive","Elmer","of the Fire Nation", "Ross", "Hoang"]
       
        bullMarketCounter = 0
        bearMarketCounter = 0
        
        global bullMarket
        global bearMarket
        
        for turn in range(turns): #for loop to allow multiple turns at once
            
            chance = randint(1,100)
            updown = chance - self.upChance
            
            if(self.rollUpBonus == True): #If a company is rising, it will most likely keep rising
            
                updown -= 20
                self.rollDownBonus = False
                
            if (self.rollDownBonus == True): #If a company is losing, it will keep losing
            
                updown += 20
                self.rollUpBonus == False
                
            if (bullMarket == True): #If the bull market event is triggered
                
                updown -=20
                self.bearMarket = False
                bullMarketCounter += 1
                
                if(bullMarketCounter > 5): #Sets cap on bear market turn count
                    
                    bullMarket = False
                    bullMarketCounter = 0
                
            if (bearMarket == True): #If bear market is triggered
                updown += 20
                bullMarket = False
                
                if(bearMarketCounter > 5):
                    
                    bearMarket = False
                    bearMarketCounter = 0
                
            if(updown <=0):
                
                gain = randint(10,self.upValue)
                self.cost += gain
                self.pastCost.append(int(self.cost))
                self.priceChange = "+" + str(gain)
                
            if(updown > 0):
                
                loss = randint(10,self.downValue)
                self.cost -= loss
                self.pastCost.append(int(self.cost))
                self.priceChange = "-" + str(loss)
                
            deathCEO = randint(1,self.stability)
            
            if(deathCEO == 1): #death of a CEO causes company stats to change
                
                messagebox.showinfo("AN EVENT!", "THE CEO OF {} HAS DIED, AND HAS BEEN REPLACED BY {}".format(self.name.upper(), ceoFirstNames[randint(0,14)].upper() + " " + ceoLastNames[randint(0,14)].upper()))
                self.upValue = randint(15,300)
                self.downValue = randint(15,300)
                self.upChance = randint(10,95)
                self.stability = randint(100,1000)
            
            if(self.cost < 0): #Bankruptcy
            
                messagebox.showinfo("SURPRISE!", "{} HAS GONE BANKRUPT! THEY RECEIVED A GOVERNMENT BAIL-OUT AND A NEW CEO, {}".format(self.name.upper(), ceoFirstNames[randint(0,14)].upper() + " " + ceoLastNames[randint(0,14)].upper()))
                self.cost = 100
                self.upValue = 200
                self.downValue = 100
                self.upChance = 60
                self.stability = 20
                
    def graphPrice(self): #Uses pyplot to chart past stock costs
        
        global turnList
        
        plt.plot(turnList, self.pastCost)
        plt.show()

def graphMoney():
    
    plt.plot(turnList, moneyOverTime)
    plt.show()
        
def checkWin(): #Another child algorithm
            
    if (profit > 50000): #Basically the win screen
        
        top = Toplevel()
        win = True
            

def bullorbear(turns): #Checks to see if it will be a bear or bull market, also a child algorithm
    
    global bullMarket
    global bearMarket
    
    for t in range(turns):
    
        marketChance = randint(-20,20)
            
        if(marketChance == -10):
            
            bearMarket = True
            messagebox.showwarning("UH OH!", "IT IS NOW A BEAR MARKET!")
            
        if(marketChance == 10):
            
            bullMarket = True
            messagebox.showinfo("HOORAY!", "IT IS NOW A BULL MARKET")

def endTurn(self, turns): #Parent Algorithm

    if (win == False):

        self.MemeCorp.change(turns)
        self.TacoBaco.change(turns)
        self.SansUndertale.change(turns)
        self.KurgerBing.change(turns)
        self.Bapple.change(turns)
        self.Shmoogle.change(turns)
        self.Hugesoft.change(turns)
        self.McNaldos.change(turns)
        self.USSR.change(turns)
        self.Conk.change(turns)
        self.Bepis.change(turns)
        self.FlexTape.change(turns)
        
        bullorbear(turns)

    checkWin()
    
class Application(Company): #Tkinter GUI class

    MemeCorp = Company("Meme Corp", 300, 100, 70, 200, 100, 200)    #The intial stats for the companies
    TacoBaco = Company("Taco Baco", 500, 500, 50, 300, 50, 300)
    SansUndertale = Company("Sans Undertale", 15, 15, 90, 100, 300, 100)
    KurgerBing = Company("Kurger Bing", 100, 500, 95, 500, 500, 500)
    Bapple = Company("Bapple", 500, 15, 5, 2000, 300, 2000)
    Shmoogle = Company("Shmoogle", 500, 500, 50, 5000, 100, 5000)
    Hugesoft = Company("Hugesoft", 250, 250, 55, 1000, 500, 1000)
    McNaldos = Company("McNaldos", 50, 40, 50, 350, 200, 350)
    USSR = Company("USSR", 1000, 15, 90, 10000, 50, 10000)
    Conk = Company("Conk", 400, 100, 25, 500, 200, 500)
    Bepis = Company("Bepis", 100, 400, 75, 500, 200, 500)
    FlexTape = Company("Flex Tape", 10000, 15, 95, 1001, 200, 1001)

    def __init__(self): #Constructs the Screen

        global money

        def createpriceChange(company):
        
            if (int(company) < 0):
                return "red"
            
            if (int(company) > 0):
                return "green"

        self.master = Tk()
        self.master.title("Stonks!")
        

        #Header Stuff
        self.stockHeader = Label(self.master, text = "Stonk Name:")
        self.stockHeader.grid(row = 0, column = 0, sticky = W)
        self.priceHeader = Label(self.master, text = "Stonk Price:")
        self.priceHeader.grid(row = 0, column = 1, padx = 5, sticky = E)
        self.amountHeader = Label(self.master, text = "Price Change:")
        self.amountHeader.grid(row = 0, column = 2, padx = 5, sticky = E)
        self.changeHeader = Label(self.master, text = "Amount Owned:")
        self.changeHeader.grid(row = 0, column = 3, padx = 5, sticky = E)
        self.underline = Label(self.master, text = "------------------------------------------------------------------------------")
        self.underline.grid(row = 1, columnspan = 4, sticky = W)
        
        #Company Names
        self.memeconame = Label(self.master, text = self.MemeCorp.name).grid(row = 2, column = 0, pady = 5, sticky = W)
        self.tacobacoName = Label(self.master, text = self.TacoBaco.name).grid(row = 3, column = 0, pady = 5, sticky = W)
        self.sansundertaleName = Label(self.master, text = self.SansUndertale.name).grid(row = 4, column = 0, pady = 5, sticky = W)
        self.kurgerbingName = Label(self.master, text = self.KurgerBing.name).grid(row = 5, column = 0, pady = 5, sticky = W)
        self.bappleName = Label(self.master, text = self.Bapple.name).grid(row = 6, column = 0, pady = 5, sticky = W)
        self.shmoogleName = Label(self.master, text = self.Shmoogle.name).grid(row = 7, column = 0, pady = 5, sticky = W)
        self.hugesoftName = Label(self.master, text = self.Hugesoft.name).grid(row = 8, column = 0, pady = 5, sticky = W)
        self.mcnaldosName = Label(self.master, text = self.McNaldos.name).grid(row = 9, column = 0, pady = 5, sticky = W)
        self.ussrName = Label(self.master, text = self.USSR.name).grid(row = 10, column = 0, pady = 5, sticky = W)
        self.conkName = Label(self.master, text = self.Conk.name).grid(row = 11, column = 0, pady = 5, sticky = W)
        self.bepisName = Label(self.master, text = self.Bepis.name).grid(row = 12, column = 0, pady = 5, sticky = W)
        self.flextapeName = Label(self.master, text = self.FlexTape.name).grid(row = 13, column = 0, pady = 5, sticky = W)

        #Prices
        self.memecoPrice = Label(self.master, text = self.MemeCorp.cost)
        self.memecoPrice.grid(row = 2, column = 1, pady = 5, sticky = E)
        self.tacobacoPrice = Label(self.master, text = self.TacoBaco.cost)
        self.tacobacoPrice.grid(row = 3, column = 1, pady = 5, sticky = E)
        self.sansundertalePrice = Label(self.master, text = self.SansUndertale.cost)
        self.sansundertalePrice.grid(row = 4, column = 1, pady = 5, sticky = E)
        self.kurgerbingPrice = Label(self.master, text = self.KurgerBing.cost)
        self.kurgerbingPrice.grid(row = 5, column = 1, pady = 5, sticky = E)
        self.bapplePrice = Label(self.master, text = self.Bapple.cost)
        self.bapplePrice.grid(row = 6, column = 1, pady = 5, sticky = E)
        self.shmooglePrice = Label(self.master, text = self.Shmoogle.cost)
        self.shmooglePrice.grid(row = 7, column = 1, pady = 5, sticky = E)
        self.hugesoftPrice = Label(self.master, text = self.Hugesoft.cost)
        self.hugesoftPrice.grid(row = 8, column = 1, pady = 5, sticky = E)
        self.mcnaldosPrice = Label(self.master, text = self.McNaldos.cost)
        self.mcnaldosPrice.grid(row = 9, column = 1, pady = 5, sticky = E)
        self.ussrPrice = Label(self.master, text = self.USSR.cost)
        self.ussrPrice.grid(row = 10, column = 1, pady = 5, sticky = E)
        self.conkPrice = Label(self.master, text = self.Conk.cost)
        self.conkPrice.grid(row = 11, column = 1, pady = 5, sticky = E)
        self.bepisPrice = Label(self.master, text = self.Bepis.cost)
        self.bepisPrice.grid(row = 12, column = 1, pady = 5, sticky = E)
        self.flextapePrice = Label(self.master, text = self.FlexTape.cost)
        self.flextapePrice.grid(row = 13, column = 1, pady = 5, sticky = E)
        
        #Price Changes
        self.memecoChange = Label(self.master, text = self.MemeCorp.priceChange, fg = createpriceChange(self.MemeCorp.priceChange))
        self.memecoChange.grid(row = 2, column = 2, pady = 5, sticky = E)
        self.tacobacoChange = Label(self.master, text = self.TacoBaco.priceChange, fg = createpriceChange(self.TacoBaco.priceChange))
        self.tacobacoChange.grid(row = 3, column = 2, pady = 5, sticky = E)
        self.sansundertaleChange = Label(self.master, text = self.SansUndertale.priceChange, fg = createpriceChange(self.SansUndertale.priceChange))
        self.sansundertaleChange.grid(row = 4, column = 2, pady = 5, sticky = E)
        self.kurgerbingChange = Label(self.master, text = self.KurgerBing.priceChange, fg = createpriceChange(self.KurgerBing.priceChange))
        self.kurgerbingChange.grid(row = 5, column = 2, pady = 5, sticky = E)
        self.bappleChange = Label(self.master, text = self.Bapple.priceChange, fg = createpriceChange(self.Bapple.priceChange))
        self.bappleChange.grid(row = 6, column = 2, pady = 5, sticky = E)
        self.shmoogleChange = Label(self.master, text = self.Shmoogle.priceChange, fg = createpriceChange(self.Shmoogle.priceChange))
        self.shmoogleChange.grid(row = 7, column = 2, pady = 5, sticky = E)
        self.hugesoftChange = Label(self.master, text = self.Hugesoft.priceChange, fg = createpriceChange(self.Hugesoft.priceChange))
        self.hugesoftChange.grid(row = 8, column = 2, pady = 5, sticky = E)
        self.mcnaldosChange = Label(self.master, text = self.McNaldos.priceChange, fg = createpriceChange(self.McNaldos.priceChange))
        self.mcnaldosChange.grid(row = 9, column = 2, pady = 5, sticky = E)
        self.ussrChange = Label(self.master, text = self.USSR.priceChange, fg = createpriceChange(self.USSR.priceChange))
        self.ussrChange.grid(row = 10, column = 2, pady = 5, sticky = E)
        self.conkChange = Label(self.master, text = self.Conk.priceChange, fg = createpriceChange(self.Conk.priceChange))
        self.conkChange.grid(row = 11, column = 2, pady = 5, sticky = E)
        self.bepisChange = Label(self.master, text = self.Bepis.priceChange, fg = createpriceChange(self.Bepis.priceChange))
        self.bepisChange.grid(row = 12, column = 2, pady = 5, sticky = E)
        self.flextapeChange = Label(self.master, text = self.FlexTape.priceChange, fg = createpriceChange(self.FlexTape.priceChange))
        self.flextapeChange.grid(row = 13, column = 2, pady = 5, sticky = E)
        
        #Amounts owned
        self.memecoAmount = Label(self.master, text = self.MemeCorp.stockOwned)
        self.memecoAmount.grid(row = 2, column = 3, pady = 5, sticky = E)
        self.tacobacoAmount = Label(self.master, text = self.TacoBaco.stockOwned)
        self.tacobacoAmount.grid(row = 3, column = 3, pady = 5, sticky = E)
        self.sansundertaleAmount = Label(self.master, text = self.SansUndertale.stockOwned)
        self.sansundertaleAmount.grid(row = 4, column = 3, pady = 5, sticky = E)
        self.kurgerbingAmount = Label(self.master, text = self.KurgerBing.stockOwned)
        self.kurgerbingAmount.grid(row = 5, column = 3, pady = 5, sticky = E)
        self.bappleAmount = Label(self.master, text = self.Bapple.stockOwned)
        self.bappleAmount.grid(row = 6, column = 3, pady = 5, sticky = E)
        self.shmoogleAmount = Label(self.master, text = self.Shmoogle.stockOwned)
        self.shmoogleAmount.grid(row = 7, column = 3, pady = 5, sticky = E)
        self.hugesoftAmount = Label(self.master, text = self.Hugesoft.stockOwned)
        self.hugesoftAmount.grid(row = 8, column = 3, pady = 5, sticky = E)
        self.mcnaldosAmount = Label(self.master, text = self.McNaldos.stockOwned)
        self.mcnaldosAmount.grid(row = 9, column = 3, pady = 5, sticky = E)
        self.ussrAmount = Label(self.master, text = self.USSR.stockOwned)
        self.ussrAmount.grid(row = 10, column = 3, pady = 5, sticky = E)
        self.conkAmount = Label(self.master, text = self.Conk.stockOwned)
        self.conkAmount.grid(row = 11, column = 3, pady = 5, sticky = E)
        self.bepisAmount = Label(self.master, text = self.Bepis.stockOwned)
        self.bepisAmount.grid(row = 12, column = 3, pady = 5, sticky = E)
        self.flextapeAmount = Label(self.master, text = self.FlexTape.stockOwned)
        self.flextapeAmount.grid(row = 13, column = 3, pady = 5, sticky = E)


        #Functionality
        self.bottomUnderline = Label(self.master, text = "------------------------------------------------------------------------------").grid(row = 14, column = 0, columnspan = 4, sticky = W)
        self.moneyAmount = Label(self.master, text = "Your Money: {}".format(str(money)))
        self.moneyAmount.grid(row = 15, column = 0, sticky = W)
        
       
        
        def refresh(configuration, stocks): #Refreshes GUI
        
            configuration(text = stocks)
            self.moneyAmount.config(text = "Your Money: {}".format(str(money)))
            
        def refreshPrice(configuration, stocks, color):
        
            configuration(text = stocks, fg = color)
        
        def maxPossible(company): #Calculates the amount of whole stocks you can buy
        
            totalpossible = int(money/company)
            
            if round(totalpossible) == totalpossible:
            
                return totalpossible
                
            else:
            
                return int(round(totalpossible - 0.5))
        
        #Functions for every button, because for some reason tkinter can't take arguments in a function
        
        #Meme Corp Buttons
        def memecorpone():
        
            self.MemeCorp.buy(1)
            refresh(self.memecoAmount.config, self.MemeCorp.stockOwned)      
                
        def memecoPossible():
                
            self.MemeCorp.buy(maxPossible(self.MemeCorp.cost))
            refresh(self.memecoAmount.config, self.MemeCorp.stockOwned)
        
        def memecosell():
            
            self.MemeCorp.sell(1)
            refresh(self.memecoAmount.config, self.MemeCorp.stockOwned)
        
        def memecosellAll():
        
            self.MemeCorp.sell(self.MemeCorp.stockOwned)
            refresh(self.memecoAmount.config, self.MemeCorp.stockOwned)
            
        #Taco Baco Buttons
        def tacobacoone():
        
            self.TacoBaco.buy(1)
            refresh(self.tacobacoAmount.config, self.TacoBaco.stockOwned)
            
        def tacobacoPossible():
        
            self.TacoBaco.buy(maxPossible(self.TacoBaco.cost))
            refresh(self.tacobacoAmount.config, self.TacoBaco.stockOwned)
            
        def tacobacoSell():
        
            self.TacoBaco.sell(1)
            refresh(self.tacobacoAmount.config, self.TacoBaco.stockOwned)
            
        def tacobacosellAll():
        
            self.TacoBaco.sell(self.TacoBaco.stockOwned)
            refresh(self.tacobacoAmount.config, self.TacoBaco.stockOwned)
        
        #Sans Undertale Buttons
        def sansundertaleone():
        
            self.SansUndertale.buy(1)
            refresh(self.sansundertaleAmount.config, self.SansUndertale.stockOwned)
            
        def sansundertalePossible():
        
            self.SansUndertale.buy(maxPossible(self.SansUndertale.cost))
            refresh(self.sansundertaleAmount.config, self.SansUndertale.stockOwned)
            
        def sansundertaleSell():
        
            self.SansUndertale.sell(1)
            refresh(self.sansundertaleAmount.config, self.SansUndertale.stockOwned)
            
        def sansundertalesellAll():
        
            self.SansUndertale.sell(self.SansUndertale.stockOwned)
            refresh(self.sansundertaleAmount.config, self.SansUndertale.stockOwned)
            
        #Kurger Bing Buttons
        def kurgerbingone():
        
            self.KurgerBing.buy(1)
            refresh(self.kurgerbingAmount.config, self.KurgerBing.stockOwned)
            
        def kurgerbingPossible():
        
            self.KurgerBing.buy(maxPossible(self.KurgerBing.cost))
            refresh(self.kurgerbingAmount.config, self.KurgerBing.stockOwned)
            
        def kurgerbingSell():
        
            self.KurgerBing.sell(1)
            refresh(self.kurgerbingAmount.config, self.KurgerBing.stockOwned)
            
        def kurgerbingsellAll():
        
            self.KurgerBing.sell(self.KurgerBing.stockOwned)
            refresh(self.kurgerbingAmount.config, self.KurgerBing.stockOwned)
            
        #Bapple Buttons
        def bappleone():
        
            self.Bapple.buy(1)
            refresh(self.bappleAmount.config, self.Bapple.stockOwned)
            
        def bapplePossible():
        
            self.Bapple.buy(maxPossible(self.Bapple.cost))
            refresh(self.bappleAmount.config, self.Bapple.stockOwned)
            
        def bappleSell():
        
            self.Bapple.sell(1)
            refresh(self.bappleAmount.config, self.Bapple.stockOwned)
            
        def bapplesellAll():
        
            self.Bapple.sell(self.Bapple.stockOwned)
            refresh(self.bappleAmount.config, self.Bapple.stockOwned)
            
        #Shmoogle Buttons
        def shmoogleone():
        
            self.Shmoogle.buy(1)
            refresh(self.shmoogleAmount.config, self.Shmoogle.stockOwned)
            
        def shmooglePossible():
        
            self.Shmoogle.buy(maxPossible(self.Shmoogle.cost))
            refresh(self.shmoogleAmount.config, self.Shmoogle.stockOwned)
            
        def shmoogleSell():
        
            self.Shmoogle.sell(1)
            refresh(self.shmoogleAmount.config, self.Shmoogle.stockOwned)
            
        def shmooglesellAll():
        
            self.Shmoogle.sell(self.Shmoogle.stockOwned)
            refresh(self.shmoogleAmount.config, self.Shmoogle.stockOwned)
            
        #Hugesoft Buttons
        def hugesoftone():
        
            self.Hugesoft.buy(1)
            refresh(self.hugesoftAmount.config, self.Hugesoft.stockOwned)
            
        def hugesoftPossible():
        
            self.Hugesoft.buy(maxPossible(self.Hugesoft.cost))
            refresh(self.hugesoftAmount.config, self.Hugesoft.stockOwned)
            
        def hugesoftSell():
        
            self.Hugesoft.sell(1)
            refresh(self.hugesoftAmount.config, self.Hugesoft.stockOwned)
            
        def hugesoftsellAll():
        
            self.Hugesoft.sell(self.Hugesoft.stockOwned)
            refresh(self.hugesoftAmount.config, self.Hugesoft.stockOwned)
            
        #McNaldos Buttons
        def mcnaldosone():
        
            self.McNaldos.buy(1)
            refresh(self.mcnaldosAmount.config, self.McNaldos.stockOwned)
            
        def mcnaldosPossible():
        
            self.McNaldos.buy(maxPossible(self.McNaldos.cost))
            refresh(self.mcnaldosAmount.config, self.McNaldos.stockOwned)
            
        def mcnaldosSell():
        
            self.McNaldos.sell(1)
            refresh(self.mcnaldosAmount.config, self.McNaldos.stockOwned)
            
        def mcnaldossellAll():
        
            self.McNaldos.sell(self.McNaldos.stockOwned)
            refresh(self.mcnaldosAmount.config, self.McNaldos.stockOwned)
        
        #USSR Buttons
        def ussrone():
        
            self.USSR.buy(1)
            refresh(self.ussrAmount.config, self.USSR.stockOwned)
        
        def ussrPossible():
        
            self.USSR.buy(maxPossible(self.USSR.cost))
            refresh(self.ussrAmount.config, self.USSR.stockOwned)
            
        def ussrSell():
        
            self.USSR.sell(1)
            refresh(self.ussrAmount.config, self.USSR.stockOwned)
            
        def ussrsellAll():
        
            self.USSR.sell(self.USSR.stockOwned)
            
        #Conk Buttons
        def conkone():
        
            self.Conk.buy(1)
            refresh(self.conkAmount.config, self.Conk.stockOwned)
            
        def conkPossible():
        
            self.Conk.buy(maxPossible(self.Conk.cost))
            refresh(self.conkAmount.config, self.Conk.stockOwned)
        
        def conkSell():
        
            self.Conk.sell(1)
            refresh(self.conkAmount.config, self.Conk.stockOwned)
            
        def conksellAll():
        
            self.Conk.sell(self.Conk.stockOwned)
            refresh(self.conkAmount.config, self.Conk.stockOwned)
            
        #Bepis Buttons
        def bepisone():
        
            self.Bepis.buy(1)
            refresh(self.bepisAmount.config, self.Bepis.stockOwned)
            
        def bepisPossible():
        
            self.Bepis.buy(maxPossible(self.Bepis.cost))
            refresh(self.bepisAmount.config, self.Bepis.stockOwned)
            
        def bepisSell():
        
            self.Bepis.sell(1)
            refresh(self.bepisAmount.config, self.Bepis.stockOwned)
            
        def bepissellAll():
        
            self.Bepis.sell(self.Bepis.stockOwned)
            refresh(self.bepisAmount.config, self.Bepis.stockOwned)
        
            self.FlexTape.buy(1)
            refresh(self.flextapeAmount.config, self.Bepis.stockOwned)
            
        #Flex Tape Buttons
        def flextapeone():
            self.FlexTape.buy(1)
            refresh(self.flextapeAmount.config, self.Bepis.stockOwned)
        def flextapePossible():
        
            self.FlexTape.buy(maxPossible(self.FlexTape.cost))
            refresh(self.flextapeAmount.config, self.Bepis.stockOwned)
            
        def flextapeSell():
        
            self.FlexTape.sell(1)
            refresh(self.flextapeAmount.config, self.Bepis.stockOwned)
            
        def flextapesellAll():
        
            self.FlexTape.sell(self.FlexTape.stockOwned)
            refresh(self.flextapeAmount.config, self.Bepis.stockOwned)
        
        #Graphing functions
        
        def graphmemecorp():
        
            self.MemeCorp.graphPrice()
            
        def graphtacobaco():
        
            self.TacoBaco.graphPrice()
            
        def graphsansundertale():
        
            self.SansUndertale.graphPrice()
            
        def graphkurgerbing():
            
            self.KurgerBing.graphPrice()
        
        def graphbapple():
        
            self.Bapple.graphPrice()
            
        def graphshmoogle():
        
            self.Shmoogle.graphPrice()
            
        def graphhugesoft():
        
            self.Hugesoft.graphPrice()
            
        def graphmcnaldos():
        
            self.McNaldos.graphPrice()
            
        def graphussr():
        
            self.USSR.graphPrice()
        
        def graphconk():
        
            self.Conk.graphPrice()
            
        def graphbepis():
        
            self.Bepis.graphPrice()
            
        def graphflextape():
        
            self.FlexTape.graphPrice()
        
        self.buymemeco = Button(self.master, text = "Buy 1 Meme Co Stonk", command = memecorpone) #All of the buttons
        self.buymemeco.grid(row = 2, column = 4, padx = 10, sticky = E)
        self.buymostmemeco = Button(self.master, text = "Buy All You Can", command = memecoPossible)
        self.buymostmemeco.grid(row = 2, column = 5, padx = 5, sticky = E)
        self.sellmemeco = Button(self.master, text = "Sell 1 Meme Co Stonk", command = memecosell)
        self.sellmemeco.grid(row = 2, column = 6, padx = 5, sticky = E)
        self.sellmemecoAll = Button(self.master, text = "Sell All Meme Co Stonk", command = memecosellAll)
        self.sellmemecoAll.grid(row = 2, column = 7, padx = 5, sticky = E)
        self.memecoGraph = Button(self.master, text = "See Meme Co Graph", command = graphmemecorp)
        self.memecoGraph.grid(row = 2, column = 8, padx = 5, sticky = E)
        
        self.buytacobaco = Button(self.master, text = "Buy 1 Taco Baco Stonk", command = tacobacoone)
        self.buytacobaco.grid(row = 3, column = 4, padx = 10, sticky = E)
        self.buymosttacobaco = Button(self.master, text = "Buy All You Can", command = tacobacoPossible)
        self.buymosttacobaco.grid(row = 3, column = 5, padx = 5, sticky = E)
        self.selltacobaco = Button(self.master, text = "Sell 1 Taco Baco Stonk", command = tacobacoSell)
        self.selltacobaco.grid(row = 3, column = 6, padx = 5, sticky = E)
        self.selltacobacoAll = Button(self.master, text = "Sell All Taco Baco Stonk", command = tacobacosellAll)
        self.selltacobacoAll.grid(row = 3, column = 7, padx = 5, sticky = E)
        self.tacobacoGraph = Button(self.master, text = "See Taco Baco Graph", command = graphtacobaco)
        self.tacobacoGraph.grid(row = 3, column = 8, padx = 5, sticky = E)
        
        self.buysansundertale = Button(self.master, text = "Buy 1 Sans Undertale Stonk", command = sansundertaleone)
        self.buysansundertale.grid(row = 4, column = 4, padx = 10, sticky = E)
        self.buymostsansundertale = Button(self.master, text = "Buy All You Can", command = sansundertalePossible)
        self.buymostsansundertale.grid(row = 4, column = 5, padx = 5, sticky = E)
        self.sellsansundertale = Button(self.master, text = "Sell 1 Sans Undertale Stonk", command = sansundertaleSell)
        self.sellsansundertale.grid(row = 4, column = 6, padx = 5, sticky = E)
        self.sellsansundertaleAll = Button(self.master, text = "Sell All Sans Undertale Stonk", command = sansundertalesellAll)
        self.sellsansundertaleAll.grid(row = 4, column = 7, padx = 5, sticky = E)
        self.sansundertaleGraph = Button(self.master, text = "See Sans Undertale Graph", command = graphsansundertale)
        self.sansundertaleGraph.grid(row = 4, column = 8, padx = 5, sticky = E)
        
        self.buykurgerbing = Button(self.master, text = "Buy 1 Kurger Bing Stonk", command = kurgerbingone)
        self.buykurgerbing.grid(row = 5, column = 4, padx = 10, sticky = E)
        self.buymostkurgerbing = Button(self.master, text = "Buy All You Can", command = kurgerbingPossible)
        self.buymostkurgerbing.grid(row = 5, column = 5, padx = 5, sticky = E)
        self.sellkurgerbing = Button(self.master, text = "Sell 1 Kurger Bing Stonk", command = kurgerbingSell)
        self.sellkurgerbing.grid(row = 5, column = 6, padx = 5, sticky = E)
        self.sellkurgerbingAll = Button(self.master, text = "Sell All Kurger Bing Stonk", command = kurgerbingsellAll)
        self.sellkurgerbingAll.grid(row = 5, column = 7, padx = 5, sticky = E)
        self.kurgerbingGraph = Button(self.master, text = "See Kurger Bing Graph", command = graphkurgerbing)
        self.kurgerbingGraph.grid(row = 5, column = 8, padx = 5, sticky = E)
        
        self.buybapple = Button(self.master, text = "Buy 1 Bapple Stonk", command = bappleone)
        self.buybapple.grid(row = 6, column = 4, padx = 10, sticky = E)
        self.buymostbapple = Button(self.master, text = "Buy All You Can", command = bapplePossible)
        self.buymostbapple.grid(row = 6, column = 5, padx = 5, sticky = E)
        self.sellbapple = Button(self.master, text = "Sell 1 Bapple Stonk", command = bappleSell)
        self.sellbapple.grid(row = 6, column = 6, padx = 5, sticky = E)
        self.sellbappleAll = Button(self.master, text = "Sell All Bapple Stonk", command = bapplesellAll)
        self.sellbappleAll.grid(row = 6, column = 7, padx = 5, sticky = E)
        self.bappleGraph = Button(self.master, text = "See Bapple Graph", command = graphbapple)
        self.bappleGraph.grid(row = 6, column = 8, padx = 5, sticky = E)
        
        self.buyshmoogle = Button(self.master, text = "Buy 1 Shmoogle Stonk", command = shmoogleone)
        self.buyshmoogle.grid(row = 7, column = 4, padx = 10, sticky = E)
        self.buymostshmoogle = Button(self.master, text = "Buy All You Can", command = shmooglePossible)
        self.buymostshmoogle.grid(row = 7, column = 5, padx = 5, sticky = E)
        self.sellshmoogle = Button(self.master, text = "Sell 1 Shmoogle Stonk", command = shmoogleSell)
        self.sellshmoogle.grid(row = 7, column = 6, padx = 5, sticky = E)
        self.sellshmoogleAll = Button(self.master, text = "Sell All Shmoogle Stonk", command = shmooglesellAll)
        self.sellshmoogleAll.grid(row = 7, column = 7, padx = 5, sticky = E)
        self.shmoogleGraph = Button(self.master, text = "See Shmoogle Graph", command = graphshmoogle)
        self.shmoogleGraph.grid(row = 7, column = 8, padx = 5, sticky = E)
        
        self.buyhugesoft = Button(self.master, text = "Buy 1 Hugesoft Stonk", command = hugesoftone)
        self.buyhugesoft.grid(row = 8, column = 4, padx = 10, sticky = E)
        self.buymosthugesoft = Button(self.master, text = "Buy All You Can", command = hugesoftPossible)
        self.buymosthugesoft.grid(row = 8, column = 5, padx = 5, sticky = E)
        self.sellhugesoft = Button(self.master, text = "Sell 1 Hugesoft Stonk", command = hugesoftSell)
        self.sellhugesoft.grid(row = 8, column = 6, padx = 5, sticky = E)
        self.sellhugesoftAll = Button(self.master, text = "Sell All Hugesoft Stonk", command = hugesoftsellAll)
        self.sellhugesoftAll.grid(row = 8, column = 7, padx = 5, sticky = E)
        self.hugesoftGraph = Button(self.master, text = "See Hugesoft Graph", command = graphhugesoft)
        self.hugesoftGraph.grid(row = 8, column = 8, padx = 5, sticky = E)
        
        self.buymcnaldos = Button(self.master, text = "Buy 1 McNaldos Stonk", command = mcnaldosone)
        self.buymcnaldos.grid(row = 9, column = 4, padx = 10, sticky = E)
        self.buymostmcnaldos = Button(self.master, text = "Buy All You Can", command = mcnaldosPossible)
        self.buymostmcnaldos.grid(row = 9, column = 5, padx = 5, sticky = E)
        self.sellmcnaldos = Button(self.master, text = "Sell 1 McNaldos Stonk", command = mcnaldosSell)
        self.sellmcnaldos.grid(row = 9, column = 6, padx = 5, sticky = E)
        self.sellmcnaldosAll = Button(self.master, text = "Sell All McNaldos Stonk", command = mcnaldossellAll)
        self.sellmcnaldosAll.grid(row = 9, column = 7, padx = 5, sticky = E)
        self.mcnaldosGraph = Button(self.master, text = "See McNaldos Graph", command = graphmcnaldos)
        self.mcnaldosGraph.grid(row = 9, column = 8, padx = 5, sticky = E)
        
        self.buyussr = Button(self.master, text = "Buy 1 USSR Stonk", command = ussrone)
        self.buyussr.grid(row = 10, column = 4, padx = 10, sticky = E)
        self.buymostussr = Button(self.master, text = "Buy All You Can", command = ussrPossible)
        self.buymostussr.grid(row = 10, column = 5, padx = 5, sticky = E)
        self.sellussr= Button(self.master, text = "Sell 1 USSR Stonk", command = ussrSell)
        self.sellussr.grid(row = 10, column = 6, padx = 5, sticky = E)
        self.sellussrAll = Button(self.master, text = "Sell All USSR Stonk", command =ussrsellAll)
        self.sellussrAll.grid(row = 10, column = 7, padx = 5, sticky = E)
        self.ussrGraph = Button(self.master, text = "See USSR Graph", command = graphussr)
        self.ussrGraph.grid(row = 10, column = 8, padx = 5, sticky = E)
        
        self.buyconk = Button(self.master, text = "Buy 1 Conk Stonk", command = conkone)
        self.buyconk.grid(row = 11, column = 4, padx = 10, sticky = E)
        self.buymostconk = Button(self.master, text = "Buy All You Can", command = conkPossible)
        self.buymostconk.grid(row = 11, column = 5, padx = 5, sticky = E)
        self.sellconk= Button(self.master, text = "Sell 1 Conk Stonk", command = conkSell)
        self.sellconk.grid(row = 11, column = 6, padx = 5, sticky = E)
        self.sellconkAll = Button(self.master, text = "Sell All Conk Stonk", command =conksellAll)
        self.sellconkAll.grid(row = 11, column = 7, padx = 5, sticky = E)
        self.conkGraph = Button(self.master, text = "See Conk Graph", command = graphconk)
        self.conkGraph.grid(row = 11, column = 8, padx = 5, sticky = E)
        
        self.buybepis = Button(self.master, text = "Buy 1 Bepis Stonk", command = bepisone)
        self.buybepis.grid(row = 12, column = 4, padx = 10, sticky = E)
        self.buymostbepis = Button(self.master, text = "Buy All You Can", command = bepisPossible)
        self.buymostbepis.grid(row = 12, column = 5, padx = 5, sticky = E)
        self.sellbepis = Button(self.master, text = "Sell 1 Bepis Stonk", command = bepisSell)
        self.sellbepis.grid(row = 12, column = 6, padx = 5, sticky = E)
        self.sellbepisAll = Button(self.master, text = "Sell All Bepis Stonk", command = bepissellAll)
        self.sellbepisAll.grid(row = 12, column = 7, padx = 5, sticky = E)
        self.bepisGraph = Button(self.master, text = "See Bepis Graph", command = graphbepis)
        self.bepisGraph.grid(row = 12, column = 8, padx = 5, sticky = E)
        
        self.buyflextape = Button(self.master, text = "Buy 1 Flex Tape Stonk", command = flextapeone)
        self.buyflextape.grid(row = 13, column = 4, padx = 10, sticky = E)
        self.buymostflextape = Button(self.master, text = "Buy All You Can", command = flextapePossible)
        self.buymostflextape.grid(row = 13, column = 5, padx = 5, sticky = E)
        self.sellflextape = Button(self.master, text = "Sell 1 Flex Tape Stonk", command = flextapeSell)
        self.sellflextape.grid(row = 13, column = 6, padx = 5, sticky = E)
        self.sellflextapeAll = Button(self.master, text = "Sell All Flex Tape Stonk", command = flextapesellAll)
        self.sellflextapeAll.grid(row = 13, column = 7, padx = 5, sticky = E)
        self.flextapeGraph = Button(self.master, text = "See Flex Tape Graph", command = graphflextape)
        self.flextapeGraph.grid(row = 13, column = 8, padx = 5, sticky = E)
        
        def endoneTurn(): #ends one turn
        
            global turn
            global turnList
        
            endTurn(self, 1)
            refresh(self.memecoPrice.configure, self.MemeCorp.cost)
            refresh(self.tacobacoPrice.configure, self.TacoBaco.cost)
            refresh(self.sansundertalePrice.configure, self.SansUndertale.cost)
            refresh(self.kurgerbingPrice.configure, self.KurgerBing.cost)
            refresh(self.bapplePrice.configure, self.Bapple.cost)
            refresh(self.shmooglePrice.configure, self.Shmoogle.cost)
            refresh(self.hugesoftPrice.configure, self.Hugesoft.cost)
            refresh(self.mcnaldosPrice.configure, self.McNaldos.cost)
            refresh(self.ussrPrice.configure, self.USSR.cost)
            refresh(self.conkPrice.configure, self.Conk.cost)
            refresh(self.bepisPrice.configure, self.Bepis.cost)
            refresh(self.flextapePrice.configure, self.FlexTape.cost)
            refreshPrice(self.memecoChange.config, self.MemeCorp.priceChange, createpriceChange(self.MemeCorp.priceChange))
            refreshPrice(self.tacobacoChange.config, self.TacoBaco.priceChange, createpriceChange(self.TacoBaco.priceChange))
            refreshPrice(self.sansundertaleChange.config, self.SansUndertale.priceChange, createpriceChange(self.SansUndertale.priceChange))
            refreshPrice(self.kurgerbingChange.config, self.KurgerBing.priceChange, createpriceChange(self.KurgerBing.priceChange))
            refreshPrice(self.bappleChange.config, self.Bapple.priceChange, createpriceChange(self.Bapple.priceChange))
            refreshPrice(self.shmoogleChange.config, self.Shmoogle.priceChange, createpriceChange(self.Shmoogle.priceChange))
            refreshPrice(self.hugesoftChange.config, self.Hugesoft.priceChange, createpriceChange(self.Hugesoft.priceChange))
            refreshPrice(self.mcnaldosChange.config, self.McNaldos.priceChange, createpriceChange(self.McNaldos.priceChange))
            refreshPrice(self.ussrChange.config, self.USSR.priceChange, createpriceChange(self.USSR.priceChange))
            refreshPrice(self.conkChange.config, self.Conk.priceChange, createpriceChange(self.Conk.priceChange))
            refreshPrice(self.bepisChange.config, self.Bepis.priceChange, createpriceChange(self.Bepis.priceChange))
            refreshPrice(self.flextapeChange.config, self.FlexTape.priceChange, createpriceChange(self.FlexTape.priceChange))
            refresh(self.seeProfit.configure, str(profit))
            
            turn = turn + 1
            turnList.append(turn)
            moneyOverTime.append(money)
           
        
        def endfiveTurns(): #ends 5 turns
        
            global turn
            global turnList
        
            endTurn(self, 5)
            refresh(self.memecoPrice.configure, self.MemeCorp.cost)
            refresh(self.tacobacoPrice.configure, self.TacoBaco.cost)
            refresh(self.sansundertalePrice.configure, self.SansUndertale.cost)
            refresh(self.kurgerbingPrice.configure, self.KurgerBing.cost)
            refresh(self.bapplePrice.configure, self.Bapple.cost)
            refresh(self.shmooglePrice.configure, self.Shmoogle.cost)
            refresh(self.hugesoftPrice.configure, self.Hugesoft.cost)
            refresh(self.mcnaldosPrice.configure, self.McNaldos.cost)
            refresh(self.ussrPrice.configure, self.USSR.cost)
            refresh(self.conkPrice.configure, self.Conk.cost)
            refresh(self.bepisPrice.configure, self.Bepis.cost)
            refresh(self.flextapePrice.configure, self.FlexTape.cost)
            refreshPrice(self.memecoChange.config, self.MemeCorp.priceChange, createpriceChange(self.MemeCorp.priceChange))
            refreshPrice(self.tacobacoChange.config, self.TacoBaco.priceChange, createpriceChange(self.TacoBaco.priceChange))
            refreshPrice(self.sansundertaleChange.config, self.SansUndertale.priceChange, createpriceChange(self.SansUndertale.priceChange))
            refreshPrice(self.kurgerbingChange.config, self.KurgerBing.priceChange, createpriceChange(self.KurgerBing.priceChange))
            refreshPrice(self.bappleChange.config, self.Bapple.priceChange, createpriceChange(self.Bapple.priceChange))
            refreshPrice(self.shmoogleChange.config, self.Shmoogle.priceChange, createpriceChange(self.Shmoogle.priceChange))
            refreshPrice(self.hugesoftChange.config, self.Hugesoft.priceChange, createpriceChange(self.Hugesoft.priceChange))
            refreshPrice(self.mcnaldosChange.config, self.McNaldos.priceChange, createpriceChange(self.McNaldos.priceChange))
            refreshPrice(self.ussrChange.config, self.USSR.priceChange, createpriceChange(self.USSR.priceChange))
            refreshPrice(self.conkChange.config, self.Conk.priceChange, createpriceChange(self.Conk.priceChange))
            refreshPrice(self.bepisChange.config, self.Bepis.priceChange, createpriceChange(self.Bepis.priceChange))
            refreshPrice(self.flextapeChange.config, self.FlexTape.priceChange, createpriceChange(self.FlexTape.priceChange))
            refresh(self.seeProfit.configure, str(profit))
            
            for t in range(5):
            
                turn = turn + 1
                turnList.append(turn)
                moneyOverTime.append(money)
                
        self.endturnOne = Button(self.master, text = "End 1 Turn", command = endoneTurn)
        self.endturnOne.grid(row = 15, column = 2, padx = 10, sticky = E)
        self.endturnFive = Button(self.master, text = "End 5 Turns", command = endfiveTurns)
        self.endturnFive.grid(row = 15, column = 3, padx = 10, sticky = E)
        self.seeProfit = Label(self.master, text = "Your Total Profit: {}".format(str(profit)))
        self.seeProfit.grid(row = 15, column = 7, padx = 10, sticky = E)
        self.profitovertime = Button(self.master, text = "Profit Over Time Graph", command = graphMoney)
        self.profitovertime.grid(row = 15, column = 8, padx = 10, sticky = E)
        
        self.master.mainloop()


Application()

