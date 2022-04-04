@MeliaSearch
Feature: Make a random searchs in the web Melia Hotels

  Scenario Outline: Random Search
    Given Open the Navigator
    When Select destination "<destinations>"
    and Select date "<dates>"
    and Select persons and search
    Then Message Hotels appears

    Examples: Random Search
      | destinations  | dates      |
      | PARIS         | 20/4/2022  |
      | ROMA          | 5/4/2022   |
      | MALAGA        | 8/5/2022   |
      | LISBOA        | 18/5/2022  |