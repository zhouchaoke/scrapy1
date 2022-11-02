# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class SchoolbagPipeline:
    def open_spider(self,spider):
        print("opened")
        try:
            self.con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",db="mydb",charset="utf8")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("delete from schoolbag")
            self.opened =True
            self.count =0
        except Exception as  err:
            print(err)
            self.opened=False
    def close_spider(self,spider):
        if self.opened:
            self.con.commit()
            self.con.close()
            self.opened=False
        print("closed")
        print("爬取了:",self.count,"本书籍")
    def process_item(self, item, spider):

        try:
            # picture
            # price
            # title
            # hot_word
            # comment,
            # publisher
            print(item["picture"])
            print(item["price"])
            print(item["title"])
            print(item["hot_word"])
            print(item["comment"])
            print(item["publisher"])
            print()
            if self.opened:
                self.cursor.execute("insert into schoolbag(picture,price,title,hot_word,comment,publisher) values (%s,%s,%s,%s,%s,%s)",
                                    (item["picture"],item["price"],item["title"],item["hot_word"],item["comment"],item["publisjer"]))
                self.count+=1
        except Exception as  err:
            print(err)
        return item
