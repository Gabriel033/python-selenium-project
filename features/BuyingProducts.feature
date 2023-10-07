Feature: BDD

  @Escenario_01
  Scenario: Do login and buy a product in Amazon
    Given navigate to "data.json|:|AmazonPage"
    When do login in the Amazon page with user "data.json|:|user" and password "data.json|:|password"
    Then return to the main page of amazon
    And search the product "data.json|:|GameProduct" and add it to the shopping cart
    Then the shopping cart should contains the product selected
    When it is being removed the product in the shopping cart
    Then the shopping cart must be empty with the message "Tu carrito de Amazon está vacío"
    And close browser


  @Escenario_outline_01
  Scenario Outline: Do login and buy a product in Amazon
    Given navigate to "data.json|:|AmazonPage"
    When do login in the Amazon page with user "<user>" and password "<password>"
    Then return to the main page of amazon
    And search the product "<product_name>" and add it to the shopping cart
    Then the shopping cart should contains the product selected
    When it is being removed the product in the shopping cart
    Then the shopping cart must be empty with the message "Tu carrito de Amazon está vacío"
    And close browser

    Examples:
      |user               | password | product_name      |
      | test1@example.com | pass111  | star wars legion  |
      | test2@example.com | pass222  | basquetball ball  |
      | test3@example.com | pass333  | train toy         |
      | test4@example.com | pass444  | lenovo thinkpad   |



