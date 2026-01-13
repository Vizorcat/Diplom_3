from selenium.webdriver.common.by import By


class FeedPageLocators:
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')
    title_of_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')
    title_of_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')
    quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    daily_quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')
