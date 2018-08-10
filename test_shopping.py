import unittest
import shopping

class TestBuyerReviewInit(unittest.TestCase):
    def test_SimpleInit(self):
        review1 = shopping.BuyerReview(1, "This sucks", "chris")
        self.assertEqual(review1.getRating(), 1)

        review2 = shopping.BuyerReview(4, "This is great", "brent")
        self.assertEqual(review2.getRating(), 4)    #testing to make sure it's 4
        self.assertEqual(review2.getReview(), "This is great")      #testing to make sure this is great
        self.assertEqual(review2.getUserId(), "brent") 

    def test_RatingWithLetters(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview("abc", "", "")

    def test_ReviewWithNumbers(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(2, 99, "")

    def test_EmptyValues(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview()
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(1)
        with self.assertRaises(Exception):
            review = shopping.BuyerReview("hello")
        with self.assertRaises(Exception):
            review = shopping.BuyerReview("hello", 1)

    def test_UserIdBadValue(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(1, "hi", 9)
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(1, "hi", 99.99)

class TestShoppingItem(unittest.TestCase):
    def test_ShoppingItemInit(self):
        reviews = [shopping.BuyerReview(1, "This sucks", "chris"),
                    shopping.BuyerReview(1, "This is great", "Aaron")]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        item = shopping.ShoppingItem("Macbook Pro", 1.00, 3, reviews, tags, buyers)

        self.assertEqual(item.getName(), 'Macbook Pro')
        self.assertEqual(item.getPrice(), 1.00)
        self.assertEqual(item.getNumberSold(), 3)

        self.assertEqual(len(reviews), len(item.getReviews()))
        for review in reviews:
            self.assertTrue(review in item.getReviews())
        
        self.assertEqual(len(tags), len(item.getTags()))
        for tag in tags:
            self.assertTrue(tag in item.getTags())
        
        self.assertEqual(len(buyers), len(item.getBuyers()))
        for buyer in buyers:
            self.assertTrue(buyer in item.getBuyers())

# name, price, sold, reviews, tags, buyers):

    def test_EmptyValues2(self):
        with self.assertRaises(Exception):
            review = shopping.ShoppingItem()
        with self.assertRaises(Exception):
            review = shopping.ShoppingItem('hi')
        with self.assertRaises(Exception):
            review = shopping.ShoppingItem('hi', 3.00)
        with self.assertRaises(Exception):
            review = shopping.ShoppingItem('hi', 3.00, 3)
    
    def test_AverageRating(self):
        reviews = [shopping.BuyerReview(1, "This sucks", "chris"),
                    shopping.BuyerReview(2, "This is great", "Aaron"),
                    shopping.BuyerReview(3, 'slam', 'piss')]
        item = shopping.ShoppingItem('bla', 1.00, 0, reviews, [], [])
        self.assertEqual(item.getAverageRating(), 2)
    
        reviews = [shopping.BuyerReview(1, "This sucks", "chris"),
                    shopping.BuyerReview(5, "This is great", "Aaron"),
                    shopping.BuyerReview(3, 'slam', 'piss'),
                    shopping.BuyerReview(3, 'This', 'Brent')]
        item = shopping.ShoppingItem('bla', 1.00, 0, reviews, [], [])
        self.assertEqual(item.getAverageRating(), 3)

    def test_getReviews(self):
        reviews = [shopping.BuyerReview(1, "This sucks", "chris"),
                    shopping.BuyerReview(1, "This is great", "Aaron")]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        item1 = shopping.ShoppingItem('Asus Laptop', 1.00, 4, reviews, tags, buyers)
        item1.addReview(shopping.BuyerReview(5, 'fantastic', 'tony'))
        

    def test_userId(self):
        with self.assertRaises(Exception):
            customer = shopping.ShopperAccount(1, [])

        with self.assertRaises(Exception):
            shopper = shopping.ShopperAccount([])

    def test_addPurchase(self):
        reviews = [shopping.BuyerReview(1, "This sucks", "chris"),
                    shopping.BuyerReview(1, "This is great", "Aaron")]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        item = shopping.ShoppingItem("Macbook Pro", 1.00, 3, reviews, tags, buyers)
        item.addPurchase('billy')
        self.assertEqual(item.getBuyers(), buyers)

        self.assertEqual(len(buyers), len(item.getBuyers()))
        for buyer in buyers:
            self.assertTrue(buyer in item.getBuyers())

    def test_setPrice(self):
        reviews = [shopping.BuyerReview(1, 'manson sucks', 'tony'),
                   shopping.BuyerReview(4, 'this is great', 'aj')]
        tags = ['computer', 'laptop', 'pc']
        buyers = ['chris', 'brent', 'anthony']
        item1 = shopping.ShoppingItem('Asus Laptop', 1.00, 3, reviews, tags, buyers)
        item1.setPrice(2.00)
        self.assertEqual(item1.getPrice(), 2.00)

class test_ShopperAccountInit(unittest.TestCase):
    def test_shopperAccountInit(self):
        customer = [shopping.BuyerReview(1, 'lovely', 'tony'),
        shopping.BuyerReview(5, 'crap', 'chris'),
        shopping.BuyerReview(3, 'this is great', 'aaron')]
        items = [shopping.ShoppingItem('android pixel', 3.00, 4, customer, ['smartphone, android'], ['aaron, trevor'])]

        customer1 = shopping.ShopperAccount('tony', items)
        self.assertEqual(customer1.getUserId(), 'tony')
        self.assertEqual(customer1.getOrderHistory(), items)

    def test_getOrderHistory(self):
        customer = [shopping.BuyerReview(1, 'boiler', 'Jim'),
        shopping.BuyerReview(5, 'this is good', 'aaron'),
        shopping.BuyerReview(3, 'i can believe it is butter', 'ramsay')]
        items = [shopping.ShoppingItem('android pixel', 3.00, 4, customer, ['smartphone, android'], ['aaron, trevor'])]

        customer1 = shopping.ShopperAccount('tony', items)
        self.assertEqual(len(items), len(customer1.getOrderHistory()))
        for item in items:
            self.assertTrue(item in customer1.getOrderHistory())
    
    def test_addPurchaseDos(self):
        customer = [shopping.BuyerReview(1, 'boiler', 'Jim'),
        shopping.BuyerReview(5, 'this is good', 'aaron'),
        shopping.BuyerReview(3, 'i can believe it is butter', 'ramsay')]
        items = [shopping.ShoppingItem('android pixel', 3.00, 4, customer, ['smartphone, android'], ['aaron, trevor'])]
    
        cust1 = shopping.ShopperAccount('brent', items)
        cust1.addPurchase(shopping.ShoppingItem('blah blah', 2.00, 5, customer, ['blah', 'blah blah'], ['anthony', 'tom', 'aaron']))
        self.assertEqual(len(items), len(cust1.getOrderHistory()))
        for item in items:
            self.assertTrue(item in cust1.getOrderHistory())

class test_ExtraCredit(unittest.TestCase):
    def test_getSize(self):
        pass

unittest.main()

