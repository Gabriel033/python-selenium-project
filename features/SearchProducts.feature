Feature: Functional Testing

  @Buying_a_product_in_Amazon
  Scenario: Buying a product in Amazon
    Given navigate to "data.json|:|AmazonPage"
    And wait for "3" seconds
    And take screenshot
    And type on "element.json|:|AmazonSearchInputtext" the value "data.json|:|GameProduct"
    And wait for "3" seconds
    And take screenshot
    And click on "element.json|:|AmazonSearchButton"
    And wait for "5" seconds
    And take screenshot
    And wait until "element.json|:|ResultadosTitle" is visible in a maximum of "30" seconds
    And close browser


  @Outline_Buying_a_product_in_Amazon
  Scenario Outline: Buying a product in Amazon
    Given navigate to "data.json|:|AmazonPage"
    And wait for "3" seconds
    And take screenshot
    And type on "element.json|:|AmazonSearchInputtext" the value "<product_name>"
    And wait for "3" seconds
    And take screenshot
    And click on "element.json|:|AmazonSearchButton"
    And wait for "5" seconds
    And take screenshot
    And wait until "element.json|:|ResultadosTitle" is visible in a maximum of "30" seconds
    And close browser

    Examples:
      | product_name      |
      | star wars legion  |
      | basquetball ball  |
      | train toy         |
      | lenovo thinkpad   |