visitors_cols =    ["name","email","is_member","is_subscriber"]
visitors =[
    ["test","test1@gmail.com",True, False],
    ['test2',"test2@gmail.com",True,True],
]

books_cols =     ["_id","title","author","category","is_bestseller","is_available","age_range","technology","awards","challenges","subject","artist"]
books= [
    ["test_id_1","test title","test author","kids",True,True,"5-7 years",None,None,None,None,None],
    ["test_id_2","test title 2","test author 2","sciencefiction",False,True, None,"technology test 2",None,None,None, None],
    ["test_id_3","test title 3","test author 3","comics",False,True, None,None,None,None,None, "artist test 3"],
    ["test_id_4","test title 4","test author 4","biography",True,False, None,None,None,None, "subject test 4",None],
    ["test_id_5","test title 5","test author 5","adventure",False,False, None,None,None,"challenges test",None, None],
    ["test_id_6","test title 6","test author 6","literary",False,False, None,None,"awards test 6",None,None, None],
]
borrow_books_cols = ["visitor_email","book_id","borrow_date","return_date","late_fee"],

borrow_books= [
    ["test1@gmail.com","test_id_4","2023-10-10","2023-10-18",0],
    ["test2@gmail.com","test_id_5","2023-10-09",None,0],
    ["test2@gmail.com","test_id_6","2023-11-18",None,0],
    ]

