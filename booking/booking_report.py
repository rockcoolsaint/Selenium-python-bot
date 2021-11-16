# This file is going to include method that will parse
# The specific data that we nee from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
  def __init__(self, hotel_boxes:WebElement):
    # self.boxes_section_element = boxes_section_element
    # self.deal_boxes = self.pull_deal_boxes()
    self.deal_boxes = hotel_boxes
    # print(len(hotel_boxes))
    # print('==============')

  # def pull_deal_boxes(self):
  #   return self.boxes_section_element.find_element_by_class_name(
  #     'div[data-testid="property-card"]'
  #   )

  def pull_deal_box_attributes(self):
    collection = []
    for deal_box in self.deal_boxes:
      # Pulling the hotel name
      hotel_name = deal_box.find_element_by_css_selector(
        'div[data-testid="title"]'
      ).get_attribute('innerHTML').strip()
      hotel_price = deal_box.find_element_by_css_selector(
        "div[data-testid='price-and-discounted-price']"
      ).find_element_by_tag_name('span').get_attribute('innerHTML').strip()
      # hotel_score = deal_box.find_element_by_css_selector(
      #   'div[data-testid="review-score"]'
      # ).find_element_by_xpath("./div").get_attribute('innerHTML').strip()

      collection.append(
        [hotel_name, hotel_price]
      )
    return collection