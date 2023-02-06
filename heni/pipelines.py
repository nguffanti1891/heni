# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd

class HeniPipeline:
    items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        x = pd.DataFrame(self.items, columns=['url','title','media','height_cm','width_cm','price_gbp'])
        x.to_csv("output_task3.csv", index=False)
